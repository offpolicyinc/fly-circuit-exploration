# Behbahani, Palmer, Corfas & Dickinson (2021): re-zeroing the path integrator at the food

[Published article](https://doi.org/10.1016/j.cub.2021.08.006) · [PMC author-manuscript HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

The most quantitative behavioral constraint in the local-search series. Flies walk in a narrow circular channel (circumference 52 body lengths, 125 mm), so position is one-dimensional. Optogenetic Gr43a activation at a fixed "food zone" produces back-and-forth excursions centered on the food: excursion distances are stable across successive excursions (mean 5.3 body lengths, Figure 1E–F), and after the zone is disabled the run lengths grow with each excursion (Figure 1H) while remaining centered on the last food location (Figure 1M) until a long "departure" run. With two food zones, flies center runs between them; with three zones at different final-food positions, the post-activation run midpoints stay near the *center of the food ensemble*, not the last activation (Figure 6N). A center-to-reversal (CR) model that reverses after traveling a fixed distance from a running average of food positions fits better than food-to-reversal models that reset at the last activation.

This is direct evidence that the return target is an internal estimate that (a) is re-zeroed by food encounters and (b) averages across multiple encounter positions. It is one-dimensional and short-range, and no neural variable is measured.

## Figures 1–2: excursions, growth after food loss, and returns to a disabled zone

Activation events are dense during the activation period (AP). Runs before and after each activation are symmetric and short; after the AP the run length rₙ increases roughly linearly with N while the first post-AP run r₁ scales with the final excursion distance (Figure 1I, slope near 1). Run midpoints during AP and post-AP are tightly concentrated at the zone (Figure 1M). Figure 2 alternates the active zone between two positions across trials: transit frequency peaks at both positions (Figure 2E), and the number of run midpoints in the activation-zone quadrant far exceeds control quadrants (Figure 2G).

## Figures 3–6: models

- **Food-to-reversal (FR):** at each food stimulus, position resets to zero; walk until |position| ≥ r_t, then reverse and draw a new r_t. Reproduces AP behavior but predicts two separate peaks with two foods (Figure 4D), whereas flies show a single central peak (Figure 4B).
- **FR′:** reset only at the first food of an excursion. Still centered on the last food (Figure 6F, peaks shift with final-food position).
- **Center-to-reversal (CR):** maintain a running center of foods, d = (1 − 1/N) d after each new food, and reverse at fixed distance from that center. Predicts a single peak in the two-food case and invariance of run midpoints to final-food position (Figure 6J), matching the data (Figure 6N).

The models are minimal state machines (Figure 3A); their fit is to run-midpoint kernel density estimates, and the discrimination rests on the two- and three-food experiments.

## Caveats for synthesis

- One-dimensional channel: heading is constrained to two directions, so the integrator only needs signed distance. Generalization to 2D search (Kim 2017, Corfas 2019) requires a direction estimate.
- Fixed fictive positions in the channel, with arena walls as potential tactile references; the authors argue against wall use but the channel is only ~4 mm wide.
- Chemical deposition on the channel floor is not controlled (see Titova 2023, Chen 2024).
- Post-AP growth in run length could reflect decaying expectation rather than integrator noise; the paper does not distinguish these.

## Remaining questions

1. Which neurons hold the running center? Candidates from later papers: hΔB/PFR travel vectors (Lu, Lyu, Flores-Valle), FC2 goal (Mussells Pires), or hΔK persistence (Kathman). D'Atri 2025 proposes an odometry-related FB population.
2. How is "distance from center" measured: step counting, optic flow, or a vector norm? The CR model is agnostic.
3. Does re-zeroing occur in 2D search? Titova 2023 (displacement) is the closest test.
