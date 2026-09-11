# Corfas, Sharma & Dickinson (2019): diverse food-sensing neurons trigger idiothetic local search

[Published article](https://doi.org/10.1016/j.cub.2019.03.004) · [PMC author-manuscript HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

An extension of Kim & Dickinson (2017). Optogenetic activation of sugar-sensing neurons (Gr43a, Gr5a) at a fixed zone in a dark arena triggers local search: repeated returns to the activation site with search center of mass near the zone. Activation of Ir76b, Or42b (an attractive olfactory channel), NPF and ppk28 (water) neurons also triggers search, but only when the fly is in the matching deprivation state (e.g. Or42b after 7 days starvation; ppk28 after dry starvation). Or59b, Orco, and R58E02 dopamine neurons do not. The behavior also occurs in tethered flies on a ball with closed-loop virtual activation (Figure 4), which is the key preparation-transfer result for later imaging.

Because activation is spatially defined but sensorially impoverished (no substrate cue, dark), and because search persists after activation ends (Figure 3A–B: persistence times up to ~4 min, distances up to ~1.6 m, most much shorter), the authors argue the return behavior uses idiothetic path integration. Note the title's word "idiothetic": the evidence is exclusion of visual cues and a fixed virtual site; substrate/chemical cues left by the fly are not addressed here (Titova 2023 later raises this).

## Figures 1–2: which sensory channels can trigger search

Arena 3 cm scale bar (~10 cm arena), activation zone at the center; 20-min baseline then activation. Metrics: center-of-mass distance to the zone, revisits per search, search distance. Gr43a and Gr5a produce large effects in fed flies. Or42b and Ir76b require prolonged starvation; NPF and ppk28 likewise state-dependent. Raster plots (Figure 1G) show repeated zone residence during activation for the effective genotypes only.

## Figure 3: persistence, two zones, and a maze

Search persists after the zone is disabled. With two activation zones, flies search around both, and residence histograms show two peaks. In a grid maze, search remains centered on the activation node. These argue the searched location is an internal estimate rather than a beacon.

## Figure 4: tethered virtual local search

FicTrac closed-loop fictive position with LED activation when the fictive position enters a zone. Gr43a flies increase revisits and search distance during activation, returning to baseline post; Gr43a/+ controls do not. Speed drops transiently at LED onset (Figure 4F), consistent with a stop-and-turn response.

## Caveats for synthesis

- "Search distance" and revisit counts are per-fly medians of skewed distributions; the violin plots show wide dispersion.
- No neural recording; no test of compass or FB involvement. Behbahani 2021 (same lab) supplies the geometric evidence for a re-zeroing integrator; Chen 2024 and Titova 2023 add chemical-cue alternatives.
- The tethered assay is one-dimensional in the FicTrac position sense but on a 2D fictive plane; later imaging experiments (D'Atri 2025, Flores-Valle 2025) build on it.

## Remaining questions

1. Which internal signal encodes displacement from the site? PFN/hΔB travel vectors (Lu 2022, Lyu 2022) are candidates but were not tested here; Chen 2024 later implicates PFNd in a different reward task.
2. How is the state-dependence (starvation) implemented upstream of the search trigger?
3. Does the fly integrate translation over the whole search, or reset at each return (Behbahani 2021)?
