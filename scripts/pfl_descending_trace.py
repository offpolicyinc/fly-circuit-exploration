#!/usr/bin/env python3
"""Trace PFL2/PFL3 (and PFL1) outputs one and two hops toward descending neurons in MaleCNS v1.0.

Pass 1 streams the full graph and keeps every edge whose presynaptic body is a PFL cell.
Pass 2 streams again to get (a) the total input of every first-hop target, so PFL share of
input can be reported, and (b) the outputs of first-hop targets that are descending neurons
or that project to descending neurons (second hop). Writes data/derived/pfl_outputs_hop1.csv,
pfl_outputs_hop2_to_dn.csv and pfl_trace_summary.json.
"""
import csv, json
from collections import defaultdict, Counter
from pathlib import Path
import pyarrow as pa, pyarrow.compute as pc, pyarrow.feather as feather
ROOT = Path(__file__).resolve().parents[1]; RAW = ROOT/'data/raw'; OUT = ROOT/'data/derived'
ann = feather.read_table(RAW/'body-annotations-male-cns-v1.0-minconf-0.5.feather').to_pylist()
A = {n['bodyId']: n for n in ann}
nt = {r['body']: r for r in feather.read_table(RAW/'body-neurotransmitters-male-cns-v1.0.feather').to_pylist()}
pfl = {i for i,n in A.items() if n['type'] in ('PFL1','PFL2','PFL3')}
def stream(pred_col, ids, keep):
    ids = pa.array(sorted(ids), type=pa.int64())
    with pa.memory_map(str(RAW/'connectome-weights-male-cns-v1.0-minconf-0.5.feather'),'r') as src:
        rd = pa.ipc.open_file(src)
        for i in range(rd.num_record_batches):
            b = pa.Table.from_batches([rd.get_batch(i)])
            m = pc.is_in(b[pred_col], value_set=ids)
            for e in b.filter(m).select(['body_pre','body_post','weight']).to_pylist(): keep(e)
hop1 = []
stream('body_pre', pfl, hop1.append)
targets = {e['body_post'] for e in hop1}
tot_in = Counter(); hop2 = []
def keep2(e):
    if e['body_post'] in targets: tot_in[e['body_post']] += e['weight']
    if e['body_pre'] in targets:
        d = A.get(e['body_post'], {})
        if d.get('superclass') == 'descending_neuron' or d.get('class') in ('descending','descending_neuron'): hop2.append(e)
# one pass serving both filters
ids = pa.array(sorted(targets), type=pa.int64())
with pa.memory_map(str(RAW/'connectome-weights-male-cns-v1.0-minconf-0.5.feather'),'r') as src:
    rd = pa.ipc.open_file(src)
    for i in range(rd.num_record_batches):
        b = pa.Table.from_batches([rd.get_batch(i)])
        m = pc.or_(pc.is_in(b['body_post'], value_set=ids), pc.is_in(b['body_pre'], value_set=ids))
        for e in b.filter(m).select(['body_pre','body_post','weight']).to_pylist(): keep2(e)
def desc(i):
    n = A.get(i, {}); t = nt.get(i, {})
    return dict(type=n.get('type') or '(untyped)', instance=n.get('instance') or '', superclass=n.get('superclass') or '', cls=n.get('class') or '',
                nt=(t.get('consensus_nt') or t.get('predicted_nt') or '') if t else '')
# aggregate hop1 by (pfl type, target body)
agg = defaultdict(int); byside = defaultdict(int)
for e in hop1:
    agg[(A[e['body_pre']]['type'], e['body_post'])] += e['weight']
    byside[(A[e['body_pre']]['type'], A[e['body_pre']].get('somaSide'), e['body_post'])] += e['weight']
with open(OUT/'pfl_outputs_hop1.csv','w',newline='') as f:
    w = csv.writer(f); w.writerow(['pfl_type','body_post','target_type','target_instance','target_superclass','target_nt','weight','from_L','from_R','target_total_input','pfl_share_of_input'])
    for (pt, b), wt in sorted(agg.items(), key=lambda x:-x[1]):
        d = desc(b); ti = tot_in[b]
        w.writerow([pt, b, d['type'], d['instance'], d['superclass'], d['nt'], wt, byside[(pt,'L',b)], byside[(pt,'R',b)], ti, round(wt/ti,3) if ti else ''])
agg2 = defaultdict(int)
for e in hop2: agg2[(e['body_pre'], e['body_post'])] += e['weight']
with open(OUT/'pfl_outputs_hop2_to_dn.csv','w',newline='') as f:
    w = csv.writer(f); w.writerow(['intermediate_body','intermediate_type','intermediate_superclass','pfl3_input','pfl2_input','pfl1_input','dn_body','dn_type','dn_instance','weight'])
    for (a,b), wt in sorted(agg2.items(), key=lambda x:-x[1]):
        d = desc(a); e = desc(b)
        w.writerow([a, d['type'], d['superclass'], agg[('PFL3',a)], agg[('PFL2',a)], agg[('PFL1',a)], b, e['type'], e['instance'], wt])
summ = dict(pfl_cells={t: sum(1 for i in pfl if A[i]['type']==t) for t in ('PFL1','PFL2','PFL3')}, hop1_edges=len(hop1), hop1_targets=len(targets),
            hop1_weight_by_pfl_type={t: sum(w for (p,b),w in agg.items() if p==t) for t in ('PFL1','PFL2','PFL3')},
            hop1_weight_by_target_superclass={t: {s: w for s,w in Counter({}).items()} for t in ()})
sc = defaultdict(Counter)
for (p,b),wt in agg.items(): sc[p][desc(b)['superclass'] or desc(b)['cls'] or '(none)'] += wt
summ['hop1_weight_by_target_superclass'] = {p: dict(c.most_common()) for p,c in sc.items()}
summ['hop2_dn_edges'] = len(agg2)
(OUT/'pfl_trace_summary.json').write_text(json.dumps(summ, indent=1)+'\n'); print(json.dumps(summ, indent=1))
