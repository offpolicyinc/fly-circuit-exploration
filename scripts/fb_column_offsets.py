#!/usr/bin/env python3
"""Column-offset (phase) profiles for every strongly connected pair of columnar CX types in
MaleCNS v1.0, and PB-glomerulus -> FB-column maps for PB-FB types. Stdlib only; reads
data/derived/cx_cells.csv and cx_cell_edges.csv. FB columns C1..C9 are folded to 8 angular
positions with C9 == C1 (hemibrain convention: edge half-columns share a heading).
Writes data/derived/fb_column_offsets.csv and pbfb_glomerulus_column_map.csv."""
import csv, re
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
cells = {int(r['bodyId']): r for r in csv.DictReader(open(D/'cx_cells.csv'))}
def col(i):
    m = re.search(r'_C(\d+)', i); 
    if not m: return None
    c = int(m.group(1)); return 0 if c == 9 else c-1   # 0..7
def glom(i):
    m = re.search(r'\)_([LR])(\d)', i); return (m.group(1), int(m.group(2))) if m else None
C = {b: col(r['instance']) for b, r in cells.items()}
T = {b: r['type'] for b, r in cells.items()}
prof = defaultdict(Counter); tot = Counter()
for r in csv.DictReader(open(D/'cx_cell_edges.csv')):
    a, b, w = int(r['body_pre']), int(r['body_post']), int(r['weight'])
    if C.get(a) is None or C.get(b) is None: continue
    o = (C[b]-C[a]) % 8; o = o-8 if o > 4 else o   # -3..4
    prof[(T[a], T[b])][o] += w; tot[(T[a], T[b])] += w
with open(D/'fb_column_offsets.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type_pre','type_post','total','offset','weight','share'])
    for k in sorted(prof, key=lambda k: -tot[k]):
        for o in sorted(prof[k]): w.writerow([*k, tot[k], o, prof[k][o], round(prof[k][o]/tot[k], 3)])
# PB glomerulus -> FB column
rows = Counter()
for b, r in cells.items():
    g, c = glom(r['instance']), col(r['instance'])
    if g and c is not None: rows[(r['type'], g[0], g[1], c)] += 1
with open(D/'pbfb_glomerulus_column_map.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type','side','glomerulus','column0','n'])
    for k in sorted(rows): w.writerow([*k, rows[k]])
def show(k):
    if k not in prof: print(k, 'none'); return
    d = prof[k]; t = tot[k]; peak = max(d, key=d.get)
    print(f"{k[0]:12s}->{k[1]:12s} n={t:6d} peak={peak:+d} ({d[peak]/t:.2f})  " + ' '.join(f"{o:+d}:{d[o]/t:.2f}" for o in sorted(d)))
pairs = [('PFNd','hDeltaB'),('PFNv','hDeltaB'),('hDeltaB','PFR_a'),('hDeltaB','PFR_b'),('PFR_b','PFR_a'),('PFR_a','PFR_b'),('PFR_b','PFR_b'),('PFR_a','PFR_a'),('PFNd','PFR_a'),('PFR_a','hDeltaA'),('hDeltaB','hDeltaJ'),('hDeltaB','hDeltaI'),('hDeltaB','hDeltaK'),('hDeltaK','PFGs'),('PFGs','hDeltaK'),('hDeltaB','PFGs'),('hDeltaJ','FC2A'),('hDeltaJ','FC2B'),('hDeltaH','FC2B'),('hDeltaC','FC2B'),('hDeltaL','FC2C'),('hDeltaF','FC2C'),('hDeltaE','FC2C'),('hDeltaD','FC2C'),('hDeltaI','PFL3'),('hDeltaA','PFL3'),('hDeltaM','PFL3'),('hDeltaH','PFL3'),('FC2C','PFL3'),('PFNp_a','PFL3'),('hDeltaI','PFL2'),('hDeltaA','PFL2'),('hDeltaB','vDeltaM'),('vDeltaM','vDeltaK'),('vDeltaK','hDeltaA'),('hDeltaB','FR1'),('FR1','FR1'),('hDeltaB','FS4A'),('FC3_a','PFR_a'),('PFNa','FC1B'),('PFNa','hDeltaJ'),('PFNp_c','hDeltaJ'),('FC2B','hDeltaM'),('hDeltaM','FC2B'),('hDeltaC','hDeltaF'),('hDeltaB','hDeltaA'),('PFR_b','hDeltaH'),('hDeltaJ','hDeltaJ'),('hDeltaB','hDeltaB'),('hDeltaK','hDeltaK'),('FC2C','FC2C'),('PFL3','PFL3')]
for k in pairs: show(k)
print('\nPB glomerulus -> FB column (column0 = 0..7):')
by = defaultdict(list)
for (t, s, g, c), n in sorted(rows.items()): by[t].append(f"{s}{g}->{c}")
for t in sorted(by): print(t, ' '.join(by[t]))
