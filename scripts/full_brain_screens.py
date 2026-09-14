#!/usr/bin/env python3
"""Unbiased whole-brain screens around the central complex, from the type-level graphs
(brain_type_edges.csv.gz, hemibrain_type_edges.csv.gz) and type_annotations.csv.
S1 external inputs to every CX type (with hemibrain replication and source superclass)
S2 neuromodulatory inputs (dopamine / octopamine / serotonin / peptidergic-named) to CX types
S3 dimorphism: annotated dimorphic partners of CX types; male vs female share of every CX edge
S4 descending-neuron targets of CX output types
S5 ascending-neuron routes into the CX (1 and 2 hops)
S6 column-shift motifs among FB columnar pairs (anything that is neither 0 nor 180 degrees)
S7 column-specific tangential inputs (tangential type whose synapses onto a columnar type sit in few columns)
Writes data/derived/screen_*.csv and prints ranked summaries."""
import csv, gzip, re, math, cmath
from collections import defaultdict, Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
A = {r['type']: r for r in csv.DictReader(open(D/'type_annotations.csv'))}
CX = {t for t, r in A.items() if r['class'] == 'CX'}
E = defaultdict(int)
for r in csv.DictReader(gzip.open(D/'brain_type_edges.csv.gz', 'rt')): E[(r['type_pre'], r['type_post'])] = int(r['weight'])
TOT = {r['type']: (int(r['total_in']), int(r['total_out']), int(r['n_cells'])) for r in csv.DictReader(open(D/'brain_type_totals.csv'))}
HB = defaultdict(int)
for r in csv.DictReader(gzip.open(D/'hemibrain_type_edges.csv.gz', 'rt')): HB[(r['type_pre'], r['type_post'])] = int(r['weight'])
HTOT = {r['type']: (int(r['total_in']), int(r['total_out']), int(r['n_cells'])) for r in csv.DictReader(open(D/'hemibrain_type_totals.csv'))}
def share(w, t): return w/TOT[t][0] if TOT.get(t, (0,))[0] else 0
def hshare(a, b): return HB[(a, b)]/HTOT[b][0] if HTOT.get(b, (0,))[0] else float('nan')
IN = defaultdict(list); OUT = defaultdict(list)
for (a, b), w in E.items():
    if b in CX and a != '(untyped)': IN[b].append((a, w))
    if a in CX and b != '(untyped)': OUT[a].append((b, w))
def sc(t): return A[t]['superclass'] if t in A else ''
def hdr(s): print('\n' + '='*100 + '\n' + s + '\n' + '='*100)
# ---------- S1 external inputs
rows = []
for t in sorted(CX):
    for a, w in IN[t]:
        if a in CX or w < 50: continue
        rows.append(dict(post=t, pre=a, syn=w, share=round(share(w, t), 3), pre_superclass=sc(a), pre_nt=A[a]['nt'], pre_n=A[a]['n'], hb_syn=HB[(a, t)], hb_share=round(hshare(a, t), 3) if hshare(a, t) == hshare(a, t) else ''))
rows.sort(key=lambda r: -r['share'])
with open(D/'screen_cx_external_inputs.csv', 'w', newline='') as f: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
hdr('S1  External (non-CX) inputs to CX types: largest shares, excluding ring-neuron visual/wind inputs (ER*, EL)')
for r in [r for r in rows if not r['post'].startswith('ER') and r['post'] != 'EL'][:45]:
    print(f"{r['pre']:16s} [{r['pre_superclass'][:14]:14s} {r['pre_nt'][:5]:5s}] -> {r['post']:12s} {r['syn']:6d} {r['share']*100:5.1f}%  hb {r['hb_syn']:6d} {str(r['hb_share'])}")
hdr('S1b  External inputs by source superclass into CX (sum of synapses, by superclass and top targets)')
bysc = defaultdict(int); bysct = defaultdict(Counter)
for r in rows: bysc[r['pre_superclass']] += r['syn']; bysct[r['pre_superclass']][r['post']] += r['syn']
for s, w in sorted(bysc.items(), key=lambda x: -x[1]): print(f"{s:20s} {w:8d}  top targets: {bysct[s].most_common(6)}")
# ---------- S2 modulators
def modclass(t):
    nt = A[t]['nt'] if t in A else ''
    if nt in ('dopamine', 'octopamine', 'serotonin'): return nt
    if re.match(r'^(OA-|5-HT|PPL|PAM|PPM|TH)', t): return 'named-' + t.split('-')[0].split('0')[0]
    return None
rows = []
for t in sorted(CX):
    for a, w in IN[t]:
        m = modclass(a)
        if m and w >= 30: rows.append(dict(post=t, pre=a, modulator=m, syn=w, share=round(share(w, t), 3), pre_in_cx=a in CX, hb_syn=HB[(a, t)]))
rows.sort(key=lambda r: (r['modulator'], -r['syn']))
with open(D/'screen_cx_modulator_inputs.csv', 'w', newline='') as f: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
hdr('S2  Neuromodulatory inputs to CX types (by predicted transmitter), top 15 per class; then which modulator types exist')
for m in sorted({r['modulator'] for r in rows}):
    print(f'--- {m}')
    for r in [r for r in rows if r['modulator'] == m][:15]: print(f"   {r['pre']:16s} -> {r['post']:12s} {r['syn']:6d} {r['share']*100:5.1f}%  hb {r['hb_syn']}")
    srcs = Counter(); 
    for r in rows:
        if r['modulator'] == m: srcs[r['pre']] += r['syn']
    print('   sources:', srcs.most_common(12))
# ---------- S3 dimorphism
hdr('S3a  Annotated sexually dimorphic / fru-dsx types connected to the CX (>=100 synapses either way)')
dim = []
toCX = defaultdict(Counter); fromCX = defaultdict(Counter)
for (a, b), w in E.items():
    if b in CX: toCX[a][b] += w
    if a in CX: fromCX[b][a] += w
for t, r in A.items():
    if not (r['dimorphism'] or r['fruDsx']): continue
    w_in = sum(toCX[t].values()); w_out = sum(fromCX[t].values())
    if w_in >= 100 or w_out >= 100: dim.append((t, r['dimorphism'], r['fruDsx'], r['superclass'], w_in, w_out, toCX[t].most_common(4), fromCX[t].most_common(4)))
for d in sorted(dim, key=lambda d: -(d[4]+d[5])): print(f"{d[0]:16s} dim={d[1][:18]:18s} fruDsx={d[2][:10]:10s} {d[3][:14]:14s} ->CX {d[4]:6d} {d[6]}   CX-> {d[5]:6d} {d[7]}")
with open(D/'screen_dimorphic_cx_partners.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type','dimorphism','fruDsx','superclass','syn_to_cx','syn_from_cx','top_cx_targets','top_cx_sources']); w.writerows([[*d[:6], str(d[6]), str(d[7])] for d in dim])
hdr('S3b  Male (MaleCNS) vs female (hemibrain) share of post input for every CX-involving edge with >=300 synapses in either; largest disagreements')
rows = []
for (a, b), w in E.items():
    if (a in CX or b in CX) and a != '(untyped)' and b != '(untyped)':
        hw = HB[(a, b)]
        if max(w, hw) < 300 or b not in HTOT or a not in HTOT: continue
        sm, sf = share(w, b), hshare(a, b)
        rows.append(dict(pre=a, post=b, male_syn=w, female_syn=hw, male_share=round(sm, 4), female_share=round(sf, 4), log2_ratio=round(math.log2((sm+1e-4)/(sf+1e-4)), 2), pre_dimorphic=bool(A.get(a, {}).get('dimorphism') or A.get(a, {}).get('fruDsx')), post_dimorphic=bool(A.get(b, {}).get('dimorphism') or A.get(b, {}).get('fruDsx'))))
for (a, b), hw in HB.items():
    if (a in CX or b in CX) and hw >= 300 and (a, b) not in E and a in TOT and b in TOT and a != '(untyped)' and b != '(untyped)':
        rows.append(dict(pre=a, post=b, male_syn=0, female_syn=hw, male_share=0.0, female_share=round(hshare(a, b), 4), log2_ratio=round(math.log2(1e-4/(hshare(a, b)+1e-4)), 2), pre_dimorphic=False, post_dimorphic=False))
rows.sort(key=lambda r: -abs(r['log2_ratio']))
with open(D/'screen_cx_edges_male_vs_female.csv', 'w', newline='') as f: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print('male-enriched (log2 ratio >= 2, male >= 300):')
for r in [r for r in rows if r['log2_ratio'] >= 2 and r['male_syn'] >= 300][:30]: print(f"   {r['pre']:16s} -> {r['post']:14s} male {r['male_syn']:6d} ({r['male_share']*100:5.1f}%)  female {r['female_syn']:6d} ({r['female_share']*100:5.1f}%)  dim={r['pre_dimorphic'] or r['post_dimorphic']}")
print('female-enriched (log2 ratio <= -2, female >= 300):')
for r in [r for r in rows if r['log2_ratio'] <= -2 and r['female_syn'] >= 300][:30]: print(f"   {r['pre']:16s} -> {r['post']:14s} male {r['male_syn']:6d} ({r['male_share']*100:5.1f}%)  female {r['female_syn']:6d} ({r['female_share']*100:5.1f}%)")
# ---------- S4 descending targets
hdr('S4  Descending neurons by share of input from CX types (>=3% of DN input), with CX sources')
dn = defaultdict(Counter)
for (a, b), w in E.items():
    if a in CX and sc(b) == 'descending_neuron': dn[b][a] += w
rows = []
for b, c in dn.items():
    tot = sum(c.values()); rows.append(dict(dn=b, cx_syn=tot, cx_share=round(share(tot, b), 3), dn_in=TOT[b][0], top_sources=';'.join(f'{a}:{w}' for a, w in c.most_common(5)), hb_cx_syn=sum(HB[(a, b)] for a in c)))
rows.sort(key=lambda r: -r['cx_share'])
with open(D/'screen_cx_to_descending.csv', 'w', newline='') as f: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in [r for r in rows if r['cx_share'] >= 0.03][:40]: print(f"{r['dn']:12s} CX {r['cx_syn']:6d} = {r['cx_share']*100:5.1f}% of {r['dn_in']:6d}  hb {r['hb_cx_syn']:5d}  {r['top_sources']}")
# ---------- S5 ascending routes
hdr('S5  Ascending neurons into the CX: direct (>=50 syn) and two-hop via a non-CX relay (path weight = min of legs, relay->CX >= 2% of target input)')
asc = {t for t in A if A[t]['superclass'] in ('ascending_neuron', 'sensory_ascending')}
direct = sorted(((a, b, w) for (a, b), w in E.items() if a in asc and b in CX and w >= 50), key=lambda x: -x[2])
for a, b, w in direct[:25]: print(f"   direct  {a:22s} -> {b:12s} {w:5d} ({share(w, b)*100:4.1f}%)  hb {HB[(a, b)]}")
two = []
relay_in = defaultdict(Counter)
for (a, b), w in E.items():
    if a in asc and b not in CX and b != '(untyped)' and w >= 100: relay_in[b][a] += w
for x, c in relay_in.items():
    for b, w2 in toCX[x].items():
        if share(w2, b) >= 0.02 and w2 >= 100:
            for a, w1 in c.items(): two.append((a, x, b, min(w1, w2), w1, w2, round(share(w2, b), 3)))
two.sort(key=lambda t: -t[3])
with open(D/'screen_ascending_to_cx.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['ascending','relay','cx_target','path_min','an_to_relay','relay_to_cx','relay_share_of_cx_input']); w.writerows([(a, '', b, w, w, w, round(share(w, b), 3)) for a, b, w in direct]); w.writerows(two)
for t in two[:40]: print(f"   2-hop   {t[0]:22s} -> {t[1]:14s} -> {t[2]:12s} min={t[3]:5d} ({t[4]},{t[5]}, relay={t[6]*100:.0f}% of target)")
# ---------- S6 shift motifs
hdr('S6  FB columnar pairs whose mean column offset is neither 0 nor 180 (conc >= 0.6, >= 300 synapses)')
for r in sorted(csv.DictReader(open(D/'fb_offset_stats.csv')), key=lambda r: -int(r['total'])):
    o, c, n = float(r['mean_offset_deg']), float(r['resultant_length']), int(r['total'])
    d0 = min(o, 360-o); d180 = abs(o-180)
    if n >= 300 and c >= 0.6 and d0 > 25 and d180 > 25: print(f"   {r['type_pre']:12s} -> {r['type_post']:12s} n={n:6d} offset={o:6.1f} conc={c:.2f}")
# ---------- S7 column-specific tangential inputs
hdr('S7  Tangential (non-columnar CX) types whose synapses onto a columnar type are concentrated in few columns (resultant >= 0.35, >= 300 syn)')
cells = {int(r['bodyId']): r for r in csv.DictReader(open(D/'cx_cells.csv'))}
ncol = defaultdict(int)
for b, r in cells.items():
    m = re.search(r'_C(\d+)', r['instance'])
    if m: ncol[r['type']] = max(ncol[r['type']], int(m.group(1)))
def angle(b):
    r = cells[b]; m = re.search(r'_C(\d+)', r['instance'])
    if not m: return None
    c = int(m.group(1)); n = ncol[r['type']]
    if n == 9: c = 1 if c in (0, 9) else c; return (c-1)/8*360
    if c == 0: c = 1
    return (c-1)/n*360
ANG = {b: angle(b) for b in cells}; T = {b: r['type'] for b, r in cells.items()}
Z = defaultdict(complex); W = defaultdict(float); percol = defaultdict(Counter)
for r in csv.DictReader(open(D/'cx_cell_edges.csv')):
    a, b, w = int(r['body_pre']), int(r['body_post']), int(r['weight'])
    if ANG[a] is None and ANG[b] is not None:
        k = (T[a], T[b]); Z[k] += w*cmath.exp(1j*math.radians(ANG[b])); W[k] += w; percol[k][round(ANG[b])] += w
rows = []
for k in W:
    if W[k] >= 300:
        conc = abs(Z[k])/W[k]; rows.append(dict(tangential=k[0], columnar=k[1], syn=int(W[k]), conc=round(conc, 2), peak_col_deg=round(math.degrees(cmath.phase(Z[k])) % 360), n_tangential_cells=A[k[0]]['n'] if k[0] in A else '', tangential_nt=A[k[0]]['nt'] if k[0] in A else '', columns=';'.join(f'{c}:{w}' for c, w in sorted(percol[k].items()))))
rows.sort(key=lambda r: -r['conc'])
with open(D/'screen_column_specific_tangentials.csv', 'w', newline='') as f: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in [r for r in rows if r['conc'] >= 0.35][:40]: print(f"   {r['tangential']:12s} ({r['n_tangential_cells']:>2} cells, {r['tangential_nt'][:5]}) -> {r['columnar']:12s} {r['syn']:6d} conc={r['conc']:.2f} peak={r['peak_col_deg']:3d}  {r['columns']}")
print('\n(uniformity baseline: median conc over all pairs =', round(sorted(r['conc'] for r in rows)[len(rows)//2], 2), ')')
