# Fly navigation: a first reading map

Checked 10 September 2026. This is a curated starting map, not a systematic review. Notes here are short orientation summaries; the methods-level reading of each paper lives in its `papers/<folder>/notes.md` and `reading-log.md`. The status table in [papers/README.md](../papers/README.md) is authoritative for which papers have been read in full; the 2026-09-10 batch listed below added twenty-six full-text readings. Dates below generally use journal issue year, with online dates called out where they differ. Preprints are explicitly separated.

## Read first

Start with **Maimon & Abbott (2026), [Functional Logic of a Cognitive Brain System for Navigation](https://doi.org/10.1146/annurev-neuro-112723-062711)**, Annual Review of Neuroscience 49:411–434. It organizes the central complex around angles, vectors, and the relationship between computation, algorithm, and biological implementation. This is an author-written synthesis, not a new experiment.

Then read Seelig & Jayaraman 2015 → the two 2017 angular-integration papers → Hulse et al. 2021 → the paired 2022 vector papers → the paired 2024 steering papers. Follow with the 2025–2026 work below to see where the account is still changing.

## Canonical experimental and anatomical foundations

| Paper | What it contributes | How to use it here |
|---|---|---|
| Seelig & Jayaraman (2013), [Feature detection and orientation tuning in the Drosophila central complex](https://doi.org/10.1038/nature12601), Nature | Visual feature tuning in ring neurons. | Start upstream of the compass, with sensory representations. |
| Seelig & Jayaraman (2015), [Neural dynamics for landmark orientation and angular path integration](https://doi.org/10.1038/nature14446), Nature | A persistent heading-related activity bump follows landmarks and self-motion in darkness. | Establish the represented variable before interpreting a wiring diagram. |
| Kim, Rouault, Druckmann & Jayaraman (2017), [Ring attractor dynamics in the Drosophila central brain](https://doi.org/10.1126/science.aal4835), Science | Optogenetically imposed activity states persist with attractor-like dynamics. | Causal support for the attractor account. |
| Green et al., Maimon lab (2017), [A neural circuit architecture for angular integration in Drosophila](https://doi.org/10.1038/nature22343), Nature | P-EN pathways shift the heading estimate; perturbations test the updating mechanism. | Interpret PEN1/PEN2 and EPG connectivity. |
| Turner-Evans et al., Jayaraman lab (2017), [Angular velocity integration in a fly heading circuit](https://doi.org/10.7554/eLife.23496), eLife | Conjunctive heading/angular-velocity coding and anatomically shifted recurrence. | Read alongside Green rather than treating either as the entire history. |
| Green et al. (2019), [A neural heading estimate is compared with an internal goal to guide oriented navigation](https://doi.org/10.1038/s41593-019-0444-x), Nature Neuroscience | Links the compass to correction toward an internal goal bearing. | Distinguish representing heading from controlling behavior. |
| Fisher, Lu, D’Alessandro & Wilson (2019), [Sensorimotor experience remaps visual input to a heading-direction network](https://doi.org/10.1038/s41586-019-1772-4), Nature | Inhibitory visual inputs and experience-dependent remapping. | Synapse presence/count alone cannot specify learned effective weights. |
| Kim, Hermundstad, Romani, Abbott & Jayaraman (2019), [Generation of stable heading representations in diverse visual scenes](https://doi.org/10.1038/s41586-019-1767-1), Nature | Experiments and modeling connect visual plasticity to a stable heading map. | Bridge attractor dynamics and learned sensory anchoring. |
| Turner-Evans et al. (2020), [The neuroanatomical ultrastructure and function of a biological ring attractor](https://doi.org/10.1016/j.neuron.2020.08.006), Neuron | Combines ultrastructure and functional analysis of compass circuitry. | A central reference for translating conceptual recurrence into cell types. |
| Hulse, Haberkern, Franconville, Turner-Evans et al. (2021), [A connectome of the Drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection](https://doi.org/10.7554/eLife.66039), eLife | Broad hemibrain CX architecture and candidate computational motifs. | The anatomical atlas for this project; distinguish observed edges from proposed functions. |
| Lyu, Abbott & Maimon (2022; online 2021), [Building an allocentric travelling direction signal via vector computation](https://doi.org/10.1038/s41586-021-04067-0), Nature | A vector computation transforms body-relative movement into world-relative travel direction. | Focus on PFN inputs and their downstream combination. |
| Lu et al., Wilson/Druckmann collaborators (2022; online 2021), [Transforming representations of movement from body- to world-centric space](https://doi.org/10.1038/s41586-021-04191-x), Nature | PFN populations combine heading and translation; hΔB represents world-relative velocity. | World-relative velocity is distinct from its time-integrated displacement. |

## Goal-to-action mechanisms and recent advances

| Paper | Main result or proposal | Evidence boundary |
|---|---|---|
| Mussells Pires, Zhang, Parache, Abbott & Maimon (2024), [Converting an allocentric goal into an egocentric steering signal](https://doi.org/10.1038/s41586-023-07006-3), Nature | FC2 goal representation and PFL3 transformation into steering. | A powerful account of directional control; not a complete account of how every goal is acquired. |
| Westeinde et al., Wilson lab (2024), [Transforming a head direction signal into a goal-oriented steering command](https://doi.org/10.1038/s41586-024-07039-2), Nature | PFL3 populations support turn direction; PFL2 increases steering strength for large errors. | Published page includes a March 2025 correction. Use the corrected version. |
| Dan, Hulse, Kappagantula, Jayaraman & Hermundstad (2024), [A neural circuit architecture for rapid learning in goal-directed navigation](https://doi.org/10.1016/j.neuron.2024.04.036), Neuron | Connectome-informed modular architecture for learning navigational goals. | Treat the proposed learning mechanism as a model to assess, not proof of all underlying plasticity. [Author code](https://github.com/HermundstadLab/flyVisualLearning). |
| Noorman, Hulse, Jayaraman, Romani & Hermundstad (2024), [Maintaining and updating accurate internal representations of continuous variables with a handful of neurons](https://doi.org/10.1038/s41593-024-01766-5), Nature Neuroscience | Small networks can support continuous representations with tuning/robustness tradeoffs. | Important theoretical constraint for building compact compass models. |
| [Connectomic reconstruction predicts visual features used for navigation](https://doi.org/10.1038/s41586-024-07967-z) (2024), Nature | Uses visual-pathway anatomy to predict features supplied to the navigation system. | Expand beyond CX when asking how the compass obtains sensory anchors. |
| Basnak et al., Drugowitsch & Wilson (2025), [Multimodal cue integration and learning in a neural representation of head direction](https://doi.org/10.1038/s41593-024-01823-z), Nature Neuroscience 28:1729–1740 | Examines integration and learning of multiple heading cues. | The DOI contains 2024; the paper was published in 2025. |
| Ishida, Sethi, Mohren, Haraguchi, Abbott & Maimon (2026 issue; online 29 Dec 2025), [Neuronal calcium spikes enable vector inversion in the Drosophila brain](https://doi.org/10.1016/j.cell.2025.11.040), Cell 189:748–764.e25 | Hyperpolarization-elicited T-type calcium spikes enable PFNa population-vector inversion. | Calcium signals need not equal fast synaptic output. The natural behavioral contribution and several downstream readouts remain unresolved. |
| Siliciano, Minni, Morton et al., Abbott & Ruta (22 July 2026), [A vector-based strategy for olfactory navigation in Drosophila](https://doi.org/10.1038/s41586-026-10827-7), Nature | Odor-boundary tracking uses directional memories; FC2 signals the return direction outside the plume. | Journal status verified via [published abstract](https://pubmed.ncbi.nlm.nih.gov/42486983/). Do not cite the February 2025 preprint as the latest version. |
| Kathman, Lanz, Freed & Nagel (25 July 2026), [Neural dynamics for working memory and evidence integration during olfactory navigation in Drosophila](https://doi.org/10.1038/s41467-026-75945-2), Nature Communications | FB local-neuron activity accumulates odor evidence and persists after odor loss; silencing impairs persistent directional behavior. | Driver-labeled population includes hΔK; do not equate a driver line with a single perfectly specific cell type. |

## Preprints worth following

- **Plitt, Turner-Evans et al., Jayaraman & Fisher**, [Octopamine instructs head direction plasticity](https://doi.org/10.64898/2025.12.11.693783), posted December 2025; still listed as bioRxiv by the [Fisher lab](https://www.fisherlab.science/publications) at this check. Proposes and tests an EPG→EL→ER feedback pathway that supplies coincidence information for inhibitory sensory plasticity. Add EL to the extraction even though it is absent from a minimal EPG/PEN compass cartoon. [Accessible manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC12724720/).
- **Weisman et al., Maimon lab**, [Drosophila maintain a consistent navigational goal angle for days to weeks](https://doi.org/10.64898/2025.12.09.693277), December 2025 preprint. Long-duration head-fixed VR behavior motivates questions about durable goal storage. This is not evidence that a particular synaptic memory substrate has been identified. [Record and abstract](https://pubmed.ncbi.nlm.nih.gov/41427349/).
- [Deep conservation of head direction circuits in bees, ants and flies](https://www.biorxiv.org/content/10.64898/2026.07.26.740564v1.full), July 2026 preprint. Useful comparative extension; do not assume every insect implements identical circuitry.


## Papers read in full on 2026-09-10 (added to the map)

| Paper | Role in the synthesis | Notes |
|---|---|---|
| van Breugel & Dickinson (2014), Curr Biol | Three flight reflexes (surge 190 ms, cast 450 ms, odor-gated object attraction); stigmergic null model | [notes](../papers/2014-van-breugel-plume-tracking/notes.md) |
| Hige et al. (2015), Neuron | Dopamine-gated KC→MBON depression; MB plasticity comparison case | [notes](../papers/2015-hige-heterosynaptic-memory-plasticity/notes.md) |
| Kim & Dickinson (2017), Curr Biol | Idiothetic local search after food in the dark | [notes](../papers/2017-kim-dickinson-idiothetic-path-integration/notes.md) |
| Currier & Nagel (2018), Curr Biol | Stripe dominates wind in tethered flight; filter-sum model | [notes](../papers/2018-currier-multisensory-flight/notes.md) |
| Giraldo et al. (2018), Curr Biol | Sun menotaxis over hours needs E-PGs | [notes](../papers/2018-giraldo-sun-navigation/notes.md) |
| Suver et al. (2019), Neuron | APN/WPN antennal wind-direction code | [notes](../papers/2019-suver-wind-direction/notes.md) |
| Corfas et al. (2019), eLife | State-dependent sensory triggers of local search | [notes](../papers/2019-corfas-food-local-search/notes.md) |
| Haberkern et al. (2019), Curr Biol | 2D VR: sugar search independent of landmarks; virtual-heat conditioning | [notes](../papers/2019-haberkern-virtual-landscape/notes.md) |
| Stern et al. (2019), Curr Biol | Trial-and-error learning of an unmarked rewarded place; MB vs ring-neuron contributions | [notes](../papers/2019-stern-spatial-trial-error/notes.md) |
| Okubo et al. (2020), Neuron | Wind anchors the EPG compass via WL-L→R1 | [notes](../papers/2020-okubo-wind-compass/notes.md) |
| Turner-Evans et al. (2020), Neuron | EM/RNA-seq/perturbation audit of the ring attractor | [notes](../papers/2020-the-neuroanatomical-ultrastructure-and-function-of-a-biological-ring-attractor/notes.md) |
| Behbahani et al. (2021), Curr Biol | Path integrator re-zeros at the centre of a fictive patch | [notes](../papers/2021-behbahani-rezero-path-integrator/notes.md) |
| Fisher et al. (2022), Nature | ExR2 dopamine gates compass plasticity during turns | [notes](../papers/2022-fisher-dopamine-compass-plasticity/notes.md) |
| Lu et al. (2022; bioRxiv v1 read), Nature | PFNd/PFNv velocity vectors, SpsP/LNO2 inputs, hΔB travel direction | [notes](../papers/2022-transforming-representations-of-movement-from-body-to-world-centric-space/notes.md) |
| Hulse et al. (2023 preprint) | GLNO rotational-velocity input to PEN; motor over visual | [notes](../papers/2023-hulse-visuomotor-angular-velocity/notes.md) |
| Kutschireiter et al. (2023), PNAS | Bayesian ring attractor; amplitude as certainty | [notes](../papers/2023-kutschireiter-bayesian-ring-attractor/notes.md) |
| Mitchell et al. (2023), Proc R Soc B | Cue integration as vector summation; contrast weighting in beetles | [notes](../papers/2023-mitchell-cue-integration/notes.md) |
| Dan et al. (2021 preprint of Neuron 2024) | Fixation/saccade policy learning; compass-indexed goal weights | [notes](../papers/2024-a-neural-circuit-architecture-for-rapid-learning-in-goal-directed-navigation/notes.md) |
| Chen et al. (2024 preprint) | Self-deposited scent marks plus PFNd self-motion in featureless arenas | [notes](../papers/2024-chen-spatial-learning/notes.md) |
| Feng et al. (2024 preprint) | DNa03/LAL013/DNa11 hierarchical steering circuit | [notes](../papers/2024-feng-central-steering/notes.md) |
| D'Atri & DasGupta (2025 preprint) | Distance vs place memory; PFN→hΔB odometer | [notes](../papers/2025-datri-odometry/notes.md) |
| Flores-Valle et al. (2025 preprint) | PFR rest drift ~180° from walking; learning shifts drift | [notes](../papers/2025-flores-valle-goal-learning-memory-drift/notes.md) |
| May et al. (2025 preprint) | PFNd airflow+optic flow, PFNp_c airspeed; wind observable during maneuvers | [notes](../papers/2025-may-multisensory-wind/notes.md) |
| Plitt et al. (2025 preprint) | EL octopamine relays EPG activity to ER terminals | [notes](../papers/2025-plitt-octopamine-compass-plasticity/notes.md) |
| Maimon & Abbott (2026), Annu Rev Neurosci | Organising review; vector arithmetic on sinusoidal codes | [notes](../papers/2026-maimon-abbott-navigation-review/notes.md) |
| Ishida et al. (2026), Cell | Ca-α1T calcium spikes invert PFNa vectors; FC3 readout | [notes](../papers/2026-neuronal-calcium-spikes-enable-vector-inversion-in-the-drosophila-brain/notes.md) |

## Who to follow, beyond the four requested names

Maimon/Abbott connect explicit computation to physiology and biophysics; Jayaraman and collaborators establish compass dynamics, anatomy, and models; Wilson and collaborators connect physiology, sensory learning, coordinate transforms, and steering. These are overlapping collaborations, not separate ownership of circuit modules. The reading above also makes clear why Hermundstad, Romani, Druckmann, Fisher, Kim, Nagel, Ruta, and the FlyEM/FlyWire teams belong in the map.

## Search trail and limitations

Searched the supplied Google release, the MaleCNS project/download/release pages, the Maimon/Jayaraman/Fisher author publication lists, and primary publisher/PubMed records. Queries combined fly/Drosophila navigation or central complex with the named investigators, 2025/2026, vector computation, angular integration, plasticity, and goal-directed steering. Checked journal-versus-preprint status where discrepancies appeared. This first pass is intentionally centered on the central complex; mushroom-body interactions, descending/VNC control, classic insect homing theory, and natural flight need deeper follow-up. No claim of exhaustive coverage or a definitive field ranking is intended.
