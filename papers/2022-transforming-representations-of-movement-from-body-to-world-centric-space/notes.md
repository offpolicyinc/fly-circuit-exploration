# Lu, Behbahani, Hamburg, Westeinde, Dawson, Lyu, Maimon, Dickinson, Druckmann & Wilson (2022): body- to world-centric velocity

[Published article](https://doi.org/10.1038/s41586-021-04191-x) · [bioRxiv v1 PDF (read)](biorxiv-2020.12.22.424001v1.pdf) · [Nature supplementary information](41586_2021_4191_MOESM1_ESM.pdf) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

The first half of the path-integration circuit: how the compass (EPG heading) is combined with body-centric translational velocity to produce a world-centric travel-direction signal. Two PFN classes are the key: PFNd (activity scales with forward velocity) and PFNv (scales with backward velocity). Each class exists as left and right populations whose PB→FB projections are shifted ±45° (PFNd) or ±135°-equivalent (PFNv) relative to heading, and each population's bump amplitude is modulated by lateralised nodulus inputs so that left and right sides are differentially scaled by the sideways component of velocity. The left/right PFN bumps therefore encode heading-rotated vectors whose lengths depend on the fly's body-centric velocity, i.e., a Cartesian decomposition of velocity along axes at ±45° from heading.

The inputs that set these amplitudes: SpsP neurons (PB) and LNO2 neurons (NO) are inhibitory and velocity-tuned, providing the ipsilateral/contralateral scaling; the preprint also identifies LNO1 for PFNv. Electrophysiology in PFNd shows that the heading-dependent tuning comes from the PB (Δ7-shaped input) and the velocity-dependent scaling from the NO, multiplicatively combined in the dendrites.

Downstream, hΔB neurons in the FB receive summed input from all four PFN populations (with the anatomical phase shifts), and imaging shows their bump tracks the fly's world-centric direction of travel rather than heading: it moves with heading when walking forward, shifts by the sideslip angle when walking sideways, and flips 180° when walking backward (rare, tested with backward-walking induced by moonwalker or with open-loop measures). A connectome-constrained model (hemibrain weights, no free parameters beyond gain) reproduces the hΔB travel-direction representation from PFN inputs.

## Math to keep

- Left/right PFNd vectors: a_L·e^{i(θ+45°)}, a_R·e^{i(θ−45°)}, with amplitudes a_L, a_R set by v_forward and the sideslip sign; their sum points in the world-centric direction of travel for forward-going velocities.
- PFNv covers backward velocities with vectors pointing roughly opposite (their FB phase shift places them at ±135°), so the four-population sum spans the full circle.
- hΔB has a 180° internal projection (dendrite in one column, axon in the opposite), which the model shows is needed to combine the inputs correctly.

## Caveats for synthesis

- Read from the bioRxiv v1 PDF; the Nature version adds data (e.g., more on PFNv, hΔB phase analysis) and the supplementary PDF covers only the Nature supplementary discussion, not extended data.
- Velocity tuning of PFNd is largely to forward walking on the ball; the flight case (May 2025, PFNd summing airflow and optic flow) came later.
- The "travel direction" readout is strongest for walking with sideslip; genuine backward walking is rare, so PFNv's contribution is inferred mainly from imaging during rare events and the model.
- Lyu, Abbott & Maimon 2022 (Nature, same issue) reached similar conclusions with a different emphasis (vector computation, PFNd/PFNv/hΔB); the two are complementary and should be read together.

## Remaining questions

1. What integrates hΔB output over time to get position (D'Atri 2025, Chen 2024, and the FC/PFL populations discussed in Maimon & Abbott 2026)?
2. How SpsP/LNO inhibition is tuned in flight versus walking.
3. Whether hΔB carries a signed speed (vector length) reliable enough for odometry.
