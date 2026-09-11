# Hige, Aso, Modi, Rubin & Turner (2015): dopamine-gated LTD at KC→MBON synapses

[Published article](https://doi.org/10.1016/j.neuron.2015.11.003) · [PMC author-manuscript HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## Why it is in this library

This is not a navigation paper. It is the reference demonstration of the mushroom-body learning rule that later navigation work borrows by analogy: coincident presynaptic (Kenyon cell) activity and compartment-specific dopamine produce lasting depression of the KC→MBON synapse, independent of postsynaptic spiking. Plitt 2025 explicitly compares the ellipsoid-body ER→EPG rule (coincident ER activity and EL octopamine, EPG spiking dispensable) to this motif. Chen 2024 invokes MB-based odor valence for self-deposited scent marks. Aso 2014 and Scaplen 2021 cover MBON valence and outputs.

## Key results

- Whole-cell recording from MBON-γ1pedc; a single 1-s odor paired with four 1-ms CsChrimson pulses to PPL1-γ1pedc (MB320C) reduces CS+ spike count from 118 ± 8 to 24 ± 7 (n = 7), with a small CS− reduction; lasts ≥ 40 min. Backward pairing (light 0.5 s before odor) has no effect (Figure 1).
- KC odor responses (GCaMP6f, pan-KC) and γ-KC excitability are unchanged by pairing (Figure 2, S7).
- Voltage clamp with QX-314 shows ~90% reduction of odor-evoked EPSC charge (Figure 3); pairing under voltage clamp with 83% spike suppression still yields LTD (Figure 4), so postsynaptic spikes are dispensable.
- Compartment specificity: activating PPL1-γ2α′1 (MB099C) does not depress MBON-γ1pedc; TH-GAL4 (broad, includes γ1pedc) does; inducing γ1pedc LTD does not alter MBON-γ2α′1 (Figure 5).
- Plasticity rules differ across compartments: 1-s pairing fails in α2 (MBON-α2sc with PPL1-α′2α2) but a 1-min, 120-pulse protocol succeeds (Figure 6).
- Depression generalizes across odors in proportion to KC representation overlap (r = 0.90, Figure 7I); behaviorally, PA training generalizes to BA and HP but not EL.

## Points to carry into navigation reading

- "Two-factor" rule: presynaptic activity + neuromodulator, no postsynaptic requirement; potentiation ("forgetting") rule not characterized here.
- Compartment-restricted dopamine action over ~3 µm scales (Fisher 2022 uses this to motivate the ExR2 proximity analysis; Plitt 2025 compares EL–ER cable distances to DAN–KC distances).
- Induction timescale and sensitivity vary by compartment; do not assume one protocol transfers.

## Caveats

- Only two MBON types characterized; whether LTD is pre- or postsynaptically expressed is unresolved.
- Recordings are somatic in awake, immobile flies; no behavior during induction.
