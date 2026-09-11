#!/usr/bin/env python3
"""Can the measured hDeltaB -> PFR_a/PFR_b wiring integrate travel direction into a displacement
vector? Rate model on 8 FB columns using MaleCNS column-offset kernels (data/derived/fb_column_offsets.csv).
Sweeps recurrent gain and an optional uniform (tangential-like) inhibition; reports whether the PFR
population vector tracks instantaneous travel direction or the integrated displacement."""
import csv, json, numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
N = 8
def kernel(pre, post):
    k = np.zeros(N); tot = 0
    for r in csv.DictReader(open(D/'fb_column_offsets.csv')):
        if r['type_pre'] == pre and r['type_post'] == post:
            k[int(r['offset']) % N] += int(r['weight']); tot += int(r['weight'])
    return k / tot if tot else k
def circ(k):  # circulant weight matrix W[post, pre] = k[(post-pre) mod N]
    return np.array([[k[(j - i) % N] for i in range(N)] for j in range(N)])
K = {p: kernel(*p) for p in [('hDeltaB','PFR_a'),('hDeltaB','PFR_b'),('PFR_b','PFR_a'),('PFR_a','PFR_b'),('PFR_b','PFR_b'),('PFR_a','PFR_a')]}
S = {('hDeltaB','PFR_a'):6717, ('hDeltaB','PFR_b'):5787, ('PFR_b','PFR_a'):2199, ('PFR_a','PFR_b'):579, ('PFR_b','PFR_b'):1722, ('PFR_a','PFR_a'):387}
ref = S[('hDeltaB','PFR_a')]
W = {p: circ(K[p]) * S[p] / ref for p in K}   # relative synapse counts
cols = np.arange(N) * 2*np.pi/N
def pv(r):  # population vector: angle, length
    z = np.sum(r * np.exp(1j*cols)); return np.angle(z), np.abs(z)/max(1e-9, r.sum())
def run(g_rec, g_in, inh, T=20.0, dt=0.005, tau=0.1, path='L'):
    ra = np.zeros(N); rb = np.zeros(N); disp = 0j; log = []
    for t in np.arange(0, T, dt):
        # travel direction: east for first half, north for second half ('L' path); speed 1
        theta = 0.0 if (t < T/2) else np.pi/2
        v = np.exp(1j*theta); disp += v*dt
        h = g_in * np.maximum(0, np.cos(cols - theta))          # hDeltaB bump
        Ia = W[('hDeltaB','PFR_a')] @ h + g_rec*(W[('PFR_b','PFR_a')] @ rb + W[('PFR_a','PFR_a')] @ ra) - inh*(ra.mean()+rb.mean())
        Ib = W[('hDeltaB','PFR_b')] @ h + g_rec*(W[('PFR_a','PFR_b')] @ ra + W[('PFR_b','PFR_b')] @ rb) - inh*(ra.mean()+rb.mean())
        ra += dt/tau * (-ra + np.maximum(0, Ia)); rb += dt/tau * (-rb + np.maximum(0, Ib))
        if abs(t - (T/2 - dt)) < dt/2 or abs(t - (T - dt)) < dt/2:
            ang, ln = pv(ra + rb); log.append(dict(t=round(t,2), travel_dir=float(np.degrees(theta)), displacement_dir=float(np.degrees(np.angle(disp))), pfr_dir=float(np.degrees(ang)), pfr_vec_len=float(ln), pfr_mean_rate=float((ra+rb).mean())))
    return log
# eigen-analysis of the linear recurrent system for the cosine mode vs the uniform mode
def modes(g_rec, inh):
    A = np.block([[g_rec*W[('PFR_a','PFR_a')], g_rec*W[('PFR_b','PFR_a')]],[g_rec*W[('PFR_a','PFR_b')], g_rec*W[('PFR_b','PFR_b')]]]) - inh*np.ones((2*N,2*N))/(2*N)*2
    ev = np.linalg.eigvals(A)
    u = np.ones(2*N)/np.sqrt(2*N); c = np.concatenate([np.cos(cols), np.cos(cols)]); c /= np.linalg.norm(c)
    return dict(uniform_mode_gain=float(np.real(u @ A @ u)), cosine_mode_gain=float(np.real(c @ A @ c)), max_eig=float(np.max(np.real(ev))))
out = {'kernels': {f'{a}->{b}': [round(x,3) for x in K[(a,b)]] for (a,b) in K}, 'runs': []}
for g_rec in [0.0, 0.5, 1.0, 1.5, 2.0, 3.0]:
    for inh in [0.0, 1.0, 2.0, 4.0]:
        m = modes(g_rec, inh); log = run(g_rec, 1.0, inh)
        out['runs'].append(dict(g_rec=g_rec, inh=inh, **m, end_of_leg1=log[0], end_of_leg2=log[1]))
(ROOT/'simulations'/'pfr_integrator_results.json').write_text(json.dumps(out, indent=1)+'\n')
print('kernels (offset 0..7):'); [print(f'  {k}: {v}') for k, v in out['kernels'].items()]
print(f"\n{'g_rec':>5} {'inh':>4} {'uniG':>6} {'cosG':>6} | leg2: travel  disp  PFRdir  veclen  meanrate")
for r in out['runs']:
    e = r['end_of_leg2']; print(f"{r['g_rec']:5.1f} {r['inh']:4.1f} {r['uniform_mode_gain']:6.2f} {r['cosine_mode_gain']:6.2f} | {e['travel_dir']:6.0f} {e['displacement_dir']:6.0f} {e['pfr_dir']:7.1f} {e['pfr_vec_len']:7.2f} {e['pfr_mean_rate']:9.2f}")
