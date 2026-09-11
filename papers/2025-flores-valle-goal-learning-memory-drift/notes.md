# Flores-Valle et al. (2025 preprint): goal learning, memory and drift in the head direction system

[bioRxiv 10.1101/2025.03.20.644317](https://doi.org/10.1101/2025.03.20.644317) · [Captured full text](biorxiv-fulltext-v1.md) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

Evidence that fan-shaped-body neurons encoding walking direction (PFR, with hΔB also examined) show state-dependent dynamics that carry a goal memory. Flies walk in a 2D virtual arena under a two-photon microscope in a heat-based spatial learning assay adapted from earlier place-learning work: the arena is hot except for a cool area positioned in front of one of two visual stripes (bright or dim), and flies are trained for 10 trials, each lasting until the fly stays in the cool area for 10 s. During walking the PFR bump tracks walking direction. When the fly stops, the bump keeps moving autonomously (drift), and the drift distribution centres on directions roughly opposite (~180°) to the directions represented during walking, so rest and walking states compute something different. Targeted optogenetic activation of PFR neurons during rest is sufficient to bias the fly's subsequent walking direction. After training, the rest-state drift distribution changes in a way that depends on the trained goal direction, revealing a memory held in the network rather than in the sensory scene.

The authors frame the head direction/FB system as a compact architecture for direction selection, learning and memory, and draw parallels with mammalian rest/sleep reactivation.

## Why it matters for the circuit program

- Provides a candidate site and readout for stored goal direction upstream or alongside FC2/PFL3 (Westeinde 2024, Mussells Pires 2024): a drift distribution during quiescence.
- The ~180° rest/walk relationship rhymes with Ishida 2026's inversion and with the Maimon & Abbott 2026 claim that FB populations can hold vectors; the mechanism here is unknown.
- D'Atri 2025 found PFR silencing among the manipulations that abolish distance memory, so PFR sits at the junction of odometry and goal representation.

## Caveats for synthesis

- Preprint read from bioRxiv HTML; figure images were viewed in the browser but not saved; supplementary material not obtained.
- Drift during rest might reflect loss of PFN velocity input rather than a goal computation; the learning-dependent shift is the main argument against a purely passive explanation.
- Whole-population optogenetic activation and heat-based aversive learning with a visual landmark; transfer to landmark-free or appetitive settings is untested.

## Remaining questions

1. Is the rest drift a general FB phenomenon (PFL, FC2, hΔ) or specific to PFR?
2. What input flips at rest, and is it related to the octopamine/dopamine signals of Plitt 2025 and Fisher 2022?
3. Does the learned drift bias predict individual flies' choices trial by trial?
