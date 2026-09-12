# Connectome findings in context

Each entry answers four questions: what the literature already knows, what this analysis found, why that matters, and what the evidence is. "Proof" here always means synapse counts in a reconstructed electron-microscopy brain: it shows wiring, never activity, sign or behaviour. Analysis dates 2026-09-10. Details and tables: [compass-recurrence.md](compass-recurrence.md), [goal-and-plasticity-motifs.md](goal-and-plasticity-motifs.md), [descending-trace.md](descending-trace.md). Function hypotheses for uncharacterised cells: [uncharacterised-neurons.md](uncharacterised-neurons.md); task decomposition: [behavioral-task-map.md](behavioral-task-map.md).

Background for all entries: the fly's compass is a ring of about 50 EPG neurons whose activity "bump" points in the fly's heading. To rotate the bump when the fly turns, PEN neurons read the bump and write it back one step to the left or right (Green 2017; Turner-Evans 2017). Delta7 neurons spread inhibition so only one bump exists. Ring (ER) neurons carry visual and wind cues into the compass and learn which cue direction goes with which heading (Kim 2019; Fisher 2019). Downstream, FC2 neurons hold a goal direction and PFL3 neurons compare it with the heading to produce a turn command (Mussells Pires 2024; Westeinde 2024). MaleCNS is a 2026 whole-brain wiring diagram of a male fly; the hemibrain (2020) is a partial wiring diagram of a female.

## 1. The bump-rotation wiring is present cell by cell, and it is the same in two flies

- **Known:** Models and imaging say each PEN should target the EPGs one step around the ring from its own position, with left and right PENs shifting in opposite directions. This had been checked by tracing a handful of cells in one brain (Turner-Evans 2020) and at cell-type level in the hemibrain (Hulse 2021).
- **Found:** In MaleCNS, every PEN of both subtypes sends its output to the EPGs exactly one glomerulus away on its own side and to the matching EPG on the other side, with the two sides shifting in opposite directions. The hemibrain gives the same numbers to within a few percent (e.g. left PEN_b: 38 %/34 % vs 40 %/35 % of synapses at the two expected positions).
- **Why it matters:** This is the physical basis of the fly's ability to keep track of heading in the dark. Showing it in full, in a second individual of the other sex, means models can use it as a fixed fact rather than a plausible assumption. It also fixes a measurable difference between the two PEN subtypes: PEN_b's output is more sharply focused than PEN_a's, which the two 2017 papers had inferred from timing but not from wiring.
- **Proof:** 9,160 synaptic connections among 152 compass cells in MaleCNS, binned by the angular position of each cell (parsed from its name); the same on hemibrain. The glomerulus-to-angle map was chosen by a data test (0.89 vs 0.51 localisation of EPG-to-EPG contacts), not assumed.

## 2. The compass feeds back onto PENs inside the ellipsoid body more than in the bridge

- **Known:** The textbook loop is EPG → PEN in the protocerebral bridge (same glomerulus) and PEN → EPG in the ellipsoid body (shifted). Turner-Evans 2020 noticed some unexpected EPG → PEN contacts inside the ellipsoid body but treated them as a curiosity.
- **Found:** Those ellipsoid-body contacts carry 2.5–3 times more synapses than the bridge contacts (hemibrain, which labels each synapse's location: 3,844 vs 1,281 for PEN_a; 3,645 vs 1,512 for PEN_b), and they sit exactly on the tile each PEN writes back to. MaleCNS shows the same mixture.
- **Why it matters:** It changes the shape of the recurrent loop: each PEN receives the heading signal both at its bridge input and at its own output location. That is a local positive-feedback motif that no current ring-attractor model includes. It could stabilise the bump or change how fast it moves; a model comparison is the obvious next step.
- **Proof:** Hemibrain per-ROI synapse table, `data/derived/hemibrain_epg_pen_by_roi.csv`; MaleCNS offsets consistent but not ROI-resolved.

## 3. The PEG → PEN_b side loop is a clean, separate circuit

- **Known:** Turner-Evans 2020 found that PEG cells feed PEN_b, and that silencing PEN_b abolishes the bump in darkness.
- **Found:** EPG → PEG contacts are almost purely same-glomerulus (bridge), PEG → PEN_b contacts are almost purely tile-matched (ellipsoid body), and PEG → PEN_a is about ten times weaker. Conserved in both brains.
- **Why it matters:** The two PEN subtypes get their compass input through different routes (PEN_a mostly directly, PEN_b heavily via PEG). Any model of why the dark bump needs PEN_b specifically has a concrete wiring difference to work with.
- **Proof:** Same tables as above; per-cell pairs such as EPG R5 → PEG R5 carry 100–150 synapses.

## 4. Delta7 wiring matches its inhibitory-stabiliser role

- **Known:** Delta7 cells are glutamatergic (inhibitory) and each outputs onto two or three bridge glomeruli far apart while collecting input across the bridge; silencing them makes the bump wobble rather than disappear (Turner-Evans 2020).
- **Found:** 95–100 % of each Delta7's output to compass cells lands in its named output glomeruli, and its EPG input comes almost entirely from 110°–160° away, with almost none from near its outputs. Conserved across both brains.
- **Why it matters:** Confirms the "inhibit the far side of the ring" architecture at full population scale, which is what the Kim 2017 model space required.
- **Proof:** Offset profiles for 42 Delta7 cells in each brain.

## 5. The three FC2 goal subtypes look alike at the output and differ at the input

- **Known:** The goal population FC2 was treated as one type in the physiology papers; the MaleCNS release splits it into FC2A, FC2B and FC2C. The heading-to-goal comparison happens where FC2 meets PFL3 in the fan-shaped body.
- **Found:** All three subtypes send the same column-matched projection to PFL3 and PFL2 (about 64 % same column, 17 % neighbouring column). They differ only in which hDelta cells feed them (FC2A: hDeltaJ, PFNp; FC2B: hDeltaJ/H/C/G; FC2C: hDeltaL/F/E/G/D, PFNm). The travel-direction population hDeltaB contributes fewer than 150 synapses to all FC2 together.
- **Why it matters:** The steering readout does not care which FC2 subtype is active, so if the subtypes have different functions it will be because different upstream information (wind, odor, learned value) is routed into each. The absence of an hDeltaB → FC2 path means the "integrate travel direction into a goal" story needs an intermediate we have not identified, exactly the gap the reading synthesis flagged.
- **Proof:** `fc2_subtype_partners.csv`, `fc2_pfl_column_offsets.csv` (MaleCNS seed graph).

## 6. PFL3's phase shift is visible in its cell names

- **Known:** Each PFL3 compares heading and goal with a built-in offset of about ±67°, so that left and right PFL3 populations disagree by ~135° (Mussells Pires 2024; Westeinde 2024).
- **Found:** Left PFL3 in bridge glomerulus g arborise in fan-shaped-body column g+2; right PFL3 in column 8−g. For one heading the two sides therefore sample columns three apart out of eight, i.e. 135°.
- **Why it matters:** Ties the published physiological offset to an anatomical rule that holds for every PFL3 in the male brain, with three labelled exceptions at the seam.
- **Proof:** `pfl_glomerulus_column.csv`.

## 7. Each EL octopamine cell is tuned to one heading, and EL feedback targets a specific subset of ring neurons

- **Known:** Plitt 2025 (preprint) showed that EL neurons carry a heading bump, release octopamine onto ring-neuron terminals, and are needed for the compass to learn visual cues.
- **Found:** Each of the 18 ELs gets 55–70 % of its compass input from a single bridge glomerulus plus its mirror partner, so the 18 cells tile the ring. EL output is concentrated on ER4d, ER3p, ER3d and ER2_c ring classes and is weak onto ER4m and ER5, even though ER4m is the strongest ring input to the compass. ER4m and ER6 instead receive direct feedback from EPG.
- **Why it matters:** Predicts that octopamine-dependent learning should be strongest for the cue types carried by ER4d/ER2_c-like rings and may be absent or use a different mechanism for ER4m-carried cues. That is a specific, testable refinement of Plitt's result. ER5, a sleep-related ring class, is the largest input to EL, hinting that compass learning may be state-gated.
- **Proof:** `el_epg_tuning.csv`, `er_subtype_motif.csv` (MaleCNS seed graph). Transmitter identity of EL comes from Plitt, not from this graph.

## 8. Ring neurons of the same class inhibit each other massively

- **Known:** Turner-Evans 2020 inferred mutual inhibition within ring classes from R4d activity and receptor expression.
- **Found:** Within-class ring connections are the largest ring-related blocks in the graph (ER4d → ER4d 39 k synapses; ER2_c, ER5, ER4m, ER3d_b each 13–16 k).
- **Why it matters:** This is the normalisation Mitchell 2023 and Basnak 2025 need for cue competition: each cue class is a winner-take-all pool before it reaches the compass.
- **Proof:** `er_subtype_motif.csv`.

## 9. PFL3 output is contralateral and mostly goes to LAL interneurons, not straight to descending neurons

- **Known:** PFL3 is said to drive the descending neuron DNa02 to produce turns (Rayshubskiy 2020; Westeinde 2024), with the left PFL3 population driving right turns.
- **Found:** In the whole-brain graph, every major PFL3 target is on the opposite side (left PFL3 → right DNa02: 380 synapses vs 0 ipsilateral). But PFL3 → DNa02 is only 1.5 % of DNa02's input; PFL3's largest typed targets are LAL interneurons, several predicted inhibitory (LAL121 gets 37 % of its input from PFL3), which in turn hit DNa02, DNa03, DNa15 and DNg04. PFL2 → DNa03 is direct and bilateral (4.5 % of DNa03 input). Feng 2024's LAL013 and DNa11 receive essentially nothing from any PFL.
- **Why it matters:** The steering signal is reshaped in the lateral accessory lobe before it becomes a descending command, so "PFL3 → DNa02 → turn" is a summary, not the circuit. It also locates the gap between the compass-steering papers and Feng's steering hierarchy: PFL3 must reach LAL013/DNa11 through intermediates such as LAL121, LAL014 or LAL122.
- **Proof:** Full MaleCNS graph, `pfl_outputs_hop1.csv` and `pfl_outputs_hop2_to_dn.csv`. Caveat: about two thirds of PFL output synapses land on untyped fragments in this export and are excluded.


## What it means, ranked by how much it should change current thinking

**Genuinely surprising (a model built today would be wrong without it)**

1. *Finding 2, the ring-side EPG→PEN loop.* Every published ring-attractor model routes EPG→PEN through the bridge only. The ellipsoid-body contacts are three times larger and sit on the tile each PEN writes to, so each PEN excites and is excited by the same EPGs: a local positive-feedback cell. A minimal simulation ([simulations/eb_epg_pen_loop.py](../simulations/eb_epg_pen_loop.py)) shows this loop acts as a brake: at a quarter of the measured strength it cuts rotation gain by a third, and at the measured strength it stops the bump moving at all. Real flies rotate their bump fine, so one of three things is true: those synapses are functionally weak, they are axo-axonic (modulating PEN output rather than driving it), or they are balanced by inhibition not in the model. Any of these is a physiology experiment nobody has done, and the answer determines whether the compass has a built-in hysteresis that stabilises heading in darkness at the cost of speed. If the loop is real and dendritic, current models over-estimate how easily the bump moves.

2. *Finding 9, the steering signal is reshaped in the lateral accessory lobe.* The steering papers treat PFL3→DNa02 as the output. In the whole-brain graph that edge is 1.5 % of DNa02's input, and PFL3's largest targets are LAL interneurons, several inhibitory, that converge on DNa02, DNa03, DNa15 and DNg04. Feng 2024's steering hierarchy (LAL013/DNa03/DNa11) receives nothing direct from PFL. There is an uncharacterised processing stage between the compass and the legs; sign inversions in it could flip the meaning of "left PFL3 drives right turns". No one has recorded from LAL121, LAL126 or LAL083 with the compass in mind.

**Interesting (turns a published claim into a specific prediction)**

3. *Finding 7, EL feedback is ring-class specific.* Predicts octopamine-dependent learning for ER4d/ER2_c-type cues and a different mechanism (direct EPG feedback) for ER4m/ER6. Also, ER5, the sleep ring class, is EL's biggest input, so compass learning may be state-gated.

4. *Finding 5, FC2 subtypes.* Identical outputs, different inputs: if goals of different kinds exist, they are separated upstream, not at the readout. hDeltaB→FC2 is absent, so the obvious "integrate travel into a goal" path does not exist as a direct edge.

**Confirmation (foundation, not news)**

5. Findings 1, 3, 4, 6, 8: the shifted PEN wiring, the PEG loop, Delta7 confinement, the PFL3 offset rule and ring-class self-inhibition all match the literature. Their value is that they now hold for every cell in two brains, which is what lets the unknown cells in [uncharacterised-neurons.md](uncharacterised-neurons.md) be interpreted relative to them.

## 10. A synaptic path integrator at hΔB → hΔJ (added 2026-09-12)

- **Known:** flies integrate, re-zero at food, and need PFNd/PFNv/hΔB/PFR for distance memory; no neuron integrates. Maimon & Abbott 2026 and Hulse 2021 suggested memory could be synaptic.
- **Found:** no columnar type has recurrence strong enough for an activity-based integrator (vector-mode gains ≤ 0.14). But at one site every element of a synaptic integrator converges: hΔB (travel direction) → hΔJ (column-matched, every cell), walking-driven dopamine FB4M/FB1H on every hΔJ cell, the reward octopamine neuron OA-VPM3 on hΔJ/hΔB/PFR, and hΔJ's 194° anatomical output into the FC2 goal, which inverts the stored displacement into a return direction. A closed-loop model with the measured kernels returns home; without the inversion it walks away.
- **Correction (2026-09-12):** anchored to the published column conventions, hΔJ and its siblings deliver the stored displacement sign-preserved; the inversion needed for return is provided only by hΔM (or hΔK/PFGs). The store is more likely hΔH/hΔA; see [exhaustive-search.md](exhaustive-search.md).
- **Why it matters:** it is a wiring-consistent account of the missing middle of the return-to-food circuit, with experiments. See [vector-memory-search.md](vector-memory-search.md) and the corrections in [exhaustive-search.md](exhaustive-search.md).
- **Proof:** synapse counts and angle-corrected phase statistics (`fb_offset_stats.csv`), full-graph trace of OA-VPM3 and FB4M inputs, two simulations. Everything about plasticity and reward is inferred.

## What none of this shows

Synapse counts do not give synaptic strength, sign (except via transmitter predictions), timing or behaviour. Every "why it matters" above is a hypothesis for physiology or modelling, not a result about what the fly does.
