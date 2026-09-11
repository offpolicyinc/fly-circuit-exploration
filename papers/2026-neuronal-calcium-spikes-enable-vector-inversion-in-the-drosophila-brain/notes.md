# Ishida, Sethi, Mohren, Haraguchi, Abbott & Maimon (2026): T-type calcium spikes invert PFNa vectors

[Published article](https://doi.org/10.1016/j.cell.2025.11.040) · [PMC HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

A cellular mechanism for negating a vector in the fan-shaped body. PFNa neurons carry a heading-aligned bump in the protocerebral bridge whose amplitude is set by airflow direction (nodulus input). Air from the front depolarises PFNa cells and lengthens the two EPG-phase-aligned vectors (left and right populations, rotated ±45° by their FB projections). Air from the rear hyperpolarises PFNa cells; when hyperpolarised, PFNa neurons switch from sodium spiking to T-type (Ca-α1T) calcium spikes, and the population bump realigns ~180° relative to the EPG phase. The same population therefore encodes +v or −v depending on membrane potential, so rear airflow is represented by vectors at ±135°, giving the four-direction basis needed to represent airflow directions with negative projections onto the ±45° axes.

Evidence chain: whole-cell recordings show hyperpolarisation-elicited calcium spikes in PFNa that are absent in Ca-α1T null flies; two-photon imaging shows the PFNa bump phase inverts relative to EPG during rear air puffs, and post-inhibitory rebound at airflow offset; FC3 neurons (postsynaptic to PFNa) sum the two PFNa outputs. Optogenetic depolarisation of PFNa (CsChrimson) aligns the FC3 phase with EPG; optogenetic hyperpolarisation (GtACR1) makes the FC3 bump antiphase to EPG, and this antiphase effect disappears in Ca-α1T null flies. During natural air puffs the calcium-spike vectors drive FC3 more weakly than in the optogenetic case (data-driven fits, Figure S6), which the Discussion attributes to spike timing and release properties.

The quantitative model (Figure 7, Methods, Figure S7) treats the left and right PFNa phasors as invertible vectors that form an orthogonal basis; summing them in FC3 yields the allocentric airflow direction across the full circle.

## Why it matters

- Adds sign inversion to the FB vector algebra summarised by Maimon & Abbott 2026 (phase shifts by anatomy, amplitude scaling by NO inputs, summation in FB). Vector subtraction, needed for goal-minus-position computations, requires this operation somewhere.
- Shows that FB population vectors depend on spike type and membrane potential, not just firing rate. Connectome weights alone would miss the inversion.
- Relates to May 2025 (PFNd/PFNp_c airflow and airspeed coding) and Currier 2020 (PFNa and airflow orientation): the PFNa airflow representation is now known to span all directions.

## Caveats for synthesis

- Function is demonstrated at the level of representation (FC3 phase), not behavior; no navigation deficit specific to inversion is reported.
- The calcium-spike-driven output is weaker under natural airflow than under optogenetic hyperpolarisation, so how much the inverted vector influences downstream steering in normal behavior is uncertain.
- Supplementary figures S1–S7 were only read via in-text citations and captions.

## Remaining questions

1. Do PFNd/PFNv or other PFN classes express Ca-α1T and invert under their own inhibitory inputs?
2. What does FC3 project to, and is the allocentric airflow direction used for upwind/downwind goal setting (Okubo 2020, Currier 2020)?
3. Whether rebound calcium spikes at airflow offset create transient spurious vectors that behavior must ignore.
