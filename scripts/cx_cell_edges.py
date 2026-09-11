#!/usr/bin/env python3
"""Cell-level edges among all CX-class neurons in MaleCNS v1.0 -> data/derived/cx_cell_edges.csv, cx_cells.csv"""
import csv
from pathlib import Path
import pyarrow as pa, pyarrow.compute as pc, pyarrow.feather as feather
ROOT = Path(__file__).resolve().parents[1]; RAW = ROOT/'data/raw'; OUT = ROOT/'data/derived'
ann = feather.read_table(RAW/'body-annotations-male-cns-v1.0-minconf-0.5.feather').to_pylist()
A = {n['bodyId']: n for n in ann}
nt = {r['body']: (r.get('consensus_nt') or r.get('predicted_nt') or '') for r in feather.read_table(RAW/'body-neurotransmitters-male-cns-v1.0.feather').to_pylist()}
cx = {i for i, n in A.items() if n.get('class') == 'CX' and n.get('type')}
with open(OUT/'cx_cells.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['bodyId','type','instance','somaSide','nt'])
    for i in sorted(cx): w.writerow([i, A[i]['type'], A[i].get('instance') or '', A[i].get('somaSide') or '', nt.get(i, '')])
ids = pa.array(sorted(cx), type=pa.int64()); n = 0
with open(OUT/'cx_cell_edges.csv', 'w', newline='') as f, pa.memory_map(str(RAW/'connectome-weights-male-cns-v1.0-minconf-0.5.feather'), 'r') as src:
    w = csv.writer(f); w.writerow(['body_pre','body_post','weight'])
    rd = pa.ipc.open_file(src)
    for i in range(rd.num_record_batches):
        b = pa.Table.from_batches([rd.get_batch(i)])
        m = pc.and_(pc.is_in(b['body_pre'], value_set=ids), pc.is_in(b['body_post'], value_set=ids))
        for e in b.filter(m).select(['body_pre','body_post','weight']).to_pylist():
            w.writerow([e['body_pre'], e['body_post'], e['weight']]); n += 1
print('edges', n)
