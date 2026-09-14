# Thread draft

## POST 1: 

The same way levent gets to do better math because of ai, someone should be doing better neuroscience because of ai. I have been unplugged from systems neuroscience for the last two years and but have iterated heavily with fable 5.1 over the course of two days to do this.

## POST 2:

I scraped the fly connectome and found a group of neurons (hΔH, hΔA, hΔI and hΔG) that could allow the fly to navigate using synaptic weights, not neural activations. This is fast-weight continual learning, something frozen LLMs cannot do.

A fly that leaves a drop of food and wanders in the dark can always find its way back. To do that it has to keep a running sum of every step it has taken, a process called path integration. The neurons that report each step are known, but the neurons that add the steps up have never been found.

There are two ways a brain can hold a sum like that. The usual answer is that some neurons holds it in activations and sustains these activations by exciting each other in a loop tuned so precisely that the signal neither fades nor blows up. Most models of navigation assumes this, and it is how RNNs and LLMs hold state too. The other answer is that nothing keeps firing at all. Each step is encoded into synaptic strengths (aka weights), and the sum of all synaptic strengths is the sum of the journey. A few papers have suggested the fly works this way but nobody has pointed to the neurons, until now.

Four neuron types, hΔH, hΔA, hΔI and hΔG, have no known functions, but I found that they have every ingredient option 2 needs. They receive input from neurons that report each step taken, they receive velocity-sensitive dopamine input that could gate memory writing, and they receive a reward-sensitive octopamine neuron that could reset the synaptic weights at food arrival. Simulations confirm this is a viable candidate for path integration.

This is the key finding, but I have posted 3 other findings in links below. These findings are built upon the work of some seminal neuroscientists (Larry Abbott, Gaby Maimon, Vivek Jayaraman, Barbara Webb). I tried to be exhaustive with published papers but may have very well missed some key published results, so inviting the cogniscenti to engage.

Background, methods, experiments, results, as well as relevant citations: https://pwang724.github.io/fly-circuit-exploration/findings/index.html
Panoramic circuit view: https://pwang724.github.io/fly-circuit-exploration/circuit.html
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
