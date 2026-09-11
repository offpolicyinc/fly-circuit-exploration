# Haberkern et al. (2019): 2D virtual reality for head-fixed walking flies, virtual sugar and virtual heat

[Published article](https://doi.org/10.1016/j.cub.2019.04.033) · [Full text](cell-fulltext.md) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

A methods-and-behavior paper introducing FlyoVeR, a projector-based 2D VR in which a tethered fly's translation and rotation both move it through a virtual world of cones and cylinders. Three behavioral results matter here:

1. Flies approach and circle visible virtual objects, not invisible impenetrable ones, and their 1D fixation behavior does not predict 2D interaction (bimodal front/back or side fixations correspond to approach/departure and circling).
2. Transient optogenetic activation of Gr64f sugar neurons at a cone triggers local search (higher path curvature, more time near the site) whose return rate to the site is **not** improved by a visible landmark at the site; turning statistics depend on time since stimulation more than on distance. So beaconing is not what drives these returns, and the authors note the tethered/virtual conditions may not deliver reliable self-motion cues, so the search may be a simpler turn-rate modulation.
3. Optogenetic "virtual heat" (HC-Gal4 > ChrimsonR) is aversive in free walking and VR. Flies avoid heat zones better with steep gradients regardless of landmarks; shallow gradients benefit slightly from landmarks. Pairing heat with cylinders but not cones shifts naïve cylinder preference toward cones after 20 min of training (anti-cylinder protocol significant; anti-cone reversed protocol not significant; spatially decoupled control shows no shift). Virtual sugar pairing does not produce shape-selective preference.

This establishes that head-fixed flies can express operant visual learning in a 2D environment where a landmark's retinal image depends on heading, and provides the platform later used for imaging in 2D VR. It does not identify neural substrates.

## Details worth keeping

- Wing-clipped flies; 9.93 mm ball; two DLP projectors; 360 Hz 8-bit greyscale; blue LED source chosen for compatibility with two-photon imaging.
- Cone forest: 10 × 40 mm cones on a triangular grid, fog beyond 70 mm. Cone-and-cylinder forest: 8 × 30 mm cylinders alternating with cones on a 60 mm Cartesian grid.
- Fixation quantified by von Mises fits (unimodal κ > 0.5, or PVA > 0.5) and bimodal two-von-Mises fits; bright-on-dark scenes produce more unimodal fixation than dark-on-bright.
- Local search: 24-h wet-starved females, 200 ms at 1.29 mW/cm² on crossing a 10 mm radius; search bouts analyzed to 55 mm radius; turns defined by |curvature| > 0.1.
- Heat conditioning: constant low baseline (0.35 mW/cm²), hot zones to 0.81 mW/cm², cool zones to 0; 25 mm zone radius; statistics by one-sample t-tests on pre–post visit ratios (anti-cylinder n = 22, p = 0.0031).

## Caveats for synthesis

- Operant learning here is weak and protocol-asymmetric; the authors themselves list several possible learned contents (avoid punished shape, approach safe shape, snapshot vs invariant recognition).
- Local search in VR lacks the evidence for directed returns seen in free walking; treat this as a caution about tethered path-integration assays, not as a refutation.
- Genotypic and temperature effects on fixation are deferred to a website (flyfizz.org), not in the paper.

## Remaining questions

1. Whether 2D VR search engages the same integrator as free-walking search (Kim 2017, Behbahani 2021) and whether the missing landmark effect reflects strategy or preparation.
2. What is stored during shape conditioning, and whether CX ring-neuron or MB circuits mediate it (Ofstad 2011 for free-walking place learning; Dan 2024 for 1D heading learning).
3. Flores-Valle 2025 uses a mechanical 2D arena and heat-based place learning with imaging, an alternative platform for the same questions.
