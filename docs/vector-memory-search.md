# Where is the fly's path integrator? A systematic search of the connectome

> **Superseded in part (2026-09-12).** The sign analysis in [exhaustive-search.md](exhaustive-search.md) §4 shows the "hΔJ anatomy inverts the stored vector" claim below is wrong once phases are anchored to the published conventions; hΔJ's input is bimodal and its stored vector cancels. The negative result on activity-based storage, the OA-VPM3 and FB4M/FB1H convergence, and the need for an inversion stand. Read this document for the search method and the corrected one for conclusions.

Date 2026-09-12. Scripts: [vector_memory_screen.py](../scripts/vector_memory_screen.py), [recurrence_modes.py](../scripts/recurrence_modes.py), [reward_inputs_trace.py](../scripts/reward_inputs_trace.py), [fb_column_offsets.py](../scripts/fb_column_offsets.py) (angle-aware version). Simulations: [synaptic_path_integrator.py](../simulations/synaptic_path_integrator.py), [closed_loop_return.py](../simulations/closed_loop_return.py). Tables: `vector_memory_screen.csv`, `recurrence_modes.csv`, `recurrence_loops.csv`, `fb_offset_stats.csv`, `reward_inputs_trace.json`.

## The question

Flies integrate their movements: after leaving sugar they return to it in darkness, they re-zero the estimate at food, and silencing PFNd, PFNv, hΔB or PFR removes a distance memory (Kim 2017; Behbahani 2021; Titova 2023; D'Atri 2025). The instantaneous inputs are known: PFNd/PFNv carry velocity, hΔB carries world-frame travel direction (Lu 2022; Lyu 2022). Nothing is known about what accumulates that over time, what stores the zero point, and what converts the accumulated displacement into a direction to walk. This document reports a systematic search of the MaleCNS connectome for wiring that could do those three things, the two mechanisms considered, and the one that survives.

## Correction applied first

Column labels in the fan-shaped body do not all mean the same angle. hΔA, hΔB, hΔC, hΔI, hΔJ, hΔK and hΔL divide the FB into 12 columns; hΔD/E/G/H/M, PFNd and FC1F into 8; hΔF into 6; the remaining types use nine labels with C1 and C9 sharing a heading. Earlier analyses in this repository folded every type to 8 positions, which distorted every phase involving a 12-column type. All offsets are now computed in degrees per type (`fb_offset_stats.csv`) and binned afterwards. With the correction, every hΔ output lands 193°–202° from its input column with concentration 0.86–0.94, exactly the 180° inversion Hulse 2021 described anatomically, plus a ~15° label offset between the 12- and 8-column systems.

## Mechanism 1: an activity-based (attractor) integrator. Not supported.

An integrator held in ongoing activity needs recurrent connections whose "which direction" mode has gain near 1 while the "everything on" mode stays below 1. Scoring every columnar type's within-type recurrence as a fraction of its total input, signed by predicted transmitter:

| type | cells | self synapses | uniform-mode gain | vector-mode gain |
|---|---:|---:|---:|---:|
| vΔA_a | 70 | 3,266 | 0.21 | 0.14 |
| PFNv | 20 | 9,048 | 0.44 | −0.05 |
| FR1 | 18 | 8,694 | 0.30 | −0.04 |
| PFNa | 58 | 13,850 | 0.36 | −0.01 |
| PFNd | 40 | 8,109 | 0.17 | 0.00 |
| PFR_b | 16 | 1,722 | 0.07 | −0.01 |
| hΔK | 31 | 372 | 0.01 | 0.01 |
| hΔJ | 31 | 440 | 0.01 | 0.00 |
| hΔB | 19 | 882 | 0.02 | 0.00 |

No columnar type has a vector-mode recurrent gain above 0.14, and most are below 0.02. The strongest cross-type loops (PFR_a↔PFR_b, PFR_a↔hΔA, hΔK↔PFGs, hΔC↔hΔF, FC2B↔hΔM) have loop gains below 0.01 in either mode. The eight-cell hΔ types (D, E, G, H, M) do form the clean reciprocal column pairs 180° apart that Hulse 2021 proposed as one-dimensional stores (e.g. hΔM C1↔C5 101/44 synapses, C2↔C6, C3↔C7, C4↔C8, and almost nothing else), but at 30–100 synapses per cell against thousands of input they cannot sustain activity on their own. Conclusion: unless synaptic efficacies are an order of magnitude larger for these specific synapses than for everything else, or the cells have intrinsic persistent currents (which a connectome cannot see), the fan-shaped body does not hold a displacement vector as recurrent activity. The rate-model test of PFR ([finding 3](findings/03-pfr-integrator.html)) is the specific case of this general result.

## Mechanism 2: a synaptic integrator. Every required element is present at one site.

The alternative, proposed in outline by Maimon & Abbott 2026 and Hulse 2021, is that the displacement is stored in synaptic weights: a travel-direction bump continuously potentiates its synapses onto a columnar target while the fly walks, so the weight pattern across columns accumulates the vector sum of the path. This needs (a) a presynaptic travel-direction population, (b) a columnar postsynaptic population that tiles heading, (c) a modulator present while walking to permit potentiation, (d) a reset signal at food, and (e) a readout that turns the stored displacement into a return goal. Screening all 56 columnar types for these:

**(a)+(b): hΔB → hΔJ.** hΔJ is the strongest two-hop route from travel direction to the goal population (hΔB→hΔJ 4,232 synapses; hΔJ→FC2A+FC2B 5,732), ahead of hΔH (1,010 / 2,776) and hΔG (736 / 3,171). Every one of the 31 hΔJ cells receives 90–200 hΔB synapses and sends 40–130 to each of FC2A and FC2B. hΔB input to hΔJ arrives at 6° mean offset (column-matched), so a weight pattern on hΔJ is in the same coordinates as the travel-direction bump.

**(c): FB4M and FB1H dopamine, driven by walking.** FB1H synapses onto every hΔJ cell uniformly across columns (73–129 per column, 1,184 total); FB4M adds 625 uniformly. FB4M's own inputs are PFNv (1,170), hΔB (739), PFNd (701), FB3A (576) and ExR7 (571): it is driven by the velocity system itself, so it fires when the fly moves. This is the same logic as ExR2 dopamine gating compass plasticity by rotational speed (Fisher 2022), applied to translation. FB4M also targets hΔB (3,391) and PFR_a (735), the other candidate sites.

**(d): OA-VPM3 octopamine targets the same cells.** *(Correction 2026-09-14: OA-VPM3 is not a reward neuron; it gates recent-memory expression in the mushroom body, Kapoor & Waddell 2024. The wiring below stands, the label does not.)* The unbiased screen of external inputs found OA-VPM3, an octopaminergic neuron pair implicated in sweet-taste reward signalling to the mushroom body (Burke 2012 and later work), projecting onto hΔB (646), PFR_a (427), hΔJ (377), hΔH (361), hΔC (353), PFGs (342), PFNv (321), hΔM (255) and PFNd (226). Its inputs include Kenyon cells (KCg-m 801), SMP457 (which FR1 and FS2 target), and the FB6A/FB6C/FB6D tangentials of the working-memory loop. It is the only identified reward-class neuron with direct access to the travel-direction and goal-input populations, and it is reciprocally coupled to them.

**(e): the hΔJ anatomy inverts the stored vector.** hΔJ output onto FC2A/FC2B arrives at 194°/195° (concentration 0.88). A displacement stored in hΔJ input coordinates is therefore delivered to the goal population pointing the opposite way: toward the start. The "invert home vector into return goal" step, which the task map listed as missing, is done by the same cells' anatomy.

## Simulation: the synaptic integrator with the measured kernels

`synaptic_path_integrator.py` potentiates weights on 8 hΔJ columns through the measured hΔB→hΔJ kernel while a walking-gated modulator is on and zeroes them at reward. Over a three-leg path the stored weight vector points within 9° of the true displacement at every step and its length tracks distance; a speed-scaled modulator adds a small bias; a partial reset (50 % at each of three rewards) gives the running average of reward positions that Behbahani 2021 inferred behaviourally.

`closed_loop_return.py` puts the whole chain in an agent: exact compass, hΔB bump, weights on hΔJ, readout as hΔJ activity = weights × presynaptic drive passed through the measured hΔJ→FC2A kernel, PFL3-style steering (turn ∝ sin(goal − heading)), 30 s random outbound walk, 60 s to return. Median outbound distance 11.1 units.

| readout kernel from hΔJ to FC2 | returned within 0.5 | median closest approach |
|---|---:|---:|
| measured (194°) | 35 % | 1.36 |
| ideal 180° | 35 % | 1.05 |
| 135° | 43 % | 0.96 |
| 90° | 20 % | 2.64 |
| no inversion (0°) | 0 % | 10.29 |
| no memory (random walk) | – | 6.76 |

The measured anatomy performs as well as an ideal inversion; without the inversion the agent walks away from food. The controller is crude (no arrival rule, no gain tuning), so the absolute return rate is not meaningful; the comparison across kernels is.

## What the search says about the other candidates

- **PFR_a/PFR_b**: receive hΔB at 195° and PFNd at 21°, i.e. the inverted travel vector and the non-inverted heading-frame velocity vector. These cancel during straight forward walking and do not cancel during sideslip or backward travel. PFR looks like a heading-versus-travel mismatch signal, sent to LAL002 and to hΔA. Not an integrator (finding 3), but a plausible reason D'Atri's distance task and Flores-Valle's drift both involve it.
- **hΔA and hΔI**: receive hΔB at ~0° and deliver to PFL3 at ~194°: a "turn back" input to the steering neurons that needs no stored goal. Gated by MB-fed tangentials (FB4G/FB4H via vΔK/vΔM).
- **FR1**: receives hΔB at 195° and has the strongest self-loop (uniform mode 0.30, no direction selectivity); outputs to MBON30 and PPL1 dopamine. A scalar (distance-like) accumulator feeding the mushroom body is the reading consistent with its wiring; it cannot hold a direction.
- **hΔK / PFGs**: hΔB→hΔK at 180°, hΔK→PFGs 196°, PFGs→hΔK 165°, round trip ≈ 0: a loop that can hold a column, which is the Lanz/Kathman working memory; loop gain is small, so persistence must come from cellular properties or the FB6A/FB6M gates.

## Hypothesis, stated once

The fly's home vector is stored as a pattern of synaptic weights at the hΔB→hΔJ synapses (and possibly hΔB→PFR_a and hΔB→hΔH in parallel), written continuously while walking under FB4M/FB1H dopamine, erased or attenuated at food by OA-VPM3 octopamine, and read out into the FC2 goal population already inverted by hΔJ's anatomy, from where PFL3 steers the fly back. Arrival corresponds to the weight vector shrinking toward zero, which silences the goal and releases local search.

## What would test it

1. Image hΔJ during Behbahani's 1D re-zeroing task: predict a bump whose position tracks the direction back to the fictive food centre and whose amplitude grows with distance from it; predict collapse at re-zeroing.
2. Silence OA-VPM3 during local search: predict search no longer centres on the food (no re-zeroing), while odometry persists.
3. Silence FB4M/FB1H or block dopamine receptors in hΔJ: predict loss of the return vector with intact instantaneous travel-direction coding in hΔB.
4. Pair OA-VPM3 activation with walking in a fixed direction: predict a shifted search centre (Behbahani's running average) without any food.
5. Block plasticity in hΔJ (e.g. cAMP pathway) and look for loss of D'Atri's distance memory with PFN/hΔB tuning intact.

## Limits

Synapse counts only; no transmitter, receptor, plasticity or timing data. OA-VPM3's reward role is from the mushroom-body literature; its relation to sugar contact in walking flies has not been recorded. The model's readout multiplies weights by presynaptic activity, so goal expression needs some hΔB drive; how the goal is expressed when the fly is stationary is untested. Cellular persistence (T-type or plateau currents, cf. Ishida 2026) could rescue mechanism 1 without any recurrence and is invisible here.
