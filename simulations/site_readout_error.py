#!/usr/bin/env python3
"""Controller-independent test of each candidate storage site: during a random outbound walk, store
weights through the measured input kernel; at 200 time points compute the goal readout through the
measured output path and measure the angular error between the readout direction and the true
direction home. Also the stored-vector length relative to an ideal store (cancellation from bimodal kernels)."""
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
 'hDeltaJ -> FC2A -> PFL3': (('hDeltaB','hDeltaJ'), [('hDeltaJ','FC2A'),('FC2A','PFL3')]),
 'hDeltaJ -> FC2B -> PFL3': (('hDeltaB','hDeltaJ'), [('hDeltaJ','FC2B'),('FC2B','PFL3')]),
 'hDeltaH -> FC2B -> PFL3': (('hDeltaB','hDeltaH'), [('hDeltaH','FC2B'),('FC2B','PFL3')]),
 'hDeltaG -> FC2B -> PFL3': (('hDeltaB','hDeltaG'), [('hDeltaG','FC2B'),('FC2B','PFL3')]),
 'hDeltaC -> FC2B -> PFL3': (('hDeltaB','hDeltaC'), [('hDeltaC','FC2B'),('FC2B','PFL3')]),
 'hDeltaA -> PFL3':         (('hDeltaB','hDeltaA'), [('hDeltaA','PFL3')]),
 'hDeltaI -> PFL3':         (('hDeltaB','hDeltaI'), [('hDeltaI','PFL3')]),
 'hDeltaM -> PFL3':         (('hDeltaB','hDeltaM'), [('hDeltaM','PFL3')]),
 'PFR_a -> hDeltaA -> PFL3':(('hDeltaB','PFR_a'),   [('PFR_a','hDeltaA'),('hDeltaA','PFL3')]),
 'PFR_a -> FC2A -> PFL3':   (('hDeltaB','PFR_a'),   [('PFR_a','FC2A'),('FC2A','PFL3')]),
 'PFN site (hDeltaB) -> hDeltaJ -> FC2A -> PFL3': (None, [('hDeltaB','hDeltaJ'),('hDeltaJ','FC2A'),('FC2A','PFL3')]),
 'hDeltaK -> PFGs (loop only)': (('hDeltaB','hDeltaK'), [('hDeltaK','PFGs')]),
 'ideal (0 in, 180 out)': ('ideal', None),
}
def run(site, seeds=60, T=40, dt=0.02):
    kin, kout = site
    if kin == 'ideal': A_in = np.eye(N); k = np.zeros(N); k[4] = 1; A_outs = [circ(k)]
    else:
        A_in = circ(kernel(*kin)) if kin else np.eye(N)
        A_outs = [circ(kernel(*p)) for p in kout]
        if any(a is None for a in A_outs): return None
    errs = []; lens = []
    for s in range(seeds):
        rng = np.random.default_rng(s); pos = 0j; H = rng.uniform(-np.pi, np.pi); W = np.zeros(N); ideal = np.zeros(N)
        for i, t in enumerate(np.arange(0, T, dt)):
            H += rng.normal(0, 0.8)*np.sqrt(dt); pos += np.exp(1j*H)*dt
            b = np.maximum(0, np.cos(cols-H)); W += dt*(A_in @ b); ideal += dt*b
            if i % 100 == 99 and abs(pos) > 1:
                act = W*((A_in @ b) + 0.3)
                for A in A_outs: act = A @ act
                g, amp = pv(act); home = np.angle(-pos)
                errs.append(abs(((g-home+np.pi) % (2*np.pi))-np.pi)); lens.append(pv(W)[1]/max(1e-9, pv(ideal)[1]))
    return np.degrees(np.median(errs)), np.degrees(np.percentile(errs, 75)), float(np.median(lens))
res = {}
print(f"{'site':46s} {'median |err|':>12s} {'75th pct':>9s} {'stored/ideal len':>16s}")
for name, site in SITES.items():
    r = run(site)
    if r is None: print(f'{name:46s} missing kernel'); continue
    res[name] = dict(median_err_deg=r[0], p75_err_deg=r[1], stored_len_ratio=r[2]); print(f"{name:46s} {r[0]:12.1f} {r[1]:9.1f} {r[2]:16.2f}")
(ROOT/'simulations'/'site_readout_error.json').write_text(json.dumps(res, indent=1)+'\n')
