# Plitt et al. (2025 preprint, Jayaraman lab): octopamine relays postsynaptic EPG activity to presynaptic visual terminals

[bioRxiv 10.64898/2025.12.11.693783](https://doi.org/10.64898/2025.12.11.693783) · [Captured full text](biorxiv-fulltext-v1.md) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

Solves the coincidence-detection problem at the inhibitory ER→EPG synapse. The Hebbian-style rule inferred by Kim 2019 and Fisher 2019 requires each ring-neuron terminal to know the postsynaptic EPG activity, but the synapse is GABAergic and ring terminals have no obvious retrograde signal. Plitt et al. find that EL octopaminergic neurons receive EPG input, carry a head-direction-tuned activity pattern (a bump that follows the EPG bump), and release octopamine onto ER presynaptic terminals in the ellipsoid body, closing a feedback loop that reports postsynaptic activity presynaptically. GRAB sensor imaging shows head-direction-specific octopamine release, while dopamine release (ExR2; Fisher 2022) is global and turn-locked rather than direction-specific.

Causal tests: silencing EL neurons prevents the compass from anchoring to visual cues (the offset between bump and cue no longer stabilises in a new scene), so the pathway is required for plasticity. Pairing structured optogenetic activation of EL neurons with a visual cue drives rapid remapping even when EPG activity itself is suppressed, so EL activity is sufficient and postsynaptic EPG activity is dispensable once the octopamine signal is provided. Octopamine receptor manipulations in ring neurons are consistent with presynaptic action.

## Why it matters for the circuit program

- Establishes a three-neuron plasticity motif (ER → EPG → EL → ER terminals) that could be reused wherever inhibitory inputs must learn a mapping onto an attractor, including FB goal populations.
- Separates the "which synapses" signal (octopamine, direction-specific) from the "when to learn" signal (dopamine, movement-locked; Fisher 2022).
- Explains how ring-neuron inhibition can be sharpened only at the correct heading, supporting Kim 2019's inhibitory Hebbian rule with a defined mechanism.

## Caveats for synthesis

- Preprint (December 2025 bioRxiv, new DOI prefix); figures viewed in browser but not saved; extended data figures only partially captured in text.
- Whether the octopamine effect is potentiation of inhibition or depression at active vs. inactive terminals should be checked in the final version.
- Head-direction tuning of EL neurons depends on EPG input; the source of EL's own bump when EPG is silenced (for the sufficiency experiment) is optogenetic patterning, so natural sufficiency remains inferred.

## Remaining questions

1. Do the same EL neurons signal to other EB inputs (e.g., wind ring neurons, Okubo 2020)?
2. How octopamine and dopamine interact at ring terminals: multiplicative gating or additive?
3. Whether EL activity is state-dependent (flight, rest), which would connect to Flores-Valle 2025.
