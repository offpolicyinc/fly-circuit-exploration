#!/usr/bin/env python3
"""Type-level input/output profiles for every central-complex cell type in MaleCNS v1.0,
including non-CX partners, plus transmitter predictions and columnar-label structure.
Writes data/derived/cx_type_profiles.json and cx_type_edges.csv. Requires pyarrow."""
import json, csv, re
from collections import Counter, defaultdict
from pathlib import Path
import pyarrow as pa, pyarrow.compute as pc, pyarrow.feather as feather
ROOT = Path(__file__).resolve().parents[1]; RAW = ROOT/'data/raw'; OUT = ROOT/'data/derived'
ann = feather.read_table(RAW/'body-annotations-male-cns-v1.0-minconf-0.5.feather').to_pylist()
A = {n['bodyId']: n for n in ann}
nt = {r['body']: r for r in feather.read_table(RAW/'body-neurotransmitters-male-cns-v1.0.feather').to_pylist()}
cx = {i for i, n in A.items() if n.get('class') == 'CX' and n.get('type')}
ids = pa.array(sorted(cx), type=pa.int64())
pair = Counter(); tot_in = Counter(); tot_out = Counter()
with pa.memory_map(str(RAW/'connectome-weights-male-cns-v1.0-minconf-0.5.feather'), 'r') as src:
    rd = pa.ipc.open_file(src)
    for i in range(rd.num_record_batches):
        b = pa.Table.from_batches([rd.get_batch(i)])
        m = pc.or_(pc.is_in(b['body_pre'], value_set=ids), pc.is_in(b['body_post'], value_set=ids))
        for e in b.filter(m).select(['body_pre','body_post','weight']).to_pylist():
            p, q, w = e['body_pre'], e['body_post'], e['weight']
            tp = A.get(p, {}).get('type') or '(untyped)'; tq = A.get(q, {}).get('type') or '(untyped)'
            if p in cx: tot_out[tp] += w
            if q in cx: tot_in[tq] += w
            pair[(tp, tq)] += w
types = sorted({A[i]['type'] for i in cx})
prof = {}
for t in types:
    cells = [i for i in cx if A[i]['type'] == t]
    ins = sorted(((a, w) for (a, b), w in pair.items() if b == t), key=lambda x: -x[1])[:15]
    outs = sorted(((b, w) for (a, b), w in pair.items() if a == t), key=lambda x: -x[1])[:15]
    nts = Counter((nt.get(i, {}).get('consensus_nt') or nt.get(i, {}).get('predicted_nt') or 'unknown') for i in cells)
    inst = A[cells[0]].get('instance') or ''
    prof[t] = dict(n=len(cells), nt=dict(nts.most_common(3)), example_instance=inst,
                   has_column='_C' in inst, has_glomerulus=bool(re.search(r'\)_[LR]\d', inst)),
                   total_in=tot_in[t], total_out=tot_out[t],
                   top_inputs=[(a, w, round(w/tot_in[t], 3)) for a, w in ins],
                   top_outputs=[(b, w, round(w/tot_out[t], 3)) for b, w in outs],
                   sides=dict(Counter(A[i].get('somaSide') for i in cells)))
(OUT/'cx_type_profiles.json').write_text(json.dumps(prof, indent=1)+'\n')
with open(OUT/'cx_type_edges.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type_pre','type_post','weight'])
    for (a, b), wt in sorted(pair.items(), key=lambda x: -x[1]): w.writerow([a, b, wt])
print(len(types), 'CX types;', len(cx), 'cells;', len(pair), 'type pairs')
