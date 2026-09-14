# The stored vector points away from food. One unassigned neuron type, hΔM, is the only thing that turns it around

**Summary.** A stored displacement points from food to fly, but steering needs the reverse, so something between the store and the steering neurons must rotate the vector by half a turn. The store cells do not do it: hΔB's synapses land on their axonal arbors, not their dendrites, so they relay the vector unrotated. Between the goal neurons FC2 and the steering neurons PFL3, the only columnar type that rotates is hΔM, eight cells with no assigned function: FC2 contacts its dendrites and its axon, 178° away, contacts PFL3 and PFL2. PFL3 therefore receives the stored vector twice, unrotated via FC2 ("keep going") and rotated via hΔM ("go back"); in a closed-loop model only the rotated copy produces return.

> **Audit note (2026-09-13).** hΔM is not the only inverter. hΔA's axon contacts hΔI's dendrites (1,388 synapses, 63 % at 180° in the hemibrain, every hΔI cell), and hΔI's axon reaches PFL3 (3,468) and PFL2 (1,942), so the stored vector reaches steering rotated by a second route that bypasses FC2. hΔM remains the only inverter downstream of FC2. In the axon frame both inverting routes return and both direct routes walk away; with synapse-count weights the direct routes dominate. Details: [docs/audit-2026-09-13.md](../docs/audit-2026-09-13.md).

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

Hulse 2021 drew this two-arbor contact motif anatomically without following its sign. The same shares appear in the hemibrain.

## Where the rotation actually happens

From the store the signal goes to the goal neurons FC2, and from FC2 to the steering neurons PFL3. Both connections stay in the same column, so by that route PFL3 receives "north" and steers the fly further north, away from the food. There is one other route from FC2 to PFL3: through hΔM. FC2 contacts hΔM's dendrites, and hΔM's axon, 180° away, contacts PFL3. Through hΔM, PFL3 receives "south". hΔM is the only cell type between the goal and the steering neurons that does this, and nobody has assigned it a function.

| FC2 → PFL3 route | synapses | rotation |
|---|---|---|
| direct | 7,690 | 2° |
| through hΔM (1,073 in, 3,983 out) | 3,983 | 178° |
| through hΔM to PFL2 | 1,555 | 178° |

FC2 columns are named directly, so there is no arbor ambiguity on this step.

## The simulation check

A model fly with the store wired to steering with no rotation walks away from the food on every run. With 180° rotation, or with hΔM's measured 178°, it returns.

| rotation between store and PFL3 | returned to food | median closest approach |
|---|---|---|
| 180° / 178° (hΔM) | 35 % | 1.05 / 1.36 |
| 90° | 20 % | 2.64 |
| 0° (direct route only) | 0 % | 10.3, walks away |
| no memory | – | 6.76 |

Distances in units of the outbound walk length, 60 runs.

## Consequence

PFL3 receives the same memory twice: "north" directly, meaning keep going, and "south" through hΔM, meaning go back. Whichever input wins decides whether the fly keeps exploring or returns. Dispersing flies do keep going for hours (Green 2019), and FB5A, a GABA neuron that inhibits FC2, PFL3 and hΔM together, is placed to set the balance. hΔM is the return path.

PFL2 also receives the rotated goal from hΔM. PFL2 is known to fire most when the fly faces away from its goal (Westeinde 2024), which this explains with no new anatomy.

## What would settle it

- Silence hΔM during a return to food and during straight heading maintenance: return should fail, heading should survive.
- Image hΔM and FC2 together: bumps half a turn apart.
- Image hΔH or hΔA during a return: bump along the outbound displacement, not toward the food.

## Prior work

Hulse 2021 drew the two-arbor contact motif on hΔ neurons without its sign consequence. Liao 2025 describe an anti-goal circuit further downstream in the lateral accessory lobe. Nanni & Lee 2026 propose FB5A as the FC2 normaliser. The hΔM rotation and its necessity for return are not in print.

## Methods

Arbor assignment uses the column offset between hΔB's name and each target's name, with hΔ cells named by dendritic column (Hulse 2021) and hΔB's output on its axonal arbor (Lyu 2022): an offset of 180° from hΔB's name means contact on the target's dendrite, 0° means contact on the target's axon. Route rotations are the mean angular offsets of FC2→hΔM (336°) and hΔM→PFL3 (202°) summed. Closed-loop agent: rate-based, eight columns, store from finding 1, PFL3 steering as left minus right proportional to sin(goal − heading), rotation between store readout and goal varied as a parameter. Tables: `data/derived/fb_offset_stats.csv`; simulation results: `simulations/closed_loop_kernel_controls.json`; notes: `docs/exhaustive-search.md` §4.

References: Hulse 2021; Lyu 2022; Mussells Pires 2024; Westeinde 2024; Green 2019; Liao 2025; Nanni & Lee 2026.
