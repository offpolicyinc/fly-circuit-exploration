#!/usr/bin/env python3
"""Recurrence modes recomputed in true angle space (12/8/6/9-label column counts), with the compass ring as a
positive control measured by the same metric. For each columnar type: uniform and cosine self-gain (share of
total input, signed by transmitter). For every columnar pair A->B->A: two-hop cosine loop gain = product of
the complex first-harmonic gains (magnitude and round-trip phase). Compass: EPG/PEN/PEG/Delta7 by EB wedge."""
import csv, json, re, math, cmath
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
P = json.load(open(D/'cx_type_profiles.json'))
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
# compass wedges (interleaved map from compass_recurrence.py): glomerulus g of side L -> wedge index
def wedge(inst):
    m = re.search(r'\)_([LR])(\d)', inst)
    if not m: return None
    s, g = m.group(1), int(m.group(2)); g = 1 if g == 9 else g
    return ((g-1)*2 if s == 'L' else (8-g)*2+1) * 360/16
ANG = {}
for b, r in cells.items():
    if r['type'] in ('EPG', 'PEN_a(PEN1)', 'PEN_b(PEN2)', 'PEG', 'EPGt'): ANG[b] = wedge(r['instance'])
    else: ANG[b] = angle(r['type'], r['instance'])
T = {b: r['type'] for b, r in cells.items()}
NT = defaultdict(Counter)
for b, r in cells.items(): NT[r['type']][r['nt']] += 1
def sgn(t):
    m = NT[t].most_common(1)[0][0] if NT[t] else ''
    return {'acetylcholine': 1, 'glutamate': -1, 'gaba': -1}.get(m, 0), m
Z = defaultdict(complex); W = defaultdict(float)
for r in csv.DictReader(open(D/'cx_cell_edges.csv')):
    a, b, w = int(r['body_pre']), int(r['body_post']), int(r['weight'])
    if ANG.get(a) is None or ANG.get(b) is None: continue
    k = (T[a], T[b]); Z[k] += w*cmath.exp(1j*math.radians(ANG[b]-ANG[a])); W[k] += w
def g(pre, post):
    """complex first-harmonic gain of pre->post as share of post input, signed by pre transmitter"""
    tin = P[post]['total_in'] or 1; s, _ = sgn(pre)
    return s*W[(pre, post)]/tin, s*Z[(pre, post)]/tin
rows = []
for X in sorted({t for b, t in T.items() if ANG[b] is not None}):
    if W[(X, X)] < 100: continue
    u, z = g(X, X)
    rows.append(dict(type=X, n=P[X]['n'], nt=sgn(X)[1], self_syn=int(W[(X, X)]), uniform_gain=round(u, 3), cosine_gain=round(z.real, 3), cosine_mag=round(abs(z), 3), self_phase_deg=round(math.degrees(cmath.phase(z)) % 360, 0)))
rows.sort(key=lambda r: -abs(r['cosine_gain']))
print(f"{'type':12s} {'n':>3s} {'nt':>13s} {'syn':>6s} {'uniform':>8s} {'cos':>7s} {'|z|':>6s} {'phase':>6s}")
for r in rows[:25]: print(f"{r['type']:12s} {r['n']:3d} {r['nt']:>13s} {r['self_syn']:6d} {r['uniform_gain']:8.3f} {r['cosine_gain']:7.3f} {r['cosine_mag']:6.3f} {r['self_phase_deg']:6.0f}")
with open(D/'recurrence_modes_v2.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
# two-hop loops between all columnar pairs
loops = []
keys = {k for k in W if W[k] >= 100}
for (A, B) in keys:
    if A >= B or (B, A) not in keys: continue
    ua, za = g(A, B); ub, zb = g(B, A)
    loops.append(dict(A=A, B=B, AB=int(W[(A, B)]), BA=int(W[(B, A)]), uniform_loop=round(ua*ub, 4), cosine_loop=round((za*zb).real, 4), loop_mag=round(abs(za*zb), 4), roundtrip_deg=round(math.degrees(cmath.phase(za*zb)) % 360, 0)))
loops.sort(key=lambda r: -r['loop_mag'])
print('\n--- two-hop loops by |cosine loop gain| ---')
for r in loops[:20]: print(f"{r['A']:12s}<->{r['B']:12s} {r['AB']:6d} {r['BA']:6d} uni={r['uniform_loop']:7.4f} cos={r['cosine_loop']:7.4f} |z|={r['loop_mag']:6.4f} rt={r['roundtrip_deg']:4.0f}")
with open(D/'recurrence_loops_v2.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(loops[0])); w.writeheader(); w.writerows(loops)
print('\n--- positive control: the compass ring by the same metric ---')
for A, B in [('EPG','EPG'),('EPG','PEN_a(PEN1)'),('PEN_a(PEN1)','EPG'),('EPG','PEN_b(PEN2)'),('PEN_b(PEN2)','EPG'),('EPG','PEG'),('PEG','PEN_b(PEN2)'),('Delta7','EPG'),('EPG','Delta7')]:
    u, z = g(A, B); print(f"{A:12s}->{B:12s} syn={int(W[(A,B)]):6d} uniform={u:7.3f} cos={z.real:7.3f} |z|={abs(z):6.3f} phase={math.degrees(cmath.phase(z))%360:5.0f}")
for A, B in [('EPG','PEN_a(PEN1)'),('EPG','PEN_b(PEN2)')]:
    ua, za = g(A, B); ub, zb = g(B, A); print(f"loop {A}<->{B}: uniform={ua*ub:.4f} cosine={(za*zb).real:.4f} |z|={abs(za*zb):.4f}")
ua, za = g('EPG','PEG'); ub, zb = g('PEG','PEN_b(PEN2)'); uc, zc = g('PEN_b(PEN2)','EPG'); print(f"loop EPG->PEG->PENb->EPG: |z|={abs(za*zb*zc):.5f}")
