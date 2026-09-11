#!/usr/bin/env python3
"""Cross-specimen check of the compass offset analysis using the public hemibrain v1.2
traced-adjacency export (data/raw/hemibrain/...; ROI-resolved), stdlib only.

Repeats scripts/compass_recurrence.py's wedge-offset binning on hemibrain, and uses the
ROI column to split EPG->PEN and PEN->EPG edges into PB, EB and NO contributions, which the
MaleCNS flat export cannot do. Writes data/derived/hemibrain_compass_offsets.csv and
hemibrain_epg_pen_by_roi.csv.
"""
import csv, re, json
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
H = ROOT/'data/raw/hemibrain/hemibrain-v1.2-all-traced-adjacencies'; OUT = ROOT/'data/derived'
TYPES = ['EPG','EPGt','PEN_a(PEN1)','PEN_b(PEN2)','PEG','Delta7']; N = 16
def gloms(inst):
    m = re.search(r'\)_((?:[LR]\d)+)', inst); return re.findall(r'[LR]\d', m.group(1)) if m else []
def wedge(g):
    s, k = g[0], int(g[1]); k = 1 if k == 9 else k
    return (2*k-2) % N if s == 'L' else (2*(9-k)-1) % N
def circ(d): d %= N; return d-N if d > N//2 else d
neu = {}
with open(H/'neurons.csv') as f:
    for r in csv.DictReader(f):
        if r['type'] in TYPES: neu[int(r['bodyId'])] = dict(type=r['type'], gloms=gloms(r['instance']), inst=r['instance'])
prof = defaultdict(lambda: defaultdict(int)); roi_prof = defaultdict(lambda: defaultdict(int)); roi_tot = defaultdict(int)
with open(H/'roi-connections.csv') as f:
    for r in csv.DictReader(f):
        a, b = int(r['bodyId_pre']), int(r['bodyId_post'])
        if a in neu and b in neu:
            A, B = neu[a], neu[b]; w = int(r['weight']); roi = r['roi']
            if not A['gloms'] or not B['gloms']: continue
            o = min((circ(wedge(gb)-wedge(ga)) for ga in A['gloms'] for gb in B['gloms']), key=abs)
            side = 'both' if A['type'] == 'Delta7' else A['gloms'][0][0]
            prof[(A['type'], side, B['type'])][o] += w
            roi_tot[(A['type'], B['type'], roi)] += w
            roi_prof[(A['type'], B['type'], roi)][o] += w
with open(OUT/'hemibrain_compass_offsets.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type_pre','side_pre','type_post','offset_wedges','weight'])
    for (tp, sd, tq), d in prof.items():
        for o, wt in sorted(d.items()): w.writerow([tp, sd, tq, o, wt])
with open(OUT/'hemibrain_epg_pen_by_roi.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type_pre','type_post','roi','offset_wedges','weight'])
    for (tp, tq, roi), d in roi_prof.items():
        for o, wt in sorted(d.items()): w.writerow([tp, tq, roi, o, wt])
print('cells', Counter(n['type'] for n in neu.values()))
def show(key):
    d = prof[key]; tot = sum(d.values())
    top = sorted(d.items(), key=lambda x: -x[1])[:4]
    print(f"{'|'.join(key):38s} total={tot:6d} within1={sum(v for o,v in d.items() if abs(o)<=1)/tot:.2f} top={[(o, round(v/tot,2)) for o,v in top]}")
for k in [('PEN_a(PEN1)','L','EPG'),('PEN_a(PEN1)','R','EPG'),('PEN_b(PEN2)','L','EPG'),('PEN_b(PEN2)','R','EPG'),('EPG','L','PEN_a(PEN1)'),('EPG','L','PEN_b(PEN2)'),('EPG','L','PEG'),('PEG','L','PEN_b(PEN2)'),('Delta7','both','EPG'),('EPG','L','Delta7'),('EPG','L','EPG')]: show(k)
print('\nEPG<->PEN by ROI (weight, share at offset 0, share at tile offsets ±2/±3):')
for (tp, tq, roi), d in sorted(roi_prof.items(), key=lambda x: -sum(x[1].values())):
    if {tp, tq} & {'EPG'} and {tp, tq} & {'PEN_a(PEN1)','PEN_b(PEN2)'} or (tp, tq) in [('EPG','EPG'),('EPG','PEG'),('PEG','PEN_b(PEN2)')]:
        tot = sum(d.values()); z = d.get(0,0)/tot; tile = sum(v for o,v in d.items() if abs(o) in (2,3))/tot
        print(f'{tp:12s}->{tq:12s} {roi:6s} {tot:6d}  off0={z:.2f} tile={tile:.2f}')
