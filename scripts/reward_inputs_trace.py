#!/usr/bin/env python3
"""Inputs to candidate reward/reset neurons (OA-VPM3, OA-VUMa1, SMP377, PLP246) from the full graph."""
import csv, json
from collections import Counter, defaultdict
from pathlib import Path
import pyarrow as pa, pyarrow.compute as pc, pyarrow.feather as feather
ROOT = Path(__file__).resolve().parents[1]; RAW = ROOT/'data/raw'; OUT = ROOT/'data/derived'
A = {n['bodyId']: n for n in feather.read_table(RAW/'body-annotations-male-cns-v1.0-minconf-0.5.feather').to_pylist()}
targets = {t: [i for i, n in A.items() if n.get('type') == t] for t in ('OA-VPM3', 'OA-VUMa1', 'SMP377', 'PLP246', 'FB4M', 'FB4L')}
ids = pa.array(sorted(sum(targets.values(), [])), type=pa.int64())
inp = defaultdict(Counter); outp = defaultdict(Counter)
with pa.memory_map(str(RAW/'connectome-weights-male-cns-v1.0-minconf-0.5.feather'), 'r') as src:
    rd = pa.ipc.open_file(src)
    for i in range(rd.num_record_batches):
        b = pa.Table.from_batches([rd.get_batch(i)])
        m = pc.or_(pc.is_in(b['body_post'], value_set=ids), pc.is_in(b['body_pre'], value_set=ids))
        for e in b.filter(m).select(['body_pre','body_post','weight']).to_pylist():
            tp = A.get(e['body_pre'], {}); tq = A.get(e['body_post'], {})
            for t, L in targets.items():
                if e['body_post'] in L: inp[t][(tp.get('type') or '(untyped)', tp.get('superclass') or '')] += e['weight']
                if e['body_pre'] in L: outp[t][(tq.get('type') or '(untyped)', tq.get('superclass') or '')] += e['weight']
res = {}
for t in targets:
    n = len(targets[t]); res[t] = dict(n=n, top_inputs=[(k[0], k[1], w) for k, w in inp[t].most_common(25)], top_outputs=[(k[0], k[1], w) for k, w in outp[t].most_common(25)])
    print(f"\n### {t} (n={n})"); print('  IN :', [(k[0], w) for k, w in inp[t].most_common(18)]); print('  OUT:', [(k[0], w) for k, w in outp[t].most_common(18)])
(OUT/'reward_inputs_trace.json').write_text(json.dumps(res, indent=1)+'\n')
