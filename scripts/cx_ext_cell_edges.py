#!/usr/bin/env python3
"""Cell-level edges between CX-class neurons and a set of external partner types (modulators, velocity-source
candidates, ascending relays): data/derived/cx_ext_cell_edges.csv (body_pre, body_post, weight) and cx_ext_cells.csv."""
import csv, re
from pathlib import Path
import pyarrow as pa, pyarrow.compute as pc, pyarrow.feather as feather
ROOT = Path(__file__).resolve().parents[1]; RAW = ROOT/'data/raw'; OUT = ROOT/'data/derived'
ann = feather.read_table(RAW/'body-annotations-male-cns-v1.0-minconf-0.5.feather', columns=['bodyId','type','instance','somaSide','class']).to_pylist()
nt = {r['body']: (r.get('consensus_nt') or r.get('predicted_nt') or '') for r in feather.read_table(RAW/'body-neurotransmitters-male-cns-v1.0.feather', columns=['body','consensus_nt','predicted_nt']).to_pylist()}
EXT_RE = re.compile(r'^(OA-|5-HT|PPL|PAM|PPM|PS196|AN06B009|LAL143|PS326|AN07B037|LLPC1|GLNO|LNO|SpsP|IbSpsP)')
cx = {n['bodyId'] for n in ann if n.get('class') == 'CX' and n.get('type')}
ext = {n['bodyId'] for n in ann if n.get('type') and (EXT_RE.match(n['type']) or nt.get(n['bodyId']) in ('dopamine', 'octopamine', 'serotonin'))} - cx
with open(OUT/'cx_ext_cells.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['bodyId','type','instance','somaSide','nt'])
    for n in ann:
        if n['bodyId'] in ext: w.writerow([n['bodyId'], n['type'], n.get('instance') or '', n.get('somaSide') or '', nt.get(n['bodyId'], '')])
cxa = pa.array(sorted(cx), type=pa.int64()); exa = pa.array(sorted(ext), type=pa.int64()); n = 0
with open(OUT/'cx_ext_cell_edges.csv', 'w', newline='') as f, pa.memory_map(str(RAW/'connectome-weights-male-cns-v1.0-minconf-0.5.feather'), 'r') as src:
    w = csv.writer(f); w.writerow(['body_pre','body_post','weight']); rd = pa.ipc.open_file(src)
    for i in range(rd.num_record_batches):
        b = pa.Table.from_batches([rd.get_batch(i)])
        m = pc.or_(pc.and_(pc.is_in(b['body_pre'], value_set=exa), pc.is_in(b['body_post'], value_set=cxa)), pc.and_(pc.is_in(b['body_pre'], value_set=cxa), pc.is_in(b['body_post'], value_set=exa)))
        for e in b.filter(m).to_pylist(): w.writerow([e['body_pre'], e['body_post'], e['weight']]); n += 1
print('ext cells', len(ext), 'edges', n)
