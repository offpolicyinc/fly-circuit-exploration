# Thread draft

## POST 1: 

The same way levent gets to do better math because of ai, someone should be doing better neuroscience because of ai

The navigational system of the fruit fly is a crown jewel of systems neuroscience due to the work of some seminal neuroscientists (Larry Abbott, Gaby Maimon, Vivek Jayaraman, Barbara Webb), but it is an unfinished story. 

A fly that leaves a drop of food and wanders in the dark walks straight back to the food. To do that it must keep a running vector sum of every step it has taken. The neurons that report each step are known, but the neurons that add those steps up over time have never been found.

There are two ways to add steps up. (1) In activity: a population keeps firing the running total. For the total not to leak away, the population must excite itself with a gain of almost exactly one. Most published model of fly path integration works this way, and so does an RNN. (2) In synapses: nothing keeps firing. Each step, neurons strengthen the synapses they are driving at that moment, and each direction of travel drives a different set of synapses. After a walk, the strengths are the sum: six steps north and four south leave the "north" synapses at 6, the "south" synapses at 4, and the difference is the vector home. I call the set of synapses that does this the "store". Maimon & Abbott (2026) and Hulse et al. (2021) proposed a synaptic memory of this kind, and Goulard, Heinze & Webb (2023) modelled one, but none identified the neurons.

I scraped the fly brain connectome to find where its spatial memory lives and found that it appears to be stored not in activity but in synaptic weights in 4 sets of neurons (hΔH, hΔA, hΔI and hΔG).

For every population in the region, I measured how strongly it excites itself in the way an activity integrator needs (gain near one). The best is 0.14, and almost everything is at or below 0.02. So I couldn't find a substrate for stateful storage of spatial memory in activity (Option 1).

Instead, I found that there are four neuron types with no known function, hΔH, hΔA, hΔI and hΔG, and these neurons have every ingredient option 2 needs. They receive input from neurons that report each step taken, they receive velocity-sensitive dopamine input that could gate memory writing, and they receive a reward-sensitive octopamine neuron that could reset the synaptic "store" at food arrival. 

So the fly's home vector is likely a set of synaptic weights, written continuously while it walks, gated by dopamine, and erased at reward: continual learning through fast weights, on a timescale of seconds, in a brain of about 140,000 neurons. These results are also supported by neural simulations during random walks. This is not possible in current LLMs, since its weights are frozen after training.

Unlike math however, systems neuroscience requires talented experimentalists handling a lot of complex equipment to test hypotheses like these. So this is just the start of an exciting journey.

For more information into background, methods, experiments, results, as well as relevant citations, see here: https://pwang724.github.io/fly-circuit-exploration/findings/01-synaptic-store.html

---

## POST 2:

There are 3 other findings but this is imo the most important one. 

I invite the cogniscenti to engage. I have been so unplugged from systems neuroscience for the last two years and have also done this in the course of two days (with my friend Fable 5.1). While I tried to be exhaustive with published papers, I may have very well missed some key published results.   

All findings: https://pwang724.github.io/fly-circuit-exploration/findings/index.html
Panoramic view of the entire circuit: https://pwang724.github.io/fly-circuit-exploration/circuit.html
GH repo: https://github.com/pwang724/fly-circuit-exploration 

___

**2 / the neuron that turns the memory around**

The store above holds the vector from the food to the fly. To walk home the fly needs the opposite vector. Something between the store and the steering neurons has to rotate it by half a turn.

The store neurons looked like they did this. Each hΔ neuron has its input end and its output end in different places, and the output end corresponds to the opposite direction (Hulse et al. 2021): a signal for "north" that enters the input end leaves as "south". But the connectome shows the hΔB step neurons connect to the store neurons' output end, not the input end (92–95 % of the connections for hΔA and hΔH). A signal that enters at the output end leaves from the output end, unrotated. The store passes the vector along still pointing away from the food. Hulse et al. (2021) drew this arrangement without following what it does to the sign.

Between the goal neurons and the steering neurons, exactly one neuron type rotates the signal by half a turn: hΔM, eight cells with no known function. The goal neurons contact its input end; its output end contacts the steering neurons with about 4,000 synapses.

So the steering neurons receive the same memory twice: unrotated, meaning keep going, and rotated through hΔM, meaning go back. Which input wins decides whether the fly explores or returns; flies that are dispersing do keep going for hours (Green et al. 2019). In a closed-loop model, without the rotation the fly walks away on every run; with it, it returns. A second steering neuron type, PFL2, is known to fire most when the fly faces away from its goal (Westeinde et al. 2024); it also receives the rotated signal from hΔM, which explains that tuning with no new anatomy.

Related: Liao et al. (2025) describe a circuit further downstream that steers away from the goal; Nanni & Lee (2026) propose an inhibitory neuron, FB5A, that contacts the goal, steering and hΔM neurons together and could set which input wins. The hΔM rotation and its necessity for return are not in print.

Prediction: silencing hΔM abolishes return but not the ability to hold a heading.

https://pwang724.github.io/fly-circuit-exploration/findings/02-return-inverter.html

[image: two-routes figure]

---

**3 / where the velocity signals come from**

The fly's compass needs to know how fast the fly is turning. Its path integrator needs to know how fast it is moving. In the dark both must come from the motor system. The neurons that deliver these signals are known: GLNO carries turning speed into the compass (Hulse et al. 2023), and two neuron types, LNO2 and SpsP, scale the step neurons' input by forward speed (Lu et al. 2022). Both papers left open what drives them.

Screening every input to those neurons, with no assumption about what to expect, names two uncharacterised types. PS196_b is the largest single input to GLNO (1,801 synapses, 19 % of its input) and also reaches the dopamine neuron that gates compass learning by turning speed (Fisher et al. 2022) and the translational side. One neuron type feeds turning speed, the learning gate, and the movement side at once, which is what a copy of the motor command would look like. FB3A, four cells, receives an ascending neuron from the fly's nerve cord, the route by which signals from the legs enter the brain, and supplies 12 % of the input to the forward-velocity neurons, the only large input to them that comes from the legs. FB3A connects back to those neurons too, so it is more likely a gain control than a pure speed signal. The PS196→GLNO connection is present in both connectomes.

A conjecture that PS196 carries turning speed has been attributed to Worden (2025); I could not find it in the paper text. FB3A's role is not in print.

Predictions: PS196_b is tuned to turning speed in darkness and leads the compass; FB3A is tuned to walking speed without vision; silencing FB3A degrades the fly's distance estimate (Behbahani et al. 2021 task).

https://pwang724.github.io/fly-circuit-exploration/findings/03-velocity-sources.html

---

**4 / a brake in the compass that no model includes**

The fly's compass is a ring of about fifty neurons with one active patch; the patch's position is the fly's heading (Seelig & Jayaraman 2015; Kim et al. 2017). When the fly turns, the patch slides. The sliding is done by about forty "shifter" neurons, each of which reads the activity at one position on the ring and writes it back one position over (Turner-Evans et al. 2017; Green et al. 2017). Every model since treats shifters as one-way conveyors.

The connectome shows each shifter receives about three times more input from the ring position it writes to than from the position it reads from (hemibrain: 1,281 vs 3,844 synapses for one shifter type, 1,512 vs 3,645 for the other; same ratio in MaleCNS). Both left-pushing and right-pushing shifters do this, so the effect has no direction: the ring neurons a shifter pushes on push back on it, and the shifters anchor the patch where it already is. Turner-Evans et al. (2020) noticed some of these synapses and called them unexpected; Hulse et al. (2021) noted the dense interconnection without comparing it to the read pathway or modelling it.

In a standard ring-attractor model, adding this feedback at the measured strength stops the patch from rotating under a constant turn signal. Real flies turn normally. So either these synapses are functionally weak, they sit where they modulate the shifter's output rather than drive it, or they are cancelled by inhibition the models leave out. The largest input pathway to the shifters is one no published compass model contains.

https://pwang724.github.io/fly-circuit-exploration/findings/04-compass-brake.html

[image: textbook vs measured figure]

---

**5 / close**

Method for all four: read the literature, find what it leaves open, ask the wiring diagram a specific question, simulate only to test the answer, state the experiment that would kill it. Code, tables, notes and the ~100 papers read:

https://github.com/pwang724/fly-circuit-exploration
