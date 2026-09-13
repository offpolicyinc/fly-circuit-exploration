# Maimon & Abbott (2026): functional logic of a cognitive brain system for navigation

[Review (Annu. Rev. Neurosci. 49:411–434, open access)](https://doi.org/10.1146/annurev-neuro-112723-062711) · [Captured full text with appendix and references](annurev-fulltext.md) · [Author PDF](https://maimonlab.rockefeller.edu/wp-content/uploads/2026/07/Maimon-and-Abbott-Functional-Logic-of-a-Cognitive-Brain-System-for-Navigation.pdf) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

The organising synthesis for this repository. The review walks the central complex through Marr's three levels and argues that its logic is vector arithmetic on sinusoidal population codes:

- **Compass (computational level):** a heading estimate maintained by a ring attractor (EPG/PEN/Δ7), updated by rotational velocity and anchored to cues by plastic inhibitory inputs (Kim 2019, Fisher 2019/2022, Plitt 2025). Bump amplitude is discussed as a possible certainty variable (Kutschireiter 2023).
- **Eight-axis coordinate system:** Δ7 neurons impose a sinusoidal profile across the 8+8 PB glomeruli, so any bump can be read as a 2D vector (phase = angle, amplitude = length). Anatomical phase shifts (±45° PFN projections into the FB; ±135° for PFNv-type classes; 180° for hΔ internal projections) implement rotations, nodulus inputs implement scaling, and convergence in FB columns implements addition. The appendix shows that symmetric inputs passed through an approximately quadratic nonlinearity cancel unwanted cross terms, which is why sinusoidal codes survive summation; the argument is a robustness result, not a licence for arbitrary nonlinearities.
- **Body-to-world velocity:** PFNd/PFNv vectors summed in hΔB give travel direction (Lu 2022; Lyu 2022); PFNa and related classes handle airflow (Currier 2020; Ishida 2026's inversion is cited as extending the representable set).
- **Goal-to-steering:** FC2 holds a goal vector; PFL3 neurons compare it with the heading vector (via ±phase-shifted copies) so that the left-minus-right output approximates a cross product, i.e., a signed turning command proportional to sin(goal − heading) (Westeinde 2024; Mussells Pires 2024). PFL2 output relates to the magnitude of error and forward drive.
- **Memory frontier:** Figure 5 proposes, as hypothesis only, that columnar populations could store vectors (a food location, a home vector) with tangential neurons gating which stored vector reaches FC2. The only cAMP data in the figure (panel d, unpublished, Thornquist) are a rotating cAMP bump in ring-neuron axons in the *compass*, used to argue that cAMP gates visual learning there; the extension to fan-shaped-body vector memory is stated as "likely", not shown. Panel e (PFNa calcium spikes) is a schematic. Direct cAMP evidence for a stored fan-shaped-body vector is Gorko et al. 2025 (Kim lab), not this review. The authors are explicit that fly evidence for vector memory is thin compared to ants and bees; Kim 2017, Behbahani 2021, Titova 2023 and D'Atri 2025 are the behavioral anchors, Chen 2024's scent-marking result the caution.

## Priority reference trails from the review

- Dopamine/octopamine-dependent compass learning (Fisher 2022; Plitt 2025).
- Cue reliability and multi-cue integration (Kutschireiter 2023; Mitchell 2023; Basnak 2025).
- Recurrent goal storage and state dependence (Dan 2024; Flores-Valle 2025).
- Food-triggered local search and odometry (Kim 2017; Corfas 2019; Behbahani 2021; D'Atri 2025).
- Descending steering (Rayshubskiy; Feng 2024).
- Distinction between demonstrated fly computations and ant/bee vector-memory models.

## Caveats for synthesis

- The review's memory architecture is a proposal; treat Figure 5 as hypotheses.
- Instantaneous vector computations are well supported; how vectors are integrated over time (position) is not shown in flies.
- Figures were read via captions and the captured text; the figure images themselves were not inspected.
