# The compass and vector systems get their motion signals from cells nobody has named

**Summary.** The compass and vector systems need rotational and translational velocity, and the neurons that deliver those signals are known (GLNO into the PEN shifters; LNO2 and SpsP into PFNd), but what drives them was left open by Hulse 2023 and Lu 2022. An unbiased screen of the connectome points at two unnamed cell types and an ascending neuron behind them. PS196_b, a posterior-slope type that Hulse 2023 flagged as GLNO's largest input, also reaches ExR2, ExR4, LPsP and FB3A, so one type feeds the rotational velocity input, the dopamine neuron that gates compass learning by rotation speed, and the translational side at once; its own largest distant input is an ascending neuron, AN07B037, which also reaches LNO2, so the signal looks body-derived rather than a motor-command copy. FB3A, four glutamatergic tangential cells, supplies 12 percent of PFNd's input and pools visual motion, antennal mechanosensation and a second ascending neuron: the candidate for the speed estimate that path integration in the dark requires.

## The question

To track heading, the compass needs to know how fast the fly is turning. To build travel direction and distance, the vector system needs to know how fast it is moving forward and sideways. In the dark, neither can come from vision. They must come from the body: either a copy of the command sent to the legs, or feedback from the legs and antennae themselves.

## What is known

Rotational velocity reaches the compass through a single pair of GLNO neurons, the only lateralised velocity input to the PEN shifters. GLNO encodes turning from both vision and "motor" information; Hulse 2023 identified PS196 as its largest input and proposed that GLNO inherits its estimate from that one type, but what PS196 carries was not resolved. Translational velocity reaches the vector system through PFNd, whose forward-velocity scaling comes from the inhibitory LNO2 and SpsP neurons (Lu 2022); where those get it from was not resolved.

## What the wiring shows

Profiling every input to GLNO, LNO2, SpsP, PFNd and FB3A across the whole brain, without any prior about which cells to expect, gives three results.

**PS196_b.** The posterior-slope type is 19 percent of GLNO's input (1,801 synapses). The same type sends 942 synapses to LPsP, 899 to ExR2, 686 to ExR4, and 195 to FB3A. ExR2 is the dopamine neuron that gates compass learning by rotational speed (Fisher 2022); ExR4 provides global feedback onto the shifters. So one type reaches the rotational velocity input, the rotational-speed learning gate, and the translational side at once. PS196's connection to GLNO replicates in the hemibrain (531 synapses), as do LAL139 and LAL184, the other two inputs Hulse 2023 named.

**AN07B037.** PS196_b's inputs are posterior-slope interneurons (PS099, PS048, PS047, PS262) and one ascending neuron, AN07B037_a, at 7 percent; no descending neuron appears among its main sources. The same ascending type sends 1,013 synapses to PS196_a, which in turn is 3 percent of LNO2's input. One ascending neuron therefore stands upstream of both velocity channels.

**FB3A.** Four glutamatergic tangential cells send 5,765 synapses to PFNd, 12 percent of PFNd's input and its third-largest source after LNO2 (9,610) and SpsP (2,384), and 4,020 back from PFNd. Their other inputs are LAL143 (727), fed by the lobula-plate columnar type LLPC1 carrying visual motion; PS326 (511), fed by the Johnston's-organ types JO-EV3 and JO-EV5 and two ascending neurons; AN06B009 (319), an ascending neuron itself; and PS196_b (195). They also reach hΔB (883) and the dopamine type FB4M (576).

## Why it matters

**One source for several velocity consumers.** If PS196_b carries a turning signal, it explains at once why GLNO prefers motor over visual information, where ExR2's rotational-speed signal originates, and how the translational side sees the same signal through FB3A. Its ascending input, and the absence of descending input, argue for a signal derived from the body rather than an efference copy.

**A multimodal input to the vector system.** FB3A is the only large PFNd input that pools optic flow, antennal mechanosensation and leg-derived ascending signals. That makes it the candidate for the speed estimate that walking-based path integration needs when vision alone cannot supply it.

**FB3A is probably a gain control, not a pure speed signal.** It is reciprocal with PFNd (4,020 in, 5,765 out) and glutamatergic, so it is more likely to scale PFNd's response than to drive it feed-forward.

## What would settle it

- Image PS196_b during walking: predict tuning to turning velocity that persists in darkness and, if the signal is body-derived, appears during passive rotation of the legs as well.
- Image FB3A during forward walking with and without visual motion and with antennae immobilised: predict speed tuning that survives loss of vision and weakens without the antennae.
- Silence FB3A and test distance behaviour in the Behbahani task and PFNd speed scaling.

## Prior work

Hulse et al. 2023 (bioRxiv 2023.09.25.559373) identify PS196 as GLNO's largest input, with LAL139 and LAL184, and propose that GLNO inherits its rotational-velocity estimate from it. The fan-out of PS196_b to ExR2, ExR4, LPsP and FB3A, the ascending neuron behind it, and FB3A's mixed inputs to PFNd were not found in print.

## Methods

Inputs to GLNO, LNO2, SpsP, PFNd, FB3A and PS196_b were profiled from the MaleCNS v1.0 flat connectome aggregated to cell type, with no prior restriction to central-complex types; percentages are of the target's total input. Ascending neurons are identified by annotation superclass. Hemibrain replication uses v1.2 traced adjacencies at type level with subtype suffixes merged; AN07B037 and PS326 are untyped there. Tables: `data/derived/brain_type_edges.csv.gz`, `screen_ascending_to_cx.csv`, `cx_type_profiles.json`; scripts: `scripts/brain_type_edges.py`, `full_brain_screens.py`, `cx_type_profiles.py`; notes: `docs/uncharacterised-neurons.md` §B2, §B3, `docs/audit-2026-09-13.md` §3 and §5.

References: Hulse 2023; Lu 2022; Fisher 2022.
