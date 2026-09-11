# Turner-Evans et al. (2020): EM reconstruction, RNA-seq and perturbation of the compass ring attractor

[Published article](https://doi.org/10.1016/j.neuron.2020.08.006) · [PMC author-manuscript HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

The structural audit of the heading network. Partial FAFB reconstruction (validated against the hemibrain) of E-PG, P-EN1, P-EN2, P-EG, Δ7 and R4d ring neurons in selected EB wedges/PB glomeruli, plus RNA-seq/FISH for transmitters and receptors, plus shibire/Kir perturbations with E-PG imaging. Results that matter downstream:

- **Transmitters:** E-PG, P-EN1, P-EN2, P-EG cholinergic; Δ7 glutamatergic (FISH-confirmed); R4d GABAergic. E-PGs express GluClα (candidate for Δ7 inhibition), nicotinic receptors, mAChR-B (possible inhibitory autoreceptor) and many voltage-gated channel genes.
- **E-PG requirement:** shibire in E-PGs (SS00096) abolishes the localized bump; the whole EB flashes with turns. PVA strength drops from ~0.3 to ~0.1 (Figure 3F–G). E-PGs are the only columnar type with substantial PB output (872 ± 80 T-bars/neuron), and E-PGs within a wedge synapse onto each other.
- **Δ7:** synapse onto E-PGs and P-ENs only in their two output glomeruli (separated by seven), receive broad E-PG input elsewhere, and synapse onto each other. Their bump is offset ~180° (3.6 ± 0.25 glomeruli) from the E-PG bump. Shibire in Δ7 (55G08) weakens the bump and makes it track heading erratically (slope distributions broaden in dark and with a stripe) without producing multiple bumps or widening; so Δ7 is a stabilizer, not the sole source of inhibition.
- **P-EN1:** E-PG→P-EN1 in the PB within a glomerulus; P-EN1→E-PG in the EB shifted to the neighboring wedge, with total P-EN1 synapses per E-PG roughly constant whether one or two P-EN1s innervate it. Unexpected E-PG→P-EN1 synapses within the EB ("hyper-local" loops). P-EN1s from one PB side interconnect in the NO.
- **Ring neurons:** R4d synapse onto E-PGs (not P-EN1s) with no obvious trough in synapse counts across the traced sector; R4d neurons heavily synapse onto each other and express GABA receptors (Rdl). Population R4d activity falls when a stripe appears, consistent with mutual inhibition. Shibire in TuBu neurons (AOTU→bulb) leaves dark tracking intact but abolishes closed-loop stripe tethering.
- **P-EG/P-EN2 loop:** P-EG receives strong E-PG input in the PB but does not synapse back onto E-PGs in the EB; it synapses onto P-EN2, which synapses onto E-PGs. P-EG and P-EN2 bumps overlap in the EB. Kir in P-EN2 (Gal80ts-gated) abolishes the dark bump at all rotational speeds while a stripe rescues it. In the PB, P-EN2 receives strong Δ7 input and its PB activity is anti-correlated with E-PG (Green 2017), a discrepancy the authors attribute to electrical compartmentalization (NEURON model in Figure S11).
- **Behavior:** when the network is disrupted (E-PG, TuBu or Δ7 shibire at restrictive temperature), flies lose individual heading preferences and all fixate the stripe frontally (Figure S12), consistent with Giraldo 2018 and Green 2019.

Figure 8B extrapolates the traced counts into a full weight matrix and compares it with the 2017 rate model; the two are qualitatively similar but the biology has redundant inhibition (Δ7 + several ring classes) and redundant local excitation (E-PG self, P-EN1, P-EG→P-EN2).

## Caveats for synthesis

- Partial tracing (~60% of inputs identified in PB/EB, ~40% in NO); the authors defer to the hemibrain for completeness. Synapse counts are not weights.
- Receptor RNA-seq for Δ7 was inconclusive; P-EN1 vs P-EN2 glutamate receptor differences were not resolved, so the sign of Δ7→P-EN1 (inhibitory) versus Δ7→P-EN2 (proposed excitatory) is inferred from activity, not molecules.
- The absence of a ring→E-PG trough in synapse counts leaves visual tethering to synaptic strength, which is what the Fisher/Kim/Plitt plasticity papers address.
- Shibire experiments use 30 °C with heated saline; temperature effects on behavior are controlled by empty-Gal4 flies.

## Remaining questions

1. Full-population synapse-count structure across all 16 wedges (hemibrain; Hulse 2021).
2. Functional sign of Δ7→P-EN2 and the role of P-EN2's PB "shoulder" bump.
3. How ring–ring inhibition shapes cue competition (Basnak 2025; Mitchell 2023's note on within-class inhibition).
