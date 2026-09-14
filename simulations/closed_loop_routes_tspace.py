#!/usr/bin/env python3
"""Closed-loop return through measured column kernels, with the travel bump anchored on the hDeltaB AXON
(Lyu 2022: T is imaged on hDeltaB terminals; hDeltaB labels are dendritic, Hulse 2021). Anchoring T on the axon
means the hDeltaB bump in label space sits at H+180, so every route is run with the bump written at H+180
(tspace=True) and, for comparison, at H (label space, as in closed_loop_sites.py). Routes are chains of measured
kernels from data/derived/fb_column_offsets.csv. Mixed routes sum several chains weighted by synapse count.
Same agent and controller as closed_loop_sites.py; 40 seeds; compass noise 0.05."""
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
ROUTES = {
 'hDeltaA -> PFL3 (direct)':                        (('hDeltaB','hDeltaA'), [[('hDeltaA','PFL3')]], [1]),
 'hDeltaA -> hDeltaI -> PFL3':                      (('hDeltaB','hDeltaA'), [[('hDeltaA','hDeltaI'),('hDeltaI','PFL3')]], [1]),
 'hDeltaA -> PFL3 + hDeltaA -> hDeltaI -> PFL3 (synapse-weighted)': (('hDeltaB','hDeltaA'), [[('hDeltaA','PFL3')], [('hDeltaA','hDeltaI'),('hDeltaI','PFL3')]], [3881, 1388]),
 'hDeltaI -> PFL3 (direct)':                        (('hDeltaB','hDeltaI'), [[('hDeltaI','PFL3')]], [1]),
 'hDeltaH -> FC2B -> PFL3 (direct)':                (('hDeltaB','hDeltaH'), [[('hDeltaH','FC2B'),('FC2B','PFL3')]], [1]),
 'hDeltaH -> FC2B -> hDeltaM -> PFL3':              (('hDeltaB','hDeltaH'), [[('hDeltaH','FC2B'),('FC2B','hDeltaM'),('hDeltaM','PFL3')]], [1]),
 'hDeltaH -> FC2B -> {PFL3 direct + via hDeltaM} (synapse-weighted)': (('hDeltaB','hDeltaH'), [[('hDeltaH','FC2B'),('FC2B','PFL3')], [('hDeltaH','FC2B'),('FC2B','hDeltaM'),('hDeltaM','PFL3')]], [2478, 1073]),
 'hDeltaJ -> FC2A -> PFL3 (direct)':                (('hDeltaB','hDeltaJ'), [[('hDeltaJ','FC2A'),('FC2A','PFL3')]], [1]),
 'hDeltaG -> FC2C -> PFL3 (direct)':                (('hDeltaB','hDeltaG'), [[('hDeltaG','FC2C'),('FC2C','PFL3')]], [1]),
}
def readout_error(route, tspace, seeds=60, T=40, dt=0.02):
    """open-loop: angular error between the route's readout direction (base frame) and the true home direction"""
    kin, chains, wts = route; A_in = circ(kernel(*kin)); chains = [[circ(kernel(*p)) for p in ch] for ch in chains]; wts = np.array(wts, float)/sum(wts)
    off = np.pi if tspace else 0.0; errs = []
    for s in range(seeds):
        rng = np.random.default_rng(s); pos = 0j; H = rng.uniform(-np.pi, np.pi); W = np.zeros(N)
        for i, t in enumerate(np.arange(0, T, dt)):
            H += rng.normal(0, 0.8)*np.sqrt(dt); pos += np.exp(1j*H)*dt; b = np.maximum(0, np.cos(cols-(H+off))); W += dt*(A_in @ b)
            if i % 100 == 99 and abs(pos) > 1:
                base = W*((A_in @ b) + 0.3); act = np.zeros(N)
                for wt, ch in zip(wts, chains):
                    a = base.copy()
                    for A in ch: a = A @ a
                    act += wt*a
                g, amp = pv(act); home = np.angle(-pos); errs.append(abs(((g-home+np.pi) % (2*np.pi))-np.pi))
    return float(np.degrees(np.median(errs)))
def trial(seed, route, tspace, noise=0.05, T_out=30, T_ret=60, dt=0.02, k_turn=3.0):
    rng = np.random.default_rng(seed); kin, chains, wts = route
    A_in = circ(kernel(*kin)); chains = [[circ(kernel(*p)) for p in ch] for ch in chains]; wts = np.array(wts, float)/sum(wts)
    off = np.pi if tspace else 0.0
    pos = 0j; H = rng.uniform(-np.pi, np.pi); W = np.zeros(N); comp = 0.0
    def bump(h): return np.maximum(0, np.cos(cols-(h+off)))
    for t in np.arange(0, T_out, dt):
        H += rng.normal(0, 0.8)*np.sqrt(dt); comp += rng.normal(0, noise)*np.sqrt(dt)
        pos += np.exp(1j*H)*dt; W += dt*(A_in @ bump(H+comp))
    d_out = abs(pos); minD = d_out
    for t in np.arange(0, T_ret, dt):
        comp += rng.normal(0, noise)*np.sqrt(dt); b = bump(H+comp)
        base = W*((A_in @ b) + 0.3); act = np.zeros(N)
        for wt, ch in zip(wts, chains):
            a = base.copy()
            for A in ch: a = A @ a
            act += wt*a
        g_ang, g_amp = pv(act)
        turn = k_turn*np.sin(g_ang-(H+comp))   # PFL3/FC2 columns are in the base (PB-FB) frame; only the hDeltaB label frame is offset*min(1.0, g_amp/(np.sum(np.abs(W))+1e-9)*N)
        H += turn*dt + rng.normal(0, 0.3)*np.sqrt(dt); pos += np.exp(1j*H)*dt; W += dt*(A_in @ b)
        minD = min(minD, abs(pos))
        if abs(pos) < 0.5: return d_out, abs(pos), True
    return d_out, minD, False
res = {}
print(f"{'route':70s} {'T on axon: err':>14s} {'ret%':>6s} {'closest':>8s} | {'label space: err':>16s} {'ret%':>6s} {'closest':>8s}")
for name, route in ROUTES.items():
    out = {}
    for tspace in (True, False):
        R = [trial(s, route, tspace) for s in range(40)]
        out['axon' if tspace else 'label'] = (float(np.mean([r[2] for r in R])), float(np.median([r[1] for r in R])), readout_error(route, tspace))
    res[name] = dict(T_on_axon_readout_err_deg=out['axon'][2], T_on_axon_returned=out['axon'][0], T_on_axon_closest=out['axon'][1], label_space_readout_err_deg=out['label'][2], label_space_returned=out['label'][0], label_space_closest=out['label'][1])
    print(f"{name:70s} {out['axon'][2]:13.0f}° {out['axon'][0]*100:5.0f}% {out['axon'][1]:8.2f} | {out['label'][2]:15.0f}° {out['label'][0]*100:5.0f}% {out['label'][1]:8.2f}")
(ROOT/'simulations'/'closed_loop_routes_tspace_results.json').write_text(json.dumps(res, indent=1)+'\n')
