#!/usr/bin/env python3
"""Systematic screen of FB columnar types for vector-integration / vector-memory capability (stdlib).
Criteria per type X:
  A recurrence: within-type synapses, share at column offset 0, share at 180 (offset 4), predicted sign
  B velocity/travel input: synapses from hDeltaB, PFNd, PFNv, PFNa and their offset concentration
  C heading input: from Delta7/EPG (PB) via cx_type_edges
  D readout: synapses to FC2A/B/C, PFL3, PFL2, hDeltaM, hDeltaA, hDeltaI
  E write/reset inputs: from dopamine CX types and from non-CX sources (external share)
  F cross-type loops: strongest reciprocal partner among columnar types, with phase of the round trip
Writes data/derived/vector_memory_screen.csv and prints ranked tables."""
import csv, json, re
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
P = json.load(open(D/'cx_type_profiles.json'))
cells = {int(r['bodyId']): r for r in csv.DictReader(open(D/'cx_cells.csv'))}
def col(i):
    m = re.search(r'_C(\d+)', i); 
    if not m: return None
    c = int(m.group(1)); return 0 if c == 9 else c-1
T = {b: r['type'] for b, r in cells.items()}; C = {b: col(r['instance']) for b, r in cells.items()}
NT = {}
for b, r in cells.items(): NT.setdefault(r['type'], Counter())[r['nt']] += 1
def sign(t):
    n = NT.get(t, Counter()); m = n.most_common(1)[0][0] if n else 'unknown'
    return {'acetylcholine': +1, 'glutamate': -1, 'gaba': -1, 'dopamine': 0, 'serotonin': 0, 'octopamine': 0}.get(m, 0), m
E = defaultdict(int); K = defaultdict(Counter)
for r in csv.DictReader(open(D/'cx_cell_edges.csv')):
    a, b, w = int(r['body_pre']), int(r['body_post']), int(r['weight'])
    E[(T[a], T[b])] += w
    if C[a] is not None and C[b] is not None:
        o = (C[b]-C[a]) % 8; K[(T[a], T[b])][o] += w
COLUMNAR = sorted({t for b, t in T.items() if C[b] is not None})
DOPA = [t for t in P if sign(t)[1] == 'dopamine']
VEL = ['hDeltaB', 'PFNd', 'PFNv', 'PFNa']; HEAD = ['Delta7', 'EPG']; READ = ['FC2A', 'FC2B', 'FC2C', 'PFL3', 'PFL2', 'hDeltaM', 'hDeltaA', 'hDeltaI']
rows = []
for X in COLUMNAR:
    n = P[X]['n']; tin = P[X]['total_in'] or 1
    self_w = E[(X, X)]; k = K[(X, X)]; ks = sum(k.values()) or 1
    s, ntname = sign(X)
    vel = {v: E[(v, X)] for v in VEL}; velk = {v: (max(K[(v, X)].values())/sum(K[(v, X)].values()) if K[(v, X)] else 0) for v in VEL}
    head = {h: E[(h, X)] for h in HEAD}
    read = {r: E[(X, r)] for r in READ}
    dopa = {d: E[(d, X)] for d in DOPA if E[(d, X)] > 0}
    ext = P[X]['top_inputs']; ext_share = sum(w for t, w, sh in ext if t not in P and t != '(untyped)')/tin
    # strongest reciprocal columnar partner and round-trip phase
    best = ('', 0, None)
    for Y in COLUMNAR:
        if Y == X: continue
        m = min(E[(X, Y)], E[(Y, X)])
        if m > best[1]:
            kx, ky = K[(X, Y)], K[(Y, X)]
            px = max(kx, key=kx.get) if kx else None; py = max(ky, key=ky.get) if ky else None
            rt = ((px or 0) + (py or 0)) % 8 if kx and ky else None
            best = (Y, m, rt)
    rows.append(dict(type=X, n=n, nt=ntname, sign=s, total_in=tin,
        self_syn=self_w, self_share=round(self_w/tin, 3), self_off0=round(k[0]/ks, 2), self_off180=round(k[4]/ks, 2), self_broad=round(1-(k[0]+k[4])/ks, 2),
        vel_total=sum(vel.values()), vel_share=round(sum(vel.values())/tin, 3), vel_hDeltaB=vel['hDeltaB'], vel_PFNd=vel['PFNd'], vel_PFNv=vel['PFNv'], vel_PFNa=vel['PFNa'], vel_peak_conc=round(max(velk.values()), 2),
        head_total=sum(head.values()), read_total=sum(read.values()), read_goal=read['FC2A']+read['FC2B']+read['FC2C'], read_steer=read['PFL3']+read['PFL2'], read_inv=read['hDeltaM']+read['hDeltaA']+read['hDeltaI'],
        dopa_total=sum(dopa.values()), dopa_top=';'.join(f'{d}:{w}' for d, w in sorted(dopa.items(), key=lambda x: -x[1])[:3]), ext_share=round(ext_share, 2),
        recip_partner=best[0], recip_w=best[1], recip_roundtrip_offset=best[2]))
with open(D/'vector_memory_screen.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def show(title, key, k=14, filt=lambda r: True, cols=('n','nt','self_syn','self_off0','self_off180','vel_total','vel_hDeltaB','head_total','read_goal','read_steer','dopa_total','recip_partner','recip_w','recip_roundtrip_offset')):
    print(f'\n--- {title} ---'); print(f"{'type':10s} " + ' '.join(f'{c:>12s}' for c in cols))
    for r in sorted([r for r in rows if filt(r)], key=lambda r: -r[key])[:k]: print(f"{r['type']:10s} " + ' '.join(f'{str(r[c]):>12s}' for c in cols))
show('velocity/travel input (criterion B)', 'vel_total')
show('within-type recurrence (criterion A)', 'self_syn')
show('recurrence AND velocity input', 'self_syn', filt=lambda r: r['vel_total'] > 300)
show('reads velocity AND writes to goal/steer', 'read_total', filt=lambda r: r['vel_total'] > 300 and r['read_total'] > 300)
show('dopamine input (criterion E)', 'dopa_total')
show('cross-type loops', 'recip_w')
print('\n--- two-hop hDeltaB -> X -> FC2 (X columnar) ---')
paths = []
for X in COLUMNAR:
    a = E[('hDeltaB', X)]; b = sum(E[(X, g)] for g in ('FC2A','FC2B','FC2C'))
    if a > 100 and b > 100: paths.append((X, a, b, min(a, b)))
for X, a, b, m in sorted(paths, key=lambda x: -x[3]): print(f'{X:10s} hDeltaB->X {a:6d}  X->FC2 {b:6d}')
