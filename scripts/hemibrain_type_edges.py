#!/usr/bin/env python3
"""Aggregate hemibrain v1.2 traced adjacencies to cell-type level: data/derived/hemibrain_type_edges.csv.gz and hemibrain_type_totals.csv."""
import csv, gzip
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; H = ROOT/'data/raw/hemibrain/hemibrain-v1.2-all-traced-adjacencies'; OUT = ROOT/'data/derived'
T = {}; ncell = defaultdict(int)
for r in csv.DictReader(open(H/'neurons.csv')):
    t = r['type'] or '(untyped)'; T[int(r['bodyId'])] = t; ncell[t] += 1
E = defaultdict(int); NP = defaultdict(int); tin = defaultdict(int); tout = defaultdict(int)
for r in csv.DictReader(open(H/'total-connections.csv')):
    a, b, w = T.get(int(r['bodyId_pre']), '(untyped)'), T.get(int(r['bodyId_post']), '(untyped)'), int(r['weight'])
    E[(a, b)] += w; NP[(a, b)] += 1; tin[b] += w; tout[a] += w
with gzip.open(OUT/'hemibrain_type_edges.csv.gz', 'wt', newline='') as f:
    w = csv.writer(f); w.writerow(['type_pre','type_post','weight','n_pairs'])
    for k in sorted(E, key=lambda k: -E[k]): w.writerow([*k, E[k], NP[k]])
with open(OUT/'hemibrain_type_totals.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type','n_cells','total_in','total_out'])
    for t in sorted(set(ncell)|set(tin)|set(tout)): w.writerow([t, ncell[t], tin[t], tout[t]])
print('type pairs', len(E), 'types', len(ncell))
