# The stored vector points away from food. Two unassigned neuron types, hΔM and hΔI, are the only things that turn it around

**Summary.** A stored displacement points from food to fly, but steering needs the reverse, so something between the store and the steering neurons must rotate the vector by half a turn. The store cells do not do it: hΔB's synapses land on their axonal arbors, not their dendrites, so they relay the vector unrotated. The wiring supplies exactly two rotating routes to the steering neurons PFL3 and PFL2, both through cells with no assigned function: after the goal neurons FC2, only hΔM rotates (FC2 contacts its dendrites; its axon, 178° away, contacts PFL3); before FC2, the store candidate hΔA contacts the dendrites of hΔI, whose axon reaches PFL3 half a turn away. PFL3 therefore receives the stored vector unrotated ("keep going") directly and rotated ("go back") by these two; in a closed-loop model only the rotated copies produce return.

## The problem

The store of finding 1 holds the fly's displacement from the food: "I am 2 north of the food". To walk home the steering neurons need the opposite vector: "walk 2 south". Somewhere between the store and the steering neurons the vector has to be rotated by 180°. The question is which neuron does that.

## Why the store cells looked like the answer

Every hΔ neuron has its dendrites in one column of the fan-shaped body and its axon in the column 180° away. A signal that arrives on the dendrites at the "north" column is emitted at the "south" column: a built-in half-turn rotation. The store candidates are hΔ cells, so the store would receive "north" and automatically emit "south", which is "go home". The rotation would come free with the anatomy.

## Why that is wrong

The connectome shows where hΔB's synapses land on each store cell. They land on the axon, not the dendrites. A signal that enters at the axon leaves from that same axon, in that same column. So the store receives "north" and emits "north". It passes the displacement along unchanged, pointing away from the food.

| hΔB synapses onto | on the axonal arbor | result |
|---|---|---|
| hΔH | 95 % | relays, no rotation |
| hΔA | 92 % | relays |
| hΔI | 82 % | relays |
| hΔG | 73 % | relays |
| hΔJ | 58 % | both arbors, cancels |
| hΔK | 1 % | dendrite: does rotate, but is not a store |

Hulse 2021 drew this two-arbor contact motif anatomically without following its sign. The same shares appear in the hemibrain, and hΔB's own PFNd input splits across both arbors the same way, which Lyu 2022 modelled as a subtraction.

## Where the rotation actually happens

From the store the signal goes to the goal neurons FC2, and from FC2 to the steering neurons PFL3. Both connections stay in the same column, so by that route PFL3 receives "north" and steers the fly further north, away from the food. Of every two-step columnar route from the stores or FC2 to PFL3 and PFL2 with at least 150 synapses per step, exactly two rotate: FC2 contacts hΔM's dendrites, and hΔM's axon, 180° away, contacts PFL3; hΔA's axon contacts hΔI's dendrites in all 17 hΔI cells, and hΔI's axon, 180° away, contacts PFL3 and PFL2. Nobody has assigned either cell a function.

| route to PFL3 | synapses | rotation |
|---|---|---|
| FC2 → PFL3 direct | 7,690 | 2° |
| FC2B → hΔM → PFL3 (1,073 in, 2,428 out) | 2,428 | 178° |
| FC2B → hΔM → PFL2 | 1,555 | 178° |
| hΔA → PFL3 direct | 3,881 | 14° |
| hΔA → hΔI → PFL3 (1,388 in, 3,468 out) | 3,468 | 195° |
| hΔA → hΔI → PFL2 | 1,942 | 197° |

FC2 columns are named directly, so there is no arbor ambiguity on that step. hΔI also receives the current step from hΔB on its axon, unrotated, so if hΔA is the store, hΔI sends PFL3 the current step minus the stored vector: a comparison, not a relay.

## The simulation check

A model fly with the store wired to steering with no rotation walks away from the food on every run. With 180° rotation, or with either measured route, it returns.

| rotation between store and PFL3 | returned to food | median closest approach |
|---|---|---|
| 180° ideal / 178° (hΔM) | 35 % | 1.05 / 1.36 |
| 90° | 20 % | 2.64 |
| 0° (direct route only) | 0 % | 10.3, walks away |
| no memory | – | 6.76 |

Distances in units of the outbound walk length, 60 runs. Through the measured kernels the readout points 34° from home via either rotating route and 145° or more from home via every direct route. Weighted by synapse count the direct routes win; something must tip the balance.

## Consequence

PFL3 receives the same memory twice: "north" directly, meaning keep going, and "south" through hΔM and through hΔI, meaning go back. Whichever input wins decides whether the fly keeps exploring or returns. Dispersing flies do keep going for hours (Green 2019), and FB5A, a GABA neuron that inhibits FC2, PFL3, hΔM and hΔH together, is placed to set the balance. hΔM and hΔI are the return path.

PFL2 also receives the rotated goal from both. PFL2 is known to fire most when the fly faces away from its goal (Westeinde 2024), which this explains with no new anatomy.

## What would settle it

- Silence hΔM, and separately hΔI, during a return to food and during straight heading maintenance: return should fail, heading should survive.
- Image hΔM and FC2 together, and hΔI and hΔA together: bumps half a turn apart.
- Image hΔH or hΔA during a return: bump along the outbound displacement, not toward the food.

## Prior work

Hulse 2021 drew the two-arbor contact motif on hΔ neurons without its sign consequence. Liao 2025 describe an anti-goal circuit further downstream in the lateral accessory lobe. Nanni & Lee 2026 propose FB5A as the FC2 normaliser. The hΔM and hΔI rotations and their necessity for return are not in print.

## Methods

Arbor assignment uses the column offset between presynaptic and target labels, with hΔ cells named by dendritic column (Hulse 2021) and hΔB's output on its axonal arbor (Lyu 2022): 180° from a presynaptic hΔ label means contact on the target's dendrite, 0° on its axon. Route rotations are the summed mean offsets of the steps (FC2B→hΔM 336° + hΔM→PFL3 202°; hΔA→hΔI 183° + hΔI→PFL3 192°) relative to the travel bump. Route screen: every columnar intermediate with ≥ 150 synapses on both legs to PFL3, PFL2, PFL1. Closed-loop agent: rate-based, eight columns, store from finding 1, PFL3 steering as left minus right proportional to sin(goal − heading), rotation as a parameter, then each measured route with the bump at the axon column. Tables: `data/derived/fb_offset_stats.csv` (hemibrain: hΔA→hΔI 1,170 synapses, 63 % at 180°); results: `simulations/closed_loop_kernel_controls.json`, `closed_loop_routes_tspace_results.json`; notes: `docs/audit-2026-09-13.md` §2.

References: Hulse 2021; Lyu 2022; Mussells Pires 2024; Westeinde 2024; Green 2019; Liao 2025; Nanni & Lee 2026.
