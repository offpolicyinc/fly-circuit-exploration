#!/usr/bin/env python3
"""Uniform screen of candidate SYNAPTIC storage sites: every (pre, post) columnar pair where pre carries a
heading/velocity/travel bump. For each site, with the same criteria:
  syn: synapses pre->post; conc: phase concentration (resultant length) and mean offset (deg)
  cells_hit: fraction of post cells receiving >=20 synapses from pre (column coverage)
  DA, OA, 5HT: modulator synapses onto post (dopamine FB types + PPL/PAM if present; OA-VPM3/OA-VUMa; FB4Y/ExR3/5HT)
  mod_uniformity: min/max across post columns of (DA+OA) synapses
  read1: post -> FC2 (goal) and post -> PFL3/PFL2 (steer) synapses; read2: best two-hop post -> X -> FC2/PFL
  ext_reward: OA-VPM3 synapses onto post (from full-graph edge list)
Writes data/derived/synaptic_site_screen.csv and prints a ranked table."""
import csv, json, re, math
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
P = json.load(open(D/'cx_type_profiles.json'))
cells = {int(r['bodyId']): r for r in csv.DictReader(open(D/'cx_cells.csv'))}
T = {b: r['type'] for b, r in cells.items()}
ncol = defaultdict(int)
for b, r in cells.items():
    m = re.search(r'_C(\d+)', r['instance'])
    if m: ncol[r['type']] = max(ncol[r['type']], int(m.group(1)))
def colidx(b):
    m = re.search(r'_C(\d+)', cells[b]['instance']); return int(m.group(1)) if m else None
COL = sorted({t for b, t in T.items() if colidx(b) is not None})
E = defaultdict(int); cellE = defaultdict(int)
for r in csv.DictReader(open(D/'cx_cell_edges.csv')):
    a, b, w = int(r['body_pre']), int(r['body_post']), int(r['weight']); E[(T[a], T[b])] += w; cellE[(a, b)] += w
stats = {}
for r in csv.DictReader(open(D/'fb_offset_stats.csv')): stats[(r['type_pre'], r['type_post'])] = (float(r['mean_offset_deg']), float(r['resultant_length']))
ext = defaultdict(int)
for r in csv.DictReader(open(D/'cx_type_edges.csv')): ext[(r['type_pre'], r['type_post'])] += int(r['weight'])
DA = [t for t in P if max(P[t]['nt'], key=P[t]['nt'].get) == 'dopamine']
OA_EXT = ['OA-VPM3', 'OA-VPM4', 'OA-VUMa1', 'OA-VUMa2', 'OA-VUMa3', 'OA-VUMa4', 'OA-VUMa5', 'OA-VUMa6', 'OA-VUMa7', 'OA-VUMa8']
SER = [t for t in P if max(P[t]['nt'], key=P[t]['nt'].get) == 'serotonin']
PRE = ['hDeltaB', 'PFNd', 'PFNv', 'PFNa', 'PFR_a', 'PFR_b', 'hDeltaA', 'hDeltaI', 'hDeltaJ', 'hDeltaK', 'PFGs', 'hDeltaH', 'hDeltaG', 'vDeltaM', 'vDeltaK', 'FC2A', 'FC2B', 'FC2C', 'Delta7', 'EPG']
GOAL = ['FC2A', 'FC2B', 'FC2C']; STEER = ['PFL3', 'PFL2']
rows = []
for pre in PRE:
    for post in COL:
        if pre == post or E[(pre, post)] < 300: continue
        postcells = [b for b in cells if T[b] == post]
        hit = sum(1 for b in postcells if sum(w for (a, bb), w in cellE.items() if bb == b and T[a] == pre) >= 20)
        da = sum(E[(d, post)] for d in DA); oa = sum(ext[(o, post)] for o in OA_EXT); ser = sum(E[(s, post)] for s in SER)
        percol = Counter()
        for (a, b), w in cellE.items():
            if b in postcells and T[a] in DA: percol[colidx(b)] += w
        unif = (min(percol.values())/max(percol.values())) if percol and max(percol.values()) else 0
        read_goal = sum(E[(post, g)] for g in GOAL); read_steer = sum(E[(post, s)] for s in STEER)
        best2 = ('', 0)
        for X in COL:
            if X in (pre, post): continue
            v = min(E[(post, X)], sum(E[(X, g)] for g in GOAL+STEER))
            if v > best2[1]: best2 = (X, v)
        mo, rl = stats.get((pre, post), (float('nan'), float('nan')))
        po, pl = stats.get((post, 'FC2B'), stats.get((post, 'PFL3'), (float('nan'), float('nan'))))
        rows.append(dict(pre=pre, post=post, syn=E[(pre, post)], offset_deg=mo, conc=rl, post_cells=len(postcells), cells_hit_frac=round(hit/len(postcells), 2),
                         DA=da, OA=oa, SER=ser, DA_col_uniformity=round(unif, 2), read_goal=read_goal, read_steer=read_steer, best_2hop=best2[0], best_2hop_syn=best2[1],
                         readout_offset_deg=po, post_nt=max(P[post]['nt'], key=P[post]['nt'].get), post_total_in=P[post]['total_in']))
def score(r):
    # all criteria must be present: geometric-style score on log scales
    s = math.log1p(r['syn']) * (0.3+r['conc']) * math.log1p(r['DA']+r['OA']) * math.log1p(max(r['read_goal']+r['read_steer'], r['best_2hop_syn'])) * (0.5+r['cells_hit_frac'])
    return s
for r in rows: r['score'] = round(score(r), 1)
rows.sort(key=lambda r: -r['score'])
with open(D/'synaptic_site_screen.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(f"{'pre':8s}->{'post':9s} {'syn':>6s} {'off':>5s} {'conc':>5s} {'hit':>4s} {'DA':>5s} {'OA':>5s} {'unif':>5s} {'goal':>5s} {'steer':>5s} {'2hop':>14s} {'rdoff':>6s} {'score':>6s}")
for r in rows[:40]:
    print(f"{r['pre']:8s}->{r['post']:9s} {r['syn']:6d} {r['offset_deg']:5.0f} {r['conc']:5.2f} {r['cells_hit_frac']:4.2f} {r['DA']:5d} {r['OA']:5d} {r['DA_col_uniformity']:5.2f} {r['read_goal']:5d} {r['read_steer']:5d} {r['best_2hop']+':'+str(r['best_2hop_syn']):>14s} {r['readout_offset_deg']:6.0f} {r['score']:6.1f}")
