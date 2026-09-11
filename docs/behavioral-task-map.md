# Task map: returning to a food source

A holistic decomposition of one complete behavior into computations, with the neurons that have evidence for each step and the steps that have none. The point is to locate the gaps so that uncharacterised cells can be assigned to them ([uncharacterised-neurons.md](uncharacterised-neurons.md)). Evidence levels: **causal** (silencing/activation changes behavior), **physiological** (activity recorded), **structural** (connectome only), **none**.

Scenario: a walking fly finds a sugar drop, leaves, walks a looping path for tens of seconds in the dark, and returns to the drop (Kim & Dickinson 2017; Behbahani 2021; Titova 2023).

| Step | Computation | Neurons with evidence | Level | What is missing |
|---|---|---|---|---|
| 1 | Detect food, switch state to "search" | Sugar GRNs; Corfas 2019 sensory triggers; state-dependent (hunger) | causal | Which CX-facing signal carries "food here". Candidates: dopaminergic FB4M/FB4L (target hDeltaB, PFNd, PFR_a), FB1H (targets hDeltaJ/FC2A), FR1 outputs to MBON30/PPL1 |
| 2 | Maintain heading | EPG/PEN/PEG/Delta7 ring; GLNO velocity input | causal + physiological | Motor source of GLNO's signal (structural candidate: PS196_b, 19 % of GLNO input) |
| 3 | Anchor heading to cues (or not, in dark) | ER classes → EPG; EL/ExR2 plasticity | causal | In darkness, drift rate sets the return error; nothing known about drift compensation |
| 4 | Body-relative velocity | PFNd/PFNv (LNO2, SpsP, LNO1 inputs) | physiological | Leg/proprioceptive source. Structural candidate: FB3A (12 % of PFNd input; fed by ascending neuron AN06B009, PS326, LAL143) |
| 5 | Rotate velocity into world frame | hDeltaB sums PFNd/PFNv | physiological + model | Backward walking coverage weak |
| 6 | **Integrate travel vector over time into a displacement (home) vector** | Behavior only: re-zeroing (Behbahani), displacement error (Titova), distance memory needing PFNd/PFNv/hDeltaB/PFR (D'Atri) | causal for the pathway, **none** for the integrator | No identified accumulator. Candidates: PFR_a/PFR_b (recurrent, hDeltaB-driven; simulation says the excitatory wiring alone tracks rather than integrates), FR1 (strongest self-recurrence in the FB, hDeltaB input), hDeltaK/PFGs loop (persistence shown for odor) |
| 7 | Store where the food was (zero point) and re-zero on re-encounter | Behavioral (Behbahani re-zeroing) | causal | Write signal unknown. Dopamine FB4M/FB4L/FB1H are the structural candidates by analogy with ExR2 gating compass plasticity |
| 8 | Compute desired direction = home vector inverted (go back) | Theory (Maimon & Abbott 2026); Ishida 2026 shows inversion is possible cellularly | physiological (inversion mechanism), **none** for this use | hDelta classes invert vectors by 180° anatomically; hDeltaM inverts the FC2 goal into PFL3/PFL2, hDeltaH/hDeltaG invert PFR/vDelta inputs into FC2B. Which of these carries "opposite of displacement" is untested |
| 9 | Express desired direction as a goal | FC2 (Mussells Pires 2024) | causal + physiological | hDeltaB has no direct FC2 edge; goal must arrive via hDeltaJ/H/C/G (FC2A/B) or hDeltaL/F/E/D (FC2C). FC2 subtype identity of the return goal unknown |
| 10 | Steer: compare goal with heading | PFL3, PFL2 | causal + physiological | Second goal-like inputs to PFL3 (hDeltaA, hDeltaI: travel-direction derived, ~+90° to +180°; hDeltaM: inverted goal) have no function assigned |
| 11 | Turn | DNa02, DNa03; LAL interneurons; Feng 2024 hierarchy | causal | PFL3→LAL121/126/083→DN stage uncharacterised; PFL has no direct link to LAL013/DNa11 |
| 12 | Detect arrival / stop / start local search | Behavior only | **none** | No candidate. Arrival should correspond to home-vector length near zero; a cell reading the amplitude of the displacement bump would do it (FB tangentials reading PFR/hDelta populations: FB4B/FB4C read hDeltaB and PFR_b; FB5A reads FC2) |
| 13 | Use chemical self-marks instead of, or with, the vector | MB, orco, PFNd (Chen 2024); Titova 2023 | causal | How MB value reaches the CX: structural candidates FB4R (MBON21/MBON09 → hDeltaB), FB4G/FB4H (MBON25/34 → vDeltaK/M → hDeltaA → PFL3), FR1 (hDeltaB → MBON30/PPL1 dopamine) |
| 14 | Broadcast navigation state to other systems (feeding, egg laying, arousal) | none in CX literature | structural | FS1A_a/b/c (goal-layer readouts) send 600–780 synapses each to oviIN, the oviposition inhibitory neuron; FS4A/B/C to SMP; FR1 to MB |

## What the table says

Steps 6, 7, 8 and 12 are the hole: the fly's behavior proves it integrates, stores, inverts and detects arrival, and no neuron has been shown to do any of it. Every other step has at least one named cell type with physiology. The uncharacterised cells whose wiring sits in that hole, with the reasoning, are in [uncharacterised-neurons.md](uncharacterised-neurons.md).

Two caveats carry through. Enclosed-arena evidence for steps 6–8 is contaminated by self-deposited scent (Chen 2024, Titova 2023), so step 13 may substitute for 6–8 over short ranges. And the walking scenario differs from flight: in flight, wind is inferred visually and by saccades (van Breugel 2014; May 2025), and the compass anchors to wind via a separate ring pathway (Okubo 2020).
