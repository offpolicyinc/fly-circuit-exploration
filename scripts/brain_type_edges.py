#!/usr/bin/env python3
"""Aggregate the full MaleCNS v1.0 flat graph (151M body->body rows) to cell-type level.
Writes data/derived/brain_type_edges.csv.gz (type_pre, type_post, weight, n_pairs) and
data/derived/brain_type_totals.csv (type, n_cells, total_in, total_out). Untyped bodies are pooled as '(untyped)'."""
import csv, gzip, numpy as np, pyarrow as pa, pyarrow.feather as feather
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; RAW = ROOT/'data/raw'; OUT = ROOT/'data/derived'
ann = feather.read_table(RAW/'body-annotations-male-cns-v1.0-minconf-0.5.feather', columns=['bodyId','type'])
bid = ann['bodyId'].to_numpy(); typ = ann['type'].to_pylist()
types = sorted({t for t in typ if t}); tid = {t: i+1 for i, t in enumerate(types)}   # 0 = untyped
codes = np.array([tid.get(t, 0) if t else 0 for t in typ], dtype=np.int64)
order = np.argsort(bid); bid_s = bid[order]; codes_s = codes[order]
def lookup(b):
    i = np.searchsorted(bid_s, b); i[i >= len(bid_s)] = 0
    return np.where(bid_s[i] == b, codes_s[i], 0)
K = len(types)+1; keys_l = []; w_l = []; n_l = []
with pa.memory_map(str(RAW/'connectome-weights-male-cns-v1.0-minconf-0.5.feather'), 'r') as src:
    rd = pa.ipc.open_file(src)
    for i in range(rd.num_record_batches):
        b = rd.get_batch(i)
        key = lookup(b.column('body_pre').to_numpy())*K + lookup(b.column('body_post').to_numpy()); w = b.column('weight').to_numpy()
        u, inv, cnt = np.unique(key, return_inverse=True, return_counts=True)
        keys_l.append(u); w_l.append(np.bincount(inv, weights=w).astype(np.int64)); n_l.append(cnt)
        if i % 200 == 0: print('batch', i, '/', rd.num_record_batches, flush=True)
keys = np.concatenate(keys_l); ws = np.concatenate(w_l); ns = np.concatenate(n_l)
u, inv = np.unique(keys, return_inverse=True); acc = np.bincount(inv, weights=ws).astype(np.int64); npair = np.bincount(inv, weights=ns).astype(np.int64)
names = ['(untyped)'] + types
with gzip.open(OUT/'brain_type_edges.csv.gz', 'wt', newline='') as f:
    w = csv.writer(f); w.writerow(['type_pre','type_post','weight','n_pairs'])
    for j in np.argsort(-acc): w.writerow([names[u[j]//K], names[u[j]%K], int(acc[j]), int(npair[j])])
tin = np.bincount(u % K, weights=acc, minlength=K); tout = np.bincount(u // K, weights=acc, minlength=K); ncell = np.bincount(codes, minlength=K)
with open(OUT/'brain_type_totals.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type','n_cells','total_in','total_out'])
    for i, n in enumerate(names): w.writerow([n, int(ncell[i]), int(tin[i]), int(tout[i])])
print('types', K-1, 'nonzero type pairs', len(u))
