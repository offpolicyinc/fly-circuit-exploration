# Feng et al. (2024 preprint, Dickson lab): a hierarchical central steering circuit

[bioRxiv 10.1101/2024.06.27.601106](https://doi.org/10.1101/2024.06.27.601106) · [Captured full text](biorxiv-fulltext-v1.md) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

Defines the motor output layer that the CX goal-steering computation (PFL3→DNa02 etc.) must pass through. Using connectomics, optogenetics, imaging and behavior in walking flies, the authors describe a hierarchy:

- **Top layer:** DNa03 descending neurons and LAL013 (a LAL interneuron), reciprocally connected. Turns are initiated by DNa03 and then reinforced and stabilised by a winner-take-all interaction through LAL013, so a turn commits to one side.
- **Intermediate layer:** DNa11 descending neurons receive input from both DNa03 and LAL013, target leg motor circuits directly and via subordinate DNs; DNa11 activation coordinately changes the stepping direction of all six legs to produce rapid saccadic turns.
- DNa02 (Rayshubskiy 2020; Westeinde 2024) sits in this scheme as another steering DN; DNa03, DNa11 and DNa02 are all needed for corrective turns during menotaxis-like heading maintenance (silencing impairs the fly's ability to correct after displacement from a preferred heading).

The same circuit produces small course corrections and large saccades, and is used both for goal-directed (exploit) and exploratory turns, arguing against fully distributed steering control.

## Why it matters for the circuit program

- Provides the bridge from PFL3/PFL2 outputs (Westeinde 2024; Mussells Pires 2024) to legs; PFL3 targets DNa02 and LAL neurons, so LAL013/DNa03 are candidates for the winner-take-all that converts a graded goal error into discrete saccades (Dan 2024's policy).
- Saccade generation by DNa11 explains how walking flies make rapid turns with stereotyped leg kinematics.

## Caveats for synthesis

- Preprint; figures viewed in browser but not saved; supplementary material not obtained; verify the published version for changes.
- Walking only; flight steering uses different DNs (e.g., DNa/DNp classes in Namiki/Schnell work) and is not covered.
- Anatomical "hierarchy" is inferred from connectivity and activation; natural recruitment order was not directly recorded during behavior for all layers.

## Remaining questions

1. How PFL3 left/right outputs map onto DNa03 vs DNa02, and where the CX goal error becomes a discrete turn.
2. Whether the LAL013 winner-take-all is the locus of the fixation/saccade decision modelled by Dan 2024.
