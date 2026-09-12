#!/usr/bin/env python3
"""Synaptic (plasticity-based) path integrator built from the measured hDeltaB -> hDeltaJ / PFR_a
column kernels. Weights from the travel-direction bump onto a columnar target potentiate while a
walking-gated modulator is present, and are reset (fully or partially) by a reward signal.
Tests: (1) does the stored weight vector track the true displacement from the last reward?
(2) how does the readout depend on the anatomical column offset of the kernel? (3) what happens with
a speed-scaled vs a walking-gated modulator, and with partial reset (Behbahani running average)?"""
import csv, json, numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
N = 8; cols = np.arange(N)*2*np.pi/N
def kernel(pre, post):
    k = np.zeros(N); tot = 0
    for r in csv.DictReader(open(D/'fb_column_offsets.csv')):
        if r['type_pre'] == pre and r['type_post'] == post: k[int(r['offset']) % N] += int(r['weight']); tot += int(r['weight'])
    return k/tot
def circ(k): return np.array([[k[(j-i) % N] for i in range(N)] for j in range(N)])  # [post, pre]
def pv(w): z = np.sum(w*np.exp(1j*cols)); return np.angle(z), np.abs(z)
def run(target, path, modulator='walking', reset='full', eta=1.0, lam=0.0, dt=0.01):
    A = circ(kernel('hDeltaB', target))          # anatomical projection of hDeltaB bump onto target columns
    W = np.zeros(N)                                # column-specific gain stored at hDeltaB->target synapses
    log = []; disp = 0j
    for seg in path:                               # seg = (duration, speed, theta_deg) or ('reward', alpha)
        if seg[0] == 'reward':
            W *= (1-seg[1]); disp = 0j; log.append(('reward', float(np.degrees(pv(W)[0])), float(pv(W)[1]), 0.0, 0.0)); continue
        dur, speed, th = seg; th = np.radians(th)
        for _ in range(int(dur/dt)):
            b = speed*np.maximum(0, np.cos(cols-th))   # hDeltaB bump, amplitude ~ speed
            pre_at_target = A @ b                        # activity arriving at each target column
            mod = 1.0 if (modulator == 'walking' and speed > 0) else (speed if modulator == 'speed' else 0.0)
            W += dt*(eta*mod*pre_at_target - lam*W)
            disp += speed*np.exp(1j*th)*dt
        ang, ln = pv(W); log.append((f'{th_deg(th)}', float(np.degrees(ang)), float(ln), float(np.degrees(np.angle(disp))), float(abs(disp))))
    return log
def th_deg(th): return int(round(np.degrees(th)))
path = [(5, 1.0, 0), (5, 1.0, 90), (5, 0.5, 180), ('reward', 1.0), (4, 1.0, 45), (4, 1.0, 45), (2, 0.0, 0), (4, 1.0, 225)]
out = {}
for target in ('hDeltaJ', 'PFR_a'):
    for modulator in ('walking', 'speed'):
        log = run(target, path, modulator=modulator)
        out[f'{target}|{modulator}'] = log
        print(f'\n=== target {target}, modulator {modulator} ===')
        print(f"{'segment':>8s} {'W_dir':>7s} {'W_len':>6s} | {'disp_dir':>8s} {'disp_len':>8s} {'dir_err':>8s}")
        for s in log:
            err = ((s[1]-s[3]+180) % 360)-180 if s[0] != 'reward' and s[4] > 0 else float('nan')
            print(f"{s[0]:>8s} {s[1]:7.1f} {s[2]:6.2f} | {s[3]:8.1f} {s[4]:8.2f} {err:8.1f}")
print('\n=== partial reset (alpha=0.5) at each of three rewards at different places: running average ===')
path2 = [(5, 1.0, 0), ('reward', 0.5), (5, 1.0, 90), ('reward', 0.5), (5, 1.0, 90), ('reward', 0.5), (3, 1.0, 180)]
log = run('hDeltaJ', path2, modulator='walking'); out['hDeltaJ|partial_reset'] = log
for s in log: print(s)
(ROOT/'simulations'/'synaptic_path_integrator_results.json').write_text(json.dumps(out, indent=1)+'\n')
print('\nkernel offsets hDeltaB->hDeltaJ:', np.round(kernel('hDeltaB','hDeltaJ'),2), ' hDeltaB->PFR_a:', np.round(kernel('hDeltaB','PFR_a'),2))
