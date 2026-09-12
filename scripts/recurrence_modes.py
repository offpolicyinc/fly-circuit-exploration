#!/usr/bin/env python3
"""Linear-mode analysis of recurrence for every columnar type and the strongest cross-type loops.
Weights are synapse counts normalised by the postsynaptic type's total input (a proxy for relative
efficacy), signed by predicted transmitter (ACh +, Glu/GABA -). For a circulant kernel k over 8 columns,
the uniform-mode gain is sum(k) and the cosine (vector) mode gain is sum(k cos). For a two-type loop
A<->B the loop gains are products. Prints ranked results; writes data/derived/recurrence_modes.csv."""
import csv, json, re, math
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
P = json.load(open(D/'cx_type_profiles.json'))
cells = {int(r['bodyId']): r for r in csv.DictReader(open(D/'cx_cells.csv'))}
def col(i):
    m = re.search(r'_C(\d+)', i)
    if not m: return None
    c = int(m.group(1)); return 0 if c == 9 else c-1
T = {b: r['type'] for b, r in cells.items()}; C = {b: col(r['instance']) for b, r in cells.items()}
NT = defaultdict(Counter)
for b, r in cells.items(): NT[r['type']][r['nt']] += 1
def sgn(t):
    m = NT[t].most_common(1)[0][0] if NT[t] else ''
    return {'acetylcholine': 1, 'glutamate': -1, 'gaba': -1}.get(m, 0), m
K = defaultdict(lambda: [0]*8); E = defaultdict(int)
for r in csv.DictReader(open(D/'cx_cell_edges.csv')):
    a, b, w = int(r['body_pre']), int(r['body_post']), int(r['weight'])
    E[(T[a], T[b])] += w
    if C[a] is not None and C[b] is not None: K[(T[a], T[b])][(C[b]-C[a]) % 8] += w
def gains(pre, post):
    k = K[(pre, post)]; tin = P[post]['total_in'] or 1; s, _ = sgn(pre)
    kn = [s*x/tin for x in k]
    uni = sum(kn); cos = sum(kn[i]*math.cos(2*math.pi*i/8) for i in range(8)); cos2 = sum(kn[i]*math.cos(4*math.pi*i/8) for i in range(8))
    return uni, cos, cos2, sum(k)
COL = sorted({t for b, t in T.items() if C[b] is not None})
rows = []
for X in COL:
    uni, cos, cos2, tot = gains(X, X)
    if tot < 100: continue
    rows.append(dict(type=X, n=P[X]['n'], nt=sgn(X)[1], self_syn=tot, uniform_gain=round(uni, 3), cosine_gain=round(cos, 3), cos2_gain=round(cos2, 3), ratio_cos_uni=round(cos/uni, 2) if uni else None))
print('--- within-type recurrence modes (fraction of total input; sign from transmitter) ---')
print(f"{'type':10s} {'n':>3s} {'nt':>14s} {'syn':>6s} {'uniform':>8s} {'cosine':>8s} {'cos2':>7s}")
for r in sorted(rows, key=lambda r: -abs(r['cosine_gain'])): print(f"{r['type']:10s} {r['n']:3d} {r['nt']:>14s} {r['self_syn']:6d} {r['uniform_gain']:8.3f} {r['cosine_gain']:8.3f} {r['cos2_gain']:7.3f}")
print('\n--- two-type loops: loop gains (product of the two legs) ---')
loops = [('PFR_a','PFR_b'),('PFR_a','hDeltaA'),('hDeltaK','PFGs'),('hDeltaC','hDeltaF'),('FC2B','hDeltaM'),('hDeltaL','vDeltaD'),('hDeltaD','vDeltaA_b'),('hDeltaJ','FB4X'),('hDeltaB','PFR_a'),('hDeltaB','PFR_b'),('vDeltaM','vDeltaK'),('hDeltaA','vDeltaK'),('hDeltaG','FB5S'),('hDeltaH','FB5U'),('PFNm_a','PFNm_b'),('hDeltaB','FB4B'),('hDeltaB','FB4C')]
print(f"{'loop':22s} {'A->B syn':>9s} {'B->A syn':>9s} {'uniform':>8s} {'cosine':>8s} {'roundtrip':>10s}")
lrows = []
for A, B in loops:
    ua, ca, c2a, ta = gains(A, B); ub, cb, c2b, tb = gains(B, A)
    if ta == 0 or tb == 0: 
        # tangential partner: no column kernel; use type-level totals with sign
        sa, _ = sgn(A); sb, _ = sgn(B)
        ua = sa*E[(A,B)]/(P[B]['total_in'] or 1); ub = sb*E[(B,A)]/(P[A]['total_in'] or 1); ca = cb = float('nan')
    ka, kb = K[(A,B)], K[(B,A)]
    pa = max(range(8), key=lambda i: ka[i]) if sum(ka) else None; pb = max(range(8), key=lambda i: kb[i]) if sum(kb) else None
    rt = (pa+pb) % 8 if pa is not None and pb is not None else None
    lrows.append(dict(loop=f'{A}<->{B}', A_to_B=E[(A,B)], B_to_A=E[(B,A)], uniform_loop_gain=round(ua*ub, 4), cosine_loop_gain=(round(ca*cb, 4) if ca == ca else None), roundtrip_offset=rt))
    print(f"{A+'<->'+B:22s} {E[(A,B)]:9d} {E[(B,A)]:9d} {ua*ub:8.4f} {(ca*cb if ca==ca else float('nan')):8.4f} {str(rt):>10s}")
with open(D/'recurrence_modes.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
with open(D/'recurrence_loops.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(lrows[0])); w.writeheader(); w.writerows(lrows)
