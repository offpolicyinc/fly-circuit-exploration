# The fly's running sum of its own steps is held in synapse strengths, on four neuron types nobody has assigned a function

**Summary.** A fly that leaves food and wanders in the dark can walk straight back, so it keeps a running vector sum of its steps. The neurons that report each step, hΔB, are known; whatever adds them up has never been found, and every model assumes a population that keeps firing the total. No fan-shaped-body population has anywhere near the self-excitation that requires. Four types with no assigned function, hΔH, hΔA, hΔI and hΔG, have exactly the wiring a synaptic store needs: hΔB's travel-direction bump lands on them in the matching column, so each step would strengthen only the synapses for that direction and the weight pattern across columns becomes the vector sum; two dopamine types active while the fly walks contact every one of them as a write gate; the reward-driven octopamine neuron OA-VPM3 contacts them as a candidate reset; and their outputs go to the goal and steering neurons. The home vector is probably a pattern of weights, which is why imaging has not found it.

## The question

To return to a place it cannot see, the fly must know the vector from that place to itself. That vector is the sum of every step it has taken since leaving, each step counted in world coordinates. The fan-shaped body has the neurons that report each step: about twenty hΔB cells whose bump of activity sits at the column matching the direction the fly is currently moving, with height proportional to speed (Lu 2022; Lyu 2022). Each column of the fan-shaped body is a compass direction, so the bump is the current step as a vector. What is missing is the thing that adds these steps up over time.

## Two ways to hold a running sum

The first is in activity. A population keeps firing the current total and adds each new step to it. For the total not to leak away, the population must excite itself with a gain of almost exactly one: each pass around the loop must regenerate the bump neither weaker nor stronger. Every published model of path integration assumes this.

The second is in synapses. Nothing keeps firing. Instead, each step makes hΔB strengthen the synapses it is currently using. After a walk, the pattern of synapse strengths across the columns is the sum: six steps north and four south leave the north synapses at six and the south ones at four, and the difference is a vector of length two pointing north. This needs no self-excitation. It does need hΔB to land on its target in the matching column, a signal that says "write now" while the fly walks, a way of resetting the store when the fly is back at food, and a path from the store to the neurons that steer.

The two options make different demands on the wiring, so a connectome can tell them apart.

## What the wiring rules out

For every population in the fan-shaped body, I counted the synapses it makes onto itself, binned by the column offset between the two cells, and extracted the cosine mode: the component of self-feedback that holds a bump in place. An activity integrator needs this gain near one.

| population | cosine-mode self-excitation |
|---|---|
| vΔA_a, the highest of ~40 populations | 0.14 |
| every hΔ, PFN, PFR and FR1 type | ≤ 0.02 |
| strongest two-population loops | < 0.01 |

Nothing comes within an order of magnitude. The same holds in the hemibrain. Unless a few synapses are ten times more effective than all others, or cells have intrinsic persistence the connectome cannot see, the running sum is not held as activity here.

## What the wiring points to

Scoring every target of hΔB for the four requirements of a synaptic store, the same four cell types come out on top.

| type | hΔB synapses | same column | dopamine (FB4M, FB1H) | octopamine (OA-VPM3) | sends to |
|---|---|---|---|---|---|
| hΔH (8 cells) | 1,010 | 82 % | 165 | 361 | FC2, PFL3 |
| hΔA (12) | 2,216 | 64 % | 1,098+ | 124 | PFL3, PFL2 |
| hΔI (17) | 3,575 | 48 % | 380+ | 72 | PFL3, PFL2 |
| hΔG (8) | 736 | 63 % | 134 | 113 | FC2 |
| hΔJ (31), rejected | 4,232 | 35 % (+28 % opposite) | 1,809 | 377 | FC2 |

Column matching is what makes the store work. hΔB lands on hΔH in hΔH's own column 82 percent of the time, so a step north strengthens the north synapses and little else. hΔJ receives more hΔB synapses than any candidate, but in two opposite columns, so every step strengthens both north and south and the total cancels. In a simulation that writes a random walk through each type's measured landing pattern, hΔH retains 86 percent of an ideal store, hΔA 76, hΔI 56, hΔG 45, and hΔJ 14.

The write signal is there. Two dopamine cell types, FB4M and FB1H, contact every cell of all four types across all columns. They are driven by the velocity neurons PFNv, PFNd and hΔB, so they fire while the fly moves and not when it stands still. They are the translational counterpart of ExR2, the dopamine neuron that gates compass learning by rotation speed (Fisher 2022).

The reset candidate is there. OA-VPM3 is an octopamine neuron, octopamine being the fly's reward transmitter, driven by Kenyon cells and reward-related tangentials. It contacts hΔH, hΔB and PFR.

And the output goes to the right place: FC2, the goal neurons, and PFL3, the steering neurons, which are known to turn a stored direction into walking (Mussells Pires 2024; Westeinde 2024). Every one of these edges is present in both connectomes.

## How the store is read

There is no recall step. A store cell fires as hΔB's drive times its synapse strength. hΔB is active whenever the fly moves, so as soon as it walks, the store's output across the columns is the stored pattern, and it flows to FC2 and PFL3 continuously. The same walking that reads also writes: every step drives the store and strengthens the synapses it is driving. Walking home strengthens the opposite columns until the difference is zero, which is arrival.

The output points from food to fly. Delivered straight to steering it says keep going, which is harmless on the outbound walk. Turning it into go back is a separate neuron, and is finding 2.

## Why nobody has seen it

The memory is a set of synapse strengths, not a firing pattern. Imaging hΔB shows the current step, not the sum. Imaging the store cells at rest shows nothing, because nothing fires until hΔB drives them. In a neighbouring fan-shaped-body system, a stored vector was recently found to be visible as cAMP but not as calcium (Gorko & Kim 2026), which is what this predicts here.

## What the simulations show

Only a running vector sum reproduces the fly's search behaviour. In Kim's and Titova's assays the search-centre error is 0.8 units for a vector sum, 12.7 for a random walk, and 26.8 for either remembering the direction at the food or the distance walked. In closed loop, an agent using the store returns to the food (median closest approach 1.1 units versus 6.8 without memory), provided the readout is rotated by half a turn before steering. Without the rotation it walks away every time.

## What is not known

Nobody has recorded plasticity at these synapses, or dopamine or octopamine acting on them. If synapses only strengthen, every trip leaves them higher (six north and six south after a round trip, not zero and zero), so they would saturate; either a reset at food or a rule that weakens the opposite synapses on the return is required, and the connectome cannot tell which. During the outbound walk the store also pushes the goal layer to keep going, which is either useful for dispersal or needs to be gated; FB5A is the candidate gate. A fly standing still has no hΔB drive and so no readout.

## What would settle it

- Image hΔH or hΔA in a fly re-zeroing its home vector (the Behbahani 2021 task): the bump should grow with distance from the food and collapse at re-zero.
- Block dopamine or cAMP signalling in those cells: the fly should stop returning while hΔB and the compass stay intact.
- Silence OA-VPM3 while the fly feeds: its subsequent search should no longer be centred on the food.

## Prior work

hΔB as the travel-direction signal: Lu 2022; Lyu 2022. Sinusoidal vector arithmetic across fan-shaped-body columns: Lyu 2022; Maimon & Abbott 2026. Synaptic storage of a vector as an idea: Hulse 2021; Goulard 2023 (model); Maimon & Abbott 2026; none named a cell type. New here: activity storage ruled out for every population; the four candidate types and hΔJ's rejection; FB4M/FB1H and OA-VPM3 as the write and reset signals; the readout and closed-loop tests.

## Methods

Column offsets: every fan-shaped-body neuron in MaleCNS v1.0 carries a column label; angular offsets use the true column count per type (12 for hΔA/B/C/I/J/K/L, 8 for hΔD/E/G/H/M and PFNd, 6 for hΔF; C9≡C1 for nine-label types). hΔ cells are named by their dendritic column (Hulse 2021), and hΔB's bump sits on its axonal arbor (Lyu 2022); these conventions fix the sign of every offset. Recurrence: within-type synapses binned by offset, normalised by total input, signed by transmitter, Fourier-decomposed; cosine-mode gain is the first harmonic. Site screen: every synapse from a travel- or heading-tuned population onto every columnar population scored for column matching, modulator coverage, reset coverage, and output to FC2/PFL3. Simulations: rate-based agent, eight columns, rectified-cosine hΔB bump, weights incremented by the bump passed through each candidate's measured landing kernel, readout as weights times drive passed through the candidate's measured output kernel. Tables: `data/derived/recurrence_modes.csv`, `fb_column_offsets.csv`, `synaptic_site_screen.csv`, `reward_inputs_trace.json`, `hemibrain_key_edges.csv`. Scripts: `scripts/recurrence_modes.py`, `synaptic_site_screen.py`, `reward_inputs_trace.py`; simulations: `simulations/site_readout_error.py`, `strategy_discrimination.py`, `closed_loop_sites.py`. Full analysis notes: `docs/exhaustive-search.md`.
