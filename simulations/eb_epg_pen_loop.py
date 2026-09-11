#!/usr/bin/env python3
"""Does the ellipsoid-body EPG->PEN contact (tile-matched, 2.5-3x the PB contact in hemibrain)
change ring-attractor behaviour? 16-wedge EPG ring, 8 left + 8 right PEN populations.
Weights: EPG->PEN in PB (same glomerulus), EPG->PEN in EB (tile the PEN projects to),
PEN->EPG shifted by one glomerulus (opposite for L/R), Delta7-like global inhibition,
optional ExR4/ExR6-like global feedback. Compares bump stability in darkness and rotation gain
with the EB loop off, at the measured ratio, and doubled."""
import json, numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
NW = 16; NG = 8   # wedges; glomeruli per side
wedge_of = {('L', g): 2*g for g in range(NG)}; wedge_of.update({('R', g): 2*(NG-1-g)+1 for g in range(NG)})
ang = np.arange(NW) * 2*np.pi/NW
def pv(r): z = np.sum(r*np.exp(1j*ang)); return np.angle(z), np.abs(z)/max(1e-9, r.sum())
def build(w_pb, w_eb, w_pen_epg, w_inh, w_exr):
    # PEN(side,g) reads EPG of its own wedge (PB) and of its target tile (EB); writes to EPG at tile = own wedge shifted
    E2P = np.zeros((2*NG, NW)); P2E = np.zeros((NW, 2*NG)); idx = 0; shift = {'L': -2, 'R': +2}   # one glomerulus = two wedges
    for side in 'LR':
        for g in range(NG):
            w0 = wedge_of[(side, g)]; tile = [(w0 + shift[side]) % NW, (w0 + shift[side] + (1 if side=='L' else -1)) % NW]
            E2P[idx, w0] += w_pb
            for t in tile: E2P[idx, t] += w_eb/2; P2E[t, idx] += w_pen_epg/2
            idx += 1
    return E2P, P2E
def simulate(w_eb, vel, T=6.0, dt=0.002, tau=0.05, w_pb=1.0, w_pen_epg=1.6, w_inh=1.2, w_exr=0.0, w_epg_self=0.6, seed=0):
    rng = np.random.default_rng(seed); E2P, P2E = build(w_pb, w_eb, w_pen_epg, w_inh, w_exr)
    e = np.maximum(0, np.cos(ang)) ; p = np.zeros(2*NG); log = []
    Wee = np.array([[w_epg_self*np.exp(-((i-j+NW/2)%NW-NW/2)**2/2.0) for j in range(NW)] for i in range(NW)])  # local EPG excitation
    for t in np.arange(0, T, dt):
        gainL, gainR = 1+vel, 1-vel
        pin = E2P @ e - w_exr*e.sum()/NW; pin[:NG] *= gainL; pin[NG:] *= gainR
        p += dt/tau*(-p + np.maximum(0, pin))
        ein = Wee @ e + P2E @ p - w_inh*e.mean()*NW/4 - w_exr*e.sum()/NW + rng.normal(0, 0.02, NW)
        e += dt/tau*(-e + np.maximum(0, ein)); e = np.minimum(e, 5)
        if t >= T/2: log.append(pv(e)[0])
    a = np.unwrap(np.array(log)); return dict(bump_len=float(pv(e)[1]), drift_deg_per_s=float(np.degrees((a[-1]-a[0])/(T/2))), peak=float(e.max()))
res = {}
for label, w_eb in [('EB loop off', 0.0), ('EB loop = measured (2.7x PB)', 2.7), ('EB loop doubled (5.4x PB)', 5.4)]:
    for w_exr in [0.0, 0.3]:
        dark = simulate(w_eb, 0.0, w_exr=w_exr); rot = simulate(w_eb, 0.3, w_exr=w_exr)
        res[f'{label} | ExR feedback {w_exr}'] = dict(dark_bump_len=round(dark['bump_len'],3), dark_drift_deg_s=round(dark['drift_deg_per_s'],1), dark_peak=round(dark['peak'],2), rotation_gain_deg_s=round(rot['drift_deg_per_s'],1), rot_bump_len=round(rot['bump_len'],3), rot_peak=round(rot['peak'],2))
(ROOT/'simulations'/'eb_epg_pen_loop_results.json').write_text(json.dumps(res, indent=1)+'\n')
for k, v in res.items(): print(f'{k:48s}', v)
