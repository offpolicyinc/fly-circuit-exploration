# Suver, Matheson, Sarkar, Damiata, Schoppik & Nagel (2019): decoding wind direction from two antennae

[Published article](https://doi.org/10.1016/j.neuron.2019.03.012) · [PMC author-manuscript HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

This is the peripheral half of the wind story. It establishes (1) that walking flies need both antennae for full odor-evoked upwind orientation, (2) that a single antenna's displacement is a hooked, ambiguous function of wind azimuth, (3) that the difference between antennae is approximately linear in azimuth, and (4) that a newly identified class of wedge projection neurons (WPNs, 70B12-GAL4, two per hemisphere) integrates both antennae to produce that linear code. It is a sensory-encoding paper; it identifies no compass, goal or memory variable.

For synthesis, its main value is as a constraint on what the wind signal entering the central brain looks like: a roughly linear, ipsilateral-excited/contralateral-inhibited representation of azimuth, computed at the wedge, before any of the central-complex circuits in Okubo (R1→E-PG) or Currier/Ishida (LNO→PFN). WPNs themselves project to PLP, SCL and ATL, not to the central complex, so the route from WPN-like neurons to R1 or LNO cells is not established here.

## Figure 1: behavior requires both antennae

Freely walking norpA (blind) flies in a miniature wind tunnel with 10 s apple-cider-vinegar pulses. Gluing both antennae abolishes odor-evoked upwind velocity but spares odor-offset local search (increased angular velocity), so the flies still detect odor. Gluing one antenna roughly halves upwind velocity. Downwind aggregation in the absence of odor is lost only when both antennae are glued. The manipulation removes the arista and glues the joint, which blocks mechanosensation; olfactory sensilla on the third segment are largely unobscured.

## Figures 2–3: single antennae are ambiguous; APNs are ipsilateral

Five wind directions (−90° to +90°) at 60 cm/s. Each arista's steady-state deflection follows a hook centered around 22° contralateral to that antenna (normal to the arista's resting angle of ~68° from midline), so each antenna alone is ambiguous. The right-minus-left difference is nearly linear across the tested range and gives better resolution in front of the fly.

APN2 (24C06-GAL4, ~6 neurons/hemisphere) is nonspiking, tonically inhibited by all wind except ipsilateral, with a hooked tuning curve. APN3 (70G01-GAL4, ~11 neurons/hemisphere) fires small spikes at ~28.6 Hz and is inhibited by all wind except contralateral. Removing the ipsilateral antenna abolishes both responses; removing the contralateral antenna has no significant effect. So both second-order populations encode displacement of one antenna only.

## Figures 4–5: WPNs integrate both antennae; not via their own contralateral arm

An electrophysiological screen of 26 candidate classes found 70B12's two WPNs to be tonically and directionally wind-responsive. WPNs (baseline ~8.4 Hz small spikes) are excited by ipsilateral wind, inhibited by contralateral wind, with a nearly linear steady-state tuning and better front-angle discriminability (d′) than APNs. Stabilizing either antenna reduces the dynamic range and frontal discriminability; blocking both abolishes the response.

Dual whole-cell recordings of contralateral WPN pairs (three pairs) show no synaptic coupling. Two-photon laser lesioning of WPN axons crossing the midline does not change wind tuning relative to control lesions. So the contralateral information arrives through other neurons at the wedge, not through WPN–WPN exchange.

## Figures 6–7: multiple upstream sources

Methyllycaconitine abolishes steady-state WPN wind responses, so they require cholinergic transmission. Tetanus-toxin silencing of APN2, APN3 or B1 each reduces the onset response; silencing APN2 and APN3 together, or B1 and APN2 together, still leaves residual directional responses, and the double B1+APN2 deficit is milder than either single, which the authors take as evidence for recurrent or compensatory pathways. Chrimson activation of APN2 depolarizes WPNs transiently then hyperpolarizes; B1 activation transiently hyperpolarizes; APN3 activation has no effect. trans-Tango from JO-CE, APN2 and B1 labels WPN-like processes; from APN3 it does not. The paper's summary circuit (Figure 8) is explicitly a hypothesis with unidentified additional inputs.

## Caveats for synthesis

- The linear code is demonstrated only across ±90°; nothing is said about rear wind, and the ipsilateral/contralateral sign convention for the two WPNs means a population readout is needed for full azimuth.
- Physiology is from immobile, tethered flies with legs removed; the behavioral experiment is freely walking, blind flies. Active antennal movements during walking are an acknowledged unknown.
- Membrane potentials are not junction-potential corrected (−13 mV estimate).
- Genotype tables in the author manuscript contain typographical irregularities (e.g. "R45B07" versus "R45D07" for B1) that should be resolved against the published version before replication.
- WPN output targets (PLP/SCL/ATL) are not central-complex regions; the paper does not connect WPNs to R1 or to LNO neurons.

## Remaining questions and neighboring papers

1. Which neurons carry wind azimuth from the wedge/PLP into the LAL to reach R1 (Okubo 2020 identifies WL-L as one direct input from WED to LAL) and LNOa/LCNOp (Currier 2020, May 2025)?
2. Does the roughly linear WPN code, or the sinusoidal displacement curves, set the ±45° basis-vector tuning seen in PFNs? That is a question for connectome tracing from JO/APN/WPN-like classes toward LAL–NO cells.
3. How does antennal mechanics interact with self-generated airflow in flight (May 2025 addresses the flight case with an observability argument)?

## Implications for later connectome work

WPN-like classes should be identifiable by their WED→PLP→SCL/ATL tract; B1 (APN1), APN2, APN3 and AMMC-A1/Bb candidates can be traced to check the paper's predicted convergence and the hypothesized additional inputs.
