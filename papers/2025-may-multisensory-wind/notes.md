# May et al. (2025 preprint, Nagel lab): multisensory PFN self-motion codes suffice to infer wind direction in flight

[bioRxiv 10.1101/2025.05.09.653128](https://doi.org/10.1101/2025.05.09.653128) · [Captured full text](biorxiv-fulltext-v1.md) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

Extends the PFN velocity story from walking to flight and to an inference problem: wind direction cannot be sensed directly by a flying animal because antennal deflection confounds self-motion and external force. Imaging PFN classes in tethered flight with airflow and optic flow stimuli, the authors find:

- **PFNd** integrates airflow direction (fast, transient response) and optic flow (slower, sustained) with distinct dynamics, so its output is a temporally filtered sum of the two modalities rather than a single velocity variable.
- **PFNp_c** encodes airspeed (magnitude of airflow), a signal missing from the PFNd/PFNv description in walking flies.
- PFNa (Currier 2020; Ishida 2026) covers airflow direction with its own tuning, so wind information is spread across at least three PFN types.

They build and validate models of the multisensory dynamics for each PFN type, simulate PFN responses during rapid flight maneuvers (saccades), and apply nonlinear observability analysis: because a saccade changes body-relative airflow and optic flow differently depending on the external wind, the time series of PFN activity during active maneuvers contains enough information to decode the wind direction in free flight. Active sensing plus multisensory encoding therefore lets a compact system infer an unobservable external variable.

## Why it matters for the circuit program

- Gives a computational reason for saccadic flight (van Breugel 2014, Dan 2024): maneuvers make wind observable.
- Connects Currier & Nagel 2018 (visual cue dominance over wind in flight) and Okubo 2020 (wind anchoring of the compass) to specific PFN dynamics.
- Warns that the "PFNd = forward velocity" summary from walking (Lu 2022) is incomplete in flight.

## Caveats for synthesis

- Preprint; figures viewed in browser but not saved; supplementary material not obtained.
- The decoding claim is theoretical (observability), not a demonstration that downstream neurons perform the inference.
- Tethered flight with open-loop stimuli; the simulated free-flight maneuvers rely on the fitted models.

## Remaining questions

1. Where the inferred wind direction is represented (hΔ or FC populations? FC3 per Ishida 2026?) and whether it anchors the compass (Okubo 2020).
2. How PFNp_c airspeed and PFNd direction combine, and whether Ca-α1T-type inversion applies to these classes.
