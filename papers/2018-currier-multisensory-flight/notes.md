# Currier & Nagel (2018): a wind cue and a visual cue drive opposite orientations in tethered flight

[Published article](https://doi.org/10.1016/j.cub.2018.09.020) · [PMC author-manuscript HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

A behavioral study of multisensory cue combination in rigidly tethered flying flies. With closed-loop control of a rotating stage carrying a wind source and a dark vertical stripe, flies orient **downwind** to wind alone and **toward** the stripe alone. When both cues come from the same direction, the two drives conflict; the fly's behavior is well captured by a sum of two independently filtered single-modality turn commands (spatial tuning × temporal filter). The wind filter is transient (adapting), the visual filter is sustained. This is a compact model of how two egocentric orientation signals combine at the level of steering, with no compass or goal variable involved.

It matters for the synthesis in two ways: it shows the fly's default wind policy in flight without odor is downwind (as in Currier 2020), and it shows that multisensory conflict yields turn sequences and slowed turn rates rather than averaged headings. Neither result speaks to remembered directions or locations.

## Setup and measurements

Tethered flight in an arena with a wind tube and stripe co-mounted on a stage that rotates in closed loop with wingbeat-amplitude difference (ΔWBA). Windspeed ~45 cm/s at the fly, independent of stage angle; stimulus onset within ~30 ms. Antennae were stabilized in some experiments by gluing. Trials start with the stimulus at 0° or 90° and last ~25 s.

## Key results (Figures 2–5)

- Wind alone: flies turn away from wind until it is behind them (ΔWBA vs initial orientation is a sawtooth with reversal at 0°). Vision alone: flies turn toward the stripe. Multisensory: initial turns away from the cue, then slow drift back toward it; the polar distribution of orientations is bimodal (front and back), not an intermediate average.
- The wind response depends on intact antennae; antenna-stabilized flies do not turn downwind and their multisensory behavior collapses onto the visual response. Turn rate per unit orientation error decays over seconds for wind but not for vision, motivating an adapting wind filter.
- Increasing windspeed from 0 to 45 cm/s increases latency to the visual-directed turn and the maximal deviation, and decreases turn rate; the model reproduces this by increasing α_w with windspeed.
- Spatially offsetting wind and stripe changes the trajectories as predicted by shifting the wind spatial filter.

## The models (Figure 3, equations 1–11)

Spatiotemporal filtering (STF): turn command c(t) = α_w F_w(t) D_w(s_w(φ)) + α_v F_v(t) D_v(s_v(φ)), with D the spatial tuning (measured from ΔWBA vs orientation), F_v = 1 and F_w(t) = s_w(ρ)(t) − ((1 − β_w)/τ_w) ∫₀ᵗ e^{−x/τ_w} s_w(ρ)(t − x) dx (an adapting filter with steady-state fraction β_w). Four free parameters (α_v, α_w, τ_w, β_w) fit to median orientation traces.

Alternatives with matched parameter counts: pure sensory delays (20 ms wind, 100 ms vision), dynamic target averaging (θ_t = γF_w θ_{t,w} + θ_{t,v}, divided by 2, then proportional control), and a PID controller with integral/derivative terms only for wind. STF and the delay model fit orientation traces best (lowest RMSE, Figure 3G–H); the target-averaging model fails to reproduce the bimodality and the turn-slowing. Noise for simulation was matched to the ΔWBA power spectrum in the no-stimulus condition.

## Caveats for synthesis

- Rigid tether, no free-flight aerodynamics, no odor. The downwind default is context-dependent (see Currier 2020, van Breugel 2014 for upwind surges with odor).
- The spatial filters are measured from the same data used to fit; the model's discriminative power lies in the temporal terms.
- Bimodal orientation distributions in the multisensory condition should not be summarized as a mean heading.
- The author manuscript is pre-copyedit; some methodological sentences are garbled ("The res ulting").

## Remaining questions

1. What circuit implements the adapting wind filter and the summation? The paper points toward central-complex integration (E-PG wind responses were unknown at the time); Okubo 2020 and Currier 2020 later supply candidates (R1 and PFNa).
2. How does the sign of the wind policy flip with odor or state? Matheson 2022, Siliciano 2026 and Kathman 2026 address upwind persistence in walking.
3. Data and model code are public (Dryad doi:10.5061/dryad.m715hp3; github.com/nagellab/CurrierNagel2018) and were not checked.
