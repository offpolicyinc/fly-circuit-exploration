# Fisher, Marquis, D'Alessandro & Wilson (2022): ExR2 dopamine as a when-to-learn signal for the compass

[Published article](https://doi.org/10.1038/s41586-022-05485-4) · [PMC author-manuscript HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

Adds a neuromodulatory gate to the ER→EPG plasticity story. The four ExR2 dopamine neurons (PPM3-EB) are active in proportion to rotational speed in darkness (near-linear, Figure 1c–d; forward speed adds little), respond to widefield rotational optic flow even in stationary flies, and are lateralized (each side follows ipsilateral rotation, so the sum tracks speed). Chemogenetic (P2X2/ATP) or optogenetic (Chrimson) ExR2 activation paired with a rotating visual cue persistently sharpens single-EPG visual tuning (lower cycle-to-cycle jitter; 6 of 9 tuned cells shift their preferred cue position) and increases EPG-ensemble mutual information between bump and cue for > 10 min, without rotating the overall bump–cue offset. Activation in darkness does not. Kir2.1 in ExR2 lowers the cue's influence after closed-loop training and abolishes the correlation between bump amplitude and rotational speed.

The model (a modified Kim 2019 network) shows that scaling the Hebbian learning rate by rotational speed (η = |0.5v|) yields a more regular ER→EPG weight pattern than a fixed rate of equal total learning, and protects stored weights against synaptic noise. The functional argument: straight-line goal pursuit stabilizes the retinal image, so continuous learning would over-learn one view; dopamine compresses learning into orienting movements.

## Details worth keeping

- Extended Data 1: ER→EPG synapses lie within ~3 µm of ExR2 release sites, comparable to KC→MBON distances from MB dopamine release.
- Bath dopamine (200 µM) partly mimics ExR2 activation.
- Preferred cue positions cluster near ±90° and the bias increases after dopamine; the authors attribute this to lateralized ER receptive fields.
- ExR2 activation transiently increases bump amplitude; the tuning-consistency change outlasts it.
- Rotational speed shifts of ~300 ms maximize correlations; ExR2 imaging used R75B10-LexA, manipulations used R38A11-LexA (P2X2/Chrimson) and R75B10-Gal4 (Kir).

## Caveats for synthesis

- Plitt 2025 finds GRAB-dopamine release in the EB is global and turn-locked (consistent with this paper) but that the head-direction-specific coincidence signal is octopamine from EL neurons; ExR2 dopamine and EL octopamine are complementary, not competing, mechanisms.
- The learning-rate model is a demonstration of benefit, not a measurement of the actual rule; Plitt's data favor presynaptically gated potentiation.
- The Kir experiment is chronic; developmental effects are possible. The mutual-information test-period comparison is significant but modest (Figure 4c).

## Remaining questions

1. Which dopamine receptors on ER versus EPG neurons mediate the effect, and does dopamine potentiate or depress?
2. How ExR2 activity depends on flight, wind or other self-motion contexts.
3. Relationship to Dan 2024's proposed motor-state neuromodulation of compass weights.
