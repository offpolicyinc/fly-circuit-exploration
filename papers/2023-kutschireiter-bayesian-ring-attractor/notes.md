# Kutschireiter, Basnak, Wilson & Drugowitsch (2023): Bayesian inference in ring attractor networks

[Published article](https://doi.org/10.1073/pnas.2210622120) · [PMC HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

The theory paper behind the "bump amplitude encodes certainty" idea. Starting from a generative model in which heading performs a random walk on the circle and is observed through noisy von Mises-like cues, the authors derive a circular Kalman filter (circKF) that tracks heading as a phasor whose angle is the estimate and whose length is the certainty. The update has three terms: certainty decays through diffusion (proportional to the cube of the current certainty at high certainty), observations add a vector weighted by their reliability, and the angle moves by the tangential component of the observation. A network implementation follows: a classical ring attractor with the readout phasor as its bump, where linear dynamics plus a weak quadratic amplitude decay make the bump amplitude track the posterior certainty rather than saturating. This "Bayesian ring attractor" nearly matches the circKF and outperforms a classical (fast-saturating) ring attractor in tracking accuracy, especially when observation reliability fluctuates.

Predictions that connect to experiments: bump amplitude should fall in darkness and rise with a reliable cue; the same input should move the bump farther when certainty is low (new cues dominate weak priors); after a conflict between cues, the compass should reweight rather than snap. Basnak 2025 tests several of these in EPG imaging. The paper also builds a Drosophila-like version with EPG, PEN/Δ7-style connectivity and shows the same Bayesian regime is achievable with biologically plausible constraints, including with the amplitude-decay implemented by the nonlinearity of firing rates.

## Math worth remembering

- Posterior parameterised by phasor z = r·e^{iφ}; the circKF updates r and φ with prior diffusion constant κ and observation reliability κ_obs.
- Network: dz/dt = (α − β|z|²)z + input, with the ring's linear part implementing rotation and integration; the Bayesian regime requires slow amplitude decay, i.e., weak nonlinearity near the operating point.
- Angular velocity input is integrated by the same rotation term, so path integration and cue integration share the machinery.

## Caveats for synthesis

- The theory assumes a single heading cue class at a time and independent noise; Mitchell 2023 and Basnak 2025 address multiple cues.
- The quantitative link between bump amplitude and behavioral certainty is a hypothesis; Basnak 2025's evidence is correlational.
- The model does not say how the fly learns cue reliability, which Fisher 2022 and Plitt 2025 address at the ER→EPG synapse.

## Remaining questions

1. Does bump amplitude actually gate behavior (e.g., turn size or goal commitment)?
2. How does the Δ7 inhibitory structure map onto the required weak amplitude nonlinearity?
3. Can the framework absorb the 8-axis vector representations of the fan-shaped body (Maimon & Abbott 2026)?
