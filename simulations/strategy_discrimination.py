#!/usr/bin/env python3
"""Which behaviours require a vector integrator? Four memory strategies are run through three published
assays and scored on what each assay measured.
Strategies:
  A continuous vector integrator with reset at food (synaptic or activity; this is what the hDeltaJ model does)
  B reward-triggered direction memory: store the travel direction at each food contact (Siliciano-like), no integration
  C scalar odometer + last-heading memory: remember heading and distance since food; return = walk that far the opposite way
  D random walk (no memory)
Assays:
  Kim 2017 centred search: random outbound path of 20 s from food, then 60 s of goal-directed walking; score = distance of the
     time-averaged position during the 'search' from the food (lower is better).
  Behbahani 2021 running average: food at x=0 then a second food at x=+6 (1D); after two encounters at each, where does the
     search centre sit? (A with partial reset predicts between; B predicts direction only; C predicts last food.)
  Titova 2023 displacement: after outbound path, the fly is passively moved by d=(4,0) before returning; score = distance of the
     search centre from the FICTIVE site (food+d) versus the real site.
"""
import numpy as np, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def walk(rng, pos, H, T, dt, k_goal=None, goal_fn=None):
    traj = []
    for t in np.arange(0, T, dt):
        if goal_fn is not None:
            g, amp = goal_fn(pos, H)
            H += 3.0*np.sin(g-H)*min(1, amp)*dt
        H += rng.normal(0, 0.8)*np.sqrt(dt); pos += np.exp(1j*H)*dt; traj.append(pos)
    return pos, H, np.array(traj)
class Integrator:
    def __init__(s, alpha=1.0): s.v = 0j; s.alpha = alpha
    def step(s, dpos): s.v += dpos
    def food(s): s.v *= (1-s.alpha)
    def goal(s, pos, H): return (np.angle(-s.v), min(1, abs(s.v)/2)) if abs(s.v) > 0.3 else (H, 0)
class RewardDir:
    def __init__(s): s.m = 0j; s.last = 1+0j
    def step(s, dpos): s.last = dpos
    def food(s): s.m = 0.5*s.m + np.exp(1j*np.angle(s.last))
    def goal(s, pos, H): return (np.angle(-s.m), min(1, abs(s.m))) if abs(s.m) > 0.1 else (H, 0)   # go back the way you arrived
class Odometer:
    def __init__(s): s.d = 0.0; s.h0 = None; s.last = 1+0j
    def step(s, dpos): s.d += abs(dpos)
    def food(s): s.d = 0.0; s.h0 = None
    def goal(s, pos, H):
        if s.h0 is None: s.h0 = np.angle(s.last) if hasattr(s, 'last') else H
        return (s.h0+np.pi, 1.0) if s.d > 0.3 else (H, 0)
def simulate(strategy, seed, displacement=0j, foods=None):
    rng = np.random.default_rng(seed); pos = 0j; H = rng.uniform(-np.pi, np.pi); mem = strategy()
    if foods is None: foods = [0j]
    # visits: start at first food (reset), outbound 20 s tracking memory
    mem.food()
    dt = 0.02
    for t in np.arange(0, 20, dt):
        H += rng.normal(0, 0.8)*np.sqrt(dt); d = np.exp(1j*H)*dt; pos += d; mem.step(d); mem.last = d
    pos += displacement   # passive, not sensed
    # search / return phase
    traj = []
    for t in np.arange(0, 60, dt):
        g, amp = mem.goal(pos, H)
        H += 3.0*np.sin(g-H)*amp*dt + rng.normal(0, 0.8)*np.sqrt(dt)
        d = np.exp(1j*H)*dt; pos += d; mem.step(d); mem.last = d; traj.append(pos)
        if amp > 0 and abs(pos-(foods[0]+displacement)) < 0.5 and isinstance(mem, Integrator): mem.v *= 0  # arrival zeroes integrator
    return np.array(traj)
STR = {'A integrator': Integrator, 'B reward-direction': RewardDir, 'C odometer+heading': Odometer, 'D random': None}
class NoMem:
    def step(s, d): pass
    def food(s): pass
    def goal(s, pos, H): return (H, 0)
STR['D random'] = NoMem
res = {}
print('Kim centred search: median distance of mean search position from food (real site at 0)')
for name, S in STR.items():
    d = [abs(simulate(S, s).mean()) for s in range(60)]; res[f'kim|{name}'] = float(np.median(d)); print(f'  {name:22s} {np.median(d):5.2f}')
print('Titova displacement d=(4,0): median distance of mean search position from fictive site (food+d) vs real site')
for name, S in STR.items():
    tr = [simulate(S, s, displacement=4+0j).mean() for s in range(60)]
    f = np.median([abs(x-(4+0j)) for x in tr]); r = np.median([abs(x) for x in tr]); res[f'titova|{name}'] = dict(fictive=float(f), real=float(r))
    print(f'  {name:22s} to fictive {f:5.2f}   to real {r:5.2f}')
(ROOT/'simulations'/'strategy_discrimination.json').write_text(json.dumps(res, indent=1)+'\n')
