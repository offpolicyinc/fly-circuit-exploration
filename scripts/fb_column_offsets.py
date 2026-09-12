#!/usr/bin/env python3
"""Column-offset (phase) profiles for connected pairs of columnar CX types in MaleCNS v1.0, in ANGLE space.
Each type's column count is read from its labels: 12-column types (hDeltaA/B/C/I/J/K/L), 8-column
(hDeltaD/E/G/H/M, PFNd, FC1F), 6-column (hDeltaF), and 9-label types where C9 shares the heading of C1
(8 angular positions; C0 = bilateral, mapped to C1). angle = (c-1)/n * 360.
Outputs: fb_column_offsets.csv (offset binned to 8 x 45 deg bins, -3..4, as before, for simulations),
fb_offset_stats.csv (circular mean offset in degrees and resultant length per pair),
pbfb_glomerulus_column_map.csv (unchanged)."""
import csv, re, math
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
cells = {int(r['bodyId']): r for r in csv.DictReader(open(D/'cx_cells.csv'))}
ncol = defaultdict(int)
for b, r in cells.items():
    m = re.search(r'_C(\d+)', r['instance'])
    if m: ncol[r['type']] = max(ncol[r['type']], int(m.group(1)))
def angle(t, inst):
    m = re.search(r'_C(\d+)', inst)
    if not m: return None
    c = int(m.group(1)); n = ncol[t]
    if n == 9: c = 1 if c in (0, 9) else c; return (c-1)/8*360
    if c == 0: c = 1
    return (c-1)/n*360
ANG = {b: angle(r['type'], r['instance']) for b, r in cells.items()}; T = {b: r['type'] for b, r in cells.items()}
def glom(i):
    m = re.search(r'\)_([LR])(\d)', i); return (m.group(1), int(m.group(2))) if m else None
acc = defaultdict(lambda: [0.0, 0.0, 0]); bins = defaultdict(Counter); tot = Counter()
for r in csv.DictReader(open(D/'cx_cell_edges.csv')):
    a, b, w = int(r['body_pre']), int(r['body_post']), int(r['weight'])
    if ANG.get(a) is None or ANG.get(b) is None: continue
    d = (ANG[b]-ANG[a]) % 360; th = math.radians(d)
    k = (T[a], T[b]); acc[k][0] += w*math.cos(th); acc[k][1] += w*math.sin(th); acc[k][2] += w
    o = int(round(d/45)) % 8; o = o-8 if o > 4 else o
    bins[k][o] += w; tot[k] += w
with open(D/'fb_column_offsets.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type_pre','type_post','total','offset','weight','share'])
    for k in sorted(bins, key=lambda k: -tot[k]):
        for o in sorted(bins[k]): w.writerow([*k, tot[k], o, bins[k][o], round(bins[k][o]/tot[k], 3)])
with open(D/'fb_offset_stats.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type_pre','type_post','total','mean_offset_deg','resultant_length','ncol_pre','ncol_post'])
    for k in sorted(acc, key=lambda k: -acc[k][2]):
        c, s, n = acc[k]; w.writerow([*k, n, round(math.degrees(math.atan2(s, c)) % 360, 1), round(math.hypot(c, s)/n, 3), ncol[k[0]], ncol[k[1]]])
rows = Counter()
for b, r in cells.items():
    g = glom(r['instance']); m = re.search(r'_C(\d+)', r['instance'])
    if g and m: rows[(r['type'], g[0], g[1], int(m.group(1)))] += 1
with open(D/'pbfb_glomerulus_column_map.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type','side','glomerulus','column_label','n'])
    for k in sorted(rows): w.writerow([*k, rows[k]])
def show(k):
    if k not in acc: print(k, 'none'); return
    c, s, n = acc[k]; print(f"{k[0]:10s}->{k[1]:10s} n={n:6d} mean_offset={math.degrees(math.atan2(s,c))%360:6.1f} deg  concentration={math.hypot(c,s)/n:.2f}  bins(-3..4)={[round(bins[k][o]/n,2) for o in range(-3,5)]}")
for k in [('PFNd','hDeltaB'),('PFNv','hDeltaB'),('hDeltaB','PFR_a'),('hDeltaB','PFR_b'),('PFNd','PFR_a'),('PFR_b','PFR_a'),('PFR_b','PFR_b'),('hDeltaB','hDeltaJ'),('hDeltaJ','FC2A'),('hDeltaJ','FC2B'),('hDeltaB','hDeltaI'),('hDeltaB','hDeltaA'),('hDeltaI','PFL3'),('hDeltaA','PFL3'),('hDeltaM','PFL3'),('FC2B','hDeltaM'),('hDeltaH','FC2B'),('hDeltaB','hDeltaK'),('hDeltaK','PFGs'),('PFGs','hDeltaK'),('hDeltaB','FR1'),('FR1','FR1'),('hDeltaB','hDeltaB'),('hDeltaJ','hDeltaJ'),('hDeltaK','hDeltaK'),('FC2C','PFL3'),('hDeltaC','FC2B'),('hDeltaL','FC2C'),('hDeltaB','vDeltaM'),('PFR_a','hDeltaA')]: show(k)
