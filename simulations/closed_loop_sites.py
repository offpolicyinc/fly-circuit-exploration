#!/usr/bin/env python3
"""Closed-loop return test for every candidate synaptic-storage site, each with its own measured
input kernel (pre -> site) and readout path (site -> FC2 -> PFL3 or site -> PFL3 directly).
Sites: hDeltaJ (via FC2A), hDeltaH (via FC2B), hDeltaG (via FC2B), hDeltaA (direct to PFL3), hDeltaI (direct),
PFR_a (via hDeltaA -> PFL3), and the PFN->hDeltaB site (weights on hDeltaB read via hDeltaJ -> FC2A).
Same agent and controller as closed_loop_return.py; 40 seeds; compass noise 0.05."""
import csv, json, numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
N = 8; cols = np.arange(N)*2*np.pi/N
def kernel(pre, post):
    k = np.zeros(N); tot = 0
    for r in csv.DictReader(open(D/'fb_column_offsets.csv')):
        if r['type_pre'] == pre and r['type_post'] == post: k[int(r['offset']) % N] += int(r['weight']); tot += int(r['weight'])
    return k/tot if tot else None
def circ(k): return np.array([[k[(j-i) % N] for i in range(N)] for j in range(N)])
def pv(w): z = np.sum(w*np.exp(1j*cols)); return np.angle(z), np.abs(z)
SITES = {
 'hDeltaJ -> FC2A':      dict(kin=('hDeltaB','hDeltaJ'), kout=[('hDeltaJ','FC2A'), ('FC2A','PFL3')]),
 'hDeltaH -> FC2B':      dict(kin=('hDeltaB','hDeltaH'), kout=[('hDeltaH','FC2B'), ('FC2B','PFL3')]),
 'hDeltaG -> FC2B':      dict(kin=('hDeltaB','hDeltaG'), kout=[('hDeltaG','FC2B'), ('FC2B','PFL3')]),
 'hDeltaA -> PFL3':      dict(kin=('hDeltaB','hDeltaA'), kout=[('hDeltaA','PFL3')]),
 'hDeltaI -> PFL3':      dict(kin=('hDeltaB','hDeltaI'), kout=[('hDeltaI','PFL3')]),
 'PFR_a -> hDeltaA':     dict(kin=('hDeltaB','PFR_a'),   kout=[('PFR_a','hDeltaA'), ('hDeltaA','PFL3')]),
 'hDeltaB(PFN site) -> hDeltaJ -> FC2A': dict(kin=None, kout=[('hDeltaB','hDeltaJ'), ('hDeltaJ','FC2A'), ('FC2A','PFL3')]),
}
def trial(seed, site, noise=0.05, T_out=30, T_ret=60, dt=0.02, k_turn=3.0):
    rng = np.random.default_rng(seed)
    A_in = circ(kernel(*site['kin'])) if site['kin'] else np.eye(N)
    A_outs = [circ(kernel(*p)) for p in site['kout']]
    pos = 0j; H = rng.uniform(-np.pi, np.pi); W = np.zeros(N); comp = 0.0
    for t in np.arange(0, T_out, dt):
        H += rng.normal(0, 0.8)*np.sqrt(dt); comp += rng.normal(0, noise)*np.sqrt(dt)
        pos += np.exp(1j*H)*dt; b = np.maximum(0, np.cos(cols-(H+comp))); W += dt*(A_in @ b)
    d_out = abs(pos); minD = d_out
    for t in np.arange(0, T_ret, dt):
        comp += rng.normal(0, noise)*np.sqrt(dt); b = np.maximum(0, np.cos(cols-(H+comp)))
        act = W*((A_in @ b) + 0.3)
        for A in A_outs: act = A @ act
        g_ang, g_amp = pv(act)
        turn = k_turn*np.sin(g_ang-(H+comp))*min(1.0, g_amp/(np.sum(np.abs(W))+1e-9)*N)
        H += turn*dt + rng.normal(0, 0.3)*np.sqrt(dt); pos += np.exp(1j*H)*dt; W += dt*(A_in @ b)
        minD = min(minD, abs(pos))
        if abs(pos) < 0.5: return d_out, abs(pos), True
    return d_out, minD, False
res = {}
print(f"{'site':40s} {'in off':>7s} {'in conc':>8s} {'returned':>9s} {'closest':>8s}")
stats = {(r['type_pre'], r['type_post']): (float(r['mean_offset_deg']), float(r['resultant_length'])) for r in csv.DictReader(open(D/'fb_offset_stats.csv'))}
for name, site in SITES.items():
    if site['kin'] and kernel(*site['kin']) is None or any(kernel(*p) is None for p in site['kout']): print(name, 'missing kernel'); continue
    R = [trial(s, site) for s in range(40)]
    frac = np.mean([r[2] for r in R]); md = np.median([r[1] for r in R])
    off, conc = stats.get(site['kin'], (float('nan'), float('nan'))) if site['kin'] else (0.0, 1.0)
    res[name] = dict(returned_frac=float(frac), median_closest=float(md), in_offset=off, in_conc=conc)
    print(f"{name:40s} {off:7.0f} {conc:8.2f} {frac*100:8.1f}% {md:8.2f}")
(ROOT/'simulations'/'closed_loop_sites_results.json').write_text(json.dumps(res, indent=1)+'\n')
