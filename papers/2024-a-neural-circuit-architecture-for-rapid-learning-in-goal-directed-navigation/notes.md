# Dan, Hulse, Kappagantula, Jayaraman & Hermundstad (2024): a circuit architecture for rapid goal learning in flight

[Published article (Neuron 2024)](https://doi.org/10.1016/j.neuron.2024.04.036) · [bioRxiv v1 full text (read)](biorxiv-fulltext-v1.md) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

A behavior-plus-model paper on how tethered flying flies learn to steer toward a safe heading within minutes, and how that learning could be implemented on top of the compass and the PFL steering circuit. Flies in closed-loop VR receive laser heat unless they face a "safe" zone tied to the visual scene. They learn quickly, and the behavior is a policy over discrete actions: fixations (holding a heading) and saccades (rapid turns), with the probability of fixating and the direction and size of saccades depending on the heading relative to the safe zone. Importantly, learning transfers when the scene is unchanged but the safe zone is moved, and the model explains behavior under a two-fold symmetric scene in which the EPG bump jumps by 180° when the fly's heading crosses the ambiguity: the behavior tracks the internal compass, not the retinal scene, and goal-directed turns follow the bump jump.

The circuit model: a prestructured goal-policy network in which the EPG bump feeds PFL2/PFL3-type populations with fixed anatomical phase shifts, and plasticity sets a set of "goal weights" (one per compass direction) that scale how strongly each heading drives turns and fixations. Learning is fast because the architecture is fixed and only the goal weights change, driven by a reinforcement signal (heat) gated by the current compass state. The model reproduces the saccade-size dependence on angular distance to the goal, the fixation-probability profile, transfer across scene changes, and the bump-jump behavior; it fails without compass-referenced weights.

## Details worth keeping

- Behavior quantified as a Markov-like policy: P(fixate | heading) and P(saccade direction, magnitude | heading), estimated from wingbeat-amplitude difference.
- Learning within tens of trials; retention across a probe period without heat.
- The model separates "compass weights" (visual→EPG mapping, slow, as in Kim/Fisher) from "goal weights" (EPG→PFL, fast); the paper argues the fast component must be downstream of the compass.
- Motor-state modulation: the authors propose that neuromodulators tied to flight and heat could gate goal-weight plasticity.

## Caveats for synthesis

- Read from the 2021 bioRxiv v1; the 2024 Neuron version has revised figures and additional analyses not captured here (notes should be checked against the published version).
- No imaging of PFL neurons; the circuit is a model constrained by anatomy, not by recordings. Westeinde 2024 and Mussells Pires 2024 later show FC2 and PFL3 goal signals.
- Heat-avoidance is a punishment task; the same architecture is assumed for appetitive goals.

## Remaining questions

1. Where the goal weights live: FC2 (Westeinde 2024), PFL3 inputs, or hΔ populations? What is the reinforcement signal into the FB during flight?
2. How the slow compass plasticity (Plitt 2025, Fisher 2022) and fast goal plasticity interact when the scene changes.
3. Whether the policy parameters (saccade size vs. angular error) are the same as in walking menotaxis (Green 2019, Feng 2024).
