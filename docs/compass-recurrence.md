# Compass recurrence at cell resolution (MaleCNS v1.0)

Script: [scripts/compass_recurrence.py](../scripts/compass_recurrence.py). Outputs: [data/derived/compass_offset_profiles.csv](../data/derived/compass_offset_profiles.csv) and `.json`. Inputs are the seed-neuron and seed-edge tables already derived from the confidence-0.5 flat graph; no raw re-extraction was needed. Analysis date 2026-09-10.

## Method

Protocerebral-bridge glomeruli are parsed from the release's instance strings (e.g. `EPG(PB08)_L4`, `PEN_a(PB06a)_R7`, `Delta7(PB15)_L3R6_R`). Each glomerulus is assigned to one of 16 ellipsoid-body wedges, and every cell-to-cell edge among EPG, EPGt, PEN_a(PEN1), PEN_b(PEN2), PEG and Delta7 is binned by the circular wedge offset (post minus pre). For Delta7, whose instance names list its output glomeruli, the offset is taken to the nearest named output glomerulus.

The glomerulus-to-wedge map was not assumed. Two candidates were scored by how well EPG→EPG synapses localise (EPGs of one wedge contact each other; Turner-Evans 2020):

| Candidate ring order | EPG→EPG weight within ±1 wedge |
|---|---:|
| Interleaved: L1, R8, L2, R7, …, L8, R1 | 0.89 |
| Paired: L1, R1, L2, R2, … | 0.51 |

The interleaved map is used below. Glomerulus 9 (EPGt, some PEN/PEG) is mapped onto the wedge of glomerulus 1 of the same side; this seam assumption affects only the small EPGt/glomerulus-9 rows.

Limits: the flat graph has no ROI split, so an edge pools PB, EB and NO synapses. Edge direction separates EPG→PEN (mostly PB plus EB "hyper-local" contacts) from PEN→EPG (EB), but same-type edges such as PEN→PEN (NO) and Delta7→Delta7 (PB) cannot be localised. Weights are synapse counts, not efficacies.

## Results

Cells: 46 EPG, 4 EPGt, 20 PEN_a, 22 PEN_b, 18 PEG, 42 Delta7 (EPG occupy glomeruli 1–8 per side, PEN 2–9, PEG 1–9). Edges among them: 9,160 rows.

**Shifted PEN→EPG recurrence is present and lateralised.** Left PEN_a output peaks at −2/−3 wedges (27 % each) and right PEN_a at +2/+3 (29 %/28 %); PEN_b is tighter (−2/−3: 38 %/34 %; +2/+3: 41 %/34 %). At the individual-cell level the rule is simple: a PEN in glomerulus g of one side targets the EPG of glomerulus g−1 on the same side and the EPG of glomerulus 11−g on the other side (e.g. PEN_a L8 → EPG L7 and EPG R3; PEN_a R7 → EPG R6 and EPG L4). Those two EPG wedges are adjacent under the interleaved map, so each PEN writes into one EB tile displaced by one glomerulus from its own, in opposite angular directions for the two sides. This is the anatomical substrate of the Turner-Evans 2017 / Green 2017 rotation mechanism, now confirmed cell by cell in a male brain.

**EPG→PEN input is a mixture.** Only 14–15 % of EPG→PEN_a weight is at offset 0 (same glomerulus, the expected PB synapse); 55–60 % is at the same tile relation as the PEN→EPG output (EPG L1 → PEN_a L2, EPG R3 → PEN_a L8, and so on). Because a PEN's PB dendrite is one glomerulus away from the EPG wedge it targets, these tile-matched contacts must be in the EB. Turner-Evans 2020 reported such EB E-PG→P-EN1 "hyper-local" synapses as unexpected; here they carry more synapses than the PB route. Whether they are functionally excitatory loops within the tile is untested.

**PEG closes a second loop onto PEN_b.** EPG→PEG is strictly same-glomerulus (71 % at offset 0, per-cell pairs like EPG R5 → PEG R5 with 100–150 synapses), and PEG→PEN_b follows the tile rule (PEG L6 → PEN_b L7 and PEN_b R5), with PEG→PEN_a an order of magnitude weaker (≈ 90 vs ≈ 1,100 synapses per side). PEG→EPG is weak (≈ 500 per side) and broad. This matches the P-EG → P-EN2 → E-PG route that Turner-Evans 2020 found necessary for the dark bump.

**Delta7 outputs are confined to their named glomeruli; inputs come from far away.** Delta7→EPG, →PEN_a, →PEN_b, →PEG and →EPGt are 95–100 % within ±1 wedge of a named output glomerulus. EPG→Delta7 weight is only 4 % within ±1 wedge and peaks at 5–7 wedges (110°–160°) from the nearest output glomerulus. Delta7→Delta7 is the largest single block (26.5 k synapses) and is spread across offsets, consistent with the mutual Delta7 connectivity noted in 2020.

**Same-type PEN blocks are broad.** PEN_a→PEN_a and PEN_b→PEN_b (2.5–3.3 k per side) show no wedge structure, consistent with nodulus rather than EB contacts; PEN_a↔PEN_b cross-edges are weaker (≈ 1.5 k) and likewise unstructured.

| Edge (pre side) | Total synapses | Share within ±1 wedge | Dominant offsets (share) |
|---|---:|---:|---|
| PEN_a L → EPG | 7,368 | 0.23 | −3 (0.27), −2 (0.27) |
| PEN_a R → EPG | 7,030 | 0.22 | +2 (0.29), +3 (0.28) |
| PEN_b L → EPG | 4,830 | 0.14 | −2 (0.38), −3 (0.34) |
| PEN_b R → EPG | 4,841 | 0.14 | +2 (0.41), +3 (0.34) |
| EPG L → PEN_a | 3,008 | 0.27 | +2 (0.29), −3 (0.27), 0 (0.15) |
| EPG L → PEG | 3,013 | 0.81 | 0 (0.71) |
| PEG L → PEN_b | 1,068 | 0.04 | +2 (0.48), −3 (0.44) |
| Delta7 → EPG | 4,294 | 0.95 | 0 (0.82) |
| EPG L → Delta7 | 9,886 | 0.04 | −7 (0.22), +6 (0.21), −5 (0.17) |

Right-side rows mirror the left with opposite signs; the full table is in the CSV.

## What this does and does not establish

- Establishes: lateralised, one-glomerulus PEN→EPG shifts for both PEN subtypes; a same-glomerulus EPG→PEG and tile-matched PEG→PEN_b loop; Delta7 output confinement and distal input. These are structural predictions of the ring-attractor models, verified at synapse-count level in a second specimen (male).
- Does not establish: synaptic sign or efficacy (Delta7 glutamatergic inhibition and PEN cholinergic excitation are from Turner-Evans 2020 transmitter data, not from this graph), the PB/EB location of mixed edges, the functional difference between PEN_a and PEN_b (bridge phases and timing come from Green 2017), or whether the EB EPG→PEN contacts matter for dynamics.
- Next: split the same edges by ROI once synapse-level coordinates are available; compare the offset profiles with hemibrain/FlyWire to test whether the tile rule and the EB hyper-local share are conserved; use the measured per-offset weights as the connectivity of a rate model to see whether PEN_b's tighter profile changes integration gain.

## Cross-specimen check: hemibrain v1.2 (female) with ROI-resolved synapses

Script: [scripts/hemibrain_compass_comparison.py](../scripts/hemibrain_compass_comparison.py); data from the public hemibrain v1.2 traced-adjacency export (`data/raw/hemibrain/`, 80 MB, not tracked). Tables: `data/derived/hemibrain_compass_offsets.csv`, `hemibrain_epg_pen_by_roi.csv`.

Same cell counts as MaleCNS (46 EPG, 4 EPGt, 20 PEN_a, 22 PEN_b, 18 PEG, 42 Delta7) and nearly identical offset profiles:

| Edge (pre side) | MaleCNS dominant offsets | Hemibrain dominant offsets |
|---|---|---|
| PEN_a L → EPG | −3 (0.27), −2 (0.27) | −3 (0.28), −2 (0.28) |
| PEN_b L → EPG | −2 (0.38), −3 (0.34) | −2 (0.40), −3 (0.35) |
| EPG L → PEG | 0 (0.71) | 0 (0.72) |
| PEG L → PEN_b | +2 (0.48), −3 (0.44) | −3 (0.47), +2 (0.45) |
| Delta7 → EPG | 0 (0.82) | 0 (0.70) |
| EPG L → Delta7 | −7, +6, −5 | −7, +6, −5 |

The hemibrain ROI column settles the location question for the mixed EPG→PEN edges:

| Edge | PB synapses (share at offset 0) | EB synapses (share at tile offsets ±2/±3) |
|---|---:|---:|
| EPG → PEN_a | 1,281 (0.96) | 3,844 (0.66) |
| EPG → PEN_b | 1,512 (0.97) | 3,645 (0.88) |
| PEG → PEN_b | 7 | 1,300 (0.92) |
| PEN_a → EPG | 4 | 13,473 (0.56) |
| PEN_b → EPG | 4 | 8,403 (0.74) |

So in the female brain too, EPG→PEN contacts inside the EB outnumber the canonical same-glomerulus PB contacts by 2.5–3 to 1, and they sit exactly at the tile the PEN projects back to. The PEN→EPG return path is entirely EB. The shifted recurrence and the EB-side EPG→PEN loop are conserved across two specimens of different sex.
