#!/usr/bin/env python3
"""FC2 subtype correspondence and the EPG->EL->ER motif in MaleCNS v1.0 (stdlib only).

Reads data/derived/navigation_neurons.csv and navigation_edges.csv; writes
data/derived/fc2_subtype_partners.csv, fc2_pfl_column_offsets.csv,
pfl_glomerulus_column.csv, el_epg_tuning.csv and er_subtype_motif.csv.
"""
import csv, re
from collections import Counter, defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; D = ROOT/'data/derived'
neu = {int(r['bodyId']): r for r in csv.DictReader(open(D/'navigation_neurons.csv'))}
E = [(int(r['body_pre']), int(r['body_post']), int(r['weight'])) for r in csv.DictReader(open(D/'navigation_edges.csv'))]
T = lambda b: neu[b]['type']
col = lambda i: (lambda m: int(m.group(1)) if m else None)(re.search(r'_C(\d)', i))
glom = lambda i: (lambda m: (m.group(1), int(m.group(2))) if m else None)(re.search(r'\)_([LR])(\d)', i))
def w(name, fields, rows):
    with open(D/name, 'w', newline='') as f:
        x = csv.writer(f); x.writerow(fields); x.writerows(rows)

# 1. FC2 subtypes: in/out partners by type
rows = []
for sub in ('FC2A', 'FC2B', 'FC2C'):
    ins, outs = Counter(), Counter()
    for a, b, wt in E:
        if T(b) == sub: ins[T(a)] += wt
        if T(a) == sub: outs[T(b)] += wt
    rows += [(sub, 'in', t, v) for t, v in ins.most_common()] + [(sub, 'out', t, v) for t, v in outs.most_common()]
w('fc2_subtype_partners.csv', ['fc2_subtype', 'direction', 'partner_type', 'weight'], rows)

# 2. FB column offsets for FC2 -> PFL2/PFL3 and hDeltaB -> FC2 (columns C1..C9 as labelled; wrap at 9)
rows = []
for tp in ('FC2A', 'FC2B', 'FC2C', 'hDeltaB'):
    for tq in ('PFL3', 'PFL2', 'FC2A', 'FC2B', 'FC2C'):
        d = Counter()
        for a, b, wt in E:
            if T(a) == tp and T(b) == tq:
                ca, cb = col(neu[a]['instance']), col(neu[b]['instance'])
                if ca and cb:
                    o = cb - ca; o = o - 9 if o > 4 else (o + 9 if o < -4 else o); d[o] += wt
        rows += [(tp, tq, o, v) for o, v in sorted(d.items())]
w('fc2_pfl_column_offsets.csv', ['type_pre', 'type_post', 'column_offset', 'weight'], rows)

# 3. PFL PB glomerulus vs FB column per cell
rows = sorted((r['type'], *glom(r['instance']), col(r['instance']), 'irreg' in r['instance'], b)
              for b, r in neu.items() if r['type'] in ('PFL1', 'PFL2', 'PFL3') and glom(r['instance']) and col(r['instance']))
w('pfl_glomerulus_column.csv', ['type', 'side', 'glomerulus', 'fb_column', 'irregular', 'bodyId'], rows)

# 4. EL cells: EPG input by glomerulus
rows = []
for el, r in neu.items():
    if r['type'] != 'EL': continue
    src = Counter()
    for a, b, wt in E:
        if b == el and T(a) == 'EPG': src[''.join(map(str, glom(neu[a]['instance'])))] += wt
    tot = sum(src.values()); top = src.most_common(2)
    rows.append((el, r['instance'], tot, len(src), top[0][0], round(top[0][1]/tot, 2), top[1][0], round(top[1][1]/tot, 2)))
w('el_epg_tuning.csv', ['bodyId', 'instance', 'epg_synapses', 'n_glomeruli', 'top_glomerulus', 'top_share', 'second_glomerulus', 'second_share'], rows)

# 5. ER subtype motif table
ers = sorted({r['type'] for r in neu.values() if r['type'].startswith('ER')})
S = defaultdict(int)
for a, b, wt in E: S[(T(a), T(b))] += wt
rows = [(t, sum(1 for r in neu.values() if r['type'] == t), S[(t, 'EPG')], S[('EPG', t)], S[('EL', t)], S[(t, 'EL')], S[(t, t)]) for t in ers]
w('er_subtype_motif.csv', ['er_type', 'n', 'ER_to_EPG', 'EPG_to_ER', 'EL_to_ER', 'ER_to_EL', 'ER_to_same_ER'], rows)
print('wrote 5 tables')
