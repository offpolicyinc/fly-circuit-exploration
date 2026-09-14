# The fly's running sum of its own steps is probably held in synapse strengths, on four neuron types nobody has assigned a function

**Summary.** A fly that leaves food and wanders in the dark can walk straight back, so it keeps a running vector sum of its steps. The neurons that report each step, hΔB, are known; whatever adds them up has never been found. The sum could be held as activity or in synapses; the connectome cannot decide, since the compass, which does hold a bump, recurs no more strongly than several fan-shaped-body populations. It does show that four types with no assigned function, hΔH, hΔA, hΔI and hΔG, have exactly what a synaptic store needs: hΔB's travel-direction bump lands on them in the matching column, so each step would strengthen only the synapses for that direction and the weight pattern across columns becomes the vector sum; dopamine types cover every cell of hΔA, hΔI and hΔH as a write gate; the reward octopamine neuron OA-VPM3 covers hΔH and hΔG as a candidate reset; and their outputs go to the goal and steering neurons. In a neighbouring system a stored vector was recently seen as cAMP but not calcium, which is what this predicts here.

## The question

To return to a place it cannot see, the fly must know the vector from that place to itself. That vector is the sum of every step it has taken since leaving, each step counted in world coordinates. The fan-shaped body has the neurons that report each step: about twenty hΔB cells whose bump of activity sits at the column matching the direction the fly is currently moving, with height proportional to speed (Lu 2022; Lyu 2022). Each column of the fan-shaped body is a compass direction, so the bump is the current step as a vector. What is missing is the thing that adds these steps up over time.

## Two ways to hold a running sum

The first is in activity. A population keeps firing the current total and adds each new step to it. For the total not to leak away, the population must excite itself with a gain of almost exactly one: each pass around the loop must regenerate the bump neither weaker nor stronger. Every published model of path integration assumes this.

The second is in synapses. Nothing keeps firing. Instead, each step makes hΔB strengthen the synapses it is currently using. After a walk, the pattern of synapse strengths across the columns is the sum: six steps north and four south leave the north synapses at six and the south ones at four, and the difference is a vector of length two pointing north. This needs no self-excitation. It does need hΔB to land on its target in the matching column, a signal that says "write now" while the fly walks, a way of resetting the store when the fly is back at food, and a path from the store to the neurons that steer.

The two options make different demands on the wiring, so it is worth asking whether a connectome can tell them apart.

## What the wiring cannot decide

For every population in the fan-shaped body, I counted the synapses it makes onto itself, binned by column offset, and extracted the cosine mode: the self-feedback that holds a bump in place, as a share of total input. The compass, the one ring attractor here whose persistence is measured, was counted the same way.

| population | cosine-mode self-feedback |
|---|---|
| vΔA_a, the highest of ~40 fan-shaped-body populations | 0.145 |
| EPG, the compass ring | 0.050 |
| hΔ types (two-cell loops half a turn apart) | 0.01–0.02 |
| EPG ↔ PEN, the compass shifter loop | 0.003 |
| strongest two-population loops in the fan-shaped body | 0.001–0.002 |

The compass holds a bump for minutes in darkness with these numbers, so synapse shares are not gains and set no threshold; the wiring leaves both options open. Persistent activity is known in the fan-shaped body: FC2 holds its goal bump while the fly keeps a heading (Mussells Pires 2024), and hΔK with PFGs hold an odour-triggered intention for tens of seconds (Lanz 2025; Kathman 2026). What has never been seen is a displacement bump that grows with distance and collapses at re-zero, and the four candidates below have never been imaged in that task.

## What the wiring points to

Scoring every target of hΔB for the four requirements of a synaptic store, the same four cell types come out on top.

| type | hΔB synapses | same column | write gate (cells covered) | reset, OA-VPM3 (cells) | sends to |
|---|---|---|---|---|---|
| hΔA (12 cells) | 2,216 | 64 % | FB4M dopamine 1,098 (12/12); FB4Y serotonin 1,539 (12/12) | 124 (7/12) | PFL3, PFL2 |
| hΔH (8) | 1,010 | 82 % | FB5H dopamine 249 (8/8) | 361 (8/8) | FC2, PFL3 |
| hΔI (17) | 3,575 | 48 % | FB4M 380 (17/17); FB4Y 937 (17/17) | 72 (1/17) | PFL3, PFL2 |
| hΔG (8) | 736 | 63 % | none | 113 (7/8) | FC2 |
| hΔJ (31), rejected | 4,232 | 35 % (+28 % opposite) | FB1H 1,184 (31/31) | 377 (25/31) | FC2 |

Column matching is what makes the store work. hΔB lands on hΔH in hΔH's own column 82 percent of the time, so a step north strengthens the north synapses and little else. hΔJ receives more hΔB synapses than any candidate, but in two opposite columns, so every step strengthens both north and south and the total cancels. In a simulation that writes a random walk through each type's measured landing pattern, hΔH retains 86 percent of an ideal store, hΔA 76, hΔI 56, hΔG 45, and hΔJ 14.

The write signal is there for three of the four. The dopamine type FB4M contacts every cell of hΔA and hΔI across all columns and FB5H every cell of hΔH; hΔG has no uniform dopamine input. FB4M is fed by the velocity neurons PFNv, PFNd and hΔB and by an ascending neuron, AN19B019, so it is placed to fire while the fly walks: the translational counterpart of ExR2, which gates compass learning by rotation speed (Fisher 2022). A compass-driven serotonin type, FB4Y, is the largest modulatory input to hΔA and hΔI; its role is open.

The reset candidate is there for hΔH and hΔG. OA-VPM3 is an octopamine neuron, octopamine being the fly's reward transmitter, with Kenyon cells among its inputs. It contacts every cell of hΔH, hΔG and hΔB, seven of twelve hΔA cells, and almost no hΔI cell.

And the output goes to the right place: FC2, the goal neurons, and PFL3, the steering neurons, which are known to turn a stored direction into walking (Mussells Pires 2024; Westeinde 2024). Every one of these edges is present in both connectomes. On write gate, reset and output together, hΔA and hΔH are the strongest candidates.

## How the store is read

There is no recall step. A store cell fires as hΔB's drive times its synapse strength. hΔB is active whenever the fly moves, so as soon as it walks, the store's output across the columns is the stored pattern, and it flows to FC2 and PFL3 continuously. The same walking that reads also writes: every step drives the store and strengthens the synapses it is driving. Walking home strengthens the opposite columns until the difference is zero, which is arrival.

The output points from food to fly. Delivered straight to steering it says keep going, which is harmless on the outbound walk. Turning it into go back is a separate neuron, and is finding 2.

## Why nobody has seen it

If the memory is a set of synapse strengths, it is not a firing pattern. Imaging hΔB shows the current step, not the sum. Imaging the store cells at rest shows nothing, because nothing fires until hΔB drives them. In a neighbouring fan-shaped-body system a stored vector was recently found to be visible as cAMP but not as calcium (Gorko & Kim 2026), which is what this predicts here: a precedent from one system, not a proof.

## What the simulations show

Only a running vector sum reproduces the fly's search behaviour. In Kim's and Titova's assays the search-centre error is 0.8 units for a vector sum, 12.7 for a random walk, and 26.8 for either remembering the direction at the food or the distance walked. In closed loop, an agent using the store returns to the food (median closest approach 1.1 units versus 6.8 without memory), provided the readout is rotated by half a turn before steering. Without the rotation it walks away every time; through the measured wiring, only the two rotating routes of finding 2 read within 34° of home.

## What is not known

Nobody has recorded plasticity at these synapses, or dopamine or octopamine acting on them. If synapses only strengthen, every trip leaves them higher (six north and six south after a round trip, not zero and zero), so they would saturate; either a reset at food or a rule that weakens the opposite synapses on the return is required, and the connectome cannot tell which. During the outbound walk the store also pushes the goal layer to keep going, which is either useful for dispersal or needs to be gated; FB5A is the candidate gate. A fly standing still has no hΔB drive and so no readout. An activity-based sum in these same cells remains possible on the wiring.

## What would settle it

- Image hΔA or hΔH in a fly re-zeroing its home vector (the Behbahani 2021 task), with a cAMP sensor alongside calcium: a synaptic store shows in cAMP and grows with distance from the food; an activity store shows in calcium; either collapses at re-zero.
- Block dopamine or cAMP signalling in those cells: the fly should stop returning while hΔB and the compass stay intact.
- Silence OA-VPM3 while the fly feeds: its subsequent search should no longer be centred on the food.

## Prior work

hΔB as the travel-direction signal: Lu 2022; Lyu 2022. Sinusoidal vector arithmetic across fan-shaped-body columns: Lyu 2022; Maimon & Abbott 2026. Synaptic storage of a vector as an idea: Hulse 2021; Goulard 2023 (model); Maimon & Abbott 2026; none named a cell type. New here: the four candidate types and hΔJ's rejection; FB4M and FB5H as write signals and OA-VPM3 as reset, with cell-level coverage; the readout and closed-loop tests; the compass calibration showing that recurrence counts cannot decide the storage question.

## Methods

Column offsets: every fan-shaped-body neuron in MaleCNS v1.0 carries a column label; angular offsets use the true column count per type (12 for hΔA/B/C/I/J/K/L, 8 for hΔD/E/G/H/M and PFNd, 6 for hΔF; C9≡C1 for nine-label types). hΔ cells are named by their dendritic column (Hulse 2021), and hΔB's bump sits on its axonal arbor (Lyu 2022); these conventions fix the sign of every offset. Recurrence: within-type synapses binned by angular offset, normalised by total input, signed by transmitter, Fourier-decomposed; cosine-mode gain is the first harmonic; compass cells binned by ellipsoid-body wedge. Site screen: every synapse from a travel- or heading-tuned population onto every columnar population scored for column matching, per-cell modulator and reset coverage, and output to FC2/PFL3. Simulations: rate-based agent, eight columns, rectified-cosine hΔB bump written at the axon column, weights incremented through each candidate's measured landing kernel, readout as weights times drive through its measured output kernel. Tables: `data/derived/recurrence_modes_v2.csv`, `fb_column_offsets.csv`, `synaptic_site_screen.csv`, `cx_ext_cell_edges.csv`. Scripts: `scripts/recurrence_modes_v2.py`, `synaptic_site_screen.py`; simulations: `simulations/closed_loop_routes_tspace.py`, `strategy_discrimination.py`, `closed_loop_return.py`. Notes: `docs/exhaustive-search.md`, `docs/audit-2026-09-13.md`.
