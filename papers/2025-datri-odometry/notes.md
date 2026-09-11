# D'Atri & DasGupta (2025 preprint): distance memory and a PFN→hΔB odometer

[bioRxiv 10.1101/2025.03.23.644782 v1](https://doi.org/10.1101/2025.03.23.644782) · [Captured full text](biorxiv-fulltext-v1.md) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

A short preprint proposing a behavioral assay for distance estimation and the first causal evidence that the translation-vector pathway (PFN→hΔB) is used to measure walked distance. Single flies pace an annular track (interrupted by a wall) in the dark; electric shock is delivered in one quarter. After training, flies avoid that quarter (PI-Place) and shorten their runs between reversals to below the shock-associated run length (PI-Distance). Mean trained run length correlates with mean shock-associated run length (R² = 0.39). Distance memory persists at least an hour while place avoidance decays quickly; orco¹ mutants lose place avoidance but keep distance memory, and wall relocation or wall-less double rotation disrupts only place memory. So place avoidance is attributed to local olfactory marks, distance memory to self-motion.

GtACR1 silencing of Kenyon cell subsets during training affects neither memory. Silencing PFNd, PFNv, hΔB (and PFR per the figure) during training disrupts distance memory but not place memory. Optogenetic activation of hΔB during training near reversal points increases distance error; activation near run midpoints does not; inhibition shows the opposite spatial dependence. During testing, hΔB activation near reversals shortens runs and near midpoints lengthens them in trained flies, whereas naïve flies shorten runs regardless. The authors conclude hΔB output is integrated non-uniformly with the integrator zeroed near run midpoints, echoing Behbahani 2021's center-to-reversal model.

## What to be careful about

- Version 1 is a brief report; Methods, Figure S1 and Tables S1–S2 are in an uncaptured supplement, so genotypes, n, light powers and statistics could not be checked.
- "Distance" here is run length between reversals in a 1D track; heading is not varied. It is an odometer test, not a 2D vector test.
- The hΔB manipulations are spatially targeted light in an arena, so they perturb the population, not specific columns; interpretation as "integrated output" is inferential.
- Naïve-fly run shortening under hΔB activation suggests hΔB drive can directly trigger reversals; this complicates the pure-integrator reading.
- The place/distance dissociation supports Titova/Chen concerns about self-deposited chemical cues in enclosed arenas.

## Remaining questions

1. Where is the accumulated distance held (PFR, per Flores-Valle 2025? FC2/hΔ populations?) and how is it compared to the learned threshold?
2. Does the same odometer serve 2D local search and displacement compensation (Kim 2017, Titova 2023)?
3. Whether the published version changes claims or adds the missing methods.
