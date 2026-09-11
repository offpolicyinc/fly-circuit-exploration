# FC2 subtypes and the EPG→EL→ER motif (MaleCNS v1.0)

Script: [scripts/goal_and_plasticity_motifs.py](../scripts/goal_and_plasticity_motifs.py). Tables in [data/derived](../data/derived): `fc2_subtype_partners.csv`, `fc2_pfl_column_offsets.csv`, `pfl_glomerulus_column.csv`, `el_epg_tuning.csv`, `er_subtype_motif.csv`. Same inputs and limits as [compass-recurrence.md](compass-recurrence.md): confidence-0.5 flat graph, seed neurons only, synapse counts pooled across ROIs, no sign or efficacy.

## FC2 subtypes (analysis 2 of the circuit doc)

MaleCNS splits FC2 into FC2A (18 cells), FC2B (27) and FC2C (47). Within the seed set:

- **Outputs are the same.** Each subtype sends most of its seed-internal output to PFL3 (2.5–2.7 k synapses) and PFL2 (1.1–2.0 k), and the FB-column relation is identical: 62–66 % of FC2→PFL3 and FC2→PFL2 weight is same-column, 15–19 % at ±1 column, none beyond ±2. At the output side nothing distinguishes the three subtypes, so the Mussells Pires goal-to-steering readout is not subtype-specific in this specimen.
- **Inputs differ.** FC2A is fed mainly by hDeltaJ and PFNp_b; FC2B by hDeltaJ, hDeltaH, hDeltaC and hDeltaG; FC2C by hDeltaL, hDeltaF, hDeltaE, hDeltaG, hDeltaD and PFNm. Different hDelta classes therefore address different FC2 subtypes, which is where any functional split should be sought.
- **hDeltaB does not feed FC2.** hDeltaB→FC2A/B/C carries 21/52/73 synapses in total. The travel-direction population of Lu 2022 has no direct route to the goal population; the synthesis's refusal to draw an hΔB→memory→FC2 edge stands structurally as well.
- **Recurrence is column-matched but modest.** FC2C→FC2C (607), FC2A→FC2A (491), FC2B→FC2B (253) and the cross-subtype FC2B↔FC2C edges (≈ 200 each, 57–59 % same column) exist but are small next to the hDelta inputs.
- **PFL3 phase shift, cell by cell.** Left PFL3 in PB glomerulus g arborise in FB column g+2 (L1→C3 … L7→C9); right PFL3 in glomerulus g arborise in column 8−g (R1→C7 … R7→C1); three cells labelled `irreg` (L1→C8, L2→C9, R1→C2, R2→C1) sit at the seam. Using the Delta7 pairing of L_g with R_(9−g) as "same heading", the two PFL3 populations sample columns three apart for one heading, i.e. a symmetric shift of ±1.5 columns, consistent with the ±67.5° offsets of Mussells Pires 2024 and Westeinde 2024. PFL2 cells (12, glomeruli 1–5 only) follow L g→g+4 and R g→6−g; PFL1 L g→g+1 and R g→8−g. Converting these label relations to angles needs the release's column-to-angle convention, so only the symmetry claim is made here.

## EPG→EL→ER motif (analysis 4)

18 EL cells (9 per side). Seed-internal inputs: ER5 (10.1 k), EPG (9.2 k), PEN_a (4.8 k), ER4m (4.1 k), ER4d (3.9 k), ER2_c (3.7 k), PEN_b (3.4 k). Outputs: ER4d (4.2 k), EPG (3.7 k), ER3p_a (3.3 k), ER3d_b (2.7 k), then ER2_c, ER3w_b, ER3p_b, ER2_a, ER3m and the remaining ER classes.

- **Each EL is heading-tuned by its EPG input.** Every EL receives 370–630 EPG synapses, and 55–70 % of them come from one PB glomerulus, with the second-largest source the contralateral partner glomerulus (e.g. L7 with R3, R8 with L2, L4 with R5). Eighteen ELs therefore tile the ring at roughly one cell per wedge, matching the EL head-direction bump Plitt 2025 imaged. PEN_a/PEN_b inputs would supply the same heading with a velocity-dependent amplitude.
- **EL feedback targets a specific subset of ring classes.** Per ring class, EL→ER weight is largest for ER4d (4,178), ER3p_a (3,253), ER3d_b (2,733), ER2_c (1,377), ER3w_b (1,361) and ER3p_b (1,034). It is small for ER4m (479) and ER5 (646) even though ER4m→EPG is the largest ring-to-compass projection (21.2 k) and ER5→EL is the largest EL input (10.1 k). So the octopamine coincidence signal, if EL→ER contacts are its substrate, is not distributed in proportion to how strongly a ring class drives the compass.
- **A parallel direct EPG→ER feedback exists for a different subset.** EPG→ER is substantial for ER6 (4,580), ER4m (4,487), ER2_c (2,701) and ER4d (2,598) and near zero for the ER3 classes. ER4m and ER6 thus receive compass feedback directly rather than through EL, which is a candidate explanation for why EL silencing might spare some cue modalities.
- **Within-class ring inhibition is the largest ring-related block.** ER4d→ER4d (39.4 k), ER2_c→ER2_c (15.7 k), ER5→ER5 (15.5 k), ER4m→ER4m (14.6 k), ER3d_b→ER3d_b (13.2 k). This is the mutual inhibition Turner-Evans 2020 inferred from R4d activity and Rdl expression, present at scale for most ring classes.

| ER class | n | ER→EPG | EPG→ER | EL→ER | ER→EL | ER→same ER |
|---|---:|---:|---:|---:|---:|---:|
| ER4m | 11 | 21,202 | 4,487 | 479 | 4,052 | 14,580 |
| ER2_c | 20 | 14,590 | 2,701 | 1,377 | 3,691 | 15,739 |
| ER4d | 26 | 12,335 | 2,598 | 4,178 | 3,917 | 39,443 |
| ER3w_b | 18 | 10,568 | 587 | 1,361 | 604 | 10,441 |
| ER3p_a | 14 | 8,924 | 99 | 3,253 | 980 | 7,239 |
| ER2_a | 12 | 8,225 | 1,357 | 854 | 2,069 | 4,121 |
| ER1_b | 13 | 5,634 | 1,003 | 415 | 1,655 | 833 |
| ER5 | 21 | 3,222 | 17 | 646 | 10,073 | 15,478 |
| ER6 | 4 | 1,925 | 4,580 | 54 | 905 | 141 |

Full table for all 26 ring classes in `er_subtype_motif.csv`.

## Hypotheses this raises (not findings)

1. EL-mediated plasticity may be restricted to the ring classes EL contacts most (ER4d, ER3p, ER3d, ER2_c, ER3w); classes with direct EPG feedback (ER4m, ER6) might use a different coincidence mechanism. Test: which ring drivers lose visual anchoring after EL silencing in Plitt's assay.
2. ER5→EL (10 k) is the single largest EL input; ER5 is sleep/arousal-related, so EL output, and thus compass learning, may be state-gated. Test: EL activity across sleep/wake or rest/walk (connects to Flores-Valle 2025).
3. FC2 subtype identity is set by upstream hDelta class, so goal "content" (wind, odor, learned) could be routed to subtypes while the PFL readout stays common. Test: driver expression of the Mussells Pires FC2 line against FC2A/B/C morphology.

All three require transmitter, receptor and physiological evidence that the graph cannot supply.
