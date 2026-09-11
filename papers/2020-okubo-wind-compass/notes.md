# Okubo, Patella, D'Alessandro & Wilson (2020): wind direction as a compass cue for E-PG neurons

[Published article](https://doi.org/10.1016/j.neuron.2020.06.022) · [PMC author-manuscript HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

This paper shows that a steady wind can set and hold the E-PG heading bump, and traces a specific mechanosensory pathway that carries wind-direction information into the ellipsoid body. It therefore supplies a second sensory anchor for the compass, alongside vision. The bump is anchored to wind the same way it is anchored to a visual cue: with an arbitrary, individual-specific offset that can occasionally jump. That is evidence that wind is treated as a compass reference, not as a directly retinotopic or somatotopic reflex input.

What it does **not** establish: any navigation policy that uses the wind-anchored compass, any interaction between wind and travel-direction vectors in the fan-shaped body (the distinction from PFN airflow inputs is important, see Currier 2020 and Ishida 2026), or any memory of wind direction after the wind stops. Those belong to Mussells Pires (wind-memory task), Matheson/Kathman (odor-gated upwind persistence) and Ishida/May (PFN airflow vectors).

## Experimental preparation and its limits

- Two-photon imaging of E-PG axons in the protocerebral bridge (not dendrites in the EB, because Kir2.1-EGFP in ring neurons contaminated EB signals). GCaMP6f; 12 Hz volumetric.
- Most experiments were done in the dark with the fly's legs suspended in air, deliberately removing visual cues and walking-related self-motion signals. Wind effects were less consistent in walking flies (Figures S1H–I); the authors attribute this to competition between wind and angular-velocity inputs.
- Wind was delivered from three fixed tubes (−60°, 0°, +60°) at 0.12–0.18 m/s, or from a motorized rotating tube at 21 directions between −150° and +150° at 0.56 m/s. The stimulus set never covers directly behind the fly, which matters for the circular-linear fit.
- Recordings from R1/R3a and WL-L neurons were whole-cell patch, with forelegs removed to prevent antennal grooming.

## Figure 1: wind moves and stabilizes the E-PG bump

In eight flies, wind onset reduced bump mobility (in six of eight; one showed the opposite). Switching from left to right wind produced a consistent phase change of roughly +120°, matching the 120° separation between the tubes, although with substantial fly-to-fly variability in the traces (Figure 1F). The mean bump position under left wind was uniformly distributed across flies (Rayleigh test p = 0.61): the offset between wind and bump is individual-specific, as it is for visual cues.

With 21 wind directions, 13 of 17 flies fit the circular-linear model φ = aθ + φ0 (mod 360°) with slope close to 1 (Figure 1G–J). Four flies had slopes near zero or negative. The authors note that wind direction is treated as a linear variable in this fit because the delivered range does not wrap. Both the goodness-of-fit and slope are per-fly summary statistics; the underlying trial data (Figure 1G) show visible scatter and occasional off-line points, so "one-to-one mapping" should be read as an average tendency.

## Figure 2: R1 (and to a lesser extent R3a) neurons carry the wind signal

R1 neurons have dendrites in the lateral LAL and axons in the posterior EB; R3a in the dorsal LAL and anterior EB (MCFO and polarity markers, Figure 2A–E). Kir2.1 silencing of R1 (R31A12-Gal4), or of R1+R3a together with the new split-Gal4 LE001, abolished wind-induced bump stabilization and reduced the fraction of flies showing a bump jump. R3a-only silencing and silencing bulb-innervating R neurons (R20A02) had no significant effect. There is a residual effect of wind in the silenced flies; the authors attribute it to incomplete silencing or coverage, or to other cell types.

Note the control used: bump mobility *before* wind is unchanged across genotypes, so the manipulation is specific to the wind effect. The genotypes are LexA-driven GCaMP6f in E-PG with Gal4/Kir in R neurons.

## Figures 3–6: bilateral antennal integration, de-biasing and a weight model

- Whole-cell recordings show R1 and R3a neurons are bidirectionally tuned to wind direction: contralateral wind excites, ipsilateral wind inhibits; headwind can do either (Figure 3). Baseline rates: 4.5 ± 1.7 Hz (R1, n = 9), 5.2 ± 2.7 Hz (R3a, n = 12). Off-responses of opposite sign follow stimulus offset, consistent with adaptation.
- Antennal displacements measured with LEAP pose tracking (Figure 4) are strongly nonlinear in wind direction: most sensitive to lateral directions, flattest near 0°. Any single-antenna displacement is ambiguous (two directions per displacement at a given speed), and speed and direction are confounded; bilateral integration resolves this.
- Piezo displacement of each antenna separately (Figure 5) shows every R1/R3a neuron responds to both antennae with opposite signs ("ipsi-toward, contra-away" is the best stimulus), with cell-to-cell variation in the relative weights. Bilateral responses are well predicted by a linear sum of unilateral responses. Reconstructed wind tuning curves are roughly speed-invariant.
- Volumetric imaging of R1 somata (Figure 6) confirms functional diversity within one brain; each tuning curve is captured by f(θ) = wᵢ dᵢ(θ) − w_c d_c(θ), with nonnegative weights on the measured ipsi/contra displacement curves. E-PG tuning curves lack the sharp transitions near ±60° that R1 curves inherit from antennal mechanics.
- A perceptron with nonpositive R1→E-PG weights (each of 21 model E-PGs is a binary unit trained to respond to one target direction) reaches similar accuracy across all directions. This is an existence proof that the R1 ensemble carries enough information for uniform sensitivity, not evidence about the actual weight pattern.

## Figures 7–8: WL-L neurons as one input from the wedge to R1

One WL-L neuron per hemisphere (R26B07 labels one, in contrast to the two reported by Franconville 2018), GABAergic, dendrites in ipsilateral WED/LAL, axon in contralateral LAL. CsChrimson activation inhibits R1 neurons; this persists in TTX and is blocked by 5 µM picrotoxin, so the connection is likely monosynaptic GABA-A. WL-L neurons are also dye-coupled to ipsilateral R1 neurons, and high-intensity stimulation could evoke mixed excitation and inhibition, suggesting gap junctions.

WL-L neurons have high baseline rates (31 ± 12.6 Hz), are excited by contralateral wind and inhibited by ipsilateral wind, and are driven almost entirely by the contralateral antenna (antenna removal experiments). GtACR1 silencing of WL-L depolarizes R1 (tonic inhibition) and specifically attenuates R1 responses to ipsilateral wind, leaving contralateral/headwind responses unchanged. So WL-L is a real but partial input. The hemibrain (v1.0.1 at the time) contains a WL-L-like axon that is often the largest LAL input to individual R1 neurons and also targets some R3a neurons, but every R1 has other LAL inputs.

## Mathematics worth retaining

- Bump–wind relation: φ = [aθ + φ0] mod 360°, fitted by minimizing mean circular distance d(φ1,φ2) = 2[1 − cos(φ1 − φ2)] with slopes constrained to [−2, 2]; goodness-of-fit is 1 − (residual sum)/(total sum) using circular distances, assessed against trial-shuffled nulls.
- R1 tuning: f(θ) = wᵢ dᵢ(θ) − w_c d_c(θ) with wᵢ, w_c ≥ 0 (Equation 2).
- Classifier: binary E-PG output y = 1 if w·x > γ; perceptron update w ← w + ε(y_target − y) x/‖x‖ with weights clipped to ≤ 0.

## Caveats for synthesis

- Legs in air, darkness, and a single windspeed for most imaging: the "compass anchor" result is a permissive-condition demonstration. How wind competes with visual cues and with walking-generated angular-velocity input is explicitly deferred.
- Wind direction never covered the rear; the linear fit therefore says nothing about wraparound behavior.
- The wind speeds differ between imaging (0.12 or 0.56 m/s) and patch (0.18 m/s). R1 tuning is argued to be speed-invariant, but the E-PG mapping was only checked at one speed per experiment.
- "R1" nomenclature follows Omoto et al. (2018); older papers used R1 for other types. Table S1 is a lookup table (supplement not obtained).
- The paper proposes but does not test plasticity at mechanosensory R→E-PG synapses. Later work on ER→EPG plasticity (Fisher 2019/2022, Plitt 2025) is visual; Plitt notes ER1 neurons also receive EL octopaminergic input, so a shared mechanism is plausible but unproven.

## Remaining questions and neighboring papers

1. How does the compass weigh wind against vision and self-motion? Basnak 2025 (multimodal integration) and Kutschireiter 2023 (Bayesian ring attractor) are the direct follow-ups.
2. Is the wind→E-PG map learned by the same octopamine/dopamine mechanism as the visual map? Plitt 2025 and Fisher 2022.
3. How does the compass wind anchor relate to the PFN airflow basis vectors in the fan-shaped body? Currier 2020, Ishida 2026 and May 2025 describe an independent egocentric airflow channel via LNO neurons, not via R1.
4. The upstream source of R1's non-WL-L inputs (AMMC/WED cell types, Suver 2019's APN2/APN3/WPN) is anatomically suggested but not physiologically closed.

## Implications for later connectome work

R1/R3a→EPG synapse counts should be checked for any trough structure and compared with visual ER classes. WL-L→R1 and WL-L→R3a synapses, plus other LAL inputs to R1, can be enumerated in the MaleCNS/hemibrain datasets. The paper's own statement that WL-L is "not the only pathway" is a target for input-fraction analysis.
