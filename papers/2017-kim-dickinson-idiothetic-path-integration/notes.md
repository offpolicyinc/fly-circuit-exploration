# Kim & Dickinson (2017): idiothetic path integration during local search

[Published article](https://doi.org/10.1016/j.cub.2017.06.026) · [Full text](cell-fulltext.md) · [Supplement (Figures S1–S4, Table S1)](mmc1-supplement.pdf) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

The foundational behavioral claim that fruit flies path-integrate. After a hungry fly contacts a 1 µL yeast drop in a 170-mm dark or lit arena, it performs a centered local search: repeated outward loops and returns (median 6.5 revisits in 30 min in the light; 17 in the dark), walking hundreds of millimetres before hitting the wall. The search persists without vision (dark, 850 nm tracking), without food odor (sucrose instead of yeast), and without cuticular pheromones (oenocyte-ablated flies). When the drop is slid to the wall mid-search, most flies keep circling the original location until they re-contact the food, after which some re-center and some search both sites.

A run-and-tumble model built from the measured post-food turn-angle and run-length distributions, even with a 0.75 same-direction turn bias, produces trajectories that drift away from the food and lack the periodic returns seen in flies. Turns are initiated when the fly faces ~110°–140° away from the food and end facing ~45°–90° toward it; run lengths grow with distance from the food (Figure 5). Returns are periodic with spatial constants of ~100–300 mm (autocovariance, Figure 6).

The paper argues idiothetic path integration is the most parsimonious account. It measures no neural signal and does not test a home-vector model explicitly; Behbahani 2021 later supplies the re-zeroing evidence, and Titova 2023 the displacement test. Its "no pheromonal cues" result rests on oenocyte ablation, which removes cuticular hydrocarbons but not necessarily every deposit (Chen 2024 finds tricosene/pentacosene deposits matter in small arenas; Titova 2023 finds naïve flies prefer sites occupied by rewarded flies).

## Supplement (read)

- **Figure S1:** time to find food; orco⁻ flies find yeast as fast as wild type, so orco mutation does not remove yeast olfactory detection, which is why sucrose was used to remove odor. Small-arena (65 mm) trials for yeast, orco, sucrose (Y+ and standard diet) and water; revisits and maximum wall-free distance per condition.
- **Figure S2:** all 21 individual slider trajectories in four columns (before food; after food pre-slide; post-slide before re-encounter; after re-encounter).
- **Figure S3:** run lengths do not follow a Lévy power law; run length and preceding turn angle are uncorrelated (r = 0.055).
- **Figure S4 and Table S1:** radial residence averages before and after food for each condition, with pairwise chi-squared comparisons.

## Caveats for synthesis

- Slider movement was manual and vibration/static could be detected; the authors acknowledge this.
- "Protein-deprived" flies preferring yeast were used; nutritional state gates the behavior (Figure S1D shows no search after sucrose in protein-deprived flies).
- Post-food periodicity is spatial rather than temporal only in the few pausing flies; walking speed is otherwise near constant so distance and time are confounded.
- The Discussion explicitly rejects a claim that the fly represents "food angle"; the metric is descriptive.

## Remaining questions

1. Which neurons integrate translation? The 2017 paper had no candidates; Lu/Lyu 2022 (hΔB), D'Atri 2025 (PFN→hΔB odometry) and Chen 2024 (PFNd required for reward-site learning) are the follow-ups.
2. What sets the ~60 mm search radius and the return trigger?
3. How do chemical self-marks and internal vectors combine (Titova 2023, Chen 2024)?
