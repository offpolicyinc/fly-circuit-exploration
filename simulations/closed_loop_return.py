#!/usr/bin/env python3
"""Closed-loop test of the synaptic path-integration hypothesis.
Agent: heading H (compass, exact), walks an outbound random path from food, then 'wants to return'.
Memory: weights W over hDeltaJ columns, potentiated by the hDeltaB travel-direction bump through the
measured hDeltaB->hDeltaJ kernel while a walking-gated modulator (FB4M-like) is on; zeroed at food (OA-VPM3-like).
Readout: hDeltaJ activity = W * (presynaptic hDeltaB activity arriving at that column) [+ optional tonic drive],
passed through the measured hDeltaJ->FC2A kernel (the ~180 deg anatomical shift) to give the FC2 goal bump.
Steering: PFL3-like: turn rate = k * sin(goal - heading) * goal_amplitude (Mussells Pires / Westeinde rule).
Reports final distance from food for several readout assumptions and noise levels."""
import csv, json, numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
N = 8; cols = np.arange(N)*2*np.pi/N
def kernel(pre, post):
    k = np.zeros(N); tot = 0
    for r in csv.DictReader(open(D/'fb_column_offsets.csv')):
        if r['type_pre'] == pre and r['type_post'] == post: k[int(r['offset']) % N] += int(r['weight']); tot += int(r['weight'])
    return k/tot
def circ(k): return np.array([[k[(j-i) % N] for i in range(N)] for j in range(N)])
A_in = circ(kernel('hDeltaB', 'hDeltaJ')); A_out = circ(kernel('hDeltaJ', 'FC2A'))
def pv(w): z = np.sum(w*np.exp(1j*cols)); return np.angle(z), np.abs(z)
def trial(seed, readout='product', tonic=0.3, noise_heading=0.0, T_out=30, T_ret=60, dt=0.02, eta=1.0, k_turn=3.0, speed=1.0):
    rng = np.random.default_rng(seed)
    pos = 0j; H = rng.uniform(-np.pi, np.pi); W = np.zeros(N); comp = 0.0   # comp: compass error accumulates if noise
    # outbound: random walk with persistent heading, occasional turns
    for t in np.arange(0, T_out, dt):
        H += rng.normal(0, 0.8)*np.sqrt(dt); comp += rng.normal(0, noise_heading)*np.sqrt(dt)
        v = speed; pos += v*np.exp(1j*H)*dt
        b = v*np.maximum(0, np.cos(cols-(H+comp)))         # hDeltaB bump in (possibly drifted) compass frame
        W += dt*eta*(A_in @ b)                               # walking-gated potentiation
    d_out = abs(pos)
    # return: steer toward FC2 goal
    minD = d_out
    for t in np.arange(0, T_ret, dt):
        v = speed; comp += rng.normal(0, noise_heading)*np.sqrt(dt)
        b = v*np.maximum(0, np.cos(cols-(H+comp)))
        pre = A_in @ b
        if readout == 'product': act = W*(pre + tonic)     # hDeltaJ activity = weights x presynaptic drive (+ tonic component)
        elif readout == 'tonic': act = W*np.ones(N)           # weights read by uniform presynaptic drive
        goal = A_out @ act                                     # FC2 bump after the hDeltaJ->FC2 anatomical shift
        g_ang, g_amp = pv(goal)
        g_ang_world = g_ang - comp                             # goal is expressed in compass frame; convert for physics (comp=0 if no noise)
        turn = k_turn*np.sin(g_ang - (H+comp))*min(1.0, g_amp/ (np.sum(np.abs(W))+1e-9)*N)   # PFL3 rule, amplitude-scaled
        H += turn*dt + rng.normal(0, 0.3)*np.sqrt(dt)
        pos += v*np.exp(1j*H)*dt
        W += dt*eta*(A_in @ b)                                # keep integrating on the way back
        minD = min(minD, abs(pos))
        if abs(pos) < 0.5: return dict(outbound_dist=d_out, min_return_dist=abs(pos), returned=True, t_return=t)
    return dict(outbound_dist=d_out, min_return_dist=minD, returned=False, t_return=None)
res = {}
for readout in ('product', 'tonic'):
    for noise in (0.0, 0.05, 0.15):
        R = [trial(s, readout=readout, noise_heading=noise) for s in range(40)]
        frac = np.mean([r['returned'] for r in R]); md = np.median([r['min_return_dist'] for r in R]); od = np.median([r['outbound_dist'] for r in R])
        res[f'{readout}|noise{noise}'] = dict(returned_frac=float(frac), median_min_dist=float(md), median_outbound=float(od))
        print(f"readout={readout:8s} compass_noise={noise:.2f}  returned {frac*100:5.1f}%  median closest approach {md:5.2f} (outbound {od:5.2f})")
# control: no memory (W=0) -> random walk
R = []
for s in range(40):
    rng = np.random.default_rng(s); pos = 0j; H = 0.0
    for t in np.arange(0, 30, 0.02): H += rng.normal(0, 0.8)*np.sqrt(0.02); pos += np.exp(1j*H)*0.02
    d0 = abs(pos); m = d0
    for t in np.arange(0, 60, 0.02): H += rng.normal(0, 0.8)*np.sqrt(0.02); pos += np.exp(1j*H)*0.02; m = min(m, abs(pos))
    R.append(m)
print(f"control (no memory, random walk): median closest approach {np.median(R):5.2f}")
res['control_random_walk_median_min_dist'] = float(np.median(R))
print('\nkernels: hDeltaB->hDeltaJ', np.round(kernel('hDeltaB','hDeltaJ'),2), '\n         hDeltaJ->FC2A ', np.round(kernel('hDeltaJ','FC2A'),2))
(ROOT/'simulations'/'closed_loop_return_results.json').write_text(json.dumps(res, indent=1)+'\n')
