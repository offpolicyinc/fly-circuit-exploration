# The fly's running sum of its own steps may be held in synapse strengths, on two hΔ neuron types nobody has recorded

**Summary.** A fly that leaves food and wanders in the dark can walk straight back, so it keeps a running vector sum of its steps. The neurons that report each step, hΔB, are known. Maimon & Abbott 2026 proposed that the columnar populations feeding the goal neurons FC2 could each store a vector, for different durations, as activity or as synaptic weights; two of those populations have since been recorded in the Maimon lab and both integrate in activity over seconds, with a leak (hΔG: Janke 2025; hΔA: Avritzer 2026). A minutes-long sum that survives a detour has not been found in any of them. This page asks what the wiring says about a synaptic version: hΔB's travel-direction bump lands on hΔH and hΔI in the matching column, so each step would strengthen only the synapses for its direction and the weight pattern across columns would be the sum; dopamine types cover every cell of both as a write gate; and their outputs reach FC2 and the steering neurons PFL3. The connectome cannot decide between activity and synaptic storage, and it cannot tell a leaky integrator from a lasting one. What it can do is say where to look, and hΔH and hΔI have not been looked at.

## The question

To return to a place it cannot see, the fly must know the vector from that place to itself: the sum of every step since leaving, each step counted in world coordinates. The fan-shaped body has the neurons that report each step: about twenty hΔB cells whose bump of activity sits at the column matching the direction the fly is moving, with height proportional to speed (Lu 2022; Lyu 2022). Each column is a compass direction, so the bump is the current step as a vector. The question is what adds these steps up, and for how long.

## Two ways to hold a running sum

The first is in activity. A population keeps firing the current total and adds each new step to it. For the total not to leak away, the population must excite itself with a gain of almost exactly one. This is how most models of path integration work.

The second is in synapses. Nothing keeps firing. Each step makes hΔB strengthen the synapses it is currently using. After a walk, the pattern of synapse strengths across the columns is the sum: six steps north and four south leave the north synapses at six and the south ones at four, and the difference is a vector of length two pointing north. This needs no self-excitation. It does need hΔB to land on its target in the matching column, a signal that says "write now" while the fly walks, a reset at food, and a path from the store to the neurons that steer. Hulse 2021, Goulard 2023 and Maimon & Abbott 2026 have all described vector memories of this kind, and Dan 2024 modelled a goal angle stored as a set of synaptic weights onto the steering neurons.

## What has been recorded

Two of the hΔ populations that feed FC2 now have physiology, both from the Maimon lab and both available as thesis abstracts.

- **hΔG** (Janke 2025): activity drops sharply when the fly reaches sugar, then its mean rises over minutes while the amplitude of a sinusoidal bump tracks the distance walked over the past few seconds. The bump is built by integrating input from vΔE, with a continuous leak, so it is not a perfect path integral. The same vΔ→hΔ motif recurs across layers of the fan-shaped body.
- **hΔA** (Avritzer 2026): integrates the fly's recent travel direction over a window of 7–10 s and feeds the steering circuit as an inertia term that promotes continuing in that direction.

Both are integrators, both are leaky over seconds, and both are visible in calcium. hΔK adds a third measured case, a persistent bump that accumulates odour evidence and holds an upwind heading for tens of seconds (Lanz 2025; Kathman 2026). None of them has been shown to hold a displacement across a detour of minutes and point home afterward, which is what the behaviour requires (Kim 2017; Behbahani 2021; Titova 2023).

## What the wiring cannot decide

Could a lasting sum be held in activity somewhere in the fan-shaped body? Counting each population's synapses onto itself, binned by column offset, and taking the cosine component as a share of total input gives the same answer for the fan-shaped body as for the compass, whose bump does persist for minutes: vΔA_a 0.145, EPG 0.050, the hΔ types 0.01–0.02, the EPG↔PEN shifter loop 0.003. Synapse shares are not gains and set no threshold. The wiring leaves the activity option open, and it cannot distinguish the leaky seconds-scale integration that has been measured from the minutes-scale integration that has not.

## What the wiring points to for a synaptic store

Scoring every hΔB target for the four requirements of a synaptic store, and setting aside the two populations already recorded, two candidates remain.

| type | hΔB synapses | same column | write gate (cells covered) | reset | sends to |
|---|---|---|---|---|---|
| hΔH (8 cells) | 1,010 | 82 % | FB5H dopamine 249 (8/8) | OA-VPM3 361 (8/8) | FC2, PFL3 |
| hΔI (17) | 3,575 | 48 % | FB4M dopamine 380 (17/17) | none | PFL3, PFL2 |
| hΔJ (31), rejected | 4,232 | 35 % (+28 % opposite) | FB1H 1,184 (31/31) | OA-VPM3 377 | FC2 |

Column matching is what makes a synaptic store work. hΔB lands on hΔH in hΔH's own column 82 percent of the time, so a step north strengthens the north synapses and little else. hΔJ receives more hΔB synapses than any candidate, but in two opposite columns, so every step strengthens both north and south and the sum cancels. In a simulation that writes a random walk through each type's measured landing pattern, hΔH retains 86 percent of an ideal store, hΔI 56, hΔJ 14. (The recorded hΔA and hΔG score 76 and 45; whether a synaptic component sits under their calcium signals is untested.)

A write gate is present on both. FB5H, a dopamine type, contacts every hΔH cell; FB4M, another, contacts every hΔI cell across all columns and is fed by the velocity neurons PFNv, PFNd and hΔB and by an ascending neuron from the ventral nerve cord, so it is placed to fire while the fly walks: the translational counterpart of ExR2, which gates compass learning by rotation speed (Fisher 2022).

A reset is the weakest link. OA-VPM3, the octopaminergic pair that supplies most of the mushroom body's octopamine and gates recent-memory expression there (Kapoor & Waddell 2024), contacts every hΔH cell uniformly across columns; nothing about its known function says it fires at food. hΔI has no uniform octopamine input. Janke's hΔG reset at sugar shows a reset signal exists in this circuit; what carries it is unknown.

The output goes to the right place: FC2 and PFL3, which turn a stored direction into walking (Mussells Pires 2024; Westeinde 2024). Every edge here is present in both connectomes. hΔH meets all four requirements; hΔI lacks the reset.

## How a synaptic store is read

There is no recall step. A store cell fires as hΔB's drive times its synapse strength. hΔB is active whenever the fly moves, so as soon as it walks, the store's output across the columns is the stored pattern, flowing to FC2 and PFL3. The same walking that reads also writes: walking home strengthens the opposite columns until the difference is zero, which is arrival. The output points from food to fly; turning it into "go back" is a separate neuron, and is finding 2.

## What the simulations show

Only a running vector sum reproduces the fly's search behaviour. In Kim's and Titova's assays the search-centre error is 0.8 units for a vector sum, 12.7 for a random walk, and 26.8 for either remembering the direction at the food or the distance walked. In closed loop, an agent using the store returns to the food (median closest approach 1.1 units versus 6.8 without memory), provided the readout is rotated by half a turn before steering; without the rotation it walks away every time.

## What is not known

Nobody has recorded plasticity at these synapses, or dopamine or octopamine acting on them. If synapses only strengthen they saturate over trips; either a reset or a rule that weakens the opposite synapses on the return is required, and the connectome cannot tell which. A fly standing still has no hΔB drive and so no readout. The behavioural premise itself has a caveat: silencing the compass did not reduce direct returns to food in local search (Goldschmidt 2026). And the measured hΔ integrators are all leaky and all in activity, which is a reason to expect the same of hΔH and hΔI.

## What would settle it

- Image hΔH in a fly re-zeroing its home vector (Behbahani 2021), with a cAMP sensor alongside calcium, as Gorko 2025 did for the PFL1 goal circuit where the stored direction proved absent from calcium: a synaptic store grows with distance in cAMP or weights; an activity store grows in calcium; either collapses at re-zero.
- Block dopamine or cAMP signalling in hΔH or hΔI: the fly should stop returning while hΔB and the compass stay intact.
- Silence OA-VPM3 while the fly feeds: if it is the reset, subsequent search should no longer centre on the food.

## Prior work

hΔB as the travel-direction signal: Lu 2022; Lyu 2022. Vector memories in the columnar inputs to FC2, with durations set by mechanism: Maimon & Abbott 2026 (Figure 5). Synaptic storage of a vector or goal angle: Hulse 2021; Goulard 2023; Dan 2024. hΔG as a leaky distance integrator reset at food: Janke 2025 (thesis, abstract; full text embargoed to October 2026). hΔA as a 7–10 s travel-direction memory: Avritzer 2026 (thesis, abstract; embargoed to May 2027). hΔK persistence: Lanz 2025; Kathman 2026. What is added here is the cell-by-cell wiring test of the synaptic version: which hΔ types receive hΔB in the matching column, which have uniform dopamine and octopamine coverage, and the readout and sign analysis that follows in finding 2.

## Methods

Column offsets: every fan-shaped-body neuron in MaleCNS v1.0 carries a column label; angular offsets use the true column count per type (12 for hΔA/B/C/I/J/K/L, 8 for hΔD/E/G/H/M and PFNd, 6 for hΔF; C9≡C1 for nine-label types). hΔ cells are named by their dendritic column (Hulse 2021), and hΔB's bump sits on its axonal arbor (Lyu 2022). Recurrence: within-type synapses binned by angular offset, normalised by total input, signed by predicted transmitter, Fourier-decomposed; compass cells binned by ellipsoid-body wedge. Site screen: every synapse from a travel- or heading-tuned population onto every columnar population scored for column matching, per-cell modulator coverage, and output to FC2/PFL3. Simulations: rate-based agent, eight columns, rectified-cosine hΔB bump written at the axon column, weights incremented through each candidate's measured landing kernel, readout as weights times drive through its measured output kernel. Tables: `data/derived/recurrence_modes_v2.csv`, `fb_column_offsets.csv`, `synaptic_site_screen.csv`, `cx_ext_cell_edges.csv`. Scripts: `scripts/recurrence_modes_v2.py`, `synaptic_site_screen.py`; simulations: `simulations/closed_loop_routes_tspace.py`, `strategy_discrimination.py`, `closed_loop_return.py`. Notes: `docs/exhaustive-search.md`, `docs/audit-2026-09-13.md`.
