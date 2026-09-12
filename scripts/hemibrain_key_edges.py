#!/usr/bin/env python3
"""Replicate key MaleCNS type-level edges in hemibrain v1.2 (public traced adjacencies)."""
import csv
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; H = ROOT/'data/raw/hemibrain/hemibrain-v1.2-all-traced-adjacencies'
T = {int(r['bodyId']): r['type'] for r in csv.DictReader(open(H/'neurons.csv')) if r['type']}
E = defaultdict(int); tin = defaultdict(int)
with open(H/'total-connections.csv') as f:
    for r in csv.DictReader(f):
        a, b, w = int(r['bodyId_pre']), int(r['bodyId_post']), int(r['weight'])
        ta, tb = T.get(a), T.get(b)
        if tb: tin[tb] += w
        if ta and tb: E[(ta, tb)] += w
pairs = [('hDeltaB','hDeltaJ'),('hDeltaJ','FC2A'),('hDeltaJ','FC2B'),('FB1H','hDeltaJ'),('FB4M','hDeltaJ'),('FB4M','hDeltaB'),('FB4L','hDeltaB'),('OA-VPM3','hDeltaB'),('OA-VPM3','hDeltaJ'),('OA-VPM3','PFR_a'),('OA-VPM3','hDeltaH'),('OA-VPM3','PFGs'),('KCg-m','OA-VPM3'),('PFNv','FB4M'),('PFNd','FB4M'),('hDeltaB','FB4M'),('hDeltaB','PFR_a'),('PFNd','PFR_a'),('hDeltaB','FR1'),('FR1','FR1'),('FR1','MBON30'),('MBON21','FB4R'),('MBON09','FB4R'),('FB4R','hDeltaB'),('FS1A_a','oviIN'),('FS1A_b','oviIN'),('FS1A_c','oviIN'),('FC2C','oviIN'),('FC2B','oviIN'),('oviIN','FC2C'),('FB3A','PFNd'),('PFNd','FB3A'),('PS196_b','GLNO'),('GLNO','PEN_a(PEN1)'),('ExR7','LAL013'),('PFL3','LAL121'),('PFL3','DNa02'),('PFL2','DNa03'),('EL','ER4d'),('EL','ER4m'),('EL','ER3p_a'),('EPG','ER4m'),('EPG','ER6'),('ER5','EL'),('hDeltaM','PFL3'),('hDeltaA','PFL3'),('hDeltaI','PFL3'),('FC2C','PFL3'),('hDeltaK','PFGs'),('PFGs','hDeltaK'),('FB6A_c','hDeltaK'),('ExR6','EPG'),('ExR4','PEN_b(PEN2)'),('P6-8P9','EPGt'),('IbSpsP','PFNd'),('vDeltaA_a','hDeltaD')]
male = defaultdict(int)
for r in csv.DictReader(open(ROOT/'data/derived/cx_type_edges.csv')): male[(r['type_pre'], r['type_post'])] += int(r['weight'])
print(f"{'edge':28s} {'MaleCNS':>8s} {'hemibrain':>9s} {'hb share of post input':>22s}")
out = []
for a, b in pairs:
    hb = E.get((a, b), 0); mc = male.get((a, b), 0); sh = hb/tin[b] if tin[b] else 0
    out.append(dict(pre=a, post=b, malecns=mc, hemibrain=hb, hemibrain_share_of_post_input=round(sh, 3)))
    print(f"{a+'->'+b:28s} {mc:8d} {hb:9d} {sh:22.3f}")
with open(ROOT/'data/derived/hemibrain_key_edges.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
