# The fly's compass has a built-in brake that textbook models leave out

**Summary.** The compass ring attractor is moved by the PEN shifter neurons, which every model treats as one-way conveyors: read the heading bump at position x, write it to x±1. The connectome shows each PEN receives about three times more input from the position it writes to than from the position it reads from. Both left and right shifters do this, so the effect has no direction: the neurons a shifter pushes on push back on it, and the shifters anchor the bump where it already is. In a standard ring-attractor model, adding this feedback at the measured strength collapses rotation. Real flies turn normally, so these synapses cannot be acting the way a naive reading of the wiring says.

## The question

A fly keeps track of which way it is facing with a ring of about fifty EPG neurons in a structure called the ellipsoid body. One patch of the ring is active at a time, and the position of that patch is the fly's heading. When the fly turns, the patch has to slide around the ring by the right amount.

The sliding is done by about forty PEN neurons, the shifters. Half push the patch clockwise, half push it anticlockwise. Each shifter reads the EPG activity at one position and writes it back onto the EPGs one position over. When the fly turns left, the left-pushing shifters get stronger, so the patch moves. This is the mechanism in every compass model since 2017, and it depends on the shifters being feed-forward: input from position x, output to position x+1.

## What is known

The read contact (EPG onto PEN) lives in a structure called the protocerebral bridge. The write contact (PEN onto EPG) lives in the ellipsoid body. That anatomical separation is why the models treat read and write as two distinct one-way steps. Turner-Evans et al. (2020) noticed some EPG-to-PEN synapses inside the ellipsoid body and called them unexpected. Hulse et al. (2021) wrote that EPG and PEN neurons are so densely interconnected within the ellipsoid body that their subnetwork forms a ring, but did not compare this with the bridge route or model it.

## What the wiring shows

Counting every EPG-to-PEN synapse in the hemibrain and binning it by location gives the following.

| EPG → PEN synapses (hemibrain) | at read position (bridge) | at write position (ellipsoid body) |
|---|---|---|
| PENa | 1,281 | 3,844 |
| PENb | 1,512 | 3,645 |

The write-position input is three times the read-position input. It comes from exactly the EPGs the shifter writes onto. The same 3:1 ratio appears in MaleCNS, a second brain of the other sex.

So the largest EPG-to-PEN pathway in the brain is not the one in the models. It is a loop: the shifter excites a set of EPGs, and that same set excites the shifter back.

## What the model shows

Take the standard ring-attractor model with a constant turn signal, and add the write-position feedback at increasing strength.

| write-position feedback relative to read input | bump rotation (°/s) |
|---|---|
| 0 (textbook) | 139 |
| 0.5× | 72 |
| 1× | 0 |
| 2.7× (measured) | 0 |

Rotation collapses as the feedback grows. The zero at high feedback is partly an artefact of rate saturation in a minimal model; the defensible claim is that rotation gain falls steeply as the anchor strengthens. Models fitted to the raw connectome, which include these synapses at the measured ratio, do integrate velocity (Duan, Dong & Fiete 2025; Hulse, Aneesh, Romani, Jayaraman & Hermundstad 2026), by assigning each cell-type pair its own gain; that is the first escape route below, found by fitting rather than assumed. The collapse does not depend on how the contact is implemented: as a presynaptic gain on the shifter's terminals that only redistributes a fixed release toward the write position, rotation falls to 25°/s at 1× and 0 at the measured ratio; with divisive normalisation of the shifter population, to 34°/s and 0. The dark bump is stable in every version.

## Why it matters

The loop turns the shifters into anchors. Normal stalling of a ring attractor is two equal and opposite pushes cancelling. This is different: both shifter populations pile excitation onto wherever the bump already is, and the anchor feeds on itself, because a stronger turn signal drives the shifters harder and so drives the anchor harder too. A compass with this loop is very stable in darkness and very sluggish under rotation.

Flies are not sluggish, so one of two things is true, and each is a different compass. A third correction applies to every model here: Δ7's glutamate inhibits EPG but excites PENa and PENb (Eddy et al. 2026), so the "Δ7-like global inhibition" onto the shifters in this model has the wrong sign.

1. The write-position synapses are functionally weak despite their number, whether they drive the cell or modulate its terminals.
2. They are cancelled by inhibition the models leave out (Δ7, ExR4, ExR6).

## What would settle it

- Record a shifter while stimulating EPGs at its read position versus its write position, and compare the response.
- At the EM level, check whether the write-position contacts carry the receptors of a driving synapse or of a terminal modulator.
- Refit a ring-attractor model with the loop included. If rotation gain and dark stability cannot both be matched, the loop must be gated or silent.

## Methods

Synapse counts are from the hemibrain v1.2 traced adjacencies, with each synapse assigned to a brain region, and from MaleCNS v1.0. Read-position synapses are EPG→PEN synapses in the protocerebral bridge; write-position synapses are EPG→PEN synapses in the ellipsoid body, restricted to the EPG wedge the PEN projects to. The simulation is a rate-based ring attractor with eight EPG positions and left and right PEN populations, constant asymmetric drive to one PEN population, and an added EPG→PEN term from the write position whose strength is varied. Analysis: `docs/compass-recurrence.md`; script: `scripts/compass_recurrence.py`, `scripts/hemibrain_compass_comparison.py`; simulations: `simulations/eb_epg_pen_loop.py`, `simulations/eb_epg_pen_loop_variants.py` (somatic drive, presynaptic release gain, divisive normalisation).

References: Turner-Evans et al. 2017, 2020; Green et al. 2017; Hulse et al. 2021; Duan, Dong & Fiete 2025; Hulse et al. 2026; Eddy et al. 2026; Maimon & Abbott 2026.
