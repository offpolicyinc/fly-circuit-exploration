# Mitchell, Shaverdian, Dacke & Webb (2023): a model of cue integration in the insect compass

[Published article (Proc. R. Soc. B)](https://doi.org/10.1098/rspb.2023.0767) · [PMC HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

A computational account of how multiple directional cues (sun, polarised light, wind, landmarks) are combined in the ring→E-PG pathway. Each cue class is represented by a ring-neuron population whose inhibitory weights onto E-PGs have been shaped by plasticity so that a cue at a given azimuth pulls the bump toward a fixed heading. Because every ring population converges on the same E-PG ring and the bump responds to the vector sum of inputs, the model implements weighted vector averaging: cues that agree reinforce, cues that conflict produce a bump at the weighted intermediate direction, and a cue's weight is set by the gain of its ring population rather than by any explicit reliability estimate.

The behavioral data come from dung beetles (Dacke lab), which orient using sun and wind: when cues are rotated in conflict, beetles take an intermediate heading. The model reproduces this. A key empirical point: beetles appear to weight cues by their sensory contrast (brightness, wind strength) rather than by their actual reliability as directional references, which the vector-sum-with-fixed-gains model captures but a true Bayesian optimum would not. The authors compare with Kutschireiter 2023 and note that a Bayesian ring attractor could layer certainty on top, but the data do not require it.

## Circuit points that matter for flies

- Plasticity: an inhibitory-Hebbian rule (Kim 2019; Fisher 2019) lets each ring population map its cue onto the bump independently; conflicting cues after remapping produce a compromise rather than a switch, unless one cue's gain dominates.
- Within-class ring-ring inhibition (Turner-Evans 2020) is proposed to normalise cue populations, which matters for how many cues can be combined without saturating.
- Predicts bump-jump versus bump-slide behavior depending on cue weights and conflict angle, a distinction later tested in Drosophila by Basnak 2025 and in the symmetric-scene case by Dan 2024.

## Caveats for synthesis

- Beetle behavior, fly connectome-inspired architecture; the mapping is by analogy.
- Cue reliability learning (adjusting gains) is not modelled.
- The model treats the E-PG ring as a standard rate attractor; amplitude effects (Kutschireiter) are not included.

## Remaining questions

1. Do flies weight wind versus visual cues by intensity or by reliability (Okubo 2020 and Basnak 2025 provide partial answers)?
2. How is a cue's gain set biologically: ring-neuron response gain, ExR2 dopamine, or EL octopamine?
