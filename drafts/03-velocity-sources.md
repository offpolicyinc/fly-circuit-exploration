# The compass and vector systems get their motion signals from cells nobody has named

**Summary.** The compass and vector systems need rotational and translational velocity, and the neurons that deliver those signals are known (GLNO into the PEN shifters; LNO2 and SpsP into PFNd), but what drives them was left open by Hulse 2023 and Lu 2022. An unbiased screen of the connectome points at two unnamed cell types. PS196_b, a posterior-slope type with no published physiology, is the largest single input to GLNO and also reaches ExR2, ExR4, LPsP and FB3A, so one cell type feeds the rotational velocity input, the dopamine neuron that gates compass learning by rotation speed, and the translational side at once, consistent with a copy of the motor command. FB3A, four glutamatergic tangential cells, receives an ascending neuron from the ventral nerve cord and supplies 12 percent of PFNd's input, making it the only large PFNd input fed by an ascending pathway and the candidate for the leg-derived speed estimate that path integration in the dark requires.

## The question

To track heading, the compass needs to know how fast the fly is turning. To build travel direction and distance, the vector system needs to know how fast it is moving forward and sideways. In the dark, neither can come from vision. They must come from the motor system: either a copy of the command sent to the legs, or feedback from the legs themselves.

## What is known

Rotational velocity reaches the compass through a single pair of GLNO neurons, the only lateralised velocity input to the PEN shifters. GLNO encodes turning from both vision and "motor" information, but the motor source was not identified (Hulse 2023). Translational velocity reaches the vector system through PFNd, whose forward-velocity scaling comes from the inhibitory LNO2 and SpsP neurons (Lu 2022); where those get it from was not resolved.

## What the wiring shows

Profiling every input to GLNO, LNO2, SpsP and PFNd without any prior about which cells to expect gives two results.

**PS196_b.** A posterior-slope cell type with no published function is the largest single input to GLNO: 1,801 synapses, 19 percent of GLNO's input. The same type sends 942 synapses to LPsP, 899 to ExR2, 686 to ExR4, and 195 to FB3A. ExR2 is the dopamine neuron that gates compass learning by rotational speed (Fisher 2022); ExR4 provides global feedback onto the shifters. So one uncharacterised type reaches the rotational velocity input, the rotational-speed learning gate, and the translational side at once. The PS196→GLNO connection replicates in the hemibrain (531 synapses).

**FB3A.** Four glutamatergic tangential cells receive 319 synapses from AN06B009, an ascending neuron whose cell body is in the ventral nerve cord, plus 511 from PS326, 727 from LAL143, 195 from PS196_b, and 4,020 from PFNd itself. They send 5,765 synapses to PFNd, 12 percent of PFNd's input and its third-largest source after LNO2 (9,610) and SpsP (2,384). They also reach hΔB (883) and the dopamine type FB4M (576). Ascending neurons are the route by which leg-derived signals enter the brain.

## Why it matters

**One source for several velocity consumers.** If PS196_b carries a copy of the motor command, it explains at once why GLNO prefers motor over visual information, where ExR2's rotational-speed signal originates, and how the translational side sees the same command through FB3A.

**A leg-derived input to the vector system.** FB3A is the only large PFNd input fed by an ascending neuron. That makes it the candidate for the proprioceptive velocity estimate that walking-based path integration needs and vision cannot supply in the dark.

**FB3A is probably a gain control, not a pure speed signal.** It is reciprocal with PFNd (4,020 in, 5,765 out) and glutamatergic, so it is more likely to scale PFNd's response than to drive it feed-forward.

## What would settle it

- Image PS196_b during walking: predict tuning to turning velocity that persists in darkness and precedes the compass bump shift.
- Image FB3A during forward walking with and without visual motion: predict speed tuning that survives loss of vision.
- Silence FB3A and test distance behaviour in the Behbahani task and PFNd speed scaling.

## Prior work

A search summary attributed to Worden 2025 (arXiv, "Parallel neuron groups") conjectures that PS196 carries rotational velocity into LAL013; the passage could not be located in the paper text. FB3A's role as an ascending-fed input to PFNd was not found in print.

## Methods

Inputs to GLNO, LNO2, SpsP, PFNd and FB3A were profiled from the MaleCNS v1.0 flat connectome by presynaptic cell type, with no prior restriction to central-complex types. Percentages are of the target type's total synaptic input. Ascending neurons are identified by soma location in the ventral nerve cord. Hemibrain replication uses v1.2 traced adjacencies. Tables: `data/derived/cx_type_profiles.json`, `cx_screen.csv`; scripts: `scripts/cx_type_profiles.py`, `cx_unbiased_screen.py`; notes: `docs/uncharacterised-neurons.md` §B2, §B3.

References: Hulse 2023; Lu 2022; Fisher 2022; Worden 2025.
