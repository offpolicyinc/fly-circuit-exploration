# Hulse, Stanoev, Turner-Evans, Seelig & Jayaraman (2023 preprint): GLNO neurons build the compass's rotational-velocity input

[bioRxiv 10.1101/2023.09.25.559373](https://doi.org/10.1101/2023.09.25.559373) · [Captured full text](biorxiv-fulltext-v1.md) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

Identifies the velocity signal that drives angular path integration. The connectome shows that a single pair of GLNO neurons (one per nodulus) is the only lateralised input to PEN neurons in the NO, so the PEN asymmetry that rotates the EPG bump must come through them. GLNO activity encodes rotational velocity with high accuracy, using both optic flow and motor (efference/proprioceptive) information; silencing them impairs angular path integration in darkness.

The integration rule is not a moment-to-moment weighted sum. When visual and motor signals are congruent, GLNO follows the motor signal and adds little from optic flow. When they conflict (e.g., open-loop visual rotation during a turn, or visual motion without turning), reciprocal inhibition between the two GLNO neurons (and between their inputs) selects one signal or the other in a flip-flop manner rather than averaging. Optic flow contributes mainly when the motor signal is absent, such as a stationary fly viewing rotating scenes, which is when the EPG bump is known to follow visual motion.

## Why it matters for the circuit program

- Closes a gap in the ring-attractor model (Turner-Evans 2017; Green 2017): the PEN velocity input is now a defined pair of neurons with measured coding.
- Predicts context-dependent compass updating: motor-dominated during self-generated turns, visual during passive motion; relevant to interpreting Fisher 2022 (ExR2 rotational-speed dopamine) and Kutschireiter 2023 (cue reliability as bump amplitude).
- Winner-take-all via reciprocal inhibition at the velocity stage parallels the LAL013/DNa03 steering circuit's winner-take-all (Feng 2024).

## Caveats for synthesis

- Preprint; figures viewed in browser but not saved; supplementary material not obtained; check for a published version.
- Motor information source (efference copy vs. proprioception) is not resolved.
- Walking preparation; flight velocity inputs to PEN may differ.

## Remaining questions

1. What are GLNO's upstream sources of the motor signal (descending neuron collaterals? leg proprioceptors)?
2. Does GLNO also carry the speed that scales the PEN shift during fast saccades (Dan 2024's bump jumps)?
