#!/usr/bin/env python3
"""Per-type annotation summary from MaleCNS body annotations + consensus transmitter: data/derived/type_annotations.csv"""
import csv
from collections import defaultdict, Counter
from pathlib import Path
import pyarrow.feather as feather
ROOT = Path(__file__).resolve().parents[1]; RAW = ROOT/'data/raw'; OUT = ROOT/'data/derived'
ann = feather.read_table(RAW/'body-annotations-male-cns-v1.0-minconf-0.5.feather').to_pylist()
nt = {r['body']: (r.get('consensus_nt') or r.get('predicted_nt') or '') for r in feather.read_table(RAW/'body-neurotransmitters-male-cns-v1.0.feather', columns=['body','consensus_nt','predicted_nt']).to_pylist()}
G = defaultdict(list)
for n in ann:
    if n.get('type'): G[n['type']].append(n)
def maj(rows, k):
    c = Counter((r.get(k) or '') for r in rows); v, _ = c.most_common(1)[0]; return v
with open(OUT/'type_annotations.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['type','n','superclass','class','subclass','nt','dimorphism','fruDsx','somaNeuromere','hemibrainType','flywireType','synonyms','sides'])
    for t, rows in sorted(G.items()):
        w.writerow([t, len(rows), maj(rows,'superclass'), maj(rows,'class'), maj(rows,'subclass'), Counter(nt.get(r['bodyId'],'') for r in rows).most_common(1)[0][0],
                    ';'.join(sorted({(r.get('dimorphism') or '') for r in rows} - {''})), ';'.join(sorted({(r.get('fruDsx') or '') for r in rows} - {''})),
                    maj(rows,'somaNeuromere'), maj(rows,'hemibrainType'), maj(rows,'flywireType'), maj(rows,'synonyms'), ''.join(sorted(Counter((r.get('somaSide') or '?') for r in rows)))])
print('types', len(G))
