#!/usr/bin/env python3
"""Screen for Maimon & Abbott's tangential-store motif: a tangential neuron T whose synapses onto a columnar
population X could hold a column-specific weight pattern. Requirements scored per (T, X):
  T->X synapses spread across all X columns (uniformity = min/max per-column synapses),
  X receives a heading/travel bump (from hDeltaB, PFNd, PFNv, PFNa, Delta7, EPG) to act as the postsynaptic teacher,
  X reads out to goal/steer (FC2*, PFL2/3) within one hop,
  T receives contextual / reward input from outside the CX (external share, MBON/OA/PPL names),
  a neuromodulator (DA/OA) also reaches X.
Writes data/derived/tangential_store_screen.csv and prints the top pairs."""
import csv, json, re, math
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
P = json.load(open(D/'cx_type_profiles.json'))
cells = {int(r['bodyId']): r for r in csv.DictReader(open(D/'cx_cells.csv'))}; T = {b: r['type'] for b, r in cells.items()}
def colidx(b):
    m = re.search(r'_C(\d+)', cells[b]['instance']); return int(m.group(1)) if m else None
COL = sorted({t for b, t in T.items() if colidx(b) is not None}); TAN = sorted(t for t in P if t.startswith('FB') and t not in COL)
E = defaultdict(int); percol = defaultdict(Counter)
for r in csv.DictReader(open(D/'cx_cell_edges.csv')):
    a, b, w = int(r['body_pre']), int(r['body_post']), int(r['weight']); E[(T[a], T[b])] += w
    if T[a] in TAN and colidx(b) is not None: percol[(T[a], T[b])][colidx(b)] += w
ext = defaultdict(int)
for r in csv.DictReader(open(D/'cx_type_edges.csv')): ext[(r['type_pre'], r['type_post'])] += int(r['weight'])
TEACH = ['hDeltaB','PFNd','PFNv','PFNa','Delta7','EPG']; GOAL = ['FC2A','FC2B','FC2C','PFL3','PFL2']
DA = [t for t in P if max(P[t]['nt'], key=P[t]['nt'].get) == 'dopamine']; OA = ['OA-VPM3','OA-VUMa1']
rows = []
for Tn in TAN:
    tin = P[Tn]['total_in'] or 1
    extin = [(a, w) for a, w, s in P[Tn]['top_inputs'] if a not in P and a != '(untyped)']
    ext_share = sum(w for a, w in extin)/tin; ctx = ';'.join(f'{a}:{w}' for a, w in extin[:4])
    for X in COL:
        s = E[(Tn, X)]
        if s < 300: continue
        pc = percol[(Tn, X)]; unif = (min(pc.values())/max(pc.values())) if len(pc) >= 6 else 0
        teach = sum(E[(t, X)] for t in TEACH); read = sum(E[(X, g)] for g in GOAL)
        mod = sum(E[(d, X)] for d in DA) + sum(ext[(o, X)] for o in OA)
        nt = max(P[Tn]['nt'], key=P[Tn]['nt'].get)
        score = math.log1p(s)*(0.2+unif)*math.log1p(teach)*math.log1p(read)*(0.3+ext_share)*math.log1p(mod)
        rows.append(dict(tangential=Tn, T_nt=nt, T_cells=P[Tn]['n'], columnar=X, T_to_X=s, col_uniformity=round(unif,2), teacher_in=teach, readout=read, modulator_on_X=mod, T_ext_share=round(ext_share,2), T_context=ctx, score=round(score,1)))
rows.sort(key=lambda r: -r['score'])
with open(D/'tangential_store_screen.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(f"{'tangential':9s} {'nt':10s} {'n':>2s} -> {'columnar':9s} {'T->X':>5s} {'unif':>5s} {'teach':>6s} {'read':>5s} {'mod':>5s} {'ext':>4s} {'score':>6s}  context")
for r in rows[:30]: print(f"{r['tangential']:9s} {r['T_nt'][:10]:10s} {r['T_cells']:2d} -> {r['columnar']:9s} {r['T_to_X']:5d} {r['col_uniformity']:5.2f} {r['teacher_in']:6d} {r['readout']:5d} {r['modulator_on_X']:5d} {r['T_ext_share']:4.2f} {r['score']:6.1f}  {r['T_context'][:60]}")
