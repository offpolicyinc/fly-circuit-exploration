# Function from structure: uncharacterised central-complex neurons

Purpose: assign candidate functions to CX cell types with no published physiology, using their wiring relative to anchor populations whose function is known (EPG heading; PEN rotation; PFNd/PFNv/hDeltaB velocity and travel direction; FC2 goal; PFL2/PFL3 steering), their transmitter predictions, their column (phase) relations, and where they sit in the return-to-food task ([behavioral-task-map.md](behavioral-task-map.md)). Every function stated here is a hypothesis. Evidence is MaleCNS v1.0 synapse counts unless stated; scripts and tables are listed at the end.

Scale of the unknown: 292 CX cell types, 2,950 cells; 233 types (2,002 cells) have no functional characterisation in the literature read for this project. 158 of those are predicted glutamatergic fan-shaped-body tangential neurons (FBxx), which in the fly are usually inhibitory.

Two conventions matter for reading the phase claims. FB columns C1–C9 are folded to 8 angular positions (C9 = C1). hDelta neurons receive input at one end and output at the opposite end (verified here cell by cell: hDeltaH_01_C1 outputs to FC2B columns 5–6), so an hDelta output at "offset ±4" is the anatomical 180° inversion described by Hulse 2021; what is new is which signal each hDelta inverts and where it delivers it.

## A. Candidates for the missing computations (targeted)

### A1. PFR_a / PFR_b: recurrent, travel-direction-driven pair — relay, not integrator, unless recurrence is inhibitory

- Wiring: hDeltaB is the largest input to both (16 % of PFR_a, 22 % of PFR_b), PFNd adds a direct column-matched input to PFR_a (99 % at offset 0/+1). PFR_b→PFR_a and PFR_a→PFR_b are column-matched (43–44 % at offset 0); PFR_b→PFR_b is broad and excludes its own column (0 % at offset 0). Both project to the PB (identity glomerulus→column map, so they carry a heading-frame copy) and PFR_b's largest typed output is LAL002, a lateral-accessory-lobe cell; PFR_a's is hDeltaA (which feeds PFL3).
- Literature anchor: Flores-Valle 2025 (PFR encodes walking direction; drifts ~180° at rest; drift shifts with learning); D'Atri 2025 (PFR silencing abolishes distance memory).
- Simulation ([simulations/pfr_integrator.py](../simulations/pfr_integrator.py)): a rate model with the measured kernels and all-excitatory signs never integrates: across recurrent gains 0–3 and uniform inhibition 0–4 the PFR population vector points at travel direction rotated by a fixed ~115° (set by the hDeltaB output offset), not at the accumulated displacement, and the cosine-mode gain stays below 0.25 while the uniform mode explodes first. Making the broad within-type recurrence inhibitory (sign flip) raises the cosine-mode gain to ~1 at high gain and the vector starts to lag toward the displacement, i.e. integration becomes possible.
- Hypothesis: PFR is a heading-registered copy of travel direction sent to the LAL (PFR_b→LAL002) and to the steering input hDeltaA; it can become a displacement integrator only if its broad recurrence is effectively inhibitory (PFR_a's transmitter is "unclear") or if a tangential inhibitory input (FB3C is GABAergic and targets PFR_b) supplies the off-column suppression. Prediction: PFR bump phase is offset from the hDeltaB bump by a fixed ~90–135°; PFR_a transmitter identity decides between relay and integrator.
- Test: dual-colour imaging of hDeltaB and PFR bumps; PFR_a transmitter immunostaining; PFR imaging during Behbahani's re-zeroing task.

### A2. FR1: the strongest self-loop in the fan-shaped body, reading travel direction and writing to the mushroom body

- Wiring: 18 cholinergic cells; 30 % of FR1 input is FR1 itself (8,694 synapses, broad, excluding own column), 11 % is hDeltaB (arriving at +1..+4). Outputs: FR1 (38 %), then MBON30, CRE105, FB4C, SMP457, PPL102 (a PPL1 dopamine neuron), FB5H (FB dopamine).
- Anchor: none in physiology. Chen 2024 needs both MB and PFNd for scent-marked place learning, with no known bridge.
- Hypothesis: FR1 is a persistent, self-sustaining representation of recent travel direction that informs the reward-learning system (MBON30, PPL1 dopamine). It is the structural candidate for how "which way I was going" reaches MB-dependent place value. The recurrence is again uniform off-column, so like PFR it would sustain activity level rather than a specific direction unless inhibition shapes it.
- Test: image FR1 during walking in darkness and after sugar; silence FR1 in Chen 2024's task.

### A3. hDeltaK / PFGs / FB6A / FB6M / ExR3: the recurrent working-memory loop, with its gates named

- Wiring: PFGs→hDeltaK (4,790, 18 % of hDeltaK input) and hDeltaK→PFGs (2,846, 27 % of hDeltaK output) form the largest reciprocal columnar loop in the FB; PFGs carries heading from the PB (Delta7 input); hDeltaB adds travel direction (17 %). Round-trip offset sums to ~0, so the loop can hold a column. Glutamatergic (inhibitory) tangentials FB6M (→hDeltaK 1,995), FB6A_c (1,149) and FB6A_a (1,255) sit on the loop and receive from it; the serotonergic ExR3 pair is also reciprocal with both.
- Anchor: Kathman 2026 (hDeltaK persists after odor loss); Lanz 2025 model (PFG recurrence gated by inhibitory tangentials).
- Hypothesis: FB6A_a/c and FB6M are Lanz's gate. Their inputs are non-CX (SIP076, SMP347, SLP; plus ExR3 serotonin), so the gate is set by higher-order state. FB6A_a/c also output to hDeltaC and hDeltaF, the inputs to FC2B and FC2C, giving the working-memory loop a route to the goal population.
- Test: silence FB6A during Kathman's odor-loss persistence; image FB6A with odor onset/offset.

### A4. hDeltaM (and hDeltaH): an inverted copy of the goal delivered to the steering neurons

- Wiring: hDeltaM receives FC2B at offset −1/0 (its input end) and FB5A; it outputs to PFL3 (2,428) and PFL2 (1,555) at exactly 180° (50 % at +4, 47 % at −3), and back to FC2B at 180°. hDeltaH does the same for PFR_b/vDeltaG inputs into FC2B and PFL3.
- Hypothesis: hDeltaM is an anti-goal channel. Two readings: (i) it supplies PFL2's known anti-goal tuning (Westeinde 2024), which the published model attributed to PFL2's own PB→FB shift; (ii) it lets the same FC2 goal drive avoidance rather than approach when hDeltaM is enabled, which a heat-avoidance task (Dan 2024) would need. FB5A (GABA) gates hDeltaM and FC2 together.
- Test: image hDeltaM against FC2 (predict antiphase); silence hDeltaM in approach versus avoidance menotaxis.

### A5. hDeltaA and hDeltaI: travel-direction-derived inputs to PFL3 that rival FC2

- Wiring: hDeltaA (3,881) and hDeltaI (3,468) each give PFL3 more synapses than any single FC2 subtype (2,478–2,700); both also feed PFL2. Both receive hDeltaB at offset 0 (64 % and 48 %) and deliver to PFL at +1..+4 (broad, centred ~+2.5 columns ≈ 110°). hDeltaA's other inputs are vDeltaK/vDeltaL/vDeltaM (which receive FB4G/FB4H, fed by MBON25/MBON34) and PFR_a; hDeltaI's are FB4F/FB4E/FB2G tangentials.
- Hypothesis: a second steering channel in which the reference is current travel direction rather than a stored goal. With a ~90–135° offset it is not "keep going straight"; with MB-derived tangential gating it could implement value-dependent deflection from the current course (turn away from or toward the direction associated with an MB outcome). This is the most speculative entry and the one where the sign of the hDelta→PFL phase matters most.
- Test: PFL3 tuning to travel direction after FC2 silencing; hDeltaA activity vs MBON25/34 activation.

### A6. FB5A: GABAergic normaliser of the goal population

- Wiring: 4 cells; input dominated by FC2C/FC2B/FC2A (12 %/12 %/4 %) and PFL3; output to FC2C/B/A (9 %/6 %/4 %), PFL3, hDeltaM.
- Hypothesis: winner-take-all across goal columns and subtypes (one expressed goal at a time), plus a global gain on the steering readout. Prediction: silencing FB5A broadens or splits the FC2 bump and weakens menotaxis.

### A7. FB4M, FB4L, FB1H: dopamine at the travel-vector stage

- Wiring: FB4M (PPM3 DAN, 4 cells) receives PFNv, hDeltaB, PFNd and non-CX SMP377/PLP246 and outputs to hDeltaB (16 %), hDeltaA, PFNd, PFR_a. FB4L (4 cells) outputs 20 % to hDeltaB. FB1H (NO2/3 DAN) is reciprocal with hDeltaJ, the main input to FC2A/B.
- Anchor: ExR2 dopamine gates ER→EPG plasticity by rotational speed (Fisher 2022); Maimon & Abbott 2026 propose dopamine/cAMP for vector memory writing.
- Hypothesis: FB4M/FB4L are the "write" signal for whatever the hDeltaB→PFR/hDeltaJ stage stores; their non-CX inputs are where food or reward would enter. FB1H does the same at the goal input. Test: image FB4M/FB4L/FB1H at sugar contact in Corfas's triggers; pair their activation with walking and look for re-zeroing.

### A8. LAL121, LAL126, LAL083, AOTU019, VES054: the stage between PFL3 and the descending neurons

- Wiring (whole graph): all strictly contralateral to their PFL3 input; LAL121 gets 37 % of its total input from PFL3 (predicted glutamate); LAL126→DNg04/DNae001/DNa02/DNa16; LAL083→DNa15/DNa02/DNg04/DNa13; LAL121/LAL014/LAL122→DNa03; AOTU019 (GABA)→DNa15/DNa13/DNa02.
- Hypothesis: a sign-converting and fan-out layer. LAL121 in particular is an inhibitory relay of the PFL3 turn signal into DNa03, so left PFL3 would inhibit right DNa03 while exciting right DNa02 directly, i.e. a push-pull command. Test: LAL121 imaging during menotaxis corrections; sign of its effect on DNa03.

## B. Findings from the unbiased screen (unknown unknowns)

Method: every CX type scored for self-recurrence, strongest reciprocal partner, external (non-CX) input and output, module bridging and sharp phase offsets ([scripts/cx_unbiased_screen.py](../scripts/cx_unbiased_screen.py), table `data/derived/cx_screen.csv`). Items below were not looked for.

1. **FS1A_a/b/c → oviIN.** Three cholinergic FB output types (47 cells) that read the goal layer (FC2A/B/C, hDeltaM, hDeltaJ, hDeltaL) send their largest typed output, 600–780 synapses each, to oviIN, the oviposition inhibitory neuron. The navigation goal state has a direct line to the egg-laying decision. Nothing in the navigation literature mentions this. Test: oviposition site choice after FS1A silencing; FS1A activity vs goal expression.
2. **FB3A: an ascending-neuron route into the velocity system.** FB3A (4 glutamatergic cells) supplies 12 % of PFNd's input (5,765 synapses, the third-largest PFNd input after LNO2 and PFNd itself) and is fed by LAL143, PS326, the ascending neuron AN06B009 and PS196_b. This is a candidate leg/VNC self-motion signal into PFNd that Lu 2022 did not describe (they identified LNO2 and SpsP). Test: FB3A tuning to walking speed, and whether it survives visual removal.
3. **PS196_b as a shared motor source.** The posterior-slope type PS196_b is among the top inputs to GLNO (19 %), LPsP, ExR2, ExR4 and FB3A. Hulse 2023 left GLNO's motor signal unsourced; PS196_b is the structural candidate, and it fans out to both the rotational (GLNO) and translational (FB3A→PFNd) velocity inputs. Test: PS196_b activity during turns vs forward walking.
4. **Mushroom-body outputs reach the travel-direction system through FB4R, FB4G and FB4H.** FB4R (6 glutamatergic cells) is driven by MBON21 and MBON09 and sends 3,647 synapses to hDeltaB (8 % of hDeltaB input). FB4G/FB4H are driven by MBON25 and MBON34 and drive vDeltaK/vDeltaM→hDeltaA→PFL3. These are the missing MB→CX bridges Chen 2024's result requires. Test: image hDeltaB during MBON21/09 activation.
5. **ExR7 → LAL013 and ExR8 → DNg36: compass-derived signals that bypass PFL.** ExR7 (4 cholinergic cells, 20 % input from EPG) sends 1,247 synapses to LAL013, the top of Feng 2024's steering hierarchy, which receives nothing from PFL. ExR8 (PEN_b/EPG/GLNO inputs) targets the descending neuron DNg36 and posterior-slope cells. Four-cell populations cannot encode direction, so these likely carry bump amplitude or rotation state, i.e. a "compass is turning / confident" gate on steering. Test: ExR7 activity during saccades.
6. **ExR4 and ExR6: glutamatergic global feedback on the compass.** ExR6 takes 49 % of its input from EPG and returns 6,236 synapses to EPG and 5,089 to PEN_a; ExR4 takes PEG/EPG and returns 5,030 to PEN_b. Two cells each, so non-directional. Hypothesis: activity-dependent global inhibition that normalises bump amplitude, the slow amplitude control the Bayesian ring attractor needs (Kutschireiter 2023). Test: bump amplitude dynamics after ExR6 silencing.
7. **P6-8P9 closes the bridge seam.** Four glutamatergic cells collect Delta7 and EPG input from glomeruli 6–8 (verified: inputs from Delta7 L1L9R8, L8R1R9 and EPG R8/R7/L8/L7) and output to EPGt (glomerulus 9), PFNa glomerulus 9 and IbSpsP glomerulus 9. This is the missing closure at the outer glomeruli that Green 2017 flagged. Test: EPGt tuning with P6-8P9 silenced.
8. **IbSpsP: a second, sinusoidal heading copy into every PFN class, mixed with a gnathal input.** 31 cholinergic cells; 31 % input from Delta7, plus GNG311 (11 %) and OLVC5 (visual). Outputs to PFNa, PFNd, PFNp, PFNm and PEN_b. Hypothesis: gain control of the heading input to the vector system by a feeding/motor state carried by GNG311.
9. **Dorsal-layer state enters the goal population through hDeltaD/E and vDeltaA.** vDeltaA_a (70 cells) is driven by FB9A/FB9B, SA3 and SAF (the sleep/arousal-related SA neurons), and drives hDeltaD, which delivers a 180°-inverted signal to FC2C. FC2C is therefore the subtype coupled to arousal state; FC2A is coupled to self-motion/airflow (hDeltaJ from hDeltaB, PFNp_c, PFNa); FC2B to the MB-relay FB5AB and the working-memory loop (via hDeltaC). This is the first structural basis for a functional split among FC2 subtypes.
10. **FS4A/B/C and FS2: navigation state broadcast to the superior medial protocerebrum.** 57 + 29 + 28 + 42 cells reading hDeltaB, hDeltaD/E/L and FC2, projecting to SMP and SLP. Function unknown; the SMP is neuroendocrine/state territory, so this is where "how far and which way" could modulate metabolism or arousal.
11. **FB2I_a: 40 % self-recurrent glutamatergic tangential in the PFNa/FC1 (airflow) layer** with non-CX inputs (ATL013, LHPV6f1, PLP071). A persistent state in the airflow-vector layer; candidate for holding wind direction across gaps.
12. **LCNOpm and LCNOp: the nodulus inputs to PFNp/PFNm are dominated by external LAL/SMP sources** (LAL112, SMP147, LAL050, SIP004; 66 % of LCNOpm input is non-CX). Whatever PFNp_b (136 cells, the largest CX type) encodes, its amplitude is set from outside the CX by these cells.

## C. Simulation results used above

- [simulations/eb_epg_pen_loop.py](../simulations/eb_epg_pen_loop.py): ring attractor with EB-side EPG→PEN feedback at 0, 0.25, 0.5, 1, 1.5, 2.7 × the PB weight. Rotation gain for a fixed velocity input: −139, −102, −72, 0, 0, 0 °/s; dark drift unchanged. The loop brakes rotation and locks the bump above unit strength. Model is minimal (rate units, uniform inhibition), so treat as a qualitative prediction.
- [simulations/pfr_integrator.py](../simulations/pfr_integrator.py): see A1. Results in `simulations/pfr_integrator_results.json` and `pfr_integrator_signflip.json`.

## D. Priority list for experiments

1. PFR_a transmitter and PFR-vs-hDeltaB bump offset (decides relay vs integrator).
2. FB4M/FB4L/FB1H responses to sugar (decides whether a dopamine write signal exists at the vector stage).
3. hDeltaM antiphase to FC2 and its role in avoidance (cheap imaging test of the anti-goal channel).
4. FS1A→oviIN behavioral test (oviposition after FS1A silencing).
5. FB3A and PS196_b walking-speed tuning (sources of self-motion).
6. LAL121 sign and timing (what the steering command looks like after the LAL).

## Tables and scripts

`data/derived/cx_type_profiles.json`, `cx_type_edges.csv` ([scripts/cx_type_profiles.py](../scripts/cx_type_profiles.py)); `cx_cells.csv`, `cx_cell_edges.csv` ([scripts/cx_cell_edges.py](../scripts/cx_cell_edges.py)); `fb_column_offsets.csv`, `pbfb_glomerulus_column_map.csv` ([scripts/fb_column_offsets.py](../scripts/fb_column_offsets.py)); `cx_screen.csv`, `cx_sharp_offsets.csv` ([scripts/cx_unbiased_screen.py](../scripts/cx_unbiased_screen.py)).
