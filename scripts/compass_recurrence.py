#!/usr/bin/env python3
"""Cell-resolution test of shifted compass recurrence in MaleCNS v1.0.

Uses only data/derived/navigation_neurons.csv and navigation_edges.csv (stdlib only).
Glomerulus labels are parsed from the release's instance strings, e.g. EPG(PB08)_L4,
PEN_a(PB06a)_R7, Delta7(PB15)_L3R6_R. The flat graph has no ROI split, so a pre->post
weight pools PB, EB and NO synapses; direction of the edge is what separates
EPG->PEN (PB) from PEN->EPG (EB) here.

Two candidate PB-glomerulus -> EB-wedge maps are scored against the data rather than
assumed: 'interleaved' (L1,R8,L2,R7,...,L8,R1 around the 16-wedge ring) and
'paired' (L1,R1,L2,R2,...). Glomerulus 9 (EPGt, some PEN/PEG/Delta7 outputs) is
mapped onto the same wedge as glomerulus 1 of the same side (PB seam), and flagged.
"""
import csv, re, json
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
D = ROOT/'data/derived'
TYPES = ['EPG','EPGt','PEN_a(PEN1)','PEN_b(PEN2)','PEG','Delta7']
N = 16

def glom_list(inst):
    m = re.search(r'\)_((?:[LR]\d)+)', inst)
    if not m:  # EPGt(PB09)_R9 style also matches; ER etc. don't
        return []
    return re.findall(r'[LR]\d', m.group(1))

def wedge(g, mapping):
    side, k = g[0], int(g[1])
    if k == 9: k = 1  # seam: glomerulus 9 shares the wedge of glomerulus 1 (assumption, flagged)
    if mapping == 'interleaved':
        return (2*k-2) % N if side=='L' else (2*(9-k)-1) % N
    else:  # paired
        return (2*k-2) % N if side=='L' else (2*k-1) % N

neurons = {}
with open(D/'navigation_neurons.csv') as f:
    for r in csv.DictReader(f):
        if r['type'] in TYPES:
            g = glom_list(r['instance'])
            neurons[int(r['bodyId'])] = dict(type=r['type'], inst=r['instance'], gloms=g, side=r['somaSide'])
edges = []
with open(D/'navigation_edges.csv') as f:
    for r in csv.DictReader(f):
        a,b = int(r['body_pre']), int(r['body_post'])
        if a in neurons and b in neurons:
            edges.append((a,b,int(r['weight'])))

def circ(d): 
    d %= N
    return d-N if d > N//2 else d

def profiles(mapping):
    prof = defaultdict(lambda: defaultdict(int))  # (type_pre, side_pre, type_post) -> offset -> weight
    for a,b,w in edges:
        A,B = neurons[a], neurons[b]
        if not A['gloms'] or not B['gloms']: continue
        # offset = post wedge - pre wedge; for multi-glomerulus cells (Delta7) take the min-|offset| pairing
        offs = [circ(wedge(gb,mapping)-wedge(ga,mapping)) for ga in A['gloms'] for gb in B['gloms']]
        o = min(offs, key=abs)
        key = (A['type'], A['gloms'][0][0] if A['type']!='Delta7' else 'both', B['type'])
        prof[key][o] += w
    return prof

def score(prof):
    """Fraction of EPG->EPG and PEN->EPG weight at |offset|<=1: the correct wedge map should localize these."""
    s = {}
    for key, d in prof.items():
        tot = sum(d.values()); loc = sum(w for o,w in d.items() if abs(o)<=1)
        s[key] = (loc/tot if tot else 0, tot)
    return s

out = {}
for mapping in ('interleaved','paired'):
    prof = profiles(mapping); sc = score(prof)
    out[mapping] = {'|'.join(k): {'total': sc[k][1], 'frac_within_1_wedge': round(sc[k][0],3),
                    'profile': {str(o): prof[k][o] for o in sorted(prof[k])}} for k in prof}
# choose mapping by EPG->EPG localization (EPGs in one wedge synapse onto each other; Turner-Evans 2020)
def epg_epg(m): return sum(out[m][k]['frac_within_1_wedge']*out[m][k]['total'] for k in out[m] if k.startswith('EPG|') and k.endswith('|EPG'))/max(1,sum(out[m][k]['total'] for k in out[m] if k.startswith('EPG|') and k.endswith('|EPG')))
best = max(('interleaved','paired'), key=epg_epg)
out['chosen_mapping'] = best
out['epg_epg_localization'] = {m: round(epg_epg(m),3) for m in ('interleaved','paired')}
out['n_neurons'] = {t: sum(1 for n in neurons.values() if n['type']==t) for t in TYPES}
out['n_edges'] = len(edges)
(D/'compass_offset_profiles.json').write_text(json.dumps(out, indent=1)+'\n')
with open(D/'compass_offset_profiles.csv','w',newline='') as f:
    w = csv.writer(f); w.writerow(['mapping','type_pre','side_pre','type_post','offset_wedges','weight'])
    for m in ('interleaved','paired'):
        for k,v in out[m].items():
            tp,sd,tq = k.split('|')
            for o,wt in v['profile'].items(): w.writerow([m,tp,sd,tq,o,wt])
print('chosen mapping:', best, out['epg_epg_localization'])
print('neurons:', out['n_neurons'], 'edges:', len(edges))
for k,v in sorted(out[best].items(), key=lambda kv:-kv[1]['total']):
    prof = v['profile']; tot=v['total']
    top = sorted(prof.items(), key=lambda x:-x[1])[:4]
    print(f"{k:38s} total={tot:6d} within1={v['frac_within_1_wedge']:.2f} top offsets={[(o,round(w/tot,2)) for o,w in top]}")
