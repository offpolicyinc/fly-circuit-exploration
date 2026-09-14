#!/usr/bin/env python3
"""Compass-brake robustness: the same ring attractor as eb_epg_pen_loop.py, with the EB-side EPG->PEN contact
implemented three ways: (A) somatic drive added to the PEN input (original), (B) presynaptic gain on the PEN's
EB terminals (axo-axonic modulation of release, multiplicative), (C) somatic drive but with divisive normalisation
of PEN activity (population gain control). Reports rotation gain and dark stability for each at the measured ratio."""
import json, numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
NW = 16; NG = 8
wedge_of = {('L', g): 2*g for g in range(NG)}; wedge_of.update({('R', g): 2*(NG-1-g)+1 for g in range(NG)})
ang = np.arange(NW)*2*np.pi/NW
def pv(r): z = np.sum(r*np.exp(1j*ang)); return np.angle(z), np.abs(z)/max(1e-9, r.sum())
def build(w_pb, w_eb, w_pen_epg):
    E2P_pb = np.zeros((2*NG, NW)); E2P_eb = np.zeros((2*NG, NW)); P2E = np.zeros((NW, 2*NG)); idx = 0; shift = {'L': -2, 'R': +2}
    for side in 'LR':
        for g in range(NG):
            w0 = wedge_of[(side, g)]; tile = [(w0+shift[side]) % NW, (w0+shift[side]+(1 if side == 'L' else -1)) % NW]
            E2P_pb[idx, w0] += w_pb
            for t in tile: E2P_eb[idx, t] += w_eb/2; P2E[t, idx] += w_pen_epg/2
            idx += 1
    return E2P_pb, E2P_eb, P2E
def simulate(mode, w_eb, vel, T=6.0, dt=0.002, tau=0.05, w_pb=1.0, w_pen_epg=1.6, w_inh=1.2, w_epg_self=0.6, seed=0):
    rng = np.random.default_rng(seed); Epb, Eeb, P2E = build(w_pb, w_eb, w_pen_epg)
    e = np.maximum(0, np.cos(ang)); p = np.zeros(2*NG); log = []
    Wee = np.array([[w_epg_self*np.exp(-((i-j+NW/2) % NW-NW/2)**2/2.0) for j in range(NW)] for i in range(NW)])
    for t in np.arange(0, T, dt):
        gainL, gainR = 1+vel, 1-vel
        if mode == 'A':   # somatic drive (original)
            pin = Epb @ e + Eeb @ e
        elif mode == 'B': # presynaptic: EB contact scales the PEN's own release, not its firing
            pin = Epb @ e
        elif mode == 'C': # somatic drive with divisive normalisation of the PEN population
            pin = Epb @ e + Eeb @ e
        pin = pin.copy(); pin[:NG] *= gainL; pin[NG:] *= gainR
        p += dt/tau*(-p + np.maximum(0, pin))
        if mode == 'C': p_eff = p/(1 + p.sum()/NG)
        elif mode == 'B': p_eff = p*(1 + (Eeb @ e)/max(1e-9, w_pb))*(1/(1+w_eb))   # release gain, renormalised so total drive matches mode A at rest
        else: p_eff = p
        ein = Wee @ e + P2E @ p_eff - w_inh*e.mean()*NW/4 + rng.normal(0, 0.02, NW)
        e += dt/tau*(-e + np.maximum(0, ein)); e = np.minimum(e, 5)
        if t >= T/2: log.append(pv(e)[0])
    a = np.unwrap(np.array(log)); return dict(bump_len=float(pv(e)[1]), drift_deg_per_s=float(np.degrees((a[-1]-a[0])/(T/2))))
res = {}
for mode, label in [('A', 'somatic drive (original)'), ('B', 'presynaptic release gain'), ('C', 'somatic drive + divisive normalisation')]:
    for w_eb in [0.0, 1.0, 2.7]:
        dark = simulate(mode, w_eb, 0.0); rot = simulate(mode, w_eb, 0.3)
        res[f'{label} | EB/PB = {w_eb}'] = dict(dark_bump_len=round(dark['bump_len'], 3), dark_drift=round(dark['drift_deg_per_s'], 1), rotation_gain_deg_s=round(rot['drift_deg_per_s'], 1), rot_bump_len=round(rot['bump_len'], 3))
        print(f"{label:42s} EB/PB={w_eb:3.1f}  dark bump={dark['bump_len']:.2f} drift={dark['drift_deg_per_s']:6.1f}  rotation={rot['drift_deg_per_s']:7.1f} deg/s bump={rot['bump_len']:.2f}")
(ROOT/'simulations'/'eb_epg_pen_loop_variants_results.json').write_text(json.dumps(res, indent=1)+'\n')
