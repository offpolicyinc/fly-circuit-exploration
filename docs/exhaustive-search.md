# Exhaustive pass: where the memory is, what each candidate can and cannot do, and what was already known

Date 2026-09-12. This supersedes the single-pass conclusions in [vector-memory-search.md](vector-memory-search.md) where they conflict. Scripts: [synaptic_site_screen.py](../scripts/synaptic_site_screen.py), [tangential_store_screen.py](../scripts/tangential_store_screen.py), [hemibrain_key_edges.py](../scripts/hemibrain_key_edges.py), [recurrence_modes.py](../scripts/recurrence_modes.py). Simulations: [closed_loop_sites.py](../simulations/closed_loop_sites.py), [site_readout_error.py](../simulations/site_readout_error.py), [strategy_discrimination.py](../simulations/strategy_discrimination.py). Tables: `synaptic_site_screen.csv`, `tangential_store_screen.csv`, `hemibrain_key_edges.csv`, `fb_offset_stats.csv`, `site_readout_error.json`, `strategy_discrimination.json`.

## 1. What the behaviour requires (strategy discrimination)

Four memory strategies were run through the published assays with the same agent. Only a vector integrator with reset at food reproduces both Kim 2017's centred search (search centre 0.8 units from food, versus 12.7 for a random walk and 26.8 for direction-only memories, which walk off in a fixed wrong direction) and Titova 2023's displacement result (search centre 0.8 from the fictive site, 4.2 from the real one). A memory of "the direction I was travelling at reward" (Siliciano-style) and a scalar odometer plus last heading both fail these two assays. So the fly needs a running vector sum; the question is where and in what form.

## 2. Activity-based storage: ruled out by recurrence strength (unchanged)

No columnar type has a within-type vector-mode recurrent gain above 0.14 as a fraction of its input; the strongest cross-type loops have gains below 0.01; the 180° column pairs of hΔD/E/G/M exist but carry 30–100 synapses per cell. Replicated qualitatively in the hemibrain (e.g. FR1→FR1 7,577 there vs 8,694 here, still uniform-mode only). Cellular persistence remains invisible.

## 3. Synaptic storage: every candidate site scored the same way

Every columnar→columnar pair with a heading- or travel-tuned presynaptic type was scored on phase concentration, per-cell coverage, dopamine and octopamine convergence, column uniformity of the modulator, and one- or two-hop readout to FC2 or PFL2/3 (`synaptic_site_screen.csv`). The postsynaptic populations that receive travel direction from hΔB and reach the goal or steering layer are hΔJ, hΔH, hΔG, hΔA, hΔI, hΔM and PFR_a; the presynaptic PFN→hΔB synapses themselves are a further site (hΔB is the largest dopamine and OA-VPM3 target of all). Maimon & Abbott's tangential-store motif was screened separately (`tangential_store_screen.csv`): the tangential neurons whose synapses onto a columnar population are uniform across columns, whose target receives a travel bump and reads to goal/steer, and which carry contextual input, converge on the same two targets, hΔA (FB5V_a, FB4P_b, FB4K, FB4Z_a, FB5X…) and hΔJ (FB4X, FB4M, FB4D_a, FB4A_a…). Whichever store is used, hΔA and hΔJ are the hubs.

## 4. The sign problem: the wiring does not invert the stored vector where I said it did

Two published conventions fix the geometry. Hulse 2021 assign each hΔ neuron to the column of its *dendritic* arbor. Lyu 2022 image the hΔB bump with a synaptic-terminal-targeted indicator, so the physiological travel-direction bump T sits on the hΔB *axon*, half a turn from its label. Hulse 2021 also note (their Figure 37Biii) that a presynaptic column contacts hΔ neurons "some with primarily dendritic arbors in the column and some with primarily axonal arbors in the column", which is exactly the two-band structure I measured.

Re-deriving every readout with that anchor (Δ = offset in + offset out − 180, relative to T):

| route | hΔB axon lands on target's | Δ relative to T | what reaches the goal/steering layer |
|---|---|---:|---|
| hΔB → hΔA → PFL3 | axonal arbor (92 %) | +15° | +T, not inverted |
| hΔB → hΔI → PFL3 | axonal arbor (82 %) | +16° | +T |
| hΔB → hΔH → FC2B | axonal arbor (95 %) | +16° | +T |
| hΔB → hΔG → FC2B | axonal arbor (73 %) | +15° | +T |
| hΔB → hΔJ → FC2A/B | mixed (58 % / 42 %) | +20° and +200° | both signs, net weak |
| hΔB → PFR_a → FC2A | single arbor | +20° | +T |
| hΔB → vΔM → vΔK | single arbor | +17° | +T |
| hΔB → hΔK → PFGs | dendrite (99 %) | +196° | −T (inverted) |
| hΔB → hΔC → FC2B | dendrite (67 %) | +192° | −T |
| FC2B goal → hΔM → PFL3 | (FC2 labels are direct) | +178° | −goal (inverted) |

Consequences. (a) The claim in the first pass that hΔJ's anatomy "flips the stored displacement toward home" was wrong: relative to the physiological bump, the dominant hΔ routes relay travel direction *un*-inverted, and hΔJ carries both signs at once (which is also why its stored vector cancels to 14 % of ideal in the readout simulation). (b) A displacement stored at any of hΔA/H/G/I would therefore reach FC2 or PFL3 as the **outbound** direction. Steered directly, the fly would keep going. (c) The wiring supplies exactly two inverters downstream: hΔM, which delivers the FC2 goal to PFL3 at +178°, and the hΔK→PFGs loop. (d) The closed-loop control (`closed_loop_kernel_controls.json`) already showed that a net inversion between stored displacement and the PFL3 goal is necessary for return (0 % without it, 35 % with an ideal 180°). Put together: the minimal wiring-consistent return circuit is **store (+D) → FC2 (+D) → hΔM (−D) → PFL3**, i.e. the anti-goal channel of finding 6 is the return path, and PFL3's direct FC2 input is the "keep going" path.

That last point gives the two channels a job each. A goal that reads "the direction I have been going" drives dispersal and long-term heading maintenance when used directly (Green 2019; Weisman 2025), and drives return when inverted by hΔM. Which one wins would be set by the balance of FC2→PFL3 and hΔM→PFL3, and FB5A (which inhibits FC2, PFL3 and hΔM together; independently proposed as the FC2 normaliser by Nanni & Lee 2026) is placed to set that balance. This is a hypothesis; it is the only one I found that is consistent with all of the measured phases.

## 5. Corrections to earlier findings forced by the anchor

- Finding 3 (PFR). hΔB→PFR_a at 195° means PFR reads hΔB's *axonal* bump, i.e. +T, and PFNd→PFR_a at 21° adds the heading-frame velocity vector. PFR is a weighted **sum** of travel direction and heading, which is what Lyu 2022 observed (PFR phase tracks hΔB with a bias toward frontal/heading). The "mismatch/cancellation" reading in the first pass is withdrawn. PFR is still not an integrator.
- Finding 6 (hΔM). Upgraded from "omitted input" to the candidate return path (section 4).
- Finding 9 (hΔJ store). hΔJ remains the strongest site by synapse count and by reward/dopamine convergence, but its input is bimodal, so it is the weakest vector store of the candidates; hΔH (95 % single-arbor input, OA-VPM3 361, →FC2B and →PFL3) and hΔA (92 %, FB4M 1,098, →PFL3) are the cleaner stores. The dopamine and OA-VPM3 convergence, the walking-driven FB4M, and the necessity of an inversion stand.

## 6. Hemibrain replication of every key edge

All edges that carry the argument replicate in the female hemibrain (`hemibrain_key_edges.csv`): hΔB→hΔJ 3,365; hΔJ→FC2A/B 3,841/3,253; FB1H→hΔJ 1,535; FB4M→hΔB 5,625; OA-VPM3→hΔB/hΔJ/PFR_a/hΔH/PFGs 591/513/615/385/614; PFNv/PFNd/hΔB→FB4M 797/1,002/1,153; FS1A→oviIN 1,589 and FC2B/C→oviIN 435/287; FB3A→PFNd 3,911; PS196→GLNO 531; ExR7→LAL013 294; PFL3→LAL121 1,882; EL→ER4d/ER3p_a/ER4m 7,643/3,835/731; hΔK↔PFGs 7,890/7,453; FB6A→hΔK 3,071. Two specimens, two sexes, same wiring.

## 7. Novelty audit against the literature (web sweep, 2026-09-12)

| finding | already in print | what remains new here |
|---|---|---|
| 1 compass brake | Hulse 2021: "EPG and PEN_a neurons are so densely interconnected within the EB that a network graph of their subnetwork forms a ring"; Turner-Evans 2020 flagged EB E-PG→P-EN synapses as unexpected. | The 3:1 ratio against the bridge route, its placement on the write-back tile, conservation in two specimens, and the simulated rotation brake. |
| 2 steering stage | Rayshubskiy 2025 (eLife): PFL3 → DNa03/LAL010 → DNa02 plus contralateral inhibitors incl. LAL121 and AOTU019, a "see-saw"; Liao, Chang, Liu & Lo 2025 (bioRxiv): full pro-goal push-pull LAL circuit (LAL010/014/018/040/121/126…) and a ventral anti-goal circuit. | Only the MaleCNS input shares (PFL3 is 1.5 % of DNa02) and the absence of any PFL input to Feng's LAL013/DNa11 layer. Downgraded to confirmation. |
| 3 PFR | Lyu 2022: PFR combines hΔB and PFNd; phase biased toward heading. | The recurrence-based argument that PFR cannot integrate; the mismatch reading is withdrawn. |
| 4 MB bridges | Hulse 2021 and Li 2020: MBON09/MBON21/MBON05 converge on FB4R "a significant fraction of its input"; FR1 makes ~500 synapses on MBON30. | FB4R→hΔB as a route into the travel-direction population; the MBON25/34 → FB4G/H → vΔ → hΔA → PFL3 path; the reading of FR1 as a scalar accumulator. Mostly known. |
| 5 goal → oviIN | Weber-Langstaff, Srivastava, Kunin & Gutierrez 2025 (eNeuro): FS1A is the strongest oviIN input, FC2B/FC2C also, forming a recurrent module. | oviIN's return projections into FC2C and the FB5 tangentials, and the navigation-state interpretation. Mostly known. |
| 6 inverted goal (hΔM) | Liao et al. 2025 describe an anti-goal circuit in the LAL; Nanni & Lee 2026 (arXiv) propose FB5A as the FC2 normaliser with an hΔ contribution. | The hΔM route itself (FC2 → hΔM → PFL2/3 at 178°) and its role as the return inverter (section 4). Not found in print. |
| 7 velocity sources | A search-engine summary attributed a PS196 rotational-velocity conjecture to Worden 2025 (arXiv 2512.10525); the passage is not in the paper text, so no prior claim is confirmed. | PS196_b → GLNO/ExR2/ExR4/FB3A fan-out with shares; FB3A as an ascending-fed 12 % input to PFNd. FB3A not found in print. |
| 8 cue-specific octopamine | Plitt 2025 Extended Data: "EL provides the strongest feedback onto ER4d and ER3p neurons"; ring-class cue assignments listed. | Only the explicit prediction and the ER4m/ER6 direct-EPG contrast. Downgraded. |
| 9 synaptic integrator | Maimon & Abbott 2026 (Figure 5) and Hulse 2021 propose synaptic vector memory; Goulard, Heinze & Webb 2023 model dopamine-gated weights at FBt→PFN and FBt→hΔ synapses for goal memory (their path integration itself is activity-based in hΔ). Gorko 2026 (UCSB dissertation, Kim lab) and Gorko et al. 2025 (bioRxiv 10.64898/2025.12.20.695733): PFL1 transforms a stored allocentric goal vector to egocentric coordinates; with three-colour imaging they *rule out* a simple encoding of the stored vector in the calcium activity of PFL1's presynaptic FB neurons, and find FC1 drives a sinusoidal cAMP pattern in FB2B axons, i.e. experimental evidence that a stored FB vector is not held as activity, in a different column system from mine. | The recurrence screen that rules out activity-based storage in every columnar type; OA-VPM3's projections onto hΔB/PFR/hΔJ/hΔH/PFGs; FB4M/FB1H as walking-driven dopamine at those sites; the per-site readout and sign analysis; the inference that hΔM is the required inverter. |

The Gorko dissertation and the Kim-lab preprint were read from their PDFs; the PS196 attribution to Worden could not be verified in the paper text and is treated as unconfirmed.

## 8. What I would now claim, in one paragraph

The fly's home vector is not held in recurrent activity anywhere in the fan-shaped body. The wiring supports a synaptic store at hΔB's synapses onto a small family of hΔ types (hΔH, hΔA, hΔI, hΔG, and, weakly, hΔJ) or at the PFN→hΔB synapses upstream, written while walking under FB4M/FB1H dopamine and resettable by the reward octopamine neuron OA-VPM3. Every one of those stores delivers the accumulated displacement to the goal or steering layer with its sign preserved, so it drives continuation, not return. Return requires the one inverter the wiring provides downstream of the goal, hΔM, or the hΔK/PFGs loop. The experiments that decide it are listed on finding 9; the sharpest is hΔM silencing during a return versus during menotaxis.
