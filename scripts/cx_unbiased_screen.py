#!/usr/bin/env python3
"""Unbiased structural screen of all CX cell types in MaleCNS v1.0 (stdlib only).
Scores: self-recurrence, strongest reciprocal loop, external (non-CX) input/output share and
sources, bridging between anchor modules, sharp phase offsets. Tags literature status.
Writes data/derived/cx_screen.csv and cx_sharp_offsets.csv."""
import csv, json
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
P = json.load(open(D/'cx_type_profiles.json')); CX = set(P)
E = defaultdict(int)
for r in csv.DictReader(open(D/'cx_type_edges.csv')): E[(r['type_pre'], r['type_post'])] += int(r['weight'])
KNOWN = {  # types with a published functional characterisation in the reading corpus
 'EPG':'compass','EPGt':'compass','PEN_a(PEN1)':'compass rotation','PEN_b(PEN2)':'compass rotation','PEG':'compass loop','Delta7':'compass inhibition',
 'EL':'octopamine plasticity (Plitt 2025)','ExR2':'dopamine plasticity gate (Fisher 2022)','GLNO':'rotational velocity (Hulse 2023)',
 'PFNd':'forward velocity vector (Lu/Lyu 2022; May 2025)','PFNv':'backward velocity vector','PFNa':'airflow vector (Currier 2020; Ishida 2026)','PFNp_c':'airspeed (May 2025)',
 'hDeltaB':'travel direction (Lu/Lyu 2022)','hDeltaK':'odor working memory (Kathman 2026; Lanz 2025)','hDeltaC':'wind/odor context (Matheson 2022)',
 'FC2A':'goal (Mussells Pires 2024)','FC2B':'goal','FC2C':'goal','PFL3':'goal-heading steering','PFL2':'error-magnitude steering (Westeinde 2024)',
 'PFR_a':'walking direction / drift (Flores-Valle 2025); distance memory (D Atri 2025)','PFR_b':'as PFR_a','FC3_a':'PFNa readout (Ishida 2026)','FC3_b':'as FC3_a','FC3_c':'as FC3_a',
 'LNO1':'PFNv velocity input','LNO2':'PFNd velocity input (Lu 2022)','SpsP':'PFNd velocity input (Lu 2022)','LNOa':'PFNa airflow input (Currier 2020)','FB5AB':'MB-to-FB relay (Matheson 2022)',
 'ExR1':'sleep-related (Hulse 2021)','ER4d':'visual ring','ER4m':'visual ring','ER2_a':'visual ring','ER2_b':'visual ring','ER2_c':'visual ring','ER2_d':'visual ring','ER1_a':'wind ring (Okubo 2020)','ER1_b':'wind ring','ER3w_a':'wind ring (Okubo)','ER3w_b':'wind ring','ER3w_c':'wind ring','ER5':'sleep ring','ER6':'ring','ER3a_a':'ring','ER3a_b':'ring','ER3a_c':'ring','ER3a_d':'ring','ER3d_a':'ring','ER3d_b':'ring','ER3d_c':'ring','ER3d_d':'ring','ER3d_e':'ring','ER3m':'ring','ER3p_a':'ring','ER3p_b':'ring','ER1_c':'ring',
 'PFGs':'recurrent memory candidate (Lanz 2025)'}
ANCHOR = {'compass':{'EPG','EPGt','PEN_a(PEN1)','PEN_b(PEN2)','PEG','Delta7'}, 'velocity':{'PFNd','PFNv','PFNa','PFNp_c','hDeltaB'}, 'goal':{'FC2A','FC2B','FC2C'}, 'steer':{'PFL2','PFL3'}, 'rings':{t for t in CX if t.startswith('ER')}}
def module(t):
    for m, s in ANCHOR.items():
        if t in s: return m
    return None
rows = []
for t, v in P.items():
    tin, tout = v['total_in'], v['total_out']
    self_w = E.get((t, t), 0)
    recip = max(((u, min(E.get((t,u),0), E.get((u,t),0))) for u in CX if u != t), key=lambda x: x[1], default=('', 0))
    ext_in = {u: w for (u, q), w in E.items() if q == t and u not in CX and u != '(untyped)'}
    ext_out = {q: w for (u, q), w in E.items() if u == t and q not in CX and q != '(untyped)'}
    ext_in_sum = sum(ext_in.values()); ext_out_sum = sum(ext_out.values())
    mods_in = Counter(); mods_out = Counter()
    for (u, q), w in E.items():
        if q == t and module(u): mods_in[module(u)] += w
        if u == t and module(q): mods_out[module(q)] += w
    bridge = sorted({m for m, w in mods_in.items() if w/tin > 0.03} | set()), sorted({m for m, w in mods_out.items() if w/tout > 0.03})
    rows.append(dict(type=t, n=v['n'], nt=max(v['nt'], key=v['nt'].get), status=KNOWN.get(t, 'UNCHARACTERISED'),
        total_in=tin, total_out=tout, self_share=round(self_w/tin, 3) if tin else 0,
        recip_partner=recip[0], recip_w=recip[1],
        ext_in_share=round(ext_in_sum/tin, 3) if tin else 0, ext_in_top=';'.join(f'{k}:{w}' for k, w in sorted(ext_in.items(), key=lambda x: -x[1])[:4]),
        ext_out_share=round(ext_out_sum/tout, 3) if tout else 0, ext_out_top=';'.join(f'{k}:{w}' for k, w in sorted(ext_out.items(), key=lambda x: -x[1])[:4]),
        modules_in=','.join(bridge[0]), modules_out=','.join(bridge[1]),
        mod_in_shares=';'.join(f'{m}:{w/tin:.2f}' for m, w in mods_in.most_common()), mod_out_shares=';'.join(f'{m}:{w/tout:.2f}' for m, w in mods_out.most_common())))
with open(D/'cx_screen.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
# sharp offsets
sharp = []
for r in csv.DictReader(open(D/'fb_column_offsets.csv')):
    if int(r['total']) >= 500 and float(r['share']) >= 0.4 and int(r['offset']) != 0: sharp.append((r['type_pre'], r['type_post'], int(r['total']), int(r['offset']), float(r['share'])))
with open(D/'cx_sharp_offsets.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type_pre','type_post','total','offset','share']); w.writerows(sorted(sharp, key=lambda x: -x[2]))
U = [r for r in rows if r['status'] == 'UNCHARACTERISED']
print(f"{len(rows)} types, {len(U)} uncharacterised ({sum(r['n'] for r in U)} cells)")
def top(key, k=12, rev=True, filt=U):
    print(f'\n--- top {key} (uncharacterised) ---')
    for r in sorted(filt, key=lambda r: r[key], reverse=rev)[:k]: print(f"{r['type']:12s} n={r['n']:3d} {r['nt']:13s} {key}={r[key]}  in={r['modules_in']:24s} out={r['modules_out']:20s} ext_in={r['ext_in_top'][:70]}")
top('self_share'); top('recip_w'); top('ext_in_share'); top('ext_out_share'); top('total_out')
print('\n--- uncharacterised types that read from >=2 anchor modules or write to steer/goal ---')
for r in sorted(U, key=lambda r: -r['total_in']):
    if len(r['modules_in'].split(',')) >= 2 and r['modules_in'] or 'steer' in r['modules_out'] or 'goal' in r['modules_out']: print(f"{r['type']:12s} n={r['n']:3d} {r['nt']:13s} in[{r['mod_in_shares']}] out[{r['mod_out_shares']}]")
print('\n--- sharp non-zero column offsets (>=40% of weight at one offset) ---')
for s in sorted(sharp, key=lambda x: -x[2])[:40]: print(s)
