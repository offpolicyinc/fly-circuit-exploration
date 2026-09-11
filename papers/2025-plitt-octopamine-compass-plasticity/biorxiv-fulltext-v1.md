# Plitt et al. — "Octopamine instructs head direction plasticity" — bioRxiv 10.64898/2025.12.11.693783v1

Captured 2026-09-10 via in-app browser get_page_text from https://www.biorxiv.org/content/10.64898/2025.12.11.693783v1.full. Figures not saved.


Abstract

Many plasticity rules rely on adjusting the strength of synapses between pairs of cells based on their coincident activity. We uncovered a new mechanism for coincidence detection in the Drosophila head direction network. To maintain an accurate sense of direction, head direction neurons that signal orientation during navigation must learn to anchor to relevant external sensory cues in novel environments. Yet the synaptic mechanism for this form of unsupervised learning is unknown in any organism. In Drosophila, GABAergic visual inputs converge onto head direction neurons, and these inhibitory synapses change strength with experience to learn the relationship between visual landmarks and head direction. However, how coincident pre- and postsynaptic activity is detected across this inhibitory synapse is not understood. We discovered that neurons which release the monoamine octopamine close a feedback loop that conveys postsynaptic head direction activity onto presynaptic terminals of visual inputs. This octopamine pathway is required for anchoring the head direction network to visual cues. Furthermore, pairing structured activation of octopamine neurons with a visual cue is sufficient to drive rapid plasticity, even without postsynaptic head direction cell activity. Previous work has extensively characterized coincidence detection mechanisms at excitatory synapses; our work defines a novel mechanism for coincidence detection at an inhibitory synapse, in which postsynaptic activity is relayed via a neuromodulatory neuron onto presynaptic terminals.

Main text

The discovery of head direction cells in brains across the animal kingdom underscores their fundamental importance for adaptive navigation1–5. Each head direction cell fires most strongly when an animal faces in that cell’s preferred direction. As a population, head direction cells tile all angles such that their collective activity (referred to as the head direction representation) resembles a compass, estimating the animal’s orientation in space by combining self-motion inputs with external sensory cues (Fig. 1a-b, Extended Data Fig. 1a).

Download figureOpen in new tab
Extended Data Figure 1.
EPG bump dynamics during behavior and across dark periods

a) Schematic illustrating the landmark and self-motion pathways that collectively update the EPG bump position. Landmark signals (visual and other modalities) enter the circuit via ER neurons, while self-motion signals are conveyed via PEN neurons that serve to spin the bump position as the animal turns to the left or right. When external sensory cues are present both pathways are engaged. Without external sensory cues, such as in darkness, head direction estimation relies solely on integrating inputs to the self-motion pathway.

b) Schematic illustrating hypothesized ER-EPG synaptic strengths. Top: 3 example bump-cue offsets. Bottom: corresponding synaptic strength matrices. Connections between EPG neurons (columns, gray), sorted by angle in the ellipsoid body, and ER4d neurons (rows, purple), sorted by the azimuthal angle of their visual receptive field, are shown. Strong synapses are indicated by large circles, and weak synapses are indicated by small circles. The active EPG (red) and ER4d (cyan) neurons are highlighted. The diagonal location of the trough of weak synapses determines the bump-cue offset.

c) EPG bump movement lags changes in behavior. Correlation coefficient between the movement of the EPG bump (change in PVA angle) and the change in heading in VR as a function of the shift applied to the heading timeseries. Correlation peaks at a lag of 200 milliseconds (dotted line).

d) Change in PVA angle (bump velocity) plotted as a function of change in heading (fly rotational velocity) for closed loop and dark sessions. EPG timeseries is shifted by 200 milliseconds to maximize correlation.

e) PVA magnitude as a function of rotational speed for closed loop and dark sessions. For panels c-e, data is plotted as mean ± sem across flies.

f-g) Additional example fly imaging data as in Fig. 1g-h

Download figureOpen in new tab
Figure 1.
Evidence for presynaptic coincidence detection

a) Top: EPG neuron arbors innervate wedges around the EB that encode the fly’s head direction (HD) angle. Bottom: Visual information is relayed from the eye through the Bulb (Bu) and into the ellipsoid body (EB).

b) Visual information is carried by GABAergic ER neurons (purple) with synapses onto every EPG wedge (gray). To associate visual cues with changes in head direction, synapses between coactive ER and EPG neurons are thought to undergo depression (teal). Such a learning rule requires coincidence detection at this GABAergic synapse which could occur if active EPGs send an unknown retrograde signal to ER axons.

c) Schematic of how ER-EPG plasticity enables the bump of activity in EPGs to accurately track visual cues. As a fly makes a counter-clockwise turn (top to bottom) it will view visual cues (e.g. the sun) from a new angle and the EPG activity bump (red) will swing clockwise around the network by integrating self motion signals with these visual inputs. When the fly faces a different angle, distinct visual ER neurons are active. Plasticity forms a trough of weak synapses (large circles - strong synapses, small circles - weak synapses) that allow ER neurons with distinct visual tuning to move the EPG bump via disinhibition.

d) The relationship (offset) between a visual cue angle and the angle of EPG activity bump is arbitrary across flies and determined by ER-EPG plasticity.

e) Neural activity is monitored using a 2P microscope while a head-fixed fly walks on an air-cushioned ball in a VR arena. The angle of a blue bar serves as an orienting landmark which tracks the ball yaw angle.

f) EPG head direction activity is calculated as the population vector average (PVA) from all ellipsoid body angles weighted by their fluorescence intensity. Bump-cue offset is calculated as the difference between the PVA angle in the brain and the cue angle in VR.

g) Left: Example EPG imaging data from a single fly that first walked with an orienting visual cue (closed loop 1, top), then in darkness (middle), then with a visual cue again (closed loop 2, bottom). Heatmaps display EPG activity unwrapped by ellipsoid body angle from the first 3 minutes of each 6-minute session. Orange points indicate the cue angle or ball angle. Carets highlight how bump-cue offsets are relatively constant throughout closed loop sessions (gray) and vary dramatically in the dark session (purple). Right: Histogram of bump-cue offset across the entire session. The average offset vector length quantifies offset consistency. The orange line denotes an offset of 0 radians.

h) Average bump-cue offset vectors from [g] in polar coordinates.

i) Offsets are more consistent in closed loop vs dark sessions. Each dot is the length of the average bump-cue offset vector for a single fly in darkness or closed loop sessions.

Lines connect data from the same fly. Wilcoxon signed-rank W=0, p=1.22⃗10-4 Mean bump-cue offsets across the two closed loop sessions. Lines connect data points from the same fly.

j) Absolute difference in bump-cue offset between closed loop 1 and 2 for each fly. Thick line indicates average across flies. Bump-cue offsets are maintained across the dark period (Wilcoxon signed-rank test for difference from π/2 W=0, p=9.79⃗10-4)

k) Left: Schematic of imaging from ER axons expressing a GRAB indicator Right: Example GRAB-DA2m imaging data from ER axon terminals. Cue angle and fly rotational speed are shown below.

l) Same as [l] for GRAB-OA1 imaging from ER terminals

m) GRAB-OA1 but not GRAB-DA2m shows a bump of activity that encodes head direction. Each row in the heatmaps shows the temporal average of data from one fly, where each frame was shifted to align with a cross-validated fluorescence peak (left: GRAB-DA2m, middle: GRAB-OA1, right: across fly average, blue-GRAB-DA2m, green-GRAB-OA1). Shaded regions show +/- sem.

n) PVA magnitude quantifies the bump amplitude of GRAB-OA1 (green) and GRAB-DA2m (blue) plotted across rotational speeds (closed loop data only). Mixed effects ANOVA on log-transformed values, GRAB sensor main effect: F=32.3, p=1.22⃗10-5.

o) Lengths of average bump-cue offset vectors are larger in closed loop sessions for GRAB-OA1 but not GRAB-DA2m. Same as (j) for GRAB-DA2m (left) and GRAB-OA1 (right). Mixed effects ANOVA on logit-transformed values, GRAB sensor main effect: F=32.7 p=1.6⃗10-5, closed loop vs dark main effect: F=7.75 p=0.012. Interaction: F=19.7 p=2.81⃗10-5. Posthoc tests for difference between dark and closed loop (holm-corrected p values): GRAB-DA2m t=1.58 p=0.149, GRAB-OA1 t=4.46 p=0.002. Posthoc test for difference between GRAB-DA2m and GRAB-OA1 closed loop: t=6.58, p=2.68⃗10-6.

Anchoring to external sensory cues such as distal visual landmarks is crucial for head direction cells to maintain an accurate sense of direction6,7. Such cues can strongly influence head direction representations and correct for errors that accumulate from integrating self-movement signals over time. Indeed, when environments lack external cues, such as in darkness, the head direction representation drifts relative to the animal’s orientation3,8–13.

What are the mechanisms by which external sensory cues calibrate head direction cells? Classic models propose associative synaptic plasticity between sensory inputs and head direction neurons14,15, and in Drosophila there is considerable evidence that an associative process tethers the head direction representation to visual cues16,17 (Fig. 1c, Extended Data Fig. 1b). Yet, the core synaptic mechanisms underlying plasticity between sensory neurons and head direction cells is not known in any organism. We took advantage of the compact and highly organized head direction circuit in Drosophila to uncover the key components of plasticity between visual inputs and head direction neurons.

To identify the mechanism of visual synaptic plasticity we focused on the canonical head direction cells, EPG neurons, and their visual inputs. EPGs arborize in wedges around a donut-shaped midline structure called the ellipsoid body where adjacent wedges encode adjacent angles of head direction (Fig. 1a). As the fly turns, a single “bump” of increased neural activity swings around the donut like the needle of a compass (Fig. 1c). External sensory cues that serve as landmarks enter this network via a large population of inhibitory neurons called ER neurons (also known as ring neurons, Fig. 1b) with different ER neuron subtypes encoding distinct external cues such as visual features (ER4d, ER2a-d, and likely some ER3 subtypes), linear polarization (ER4m and likely ER5 and ER3w), and wind direction (ER1 and ER3a)18–23. Each sensory ER neuron releases γ-Aminobutyric acid (GABA) from a ring-shaped axon that synapses onto every EPG cell creating all-to-all connectivity between sensory inputs and head direction cells24–31. In this work, we focus on visual ER neurons, which have local receptive fields that tile the fly’s field of view20,22.

Associative plasticity of ER→EPG synapses is proposed to flexibly link the head direction representation to visual cues (Fig. 1b,c). Prior work suggests that synapses between co-active ER neurons and EPG cells depress (Fig. 1b,c, Extended Data Fig. 1a,b)16,17. As a result of this plasticity, recurring experience of a visual cue at a particular position on the retina reliably disinhibits the same subset of EPG neurons. This pushes the EPG bump to the same location in the ellipsoid body for each corresponding azimuthal location of the cue, resulting in head direction activity that is robustly anchored to the fly’s current visual surroundings (Fig. 1c).

Explicitly, when a fly encounters a novel environment, visual synaptic weights are predicted to be uninformative and the head direction circuit’s orientation estimate relies solely on error-prone integration of self-movement signals. Through exploration, visual synapses become sculpted, allowing the network to error-correct using visual cues32,33. Indeed, the relationship between visual cues and the EPG head direction representation is not hard-wired, suggesting it forms de novo in each environment3,16 (Fig. 1d, Extended Data Fig. 1b). Optogenetic pairing or disorienting visual experience can also induce changes in the visual-to-EPG mapping, providing evidence that visual tethering is associative16,17,34. Thus, plasticity at the GABAergic synapses between ER and EPG neurons serves as a form of spatial memory that keeps the brain’s internal compass aligned with current surroundings. However, the mechanisms that mediate associative plasticity at this inhibitory synapse are unknown6,35. We discovered that a population of octopaminergic neurons provides feedback from head direction cells (EPG neurons) to their visual presynaptic partners (ER neurons). This octopamine pathway is both necessary and sufficient for plasticity. We propose a model where octopamine instructs plasticity by signaling to presynaptic sensory axons when postsynaptic head direction cells are active, implementing a retrograde signal via a circuit mechanism.

The head direction representation stores its relationship to visual cues

We first established that head direction cells anchor to a visual cue and store this relationship over many minutes in our experimental set-up. We performed two photon (2P) calcium imaging in the ellipsoid body from EPG neurons while a fly walked on an air-cushioned ball in darkness or in virtual reality (VR) with a visual cue (Fig. 1e). In the initial trial, a visual cue tracked the fly’s angular orientation as the fly walked on the ball, simulating a cue at infinity (closed loop 1). We decoded the EPG head direction angle at each timepoint by calculating the population vector average (PVA) using fluorescence values from each ellipsoid body wedge (Fig. 1f, see Methods3). With a visual cue to orient the fly, the EPG activity bump (PVA angle), closely tracked the cue; the angular relationship between the EPG bump and VR cue was consistent over time (see Methods, Fig. 1g-i, Extended Data Fig. 1). To assess the impact of this visual cue on compass tracking, next we had the fly explore in darkness. To quantify tracking consistency in darkness, we compared the offset between the EPG bump and the rotation of the ball (which is the signal used to animate the cue location in closed loop). In darkness, the offset between the bump angle and the fly’s orientation in darkness (bump-ball offset) was highly variable (Fig. 1j)3. Next, we assessed whether the network’s relationship to the visual cue is stored. After the fly explored in darkness for 6 minutes, we returned it to the original VR environment with the same visual cue (closed loop 2). We found that the network’s relationship to the visual cue was stored across this experience (Fig. 1g,h). In the majority of flies, a consistent bump-cue offset was maintained between the first and second exposure to the cue (Fig. 1j,k). A small subset of flies remapped, exhibiting a distinct bump-cue offset on the second closed loop trial. Prior studies observed that the head direction network can recall its relationship with a single visual cue or a complex scene over similar timescales16,36,37. Thus, our data, together with previous work, suggest that the learning mechanism that anchors head direction cells to visual cues can reliably store a visual association for minutes. Moreover, our experiments showing robust recall of the EPG bump-cue offsets following exploration in darkness favors models that require visual experience for synapses to change strength16. Corroborating these results, our data was better fit by computational models in which both synaptic potentiation and synaptic depression require presynaptic activity (Extended Data Fig. 2).

Download figureOpen in new tab
Extended Data Figure 2.
Simulated network dynamics across dark periods

a) Schematic illustrating plasticity model. Active ER-EPG synapses that coincide with the EPG bump depress; other synapses potentiate.

b) Summary of synaptic learning rules under the “presynaptic gating” and “postsynaptic gating” models. Depression conditions highlighted in teal. Potentiation conditions highlighted in orange.

c) Simulated network activity using walking trajectories from behavioral data in Fig. 1g (left-presynaptically gated learning rule, right-postsynaptically gated learning rule)

d) A presynaptically gated learning rule results in smaller changes to bump-cue offsets across dark periods for a range of learning rates. Change in simulated bump-cue offset across the two closed loop sessions using the same walking trajectories as in Fig. 1i-k. Each dot is a single model run using the walking data from a single fly.

e) Dark periods do not affect synaptic structure in presynaptically gated models but abolish synaptic structure in postsynaptically gated models. ER-EPG synaptic strength matrices at the beginning and end of the dark session for the simulations shown in [c].

Presynaptic neuromodulators track locomotion and head direction

To uncover how synaptic plasticity is implemented, we examined candidate pathways that could mediate the detection of coincident activity between presynaptic ER neurons and postsynaptic EPG neurons. Previous results support a plasticity rule where coincident ER and EPG activity triggers synaptic depression of the GABAergic synapse that connects them16,17,38. In mammalian circuits, associative depression at GABAergic synapses often occurs in the presynaptic terminal and requires a retrograde signal from the postsynaptic cell39. This retrograde signal is then bound by receptors on the presynapse and coincidence between this signal and presynaptic activity induces depression40–42 (but see43). It is unlikely that a direct analog to this retrograde signaling mechanism exists at ER-EPG synapses. Flies do not have direct homologs for common retrograde pathways such as endocannabinoid signaling or BDNF/Trk-B44–46 and, enzymes for gaseous retrograde transmitters47–52 are not highly expressed in EPG neurons29 (Extended Data Fig. 3a). However, inspired by studies of plasticity in other circuits53–55, we wondered whether a monoamine released by a third neuron onto presynaptic terminals could function like a retrograde signal. A monoaminergic signal that conveys postsynaptic activity to the presynaptic terminal would exhibit a highly local release pattern that closely tracks the EPG head direction activity. We focused on two monoamines: dopamine and octopamine. We chose dopamine because previous work suggests that dopamine regulates head direction plasticity38. We also explored octopamine, a common invertebrate neuromodulator that is similar to norepinephrine, because of recent reports of a putative octopaminergic cell type with arbors that tile the ellipsoid body in a similar pattern to EPG cells25,28,56. Furthermore, RNA sequencing and receptor knock-in studies suggest that visual ER neurons express dopamine and octopamine receptors29,57–60, a finding we confirmed using expansion-assisted fluorescent in situ hybridization (EASI–FISH)61 (Extended Data Fig. 3b,c).

Download figureOpen in new tab
Extended Data Figure 3.
mRNA transcript levels for retrograde signals and monoamine receptors in EPG and ER4d neurons

a) Analysis of RNA sequencing data from a previously published dataset of EPG and ER4d neurons29 showing genes related to potential retrograde signaling molecules. Enzymes for gaseous transmitter production: nitrous oxide (NO), hydrogen sulfide (H2S) and carbon monoxide (CO). Peptides with potential retrograde signaling functions are also listed. Log FPKM values from each cell type with a whole brain reference. EPG data shows multiple replicates from bulk sequencing. ER4d data is averaged low cell sequencing values.

b) Monoaminergic receptors RNA transcripts from EPG, ER4d, and whole brain as in [a].

c) Example images from EASI-FISH showing octopamine receptor mRNA transcripts in ER4d somata (anti-GFP-green, RNA-magenta, DAPI-cyan, see Methods). Images are partial z-stack maximum intensity projections through example cell bodies. Octα2R and Octβ3R data are from different channels in the same field of view. Scale bars are 10 μm.

To assess whether dopamine or octopamine signals head direction information onto ER presynaptic terminals, we measured the release patterns of these monoamines using the fluorescent dopamine sensor, GRAB-DA2m62, and, separately, the fluorescent octopamine sensor, GRAB-OA1.063. We expressed either sensor in ER neurons using a split-Gal4 driver line we developed that strongly and specifically labels a large population of these cells (Extended Data Fig. 4). We then performed 2P imaging of ER neuron axons in the ellipsoid body while the fly walked in VR.

Download figureOpen in new tab
Extended Data Figure 4.
Characterization of ER split-Gal4 driver line.

a-e) Adult brains with mCD8::GFP expression (anti-GFP, green) driven by the ER neuron split Gal4 (R56H10-p65.AD {VK00027}, R20A02-DBD {attp2}) with Bruchpilot staining (nc82, grey). Confocal images are partial Z-stack maximum intensity projections. Expression in the central brain is largely restricted to ER neurons. A small number of neurons are labeled in the superior protocerebrum, optic lobe, and ventral nerve cord.

a) Anterior brain

b) Posterior brain

c) Optic lobe

d-e) Ventral nerve cord

We observed that dopamine (GRAB-DA2m) signaling was distributed globally across the ER axons. Bursts of dopamine release were relatively uniform across the entire ellipsoid body and peaked when the fly made rapid turns (Fig. 1l, Extended Data Fig. 5). Each of the four dopamine neurons in this region, called ExR2 cells, have arbors that span the full ellipsoid body. These imaging data therefore suggest that dopamine release from ExR2 axons is not compartmentalized. These data are also consistent with calcium imaging measurements showing that ExR2 activity is locked to the fly’s rotational speed38,64.

Download figureOpen in new tab
Extended Data Figure 5.
Schematics and further analyses of GRAB sensor imaging

a-b) Illustration of analysis in Fig. 1n.

a) Top: Example 6-minute ER>GRAB-OA1 closed loop imaging session for an additional example fly. Middle: Each column in the heatmap is circularly shifted such that heading makes a straight line. Bottom left: For the first half of the imaging session, a temporal average is taken from the heading-aligned data. The spatial shift required to center the peak of that average trace is then calculated. Bottom right: The shift is applied to the temporal average of the second half of the data, resulting in a cross-validated centering of the activity bump.

b) Same as [a] for the example ER>GRAB-DA2m session in Fig. 1l. Note that there is no clear bump of activity.

c) Same as Fig. 1o but for dark sessions. Mixed effects ANOVA on log-transformed values: GRAB sensor main effect: F=10.6, p=0.004.

d) Whole ellipsoid body GRAB fluorescence as a function of flies’ rotational speed. GRAB-DA2m fluorescence (blue) shows a larger increase as a function of rotational speed than GRAB-OA1 fluorescence (green) in both closed loop (left) and dark sessions (right). Mixed effects ANOVA on log-transformed values: closed-loop - GRAB sensor main effect F=10.6 p=0.005; dark - GRAB sensor main effect F=5.07 p=0.048.

In contrast, octopamine signaling was highly localized and tracked the fly’s head direction in VR (Fig. 1m). To visualize head direction tracking, we first aligned all timepoints by the heading of the fly. We then averaged the first half of the data over time and found the phase of the largest peak in fluorescence (see Methods, Extended Data Fig. 5). That phase was then used to shift held-out imaging data to align the peaks across flies (Fig. 1n, Extended Data Fig. 5). For octopamine, this cross-validated analysis revealed a peak that was consistent across flies (Fig. 1n), indicating that octopamine release tracks flies’ head direction. When we performed the same analysis on dopamine, we found no evidence that dopamine tracks heading as the heading-aligned data showed a uniform activity profile (Fig. 1n). Quantitatively, the GRAB-OA1 bump magnitude (PVA magnitude, see Methods) was significantly larger than the GRAB-DA2m bump magnitude (Fig. 1o). The GRAB-OA1 bump magnitude also increased further when the fly walked with high rotational speed, similar to observations of EPG population activity (Extended Data Fig. 1 & 5)3,8,9,38,65. In addition, the bump-cue offsets were more consistent in closed loop trials than darkness trials for GRAB-OA1 but not for GRAB-DA2m (Fig. 1p). In summary, we find that dopamine signaling in the ellipsoid body is global, suggesting it does not signal head direction information to ER presynaptic terminals. Global motor-locked dopamine is well positioned, however, to modulate plasticity at times when the fly makes rapid turns (Extended Data Fig. 5)34,38,64. On the other hand, octopamine signaling tracks head direction and is a strong candidate to convey EPG activity onto ER terminals for coincidence detection.

EL neurons are octopaminergic and carry head direction activity

To identify the octopaminergic neurons that relay head direction information onto local sections of visual ER neuron axons we analyzed RNA expression levels and connectomic data (Fig. 2a). Recent work identified EL neurons, a columnar cell type that tiles wedges of the ellipsoid body and expresses the enzymes required for octopamine biogenesis25,28. We used two split-Gal4 driver lines that label EL neurons to confirm the neurotransmitter identity of these cells. Using RNA sequencing and FISH we confirmed that EL neurons are enriched for RNAs that encode enzymes necessary for octopamine production and vesicle loading (tyrosine decarboxylase-2: Tdc2, tyramine beta-hydroxylase: TβH, & vesicular monoamine transporter: VMAT) and found no evidence that EL co-produces any other fast neurotransmitter (Fig. 2b, Extended Data Fig. 6).

Download figureOpen in new tab
Extended Data Figure 6.
Characterization of EL and ExR2 transmitter, receptor, peptides, and channel expression

a) FISH showing TβH RNA in EL neurons. Top: EL Line 1 (flylight number SS00027, see Methods for full genotype) SNAP tag expression (greyscale). Middle: TβH RNA (green). Bottom: Merged. All EL somata are double labeled.

b) Select results from bulk RNA sequencing of EL Line 1 (SS00027), EL Line 2 (SS50573), ExR2 Line 1 (SS704424) and ExR2 Line 2 (MB233B). Log CPM values are shown for all replicates and a whole brain reference.

c) Whole-cell current-clamp recording from an EL neuron demonstrating that EL neurons are intrinsically capable of generating action potentials. Putative action potentials are annotated with tick marks.

Download figureOpen in new tab
Figure 2.
EL neurons are octopaminergic and carry head direction activity

a) Each EL neuron (green) innervates a slice of the ellipsoid body, forming a feedback loop that relays activity from the EPG bump (red) to segments of visual ER axons (purple).

b) Bulk RNA sequencing shows EL neurons express mRNA for enzymes necessary for octopamine (OA) synthesis and vesicular packaging, but no other neurotransmitters. Heatmap shows average log counts per million (CPM) across replicates for two different EL split-Gal4 lines and a whole brain reference.

c) Synapse counts between visual ER neurons (ER2 and ER4d), EPG neurons, and EL neurons from Hemibrain connectome 24,116. Numbers in circles indicate the number of neurons in each class. Arrow width indicates synapse counts (also shown numerically).

d) EL neurons tile the ellipsoid body (grey). EM reconstruction of a single EL neuron (green). The most dense region of presynapses from the highlighted EL neuron are outlined in red (peeled convex hull, see Methods) while other colors indicate presynapse dense regions for the 17 other EL neurons.

e) ER4d neurons receive inputs from every EL neuron around the ellipsoid body. EM reconstruction of a single ER4d neuron (purple) with input synapses from EL neurons are colored according to EL neuron identity as in [d].

f) EL-ER synapses are intermingled with ER-EPG synapses. Top: EM reconstructions of example interconnected ER4d (purple), EPG (black) and EL (green) neurons. Bottom: Close up of the ER4d axon segmented with EL synaptic inputs shown in green and EPG synaptic outputs in black.

g) Histogram of the cable distance through the ER neuron (ER2 & ER4d) arbors from each ER-EPG synapse to the closest modulatory (EL-ER) contact (green). For analysis of all ER subtypes see Extended Data Fig. 7. For comparison, cable distances through γ-kenyon cell (KC) arbors between each γ-KC-mushroom body output neuron (MBON) synapse and the closest modulatory (dopamine neuron [DAN]-γKC) synapse is shown in black.

h) Example closed loop VR dual imaging session EPG (top) and EL (bottom). Plotted as in Fig. 1g.

i) EL and EPG activity bumps have similar phases. Average absolute differences in bump angle (PVA angle) are plotted for each fly for dark and closed loop sessions. Differences are significantly less than chance (π/2) in both conditions by Wilcoxon signed-rank test. holm-corrected p-values: dark W=0 p=9.77⃗10-4, closed loop W=0 p=9.77⃗10-4. One wedge is defined as the average angular span of a single EPG dendritic arbor.

Download figureOpen in new tab
Extended Data Figure 7.
Analysis of the Hemibrain connectome exploring input and output connectivity of EL and ExR2

a) All synaptic inputs to EL and ExR2 neurons with at least 3 synapses. Synapse counts are scaled to show proportion of EL and ExR2 postsynapses to account for differences in total synapse number between the two populations.

b) All synaptic outputs from EL and ExR2 neurons with at least 3 synapses. Counts are normalized to proportions of presynapses.

c) EL provides the largest source of columnar neuron feedback onto ER neurons. EL provides the strongest feedback onto ER4d and ER3p neurons. Left: Synapse counts between presynaptic columnar neurons (ExR2 also included) and postsynaptic sensory ER neuron subtypes. Right: Summed synapse counts across all ER neurons. EL overwhelmingly makes the most synapses onto ER neurons. Note that polarized light encoding ER4m neurons receive stronger EPG input than EL input which likely represents a special case. Mechanosensory coding ER1 neurons also receive relatively strong PENa input.

d) EL neurons have regions of their arbors in the ellipsoid body with distinct synaptic partners. Reconstruction of a single EL neuron (left) with overlaid synapse locations from its strongest inputs (ER5-cyan, EPG and PENa-black) and its strongest ER neuron outputs (ER4d, ER3p and ER2-purple).

e) Density of synapse locations for top inputs and output shown for all EL neurons. Each EL neuron’s arbor is projected along the ring onto a single wedge (see Methods). ER5 inputs in cyan, EPG & PENa inputs in black. ER4d, ER3p and ER2 outputs are shown in purple.

f) Cable distance from ER-EPG presynapses to EL-ER postsynapses (green, same as Fig. 2f) and for comparison the same analysis for ExR2 is shown in blue with cable distance from ER-EPG presynapses to ExR2-ER postsynapses.

g) Left- Cable distance analysis from f (and Fig. 2g) was repeated for different ER neuron subtypes and shown here as a cumulative histogram. EL contacts are particularly close to ER3p-EPG synapses and ER4d-EPG synapses. Right- Cable distance analysis for ExR2, cumulative histogram shows distance from ER-EPG synapses to closest ExR2-ER synapse for different ER neuron subtypes.

h) EL neurons pool inputs from multiple EPG neurons. The number of EPG presynaptic partners with greater than 10 synapses for each EL neuron.

i) Strip chart showing the number of EL neuron synaptic partners with greater than 3 synapses that inputs to each ER neuron subtype. Each dot is one ER neuron instance.

j) Same as in [i] but for PENa (left), PENb (middle) and EPG (right)

We also made several notable observations from RNA sequencing that we do not investigate further in this work. Consistent with a previous report, EL neurons appear to express the peptide SIFamide (Extended Data Fig. 6)28,66. EL neurons also express receptors for dopamine and serotonin, suggesting that octopamine signaling may be regulated by other monoamines. ExR2 neurons, on the other hand, do not express high levels of octopamine or serotonin receptors (Extended Data Fig. 6). Lastly, EL neurons express transcripts encoding voltage-gated sodium channel subunits at high levels, and whole-cell electrophysiological recordings from EL neurons showed that they fire action potentials (Extended Data Fig. 6).

We next used connectomic data24 to show that EL neurons are uniquely positioned to instruct plasticity at ER-EPG synapses. EL neurons receive strong synaptic input from EPGs within the ellipsoid body and, in turn, send the majority of their synaptic outputs to nearby sensory ER neuron axons (Fig. 2c, Extended Data Fig. 7)25. EL neurons make substantially more synapses onto sensory ER neurons than any other columnar cell type (i.e. cell types that tile the ellipsoid body wedges, Extended Data Fig. 7) making them the best candidate to implement a local feedback loop from head direction neurons onto sensory axons (Fig. 2d). For ER terminals to flexibly learn to anchor to the EPG activity bump, ER axons need to receive local feedback about EPG activity in each wedge. Accordingly, visual ER neurons (ER4d, ER2, ER3p subtypes) receive synaptic input either from all EL neurons or nearly all EL neurons (example ER4d-Fig. 2e, Extended Data Fig. 7). Furthermore, we found that EL-ER synapses are in very close proximity to ER-EPG synapses and thus well positioned to modulate their synaptic strength (Fig. 2f,g, Extended Data Fig. 7). For example, in Fig. 2f, we show one ER4d cell (purple), one of its EPG partners (black) and the EL neuron (green) that receives the most synaptic input from that EPG neuron. Octopamine inputs (EL-ER4d synapses) are intermingled with GABA release sites onto head direction cells (ER4d-EPG synapses). For visual ER neurons (ER2a-d and ER4d), we estimate that second messengers from the EL-ER contact would often need to diffuse intracellularly less than 2 μm to reach a given ER-EPG synapse (Fig. 2g). As a notable comparison, in the gamma lobe of the mushroom body, dopamine receptor second messengers need to diffuse a similar distance through kenyon cell axons to drive synaptic plasticity at kenyon cell-mushroom body output neuron synapses (Fig. 2g, Extended Data Fig. 7). Together, our GRAB data, sequencing, and connectomic analyses identify EL neurons as a strong candidate for relaying local EPG activity onto ER neuron terminals. This octopaminergic signal is well positioned to enable coincidence detection that could instruct plasticity of ER-EPG synapses.

To show that EL population activity tracks EPG activity, we performed simultaneous imaging from EL neurons and EPG neurons by using orthogonal genetic driver lines for the two populations (EPG-Gal4 & EL-LexA) to express two spectrally separable calcium indicators (jGCaMP8s and jRGECO1a) (Fig. 2h, see Extended Data Fig. 8 for EL-LexA characterization)67–69. We found that both cell types exhibited a clear bump of neural activity that tracked head direction when the fly walked in VR or in darkness (Fig. 2h,i, Extended Data 9). Importantly, when the activity of both cell types was measured simultaneously, they circled the network together. When the fly walked in VR, the two neural populations had extremely similar bump-cue offsets (Extended Data Fig. 9) and the phases of the EL bump and EPG bump were nearly identical when the fly walked in VR or darkness (mean absolute difference <π/4 Fig. 2i, Extended Data Fig. 9). Significant deviations in EL and EPG bump phases only occur when the amplitude of the bumps (PVA magnitude) is small, indicating that these deviations are likely driven by measurement noise (Extended Data Fig. 9). Examining the dynamics of these populations more closely we found the EL bump slightly leads the EPG bump (Extended Data Fig. 9). This effect is unlikely to be due to differences in indicator dynamics because we observed a similar phase difference in a separate cohort in which we controlled for this confound explicitly (Extended Data Fig. 9d-g). It is somewhat surprising that the EL population leads the EPG population since EL is largely postsynaptic to EPG, but we note that EL also receives input from PENa neurons (Extended Data Fig. 7) that conjunctively encode head direction and rotation velocity and whose population activity leads the EPG bump8,9. Collectively, these data argue that EL neurons release octopamine locally near where head direction activity is highest.

Download figureOpen in new tab
Extended Data Figure 8.
Characterization of EL LexA driver line (R18B05-LexA)

a) EM reconstruction of all EL neurons showing key elements of their anatomy24,116. Cell bodies are near the protocerebral bridge. EL neurons, however, do not arborize in the protocerebral bridge. Their processes tile the wedges of the ellipsoid body and they additionally arborize in the gall surround.

b) Confocal images of an adult brain with mCD8::GFP expression driven by the R18B05-LexA driver line (left: protocerebral bridge, right: ellipsoid body; anti-GFP-green; anti-Bruchpilot/nc82-grey). Images are partial z-stack maximum intensity projections. Scale bars are 40μm. This driver line is specific for EL neurons in the central complex. A small number of unidentified putative ascending neurons are labeled as well.

c) Number of EL neurons labeled by R18B05-LexA per brain. Each dot represents the number of GFP-labeled EL cell bodies from one brain. The green bar shows the mean cells per brain (16.75). Connectomics data suggests there are 17-18 EL neurons per fly brain 24,125,126.

d) MultiColor FlpOut (MCFO) 112 anatomical characterization of the R18B05-LexA driver line. Stochastically labeled example neurons expressing HA-tagged smGFP reporter from two different flies. Left: 2 EL neurons. Right side: 3 EL neurons. Both images are maximum intensity projections from the bulb to the protocerebral bridge.

e) : Pie chart summarizing R18B05-LexA MCFO data. All neurons with arbors in the ellipsoid body were identified as EL neurons. 77.6% of all cells labeled were identified as EL neurons, 22.4% of cells were non-EL, non-columnar neurons, and 0% were non-EL, columnar neurons. Importantly we never identified cells with EPG, PEG, PENa or PENb morphology. N flies = 7, N cells = 49.

Download figureOpen in new tab
Extended Data Figure 9.
Co-imaging of EPG and EL activity with additional indicator combinations

a) Analysis of EL and EPG bump phase during closed loop VR dual imaging session (same data set as in Fig. 2). The EL bump phase slightly leads the EPG bump phase. Data from both EL (green) and EPG (black) is centered by the location of peak EPG activity during rapid counterclockwise (left) or clockwise (right) turns. The direction of bump motion during the turns is indicated by the arrows. Data is plotted as mean ± sem across flies. Inset lines indicate the PVA angle of the plotted data.

b) The difference in EL and EPG bump phase is plotted against the fly’s rotational speed in closed loop (black) or darkness (purple). Inset statistics show Spearman rank correlation. Data is plotted as mean ± sem across flies.

c) Large deviations in EL and EPG bump phase only occur when bump magnitudes are small. The absolute value of the difference in EL and EPG bump phase is plotted against the average EL and EPG bump magnitude in closed loop (black) or darkness (purple). Data is plotted as mean ± sem across flies.

d-e) Example data of simultaneous 2P imaging of EL and EPG during closed loop VR as in Fig. 2 for two additional calcium indicator combinations. For all flies indicators are driven by EL-Gal4 and EPG-LexA. For remaining panels, data from both color combinations are combined.

f) EL and EPG activity bumps have similar phases with these additional indicator combinations. Average absolute differences in bump angle (PVA angle) are plotted for each fly from closed loop sessions. Differences are significantly less than chance (π/2) in both conditions by Wilcoxon signed-rank test: W=0 p=0.002

g) Data as in [a] for flies with indicator combinations shown in [d-e]

h) Data as in b for flies with indicator combinations shown in [d-e]. N=10 flies, 5 for each indicator combination. Spearman rank correlation shown in panel.

Octopaminergic EL neurons are necessary for visual plasticity

We hypothesized that this octopaminergic feedback loop is necessary for visual plasticity. To test this, we disrupted the ability of EL neurons to produce octopamine and measured changes in how the head direction network anchored to a visual cue. First, we used RNA interference (RNAi) to knock-down the octopamine synthesis enzyme TβH in EL neurons and confirmed TβH knockdown largely eliminated octopamine immunolabeling in EL somata (Extended Data Fig. 10a-c), a result that provides additional evidence these cells are octopaminergic. Then, we measured EPG neural activity as these flies walked in VR (Fig. 3a-c). To quantify EPG visual tracking, we compared trials where the fly walked in darkness to trials with a visual cue. As also shown above (Fig. 1g-i), when control genotypes walked in darkness, their EPG bump drifted relative to the fly’s heading in darkness (low vector length), but when the cue was visible the EPG bump accurately tracked the cue angle (high vector length)(Fig. 3b,c). However, when octopamine synthesis was disrupted, EPG tracking of head direction was poor regardless of whether the fly walked in darkness or was given a visual cue (Fig. 3c). Moreover, in flies with reduced EL octopamine, the EPG activity was significantly less tethered to the cue than in either control genotype (Fig. 3c). We also obtained similar results in a parallel set of experiments where we instead used EL population activity to measure bump position. This allowed us to use a more specific EL split-Gal4 driver line for TβH knockdown (Extended Data Fig. 10). Importantly, network deficits caused by disrupting TβH were specific to the bump’s ability to track a visual cue, as the movement of the EPG (or EL) bump still tracked the fly’s angular rotation, as in control genotypes (Extended Data Fig. 10d-e). Thus, when EL neurons lack octopamine, the dynamics of the head direction representation are similar to conditions without visual cues. Our interpretation is that this perturbation disrupts synaptic plasticity between visual inputs and head direction cells.

Download figureOpen in new tab
Extended Data Figure 10.
Additional quantification of the effects of knocking down TβH in EL neurons

a) Confocal images of adult brains showing staining for octopamine alone (anti-octopamine, magenta, left) or merged with EL cell bodies labeled by mCD8::GFP using an EL Split-GAL4 driver line (anti-GFP, green, right). Top: GFP only control. Bottom: TβH RNAi. Images are maximum intensity projections. Scale bars are 40μm. Dotted boxes show insets in [b]

b) Confocal images showing the cell bodies from [a]. Staining for octopamine (anti-octopamine, left), mCD8::GFP (anti-GFP, green, middle), and merged (right). Top: GFP only control. Bottom: TβH RNAi. Images are maximum intensity projections. Scale bars are 20μm.

c) Expressing TβH RNAi in EL neurons decreases octopamine antibody staining intensity. Mean anti-octopamine fluorescence within GFP-labeled EL cell bodies in the control brains (black) versus the TβH knockdown brains (green). Each dot is a single brain (N control = 5 flies, N TβH knockdown = 5 flies). Mann Whitney U=0 p = 0.008

d) PVA magnitude as a function of rotational speed for data in Fig. 3c. Data is plotted as mean ± sem across flies. Kruskal-Wallis test for difference across genotypes: closed loop - H=5.32 p=0.070; dark - H=1.87 p=0.393.

e) Change in PVA angle as a function of rotational velocity for data in Fig. 3c. Data is plotted as mean ± sem across flies. Linear model including genotype and genotype x rotational speed as predictors. Wald test for significant genotype coefficients: F(2,552)=0.985 p=0.374. Wald test for significant genotype x rotational speed interaction: F(2,552)=0.875 p=0.417

f-i) TβH RNAi experiments were repeated using a more specific EL-split Gal4 line while also imaging calcium from EL neurons. In addition to an EL-Gal4 only control we performed RNAi against the vesicular glutamate transporter (VGluT), a required protein for vesicular packaging of glutamate. This condition serves as an additional control for nonspecific effects of RNAi.

f) Example data from closed loop imaging sessions from each genotype as in Fig. 3b.

g) Average offset vector lengths for each genotype. Mixed effect ANOVA on logit transformed vector lengths: main effect of genotype: F=15.43 p=2.73×10-5, main effect of dark vs closed loop: F=58.0 p=2.13×10-8, interaction: F=14.5 p=4.42×10-5. Posthoc paired t-tests for dark vs closed loop (p-values holm corrected): Gal4 only control: t=5.60 p=6.69×10-4, EL-Gal4>VGluT-RNAi: t=8.25 p=2.70×10-5, EL-Gal4>TβH-RNAi: t=0.122 p=0.905. Posthoc unpaired t-test for difference in closed loop vector length between genotypes (p-values holm corrected): EL-Gal4 only vs EL-Gal4>VGluT-RNAi: t=1.39 p=0.723, EL-Gal4 only vs EL-Gal4>TβH-RNAi: t=6.39 p=1.97×10-5, EL-Gal4>VGluT-RNAi vs EL-Gal4>TβH-RNAi: t=8.73 p=1.77×10-7.

h) PVA magnitude as a function of rotational speed. Kruskal-Wallis test for difference across genotypes H=8.06 p=0.018. Posthoc Mann-Whitney U (p-values holm corrected): EL-Gal4 only vs EL-Gal4>VGluT-RNAi: U=56 p=0.971, EL-Gal4 only vs EL-Gal4>TβH-RNAi: U=90 p=0.045, EL-Gal4>VGluT-RNAi vs EL-Gal4>TβH-RNAi: U=97 p=0.045

i) Change in PVA angle vs rotational speed. Linear model including genotype and genotype x rotational speed as predictors. Wald test for significant genotype coefficients: F=0.044 p=0.967. Wald test for significant genotype x rotational speed interaction: F=1.54 p=0.215.

Download figureOpen in new tab
Figure 3.
Octopaminergic EL neurons are necessary for visual plasticity

a) Schematic showing final step of octopamine synthesis pathway.

b) Example EPG imaging data in closed loop from a control fly (top: TβH-RNAi only) and experimental fly with TβH-RNAi expressed in EL neurons (bottom: EL-Gal4>TβH-RNAi). Data plotted as in Fig. 1g.

c) EL TβH-RNAi prevents the EPG bump from learning a visual scene. Lengths of average bump-cue offset vectors are plotted as in Fig. 1i. Vector lengths are not different between darkness and closed loop when flies lack octopamine in EL neurons. Mixed effects ANOVA on logit-transformed vector lengths: main effect of genotype F=9.64 p=7.37⃗10-5; main effect of dark vs closed loop F=37.6 p=1.76⃗10-6; interaction F=8.11 p=0.002. Posthoc comparisons (p-values holm corrected): darkness vs closed loop - TβH-RNAi only: t=4.24 p=0.004 EL-Gal4 only: t=5.95 p=6.49×10-4 EL-Gal4>TβH-RNAi: t=0.086 p=0.933. Closed loop comparisons (independent t-tests, p-values holm-corrected): TβH-RNAi only vs EL-Gal4 only: t=1.10 p=0.285, TβH-RNAi only vs EL-Gal4>TβH-RNAi: t=7.07 p=1.87×10-6, EL-Gal4 only vs. EL-Gal4>TβH-RNAi: t=5.21 p=7.07×10-5.

d) Schematic of simultaneous 2P imaging and 2P optogenetics. Flies walk in VR while two independent light paths are used for imaging (920 nm, resonant-galvo) and optogenetics (1064 nm, galvo-galvo).

e) In the experiment a subset of ER neurons are activated by the visual cue. EPG activity is measured using GCaMP, and they are depolarized using CsChrimson. HcKCR1 is used to hyperpolarize EL neurons.

f) In the optogenetic plasticity protocol, first flies walk in closed loop VR to measure the baseline EPG bump-cue offset (top left). Then a new bump-cue offset is entrained by pairing visual cue presentations with focal 2P optogenetics (opto-pairing, π offset shown in example). The bump-cue offset is measured again after 2P entrainment (post-pairing, top right).

g) Example data showing successful EPG bump-cue plasticity induction in a fly with EPG stimulation but no EL inhibition. Imaging data as shown previously (top-baseline, middle-post π pairing, bottom-post 0 pairing).

h) Example fly with EPG stimulation and EL inhibition showing no opto-pairing induced plasticity and instead a stable EPG bump-cue offset throughout (top-baseline, middle-post π pairing, bottom-post 0 pairing).

i) Average bump-cue offset vectors for example shown in [g](left) and all control flies (right).

j) Same as [i] for flies with EL inhibition

k) EL inhibition with HcKCR1 prevents optogenetically induced plasticity. Average remapping error for each fly. Lines show mean across flies. Wilcoxon signed-rank test for difference from π/2 (holm-corrected p-values): EL-Gal4 only: W=1 p=9.77×10-4, EL-Gal4>HcKCR1: W=34 p=0.455. Mann-Whitney U EL-Gal4 only vs EL-Gal4>HcKCR1: U=12 p=2.22×10-4.

The data so far supports a model in which EL neurons release octopamine onto visual ER presynaptic terminals allowing visual information and the head direction representation to be associated. That is, if an ER neuron terminal is active and also receives octopamine, then that local axon segment has detected coincident ER-EPG activity, and nearby synapses could undergo depression (Fig. 1b). However, our constitutive knockdown experiments (RNAi) cannot distinguish between the acute role of octopamine for plasticity induction and its requirement to establish or maintain synaptic function. To test whether EL activity is required during plasticity induction we combined acute EL silencing (HcKCR1)70 with a previously established optogenetic plasticity protocol16. In this experiment, EPG neurons express CsChrimson and focal 2P optogenetics is used to generate bump activity at experimentally defined locations around the network (Fig. 3d-f, Methods). Using this approach, we could entrain a new arbitrary bump-cue offset in the EPG network (Fig. 3g). For each wedge of the ellipsoid body, we paired localized activation of EPG arbors with the presentation of a visual cue at a consistent bump-cue offset (Fig. 3d-f)16. The optogenetic stimulation is moved through eight stimulation locations around the ellipsoid body and the visual cue is rotated correspondingly to maintain a constant bump-cue offset (Fig. 3f). Before and after this pairing protocol, we monitored EPG activity to assess each fly’s baseline bump-cue offset, and to measure changes to the network’s visual tethering following pairing. Each fly underwent two rounds of plasticity induction (0 radians and π radians in pseudorandom order) so that changes in bump-cue offset due to plasticity could be easily distinguished from random fluctuations in bump-cue offset or preexisting differences at baseline. This plasticity protocol robustly induced changes to the bump-cue offset that were aligned to the phase offset reinforced during pairing (Fig. 3g,i, Extended Data Fig. 11).

Download figureOpen in new tab
Extended Data Figure 11.
Validation of optogenetic approach to stimulating EPG neurons while silencing EL neurons

Panels in this figure pertain to data included in Fig. 3d-k.

a) Adult brain with HcKCR1::V5 expression (anti-V5, gray) driven by the EL split Gal4. Confocal images are partial Z-stack maximum intensity projections of the posterior brain (left), ellipsoid body (middle), and cell bodies (right). Scale bars are 40μm. Note that there may be trafficking issues or toxicity of HcKCR1 as we see what is likely lysosomal buildup in the cell bodies.

b) Representative current-clamp trace from an HcKCR1-expressing EL neuron in response to 10 pulses of 100 ms LED stimulation (620 nm; orange bar) delivered at 5-second intervals. Individual responses from three LED pulses are shown in gray; the black trace is the trial-averaged voltage response from all 10 pulses.

c) Summary of the peak light-evoked hyperpolarization (Δvoltage) in EL neurons expressing HcKCR1 (green) versus GFP-only controls (gray). Each dot represents the mean response from a single cell, and lines indicate group averages. HcKCR1 positive neurons show significantly greater hyperpolarization (Mann–Whitney U test HcKCR1 (n=5) vs. control (n=6): U = 0.0, p=0.0015).

d) EPG response to optogenetic stimulation during pairing protocol. The across-fly average z-scored fluorescence in the 200 milliseconds following the optogenetic stimulation is shown for every ellipsoid body wedge (rows) at each stimulation location (columns). Orange dots show the location of the visual cue during optogenetic stimulation. The 0 radian (left-red colormap) and π radian (middle-blue colormap) pairings are shown separately as well as the combined responses regardless of the location of the visual cue (right-greyscale colormap). Top: EL-Gal4 only control. Bottom: EL-Gal4>HcKCR1

e) Average EPG response to optogenetic stimulation combined across stimulation locations. Each column in [d] is shifted to align the locations of stimulation. Data is plotted as across fly mean ± sem.

f) Average offset vector lengths for all baseline and post pairing sessions. Each dot represents the vector length from one session from a single fly. Lines indicate across fly means.

g) EPG bump-cue offsets for baseline and post pairing sessions. Each dot represents data from a single session. Lines connect data from the same fly.

Our hypothesis is that pairing EPG stimulation with a visual cue drives plasticity because focally activating EPG cells also recruits EL neurons innervating the same angle in the ellipsoid body. To test this directly we silenced EL neurons during plasticity induction using the potassium-selective inhibitory opsin (HcKCR1)70. First, we generated transgenic flies to express HcKCR1 with an epitope tag (V5) and used immunostaining to confirm that HcKCR1-V5 is well expressed by EL neurons (Extended Data Fig. 11). In a separate validation experiment, we also confirmed using electrophysiological recordings that photostimulation of HcKCR1 robustly hyperpolarizes EL neurons (Extended Data Fig. 11b,c). HcKCR1 has a similar 2P absorption to CsChrimson, which allowed us to use the same laser (1064 nm) to both locally activate EPG neurons using CsChrimson and to locally silence EL neurons using HcKCR1 (Fig. 3d,e, Methods). Thus, in this experiment, optogenetic photostimulation simultaneously activates EPG neurons and hyperpolarizes EL neurons in the same location. We found that acutely silencing EL neurons in this manner completely disrupted optogenetically-induced plasticity (Fig. 3h,j,k). Notably, flies with HcKCR1 expressed in EL neurons exhibited an EPG bump that was well tethered to the cue at baseline, showing that visual plasticity is still intact in this genotype (Fig. 3h, Extended Data Fig. 11). However, the optogenetic pairing protocol no longer induced new bump-cue offsets, and most flies retained the same bump-cue offset as the baseline session across the full plasticity protocol (Fig. 3h, j, Extended Data Fig. 11g). We quantified the effectiveness of optogenetic pairing by measuring the average angular error between the entrained bump-cue offset during optogenetic pairing and the offset exhibited afterwards in the post-pairing trial (‘remapping error’). Flies that expressed CsChrimson in EPG neurons without EL silencing had low remapping error, indicating robust plasticity induction, while flies that expressed HcKCR1 in EL neurons showed no evidence of plasticity and thus a high remapping error (Fig. 3k, Extended Data Fig. 11). EL silencing led to an average remapping error of around π/2 which is what we would expect if there were no plasticity and the bump-cue offset stayed unchanged across the two optogenetic pairing bouts (Extended Data Fig. 11g).

One explanation for this result is that EL silencing abolished our ability to optogenetically generate a bump in the EPG population. However, we could robustly move the EPG bump in this genotype (Extended Fig. 11d-e), which favors the interpretation that plasticity requires local EL activity at the position of the EPG bump. When EL neurons at that location are silenced during induction, plasticity does not occur, and the network retains its previously learned relationship to the visual cue. In summary, EL octopamine release, and more specifically, the activity of EL neurons at the location of peak EPG activity is necessary for the head direction network to learn a new association with a visual cue.

Localized EL activity and visual experience alone are sufficient for plasticity

We next sought to find the minimal circuit conditions that can elicit plasticity. We hypothesized that octopamine release onto ER terminals acts as the proximal signal for plasticity, which predicts that we should be able to bypass EPG activity by directly stimulating EL neurons to drive plasticity. To do this, we modified our optogenetic plasticity protocol by replacing EPG>CsChrimson activation with EL>CsChrimson activation. This new plasticity protocol was also successful in instructing new EPG bump-cue offsets by pairing EL stimulation with a visual cue (Fig. 4a-d). Importantly, optogenetically stimulating EL neurons without a visual cue did not systematically shift EPG bump-cue offsets (Fig. 4d). Additionally, when we repeated the same pairing protocol in a control genotype with no CsChrimson expression, EPG bump-cue offsets did not change (Fig. 4d) showing that laser induced heating of the tissue does not cause this effect. Therefore, this EL-induced plasticity is associative exactly like EPG-driven plasticity16; changes in bump-cue offset required the simultaneous presentation of a visual cue and EL optogenetic stimulation. In separate experiments in which we imaged EL, instead of EPG, and also optogenetically stimulated EL, we confirmed that the EL activity bump moves to the location of optogenetic stimulation and that the EL bump-cue offset is also plastic, consistent with EL carrying a copy of columnar neuron activity (Extended Data Fig. 12). Thus, pairing EL stimulation with a visual cue is sufficient to drive plasticity that changes how multiple head direction cell types tether to visual cues.

Download figureOpen in new tab
Extended Data Figure 12.
Pairing localized EL activation with visual experience drives plasticity of EL bump-cue offsets

a) Illustration of optogenetic plasticity strategy as in Fig. 4a, but here EL neurons are simultaneously imaged with GCaMP and stimulated using CsChrimson (EL-split Gal4>jGCaMP7f & CsChrimson).

b) Example imaging data showing successful EL-induced EL bump-cue plasticity. Data as shown in Fig. 1, 3 & 4.

c) Bump-cue offset average vectors for example data in [b] (left) and all flies from this genotype (right).

d) EL bump-cue offsets for baseline and post pairing sessions. Each dot represents data from a single session. Lines connect data from the same fly.

e) Remapping errors as shown previously. Wilcoxon signed-rank test for difference from π/2: W=0 p=0.002.

f) EL response to optogenetic stimulation during pairing protocol as in Extended Data Fig. 11d.

g) Average EL response to optogenetic stimulation combined across stimulation locations as in Extended Data Fig. 11e.

h) Average offset vector lengths for all baseline and post pairing sessions. Each dot represents the vector length from one session from a single fly. Lines indicate across fly means.

Download figureOpen in new tab
Figure 4.
Localized EL activity and visual experience alone are sufficient for plasticity

a) Illustration of optogenetic plasticity strategy as in Fig. 3e, but now EL neurons are stimulated using CsChrimson (EL-LexA>CsChrimson) while EPG neurons are imaged (EPG-Gal4>jGCaMP7f).

b) Example imaging data showing successful EL-induced EPG bump-cue plasticity. Data as shown in Fig. 1 & 3.

c) Average bump-cue offset vectors for example data in [b] (left) and all flies from this genotype (right).

d) EL-induced plasticity is associative. Data as shown in Figure 3k. “n” shows the number of flies. Wilcoxon signed-rank test for difference from π/2 (holm-corrected p-values): EL-LexA>CsChrimson: W=0 p=3.66×10-4, EL-LexA only: W=19 p=1.00, EL-LexA>CsChrimson no visual cue: W=24 p=1.00. Kruskal-Wallis test for differences in experimental conditions: H=23.6 p=7.57×10-6. Posthoc Mann-Whitney U tests (holm-corrected p-values): EL-LexA>CsChrimson vs EL-LexA only: U=0 p=1.65×10-4, EL-LexA>CsChrimson vs EL-LexA>CsChrimson no visual cue: U=0 p=1.41×10-4, EL-LexA only vs EL-LexA>CsChrimson no visual cue: U=52 p=0.596.

e) EL stimulation excites EPGs, and EPG inhibition is effective regardless of EL stimulation. EPG fluorescence in response to optogenetic stimulation, centered on the stimulated wedge (green: EL-LexA>CsChrimson EPG-Gal4>jGCaMP7f, purple: EL-LexA>CsChrimson EPG-Gal4>HcKCR1 & jGCaMP7f).

f) Illustration of plasticity strategy as in [a]. EL neurons are depolarized using CsChrimson while EPG neurons are hyperpolarized using HcKCR1 (EL-LexA>CsChrimson, EPG-Gal4>HcKCR1 & jGCaMP7f)

g) Example data showing successful EL-induced EPG bump-cue plasticity despite EPG inhibition.

h) Average bump-cue offset vectors for example data in [g] (left) and all flies from this genotype (right).

i) EPG depolarization is not required for EL-induced bump-cue offset plasticity and EPG hyperpolarization alone does not induce bump-cue offset plasticity. Remapping errors as shown previously. Wilcoxon signed-rank test for difference from π/2: EL-LexA>CsChrimson EPG-Gal4>HcKCR1: W=0 p=4.88×10-4, EL-LexA only EPG-Gal4>HcKCR1: W=25 p=0.846. Mann-Whitney U test EL-LexA>CsChrimson EPG-Gal4>HcKCR1 vs EL-LexA only EPG-Gal4>HcKCR1: U=0 p=8.73×10-5

j) Schematic of similar plasticity rules in the ellipsoid body (top) and the mushroom body (bottom). The ellipsoid body is linearized. Coincident EL and ER activity drives synaptic depression. EPG activity is not necessary for plasticity. Similarly, in the γ-lobe of the mushroom body, plasticity between KCs and MBONs is driven by the coincident activity of KCs and DANs.

Intriguingly, we noticed that EL optogenetic activation reliably moved the EPG bump to the site of EL stimulation regardless of whether a visual stimulus was present (Fig. 4e, Extended Data Fig. 13a,b). This activation may occur because EPG neurons do have modest transcript levels for octopamine receptors (Extended Data Fig. 3)29. Regardless of the mechanism, this means that the above experiment cannot determine whether EL activation and visually-driven ER activity alone are sufficient for plasticity, as EPG activity was also recruited during optogenetic pairing.

Download figureOpen in new tab
Extended Data Figure 13.
Quantification of the impact of EL activation and validation of optogenetic silencing of EPG neurons with HcKCR1

Panels in this figure pertain to data in Fig. 4.

a,b) Localized optogenetic activation of EL moves the EPG bump (Same as Extended Data Fig. 11d,e for conditions in Fig. 4a-d). Without CsChrimson (EL-LexA> +) there is no bump movement. For the “No visual” control condition with EL-LexA>CsChrimson, only the combined optogenetic response is shown.

c,d) Pairing localized optogenetic activation of EL with visual input changes the bump-cue offset. Same as Extended Data Fig. 11e-g for conditions in Fig. 4a-d. “No CsChrimson” control data is shown in black. “No visual” control data is shown in grey (post no-vis 1 and 2 - closed loop VR imaging sessions that follow optogenetic plasticity induction in which no visual cue was present).

e) Adult brain with HcKCR1::V5 expression (anti-V5, gray) driven by the R60D05-Gal4 driver line. Confocal images are maximum intensity projections of cell bodies (left), ellipsoid body (middle left), and protocerebral bridge (middle right). Right: brain in which EL neurons are also labeled by CsChrimson::tdTomato (anti-dsRed, magenta).

Scale bars are 40μm.

f-i) EPG silencing alone (top & black) suppresses the EPG bump but does not induce changes in bump-cue offset, while EPG silencing during EL optogenetic pairing (bottom & purple) suppresses the EPG bump and displays successful EPG bump-cue plasticity. Same as (a-e) for conditions in Fig. 4f-i

To distinguish between a learning rule for synaptic depression that requires simultaneous activity of ER, EPG and EL neurons (three-factor) and a rule that requires only the coactivity of ER and EL neurons (two-factor), we modified our experiment to inhibit EPG neurons, using HcKCR1, while simultaneously activating EL neurons with CsChrimson and activating ER neurons using a visual cue (Fig. 4f). First, we confirmed that photostimulating HcKCR1 suppresses EPG activity at the site where EL neurons are activated by CsChrimson (Fig. 4e, Extended Data Fig. 13e-i). This allowed us to repeat the optogenetic experiment, now testing whether EPG activity is dispensable for optogenetically induced plasticity. Pairing visual stimuli with simultaneous EL stimulation during EPG inhibition robustly drove plasticity (Fig. 4g,h). The enforced changes in EPG bump-cue offsets were consistently observed (Fig. 4h,i) even though EPG neurons were locally silenced during plasticity induction. These results indicate that simultaneous EL and ER neuron activity are together sufficient conditions for inducing plasticity at ER-EPG synapses. In a control experiment, we also confirmed that silencing EPGs without activating EL neurons had no significant effect on visual tethering (Fig. 4i, Extended Data Fig. 13f-i). Thus, plasticity induction can, in principle, be decoupled from the activity of the core head direction neurons. These data support a two-factor learning rule where visual activation of ER neurons simultaneous with EL neuron activity is sufficient to drive plasticity, while EPG depolarization during induction is dispensable.

Discussion

Here we describe a novel motif for synaptic plasticity where coincidence detection at an inhibitory synapse is enabled by activity of a third octopaminergic cell type. This mechanism provides insight into the biological implementation for synaptic learning rules that were proposed for scene learning in head direction circuits over 30 years ago14. Specifically, we propose that ER-EPG synaptic depression occurs when visually-driven ER neuron activity is coincident with octopamine released by EL neurons onto active presynaptic terminals (Fig. 4j). EL neuron activity mirrors local EPG activity which means that ER neurons receive a copy of head direction information via this feedback loop. ER neurons express numerous octopamine receptors (Extended Data Fig. 3)29,57–60, and EL synaptic inputs are adjacent to EPG output synapses, allowing signaling for plasticity induction to be spatially confined within the ellipsoid body. Our data support a model in which ER presynapses undergo depression when their own activity is correlated with octopamine receptor signaling pathways (e.g. cAMP)71,72.

While octopamine has been extensively studied in the Drosophila nervous system it has not been previously implicated in spatial navigation. For example, octopamine has been shown to modulate odor learning by shaping synaptic plasticity in the mushroom body, often by modulating dopamine-dependent plasticity of kenyon cell cholinergic transmission54,63,73 or by changing the sign of spike timing dependent plasticity74. Beyond olfactory learning, octopamine has been found to regulate various physiological processes, including locomotion75, sleep28,76, courtship77, ovulation59, feeding78, and aggression79. Interestingly, at the Drosophila neuromuscular junction octopamine also alters presynaptic function either by acutely modulating glutamate release or by regulating synapse growth during development80,81. These results extend our understanding of the diverse synaptic actions of octopamine to include depression of GABAergic synapses in the central complex.

In this work, we focus on visual plasticity, which is thought to be mediated by ER4d and ER2a-d visual ER neurons. However, EL neurons also provide feedback onto many other ER neuron subtypes (Extended Data Fig. 7), including ER3p and ER3d subtypes that are predicted by connectomics to have localized visual responses22 and may also carry motor information19,82. ER1 neurons that encode wind direction also receive substantial input from EL neurons suggesting that wind and visual input pathways engage similar plasticity mechanisms21,37. Interestingly, EL neurons only rarely synapse onto ER4m neurons that are tuned to the e-vector angle of polarized light18,22 suggesting the association between sky polarization signals and head direction may not be plastic25, or may engage distinct plasticity mechanisms.

It is puzzling that EL neurons carry a copy of EPG activity, when a retrograde molecule could have conveyed the same information. For example, in mammals, endocannabinoids are often released from postsynaptic neurons and drive associative synaptic depression at inhibitory presynapses39. However, decoupling plasticity from postsynaptic network activity may confer computational advantages to this network. First, it could allow plasticity to be regulated without affecting the ongoing network dynamics. For example, EL neurons receive strong inputs from neurons involved in sleep and circadian rhythms (ER5, ExR1) and express dopamine and serotonin receptors suggesting that EL activity, and thus synaptic plasticity, is modulated by fly behavior38,64 and other internal states25,83–85. Another potential advantage of utilizing a third neuron for coincidence detection is to counteract circuit delays. For example, the EPG bump often lags behavior (Extended Data Fig. 1b)8,9. Having EL neurons’ activity precede the EPG activity bump could compensate for differences in timing between movement of the head direction bump and arrival of feedforward sensory inputs17,22. Another potential benefit of a third neuron over a retrograde molecule is to reduce noise. Each EL neuron pools inputs from 6-10 EPG neurons (Extended Data Fig. 7h) meaning that an instructive signal from EL neurons is potentially less noisy than if a retrograde signal was released by each individual EPG neuron. Lastly, signaling via octopamine receptors provides more cell-type and synaptic specificity than a gaseous retrograde transmitter that readily permeates membranes. NO, for example, activates soluble guanylyl cyclases which are expressed in many cell types in addition to ER neurons47,86.

To enable network balance, visual inputs should undergo synaptic depression or synaptic potentiation. Such bidirectional plasticity would allow highly structured visual inputs to emerge robustly with experience16,17,87,88. Our data strongly constrains the learning rule that associates visual cues with head direction activity via depression of ER-EPG synapses. We predict coincident ER activity and octopamine signaling is sensed in the ER axon terminal; however, we cannot fully exclude some contribution from activity-independent GPCR signaling in EPG neurons. In parallel to synaptic depression, potentiation of ER-EPG synapses would serve as the “forgetting” rule for visual-head direction associations. Our results are consistent with two categories of potentiation conditions: 1) Potentiation occurs when ER neurons are visually active without receiving octopamine (pre-synaptic gating)14,16 or 2) potentiation occurs when visual activity and octopaminergic input occur with non-coincident or incorrect timing– similar to time-window based plasticity observed in the fly mushroom body72, hippocampus89,90, and many other systems74,91. Notably, we think potentiation is gated by visual activity because the network’s bump-cue offset is well recalled after prolonged periods in darkness (Fig. 1g,h,j,k) or following interleaved experiences of distinct visual scenes16. In addition, activation of EL neurons in darkness does not reset the network’s relationship to a visual cue (Extended Data Fig. 13a-c). More direct synaptic measurements in future work will be important to determine the exact synaptic algorithm and to uncover how learning is modulated by motor-locked dopamine16,34,38.

To our knowledge, the use of an octopamine neuron as a feedback pathway to implement coincidence detection represents a novel plasticity motif. Our findings highlight how neuromodulation of presynaptic terminals can enable coincidence detection at GABAergic synapses, where postsynaptic induction mechanisms are far less common (but see43). Our experiments suggest that plasticity between ER neurons and EPG neurons is induced presynaptically. This novel motif bears strong resemblance to plasticity mechanisms in other invertebrate circuits where coincident neuromodulatory drive and presynaptic activity changes synaptic strength53,92,93. The similarities between the synaptic mechanisms we have uncovered in the head direction network and plasticity in the γ-lobe of the mushroom body are particularly striking (Fig. 4j). In the mushroom body, synaptic plasticity for odor learning is instructed by dopamine neurons (DANs) that innervate specific compartments of odor-driven kenyon cell axon terminals94–96. Coincident kenyon cell activity and DAN input are necessary and sufficient for depression of synapses between kenyon cells and mushroom body output neurons (MBONs). An important topic for future work will be to uncover whether mechanisms of plasticity expression are also shared between these circuits.

Neuromodulation of presynaptic terminals by monoamines such as dopamine97, serotonin98, and norepinephrine99–101 is also widespread in vertebrates. What distinguishes the synaptic plasticity we have discovered in the ellipsoid body from previous reports is that here the neuromodulatory cell carries a near copy of the postsynaptic neuron’s activity. By contrast, in other systems monoaminergic neurons that instruct plasticity often carry information about valence, novelty, or movement54,102–104. It appears evolution has co-opted a motif that is common in reinforcement-based learning to solve the problem of forming an accurate internal representation of space. Given the widespread expression of G-protein coupled receptors for biogenic amines on presynaptic terminals, we speculate that similar presynaptic neuromodulation motifs could implement diverse learning algorithms in many other circuits.

Our experiments provide insight into the synaptic mechanisms by which head direction circuits anchor their representations to the sensory world. Importantly, recent theoretical work argues that the principles governing unsupervised spatial learning, such as the tethering of head direction cells to landmarks, generalizes to all relational memory105–107. Therefore, the synaptic principles engaged by head direction cells can inform not only spatial learning performed by grid and place cells but also non-spatial relational learning. This work lays a foundation for future investigations into the synaptic and biochemical substrates of unsupervised learning algorithms and should motivate exploration into the role of neuromodulators for associative plasticity beyond reinforcement learning contexts.

Methods
Flies

Unless otherwise specified, Drosophila melanogaster were raised on molasses-based food in an incubator (IN034, Darwin Chambers) on a 12 h:12 h light:dark cycle at 25 °C and ∼70% relative humidity. Flies expressing HcKCR170 or CsChrimson108 were raised throughout development on Nutri-Fly “German Food” Sick Fly Formulation no. 66-115 (Genesee), containing ∼0.6 mM all-trans-retinal (Sigma) and the anti-fungal agent (Tegosept). Fly vials containing all-trans retinal were wrapped in foil to prevent its photoconversion.

Experimenters were not blinded to fly genotype. Data from experimental and control genotypes were collected concurrently to avoid batch effects. Sample sizes were chosen based on conventions in the field, expected fly-to-fly variability from published results, and pilot data. For all in vivo experiments flies had at least one wild-type copy of the white (w) gene. Fly genotypes used in each figure are as follows:

View inlineView popup
 
Origins of Transgenic stocks
View inlineView popup
 
Creation of UAS-HcKCR1 transgenic flies

Generation of the UAS-HcKCR1 transgenic fly line was performed by WellGenetics Inc. (New Taipei City, Taiwan). The HcKCR1-V5-6xHis sequence was designed using the HcKCR1 sequence from HcKCR1_mCherry_pcDNA3.1 (Addgene plasmid # 177336)70 with the C terminal mCherry sequence replaced by a three alanine linker and V5 and 6xHis sequences followed by a stop codon. This HcKCR1-V5-6xHis 917bp fragment was synthesized with a 4bp Drosophila Kozak sequence added in front of the start codon and cloned into Not1/Xbal sites of the pJFRC7-20XUAS-IVS-mCD8::GFP plasmid replacing the mCD8::GFP coding region using sequence and ligation-independent cloning methods. pJFRC7-20XUAS-IVS-mCD8::GFP was a gift from G. Rubin (Addgene plasmid # 26220)109. PhiC31 mediated transgenesis was performed using standard methods to incorporate the plasmid into flies containing the Su(Hw)attP1 landing site to create a final genotype of:

P{y[+t7.7]=CaryPw[+mC]=pJFRC7 20XUAS IVS HcKCR1 V5 6xHis}Su(Hw)attP1

Data analysis

Two-photon imaging, behavioral, electrophysiology, sequencing, and connectomic data were analyzed using custom Python and R scripts (repositories will be made available upon acceptance). Statistical tests were performed using the Pingouin (https://pingouin-stats.org/build/html/index.html) and SciPy (https://scipy.org/) Python libraries. For parametric tests, Q-Q plots were used to assess normality of residuals.

Measuring locomotor behavior

In all two-photon experiments excluding Extended Data Fig. 9d-g, the fly stood on an air-cushioned 9-mm ball made of white foam (FR-4615, General Plastics), painted with black shapes. The ball floated in a custom plastic holder (ABS-like Gray, machined by Proto Labs Inc.) with a semi-spherical depression that cradled the ball. Air flowed into the holder at the base and out of the center of the semi-spherical depression to support the foam ball. The ball was illuminated using infrared LEDs. The movement of the ball was tracked at approximately 450 Hz using a high-speed video camera (Teledyne Flir Chameleon 3, CM3-U3-13Y3M-CS).

FicTrac software113 converted the image of the ball into an estimate of its orientation along three axes of rotation. Data from each processed frame was streamed via serial port to a microcontroller (Teensy 4.1). An I2C connection to a 12-bit digital-to-analog converter and a custom op-amp circuit converted the yaw orientation of the ball to a 0-10 Volt analog signal used to control the visual stimulus. We achieved low latency processing such that analog voltage updates were faster than camera frame acquisitions.

Visual arena and visual stimuli

Visual stimuli were presented using a circular arena composed of modular square panels with a refresh rate of approximately 166 Hz114. Each square panel consisted of an 8 x 8 array of blue LEDs (460-475 nm peak wavelength). We used an arena composed of 11 x 2 panels that spanned 330° in azimuth. The remaining 30° degree gap was positioned behind the fly (-150° clockwise from directly in front of the fly) to allow for imaging of the ball. The top edge of the visual arena was approximately aligned with the fly’s vertical position, and the visual arena spanned ∼43° vertically of the fly’s visual field. All visual stimuli consisted of a vertical bar that spanned the full height of the arena and was 2-pixels wide (∼7.5° in azimuth). During closed loop trials, the angle of the bar was set to the yaw angle estimate of the ball via the 0-10 V analog input. During dark experiments, all pixels were turned off. See below (“Optogenetic plasticity protocol”) for description of visual stimuli during optogenetic pairing. To minimize detection of the visual stimulus by the PMTs, the front surface of the visual arena was covered with 3 layers of a blue bandpass gel filter (Tokyo Blue-071 LEE Filters) and a single layer of a neutral density dimming filter (0.9 ND-211 LEE Filters). To reduce reflections, a layer of Parafilm was stretched over the front of the filters. The remaining surfaces of the arena were covered with blackout fabric (BK5, Thorlabs Inc.).

Two-photon imaging and optogenetics
Fly preparation

To promote walking flies were starved for 12-24 hours prior to imaging. Female flies 5-10 days post eclosion were cold-anaestethized and placed in a custom fly holder with an inverted pyramid shape (Acetal Homopolymer Delrin 150, machined by Proto Labs Inc). The fly’s thorax and head were secured in the holder with the head pitched forward such that most of the eye was below the edge of the holder and the posterior surface of the head was roughly flush with the bottom of the holder. The head was further secured using UV curable glue (Loctite 3972) and a brief pulse (<1s) of UV light (LED-200, Lightning Enterprises). The wings were repositioned to be within the pyramid of the holder and out of the way of the legs. The proboscis was then paralyzed by clipping the rostral protractor muscle using sharpened forceps. The dorsal surface of the fly was covered with saline and a hole was cut in the posterior surface of the head capsule to expose the area above the central complex. Some tracheae were removed to allow optical access and reduce brain movement. The external solution contained (in mM): 103 NaCl, 3 KCl, 5 N-tris(hydroxymethyl) methyl-2-aminoethane-sulfonic acid, 8 trehalose, 10 glucose, 26 NaHCO3, 1 NaH2PO4, 1.5 CaCl2 and 4 MgCl2. For dual calcium indicator imaging (Fig 2 and Extended Data Fig 9a-d) and optogenetic experiments (Fig 3 & 4, Extended Data Fig 11-13) calcium concentration was increased to 2 mM to increase signal to noise ratio. For all external saline, osmolarity was adjusted to 270–275 mOsm. The external solution was bubbled with 95% O2 and 5% CO2 and reached a final pH of 7.1-7.3. After dissection, the fly was immediately placed on the floating ball under the two-photon microscope. The microscope objective was positioned over the region of interest and warmed bubbled saline (25-27°C) was continuously perfused over the brain by a peristaltic pump running at 40 revolutions per minute (120 Series Pump (120U/DM2), Watson-Marlow). The fly walked in closed loop with a vertical bar for at least 10 minutes prior to imaging.

Two-photon imaging

All two-photon imaging and optogenetic experiments with the exception of data included in Extended Data Figure 9d-g were performed on a Bruker Ultima 2P microscope using two fixed-wavelength femtosecond pulsed lasers (Coherent Axon 920 nm and Coherent Axon 1064 nm, a subset of data was collected using a Spark Alcor 920 nm) and piezoelectric objective scanner. Images were collected using a 25x objective (HC FLUOTAR L 25x/0.95 W VISIR, Leica inc.). Emitted fluorescence was first split using a 565 longpass filter (Chroma). Rejected light was filtered with a 525/80 bandpass filter (Chroma) and passed light was filtered with a 610/75 bandpass filter before being collected using GaAsP photomultiplier tubes (Model H10770PB-40, Hamamatsu).

The imaging region was centered on the ellipsoid body and set for each fly to achieve a high imaging rate (resonant-galvo scanning) while ensuring enough boundary for motion correction. A typical imaging field of view was 300 x 250 pixels collected at 4.83x zoom. All data was collected using volumetric z-scanning with 6 z-slices spaced 5 μm apart, resulting in a volumetric scan rate of 7.6-11.7 Hz. Imaging data was synchronized with behavioral data from FicTrac and the visual arena using the Bruker voltage recording module. For all figures a 920 nm laser was used to image green fluorescent proteins. For dual color imaging (Fig. 2 and Extended Data Fig. 9a-d) simultaneous stimulation with the 920 nm and 1064 nm lasers was used. For optogenetic experiments, the 1064 nm laser was controlled with an independent galvo-galvo scanning module. Laser power for each laser line was typically between 5 mW and 15 mW as measured at the sample plane.

For imaging experiments that did not involve optogenetics, imaging was performed in repeated 6-minute sessions. Closed loop sessions in which a vertical blue stripe was visible and rotating with the ball were interleaved with dark sessions in which the visual arena was not illuminated. Between imaging sessions, the imaging field of view was recentered and the tissue was briefly assessed for photobleaching and damage. The fly walked in closed loop between imaging sessions.

Data in Extended Data Figure 9d-g were collected and preprocessed using previously described methods29.

Optogenetic plasticity protocol

For optogenetic experiments, 920 nm imaging power was <14 mW as measured during laser scanning at the sample plane. Flies were given at least 10 minutes of closed loop experience prior to baseline imaging sessions. Each fly first underwent a 3-minute baseline imaging session in which they walked in closed loop VR. Next, each fly underwent two rounds of opto-pairing and post opto-pairing imaging sessions: 0 radian bump-cue offset opto-pairing and π radian bump-cue offset opto-pairing in a pseudorandom order.

Opto-pairing session: Each opto-pairing session began with a brief closed loop period. The visual arena then went blank for 5 seconds. The blue bar was then flashed at 8 different orientations around the fly for 2 seconds each in clockwise order. This was repeated 5 times. At the onset of each bar flash, a corresponding wedge of the ellipsoid body was stimulated with the 1064 nm laser at the desired bump-cue offset for 1800 msec (10 μm circle, spiral scanned 100 times). For experiments included in Fig 3 and Extended Data Fig 11, 1064 nm laser power was approximately 20 mW, as measured at the sample plane during mock optogenetic stimulation. For all other optogenetic experiments, 1064 nm laser power was approximately 10 mW. A shutter protected PMTs during optogenetic stimulation but reopened for the last 200 msec of each bar flash, allowing us to measure the calcium response to optogenetic stimulation (analysis details below). Immediately after the last blue bar flash, the visual arena went blank for 5 seconds and then the blue bar reappeared in closed loop. We continued imaging in closed loop for a brief period before ending the opto-pairing session. Opto-pairing sessions lasted less than 3 minutes. After recentering the field of view, we began the post opto-pairing session.

Post opto-pairing imaging sessions were a 3-minute-long closed loop session.

Data processing for two-photon imaging
Preprocessing

Images from two-photon microscopy were motion corrected in each z plane independently. For each plane, a reference image was computed using one tenth of the frames. To compute the reference image: first, a temporal average of the reference frames was computed; second, each frame was aligned to the average using the peak of the spatial cross correlation; third, the temporal average was recomputed. The remaining frames from the imaging session were then aligned to the reference image using the maximum of the spatial cross correlation. Using Napari (https://napari.org/stable/)115, for each z plane, one region of interest (ROI) was drawn around the perimeter of the ellipsoid body and a second ROI was drawn around the inner circle of the ellipsoid body. Pixels were considered in the ellipsoid body if they fell within the outer ROI but not inner ROI. The center of mass of the inner ROI was considered the center of the ellipsoid body for each z plane, and the phase of each pixel in the ellipsoid body was calculated relative to this origin (arctac(y/x)). The phases were divided into 16 bins to create wedge-shaped ROIs around the ellipsoid body. Bins with the same phase were combined for all z-planes. Average fluorescence values for each volume were extracted from each ROI. To simultaneously remove artifacts from the visual arena and to correct for photobleaching and slow z drift, time series were fit with a linear model that included a single exponential and the timeseries from a background ROI which did not include fluorescent pixels (log(ỹk) = log(ŷk) + ϵ(t) with ŷk = exp(β2t + β1log(ybackground) + β0)) where ỹk is the raw fluorescence time series of the kth ROI, ybackground is the background signal intensity, t is time, βi are coefficients fit by least squares regression, and ϵ(t) is the error of the fit at each time point. The residual time series with nuisance terms removed, yk = y>k − ỹk, was then z-scored, temporally smoothed by a gaussian kernel of width 100 msec (∼1 imaging volume), and spatially smoothed with a gaussian kernel of width ½ of an ROI (π/16 radians of the ellipsoid body).

Fictrac phases were shifted so that a 0 radian orientation aligned with the 0 radian angle of the ellipsoid body and smoothed by a gaussian kernel of width 100 msec. Based on analyses in Extended Data Fig. 1, we temporally shifted Fictrac phases by -200 msec (approximately 2 imaging volumes) to maximize correlation between behavioral and neural data.

Data in Extended Data Fig. 9d-g was preprocessed using previously described methods 29. ROI timeseries were smoothed and z-scored using identical parameters as above.

Population vector analyses

We define the population vector (PV) of ellipsoid body activity as in previous work 3. The population vector (PV) at time t is defined as PVt = [y1,teπj/8, . . . , yk,t eπkj/8, . . . , y16,te2πj], where j is the imaginary unit and yk,t is the fluorescence of the kth ROI at time t. This definition multiplies the fluorescence intensity of each ROI by a vector on the unit circle of the complex plane, thus assigning each ROI to its corresponding angle around the ellipsoid body and scaling it by the fluorescence intensity. The population vector average (PVA) at time t is the across-ROI average of PV:  The angle and magnitude of of the population vector at time t is defined as is typical for complex numbers: PVA angle,  with  PVA magnitude,  The bump-cue offset at time t is the difference in angles between the PVA and the angle of the ball (or the vertical bar’s azimuthal angle in closed loop),  where ej∠ballt is a vector on the unit circle indicating the orientation/phase of the ball (or bar) at time t as measured by Fictrac. The average bump-cue offset over an imaging session is defined as the angle of the average offset vector, ∠Ō, where Ō = 1/T ∗ ∑texp(j ∗ ot) and T is the total number of timepoints in the imaging session. To measure the consistency of the bump-cue offset, we calculated the length of the average offset vector ||Ō||. Note that circular variance = 1 - ||Ō||.If all of the bump-cue offsets are identical (i.e. the bump angle perfectly tracks the ball angle) this value will be 1. If the bump-cue offsets are uniformly distributed (i.e. bump angle contains no information about the bar angle) the length of the average vector will be 0. The absolute value of the difference in PVA offsets between two imaging sessions (Fig. 1k, Extended Data Fig. 2d) is 

ER octopamine/dopamine bump visualization (Fig 1n, Extended Data Fig 5)

Consider the matrix of ROI fluorescence values over time  where  is a column vector. For each t, we shifted the indices of y⃗t by heading (inverse of the binned orientation of the ball/bar, 16 bins identical to ROI bins) to yield Ŷ. We then took the temporal average of Ŷ for the first and second half of the imaging session separately. To perform a cross-validated alignment of the peaks across flies, we calculated the index of the peak (argmax) from the first half’s average and used that value to circularly shift the second half’s average.

Difference in EL and EPG PVA angles (Fig 2, Extended Data Fig 9)

To quantify the average angular distance between the EL and EPG bumps we calculated the temporal average of the absolute angular difference between the EL PVA angle and EPG PVA angle (Fig. 2i, Extended Data Fig. 9f). For Extended Data Fig. 9c, we binned the absolute angular difference by the average PVA magnitude of the EL and EPG populations at each timepoint. Averages were calculated first within flies and then across flies.

To visualize the extent to which the EL PVA can lead the EPG PVA during rapid turns (Extended Data Fig. 9a,g), the columns of YEL (the matrix of ROI fluorescence for the EL channel) and YEPG (the matrix of ROI fluorescence for the EPG channel) were circularly shifted by argmax( y⃗t,EPG). We separately took the average of timepoints where the fly’s rotational velocity was greater than π rad/s or less then -π rad/s.

To quantify the extent to which EL PVA angle leads the EPG PVA angle for all turning speeds (Extended Data Fig. 9b,h), we calculated the mean PVA angle difference (EL minus EPG) for time points within each rotational velocity bin. Averages were calculated within each fly and then combined data across flies.

Response to optogenetic stimulation (Fig. 4e, Extended Data Fig. 11-13)

Fluorescence was extracted from ellipsoid body ROIs from the period when the PMT-shutter was open, this was the final 200 msec of each bar flash. This fluorescence data was processed the same as all other data with the difference being that no detrending (linear model fit) or smoothing was performed because of the discontinuous nature of the recordings. Instead, background fluorescence was regressed from each ROI and fluorescence values were z-scored for each ROI independently. Each ROI’s time series was averaged across repeated bar flashes/optogenetic stimulations.

Remapping error

For each post-pairing session, we calculated the absolute value of the difference between the average PVA angle and the opto-paired PVA angle. We then averaged this value across the two pairing sessions to get remapping error:  where  is the average offset vector for the post-0 imaging session and  is the average offset vector before the the post-π imaging session.

Plasticity network model

We translated a previously published model16 from MATLAB to Python, implementing both presynaptically-gated and postsynaptically-gated plasticity rules. We modified the learning rate (ϵ in the previously published model) to assess robustness of presynaptically and postsynaptically gated learning rules. We simulated a thin vertical bar as a narrow von Mises function with a concentration parameter κ=15 as done previously. Uniformly distributed noise was added to rotational velocity at each timepoint 𝑣 = 𝑣actual + 0.4max(𝑣actual) σ, where σ∼ U(−.5, .5) and 𝑣actual is the scaled true rotational velocity of the animal.The visual input drive was set to zero to simulate dark trials. All other parameters were identical to the previous implementation16.

Walking trajectories from the flies included in Fig 1g-k were used to simulate network dynamics. The full walking trajectory including data prior to imaging sessions was included in each simulation.

Simulated EPG time series were analyzed similarly to the in vivo data except no preprocessing was applied. Each EPG (n=32 model cells) was assigned an orientation around the ellipsoid body at evenly spaced intervals, and we computed PVAs and associated metrics identically as above.

Cell type naming conventions
All cell types are named as in the hemibrain connectome (v1.2.1)24 Connectome analysis

All connectomics analyses utilized the hemibrain connectome (v1.2.1) and its Python API24,116. Summary graphs and cable distance quantifications were created using the NetworkX Python package117. For Fig. 2c & Extended Data Fig. 7a-c, only connections between neurons with >3 synapses were considered. For Fig. 2f-g & Extended Data Fig. 7f-g all connections between neurons were considered. For remaining analyses, synapse number cutoff is stated explicitly in figure.

Visualizations in ellipsoid body coordinates

We created a Python implementation of a previously published algorithm for centering visualizations of neuron skeletons on the major axes of a neuropil of interest118. Briefly, we performed principal components analysis on the vertices of the ellipsoid body ROI mesh from the hemibrain dataset. We then applied the change of basis from PCA to neuron skeletons and synapse locations. This approach defines the origin as the center of the annulus. The first two principal axes (approximately, medial-lateral and dorsal-ventral) give the plane of the ring, and the third principal axis gives the depth (approximately anterior-posterior). We assigned each voxel an ellipsoid body radius and phase using the coordinates in the first two principal axes.

To collapse synapse counts across different ellipsoid body phases (Extended Data Fig. 7e), we considered the radius and third principal axis coordinates for each synapse. To correct for the fact that the ellipsoid body radius and third principal axis position are not homogeneous across the structure, for each synapse, we centered the synapse locations by the local radial and third principal axis center of mass of the ellipsoid body mesh.

To obtain peeled convex hulls of each EL neuron’s presynapses (Fig. 2d), we first transformed synapse locations for each neuron into ellipsoid body coordinates and considered only the first two principal axes. To visualize only the most dense region of synapses, we iteratively computed the convex hull of synapse locations and then deleted synapses that formed the vertices of the convex hull. We repeated this procedure 20 times for each cell.

Cable distance

To compute cable distances, neuron skeletons of ER neurons in the hemibrain connectome (v1.2.1) were obtained from Neuprint116 and upsampled to maximal resolution, ER-EPG presynapses as well as EL-ER and ExR2-ER postsynapses were attached to the ER skeletons, and the skeletons were converted to NetworkX weighted graphs. For each EL or ExR2 postsynapse, candidate nearest ER-EPG presynapses were chosen as all of those within a 10 μm Euclidean distance, and then Dikstra’s algorithm was used to find the cable distance (through the skeleton) to the closest ER-EPG presynapse amongst those candidates. For comparison, the same analysis was also run on γ-kenyon cell skeletons analyzing the cable distance between γKC-mushroom body output neuron (MBON) presynapses and dopamine neuron [DAN]-γKC, DANs include γ-lobe innervating PPL and PPM neurons) postsynapses.

Standard IHC protocol & Confocal Imaging

To image adult brains, female flies that were 6–10 days post eclosion were anesthetized with CO2 and dissected at room temperature in phosphate buffer solution (PBS).

All immunohistochemistry steps were performed at room temperature in Nunc trays (Cat#:136528, ThermoFisher) with 3-5 brains per well. Brains were transferred between wells using blunt forceps. After dissection, brains were fixed in 24μL 32% aqueous formaldehyde solution in 200μL PBS for exactly 14 minutes. Following fixation, brains were washed in PBS for 10 minutes while moving them between 5 wells. Brains were then incubated for approximately 20 minutes in 5% normal goat serum (NGS) (G9023-10ML, Sigma Aldrich) in PBST (0.2% Triton-X in PBS). After this blocking step, brains were incubated in primary antibody solution for approximately 48 hours while mixing on a Nutator. Then brains were washed in 5 wells filled with PBS with 0.2% Triton X-100 (PBST) for 10 minutes. Next, brains were incubated in a secondary antibody solution for approximately 24 hours while mixing on a Nutator. Finally, brains were then washed in 5 wells filled with PBST for 10 minutes and then transferred to 70% Glycerol in PBS to be stored at 4°C.

Within one week in 70% Glycerol, fly brains were mounted on a slide with Vectashield. Brains were imaged using a Zeiss LSM780 NLO laser scanning confocal microscope (Oberkochen, Germany) housed at the UC Berkeley CRL Molecular Imaging Center, RRID:SCR_017852. The following excitation lasers were used: 488nm, 561nm, 635nm. The samples were imaged using a 40x/1.4 oil-immersion lens. Z-stacks of 120 to 160 optical sections were taken with 1.0-μm spacing. To allow quantitative comparison between genotypes (Extended Data Fig. 10a-c, Tyramine β-Hydroxylase RNAi vs control), a fixed gain and laser power was used for all brains. For all other imaging, gain and laser power were optimized for each brain.

MultiColor Flp Out IHC protocol (R18B05-LexA)

For MultiColor FlpOut (MCFO)112 analysis of the R18B05 LexA line, flies were heat-shocked for 1-2 hours 8 days after egg laying and dissected at 8 days post eclosion. To administer heat-shock, the vial of flies was submerged in a 37°C water bath for 1-2 hours. The same standard IHC dissection, fix, and blocking steps as outlined above was used except with an additional round of staining for the V5 epitope that occurred before brains were transferred to glycerol where brains were incubated in 5% normal mouse serum (NMS) in PBST for 20 minutes then incubated in mouse anti-V5::Alexa 488 (1:500, Invitrogen 37-7500-A488) in 5% NMS in PBST for 24 hours. Finally, brains were washed in 4 wells filled with 10 μL PBST for 10 minutes and placed in 70% glycerol in PBS to be stored at 4°C.

Primary and Secondary Antibody Solutions
R18B05 LexA full line

Primary antibody solution: mouse anti-nc82 (1:20, Developmental Studies Hybridoma Bank, nc82), chicken anti-GFP (1:1000, Abcam, ab13970), and 5% normal goat serum (NGS) (G9023-10ML, Sigma Aldrich) in PBST (0.2% Triton-X in PBS).

Secondary antibody solution: goat anti-mouse Alexa 633 (1:250, Invitrogen, A-21050), goat anti-chicken Alexa 488 (1:250, Invitrogen, A11039), and 5% NGS in PBST.

R18B05 LexA MCFO

Primary antibody solution: mouse anti-nc82 (1:20, Developmental Studies Hybridoma Bank, nc82), rabbit anti-HA tag (1:300, Cell Signaling, #3724), rat anti-OLLAS tag (1:200, Invitrogen, MA5-16125), and 5% NGS in PBST.

Secondary antibody solution: goat anti-mouse Alexa 633 (1:250, Invitrogen, A-21050), goat anti-rabbit Alexa Plus 555 (1:500, Invitrogen, A32732), goat anti-rat Alexa Plus 405 (1:250, Invitrogen, A48261) and 5% NGS in PBST.

Tyramine Beta Hydroxylase RNAi

Primary antibody solution: mouse anti-nc82 (1:20, Developmental Studies Hybridoma Bank, nc82), chicken anti-GFP (1:1000, Abcam, ab13970), rabbit anti-octopamine (1:100, MyBioSource, MBS2090493), and 5% normal goat serum (NGS) (G9023-10ML, Sigma Aldrich) in PBST (0.2% Triton-X in PBS).

Secondary antibody solution: goat anti-mouse Alexa 633 (1:250, Invitrogen, A-21050), goat anti-chicken Alexa 488 (1:250, Invitrogen, A11039), goat anti-rabbit Alexa 568 (1:250, Invitrogen, A11011) and 5% NGS in PBST.

HcKCR1::V5 in EL and EPG

Primary antibody solution: mouse anti-V5 (1:500, Abcam, ab27671), chicken anti-GFP (1:1000, Abcam, ab13970), rabbit anti-dsRed (1:250, Takara Bio USA, 632496), and 5% normal goat serum (NGS) (G9023-10ML, Sigma Aldrich) in PBST (0.2% Triton-X in PBS)

Secondary antibody solution: goat anti-mouse Alexa 633 (1:250, Invitrogen, A-21050), goat anti-chicken Alexa 488 (1:250, Invitrogen, A11039), goat anti-rabbit Alexa 568 (1:250, Invitrogen, A11011) and 5% NGS in PBST.

Confocal Image Analysis

For all data maximum intensity Z-projections were created using threshold tools in Fiji/ImageJ. Further analysis was performed on specific genotypes as outlined below:

R18B05 LexA full line

For analyzing R18B05 LexA full-line histology, the number of EL neurons per brain was determined by counting cell bodies by eye in Napari 115.

R18B05 LexA MCFO

For R18B05-LexA Multi-Color FlpOut, labeled neurons were identified as EL or non-EL by their morphology. Both the number of distinct labeled cell bodies and distinct wedges in the EB were used to quantify the number of unique EL neurons targeted across the HA, V5, and OLLAS epitope tags. Due to low signal-to-noise, contrast was increased to make the neuronal structure more visible in maximum intensity projections. This introduced significant background noise.

FIJI’s freehand selection tool and clearing tool were used to manually remove background noise and improve morphological visualization.

Tyramine Beta Hydroxylase RNAi

To compare octopamine levels in TβH RNAi experiments, the fluorescence of Alexa568 (Octopamine) was used. Pixels with a fluorescence value above 100 in the Alexa488 channel (R38C04-AD; R18B05-DBD driving mCD8::GFP) were used to determine which pixels to include in the ROI. Alexa568 fluorescence values within the chosen ROI were averaged to generate the strip plot. An unpaired Mann Whitney U test used to compare genotypes.

Electrophysiology from EL neurons
Electrophysiology fly preparation and dissection

Newly eclosed female flies were collected using cold anesthesia 3–10 hours before the experiment. Then for the dissection, each fly was cold anaesthetized and placed in a fly holder consisting of flat titanium foil secured within an acrylic platform. The fly’s head was pitched slightly forwards (<30°). The fly was secured in the holder using ultraviolet-curable adhesive (Loctite AA 3972) cured by a brief (<1 s) pulse of ultraviolet light (LED-200, Electro-Lite Co.). To reduce brain movement, muscle 16 and proboscis muscles were clipped with forceps. After the dorsal portion of the head (above the holder surface) was covered in external saline solution, a hole was cut in the head capsule and trachea were removed to expose the posterior surface of the brain. An aperture was made in the perineural sheath by pulling gently with fine forceps or by using suction from a patch pipette containing external saline solution.

The external saline solution was identical to the solution used for two-photon imaging with a 1.5 mM CaCl2 concentration.

Whole-cell Patch-clamp recordings

Patch pipettes were made from borosilicate glass (Sutter, 1.5 mm o.d., 86 mm i.d.) using a Sutter P-97 puller. Pipettes were fire polished down after pulling using a microforge (ALA Scientific Instruments) to a final resistance of 8–15 MΩ. The internal pipette solution contained (in mM): 140 potassium aspartate, 10 4-(2-hydroxyethyl)1-piperazineethanesulfonic acid, 4 MgATP, 0.4 Na3GTP, 1 ethylene glycol tetraacetic acid, 1 KCl and 13 biocytin hydrazide. The pH was 7.15, and the osmolarity was adjusted to about 267 mOsm. Recordings were performed at room temperature.

To visualize the brain, we used an epifluorescent microscope customized for electrophysiology (Vivoscope, Scientifica) with an Olympus BX51WI fluorescence turret and a 40x water-immersion objective. For illumination far-red light was delivered by a fibre-coupled light-emitting diode (LED; 740 nm, M740F2, Thorlabs) through a ferrule patch cable (200 μm Core, Thorlabs) plugged into a fibre optic cannula (1.25-mm SS ferrule 200-μm core, 0.22 NA, Thorlabs) glued to the recording platform, with the tip of the cannula about 1 cm behind the fly. GFP fluorescence was visualized using a CoolLED light source (pE-300-ultra) with an eGFP-long-pass filter (49018, Chroma). Somatic recordings were obtained in current-clamp mode using a MultiClamp 700B amplifier and a CV-7B headstage (Molecular Devices). Voltage signals were low-pass filtered at 5 kHz before digitization and then acquired with a NiDAQ PCIe-6351 (National Instruments) at 20 kHz. For all electrophysiological recordings, liquid junction potential correction was performed post hoc by subtracting 13 mV from recorded voltages 119.

HcKCR1 stimulation

For optogenetic stimulation during electrophysiology, we used the CoolLED light source (pE-300ultra) to deliver pulses of orange light (590–650 nm, 2 mW, Cy5 long-pass filter cube (49019, Chroma) through the objective. Raw voltage traces from whole-cell current-clamp recordings were collected during a train of 10 light pulses (100 ms duration, delivered every 5 seconds; 0.2 Hz). TTL pulse trains were generated using custom MATLAB scripts and output via a National Instruments PCIe-6351 DAQ board to control illumination timing. A constant depolarizing current was injected before each trial to increase the somatic membrane potential to about -45mV to -55mV.

Electrophysiology data analysis

Raw voltage traces from whole-cell current-clamp recordings data were imported into Python and analyzed using custom scripts. Voltage recordings were aligned to stimulation time using a recorded TTL signal from the LED controller. For each trial, the light-evoked voltage response was quantified as the difference between the baseline membrane potential (averaged over a 500 ms window prior to LED onset) and the average voltage during the 100 ms LED stimulation. Responses from individual trials were then averaged to compute the mean response for each cell. Group comparisons were performed using non-parametric statistics (Mann–Whitney U test) to assess whether peak hyperpolarization differed significantly between control and HcKCR1-expressing EL neurons.

ER4d octopamine receptor EASI-FISH

Expansion-Assisted Iterative Fluorescence In Situ Hybridization (EASI-FISH), DAPI staining, and light sheet imaging were performed as described previously 61,120. Brains were hybridized with probes designed by Molecular Instruments Inc. to target Drosophila melanogaster octopamine receptors (LOT numbers - Oamb: PRH792, Oct-TyR: PRH797, Octβ1R: PRH794, Octβ2R: PRH795, Octα2R: PRH793 Octβ3R: PRH796). Two octopamine receptor types were labeled in each brain. Pair 1:Oamb was detected with Alex Fluor (AF) 546 and Oct-TyR with AF647 hairpins. Pair 2: Octβ1R was detected with to AF546 & Octβ2R with AF647 hairpins. Pair 3:Octα2R was detected with AF546 & Octβ3R with AF647 hairpins. A split-Gal4 line labeling ER4d neurons was used to express myr-GFP (see “Flies” section above).

FISH labeling of TβH

FISH for TβH RNA and associated Confocal imaging were performed as described previously121. Probe sequences can be found in the original publication (Probe set 2, Figure 3).

RNA-Seq
RNA-Seq: Expression checks

Neurons of interest were isolated by expressing the fluorescent reporters 20XUAS-IVS-nls-tdTom-BCp10 (attP18);; 10XUAS-unc84-2XGFP (attP2) using split-Gal4 drivers specific for particular cell types and then manually picking the fluorescent neurons from dissociated brain tissue. Each driver/reporter combination was ‘expression checked’ to confirm that the marked cells were sufficiently bright to be sorted effectively and that there was minimal off-target expression in neurons other than those of interest.

RNA-Seq: Sorting of labeled neurons

Adult flies were collected when they eclosed, and aged 3-5 days prior to dissection. For each sample, 60-100 brains were dissected in freshly prepared, ice cold Adult Hemolymph Solution (AHS, 108 mM NaCl, 5 mM KCl, 2 mM CaCl2, 8.2 mM MgCl2, 4 mM NaHCO3, 1 mM NaH2PO4, 5 mM HEPES, 6 mM Trehalose, 10 mM Sucrose), and the major tracheal branches removed. The brains were transferred to a 1.5 mL Eppendorf tube containing 500 μL 1 mg/ml Liberase DH (Roche, prepared according to the manufacturer’s recommendation) in AHS, and digested for 1 h at room temperature. The Liberase solution was removed, and the brains washed twice with 800 μl ice cold AHS. The final wash was removed completely and 400 μL of AHS+2% Fetal Bovine Serum (FBS, Sigma) were added. The brain samples were gently triturated with a series of fire-polished, FBS-coated Pasteur pipettes of descending pore sizes until the tissue was homogenized, after which the tube was allowed to stand for 2-3 m so that the larger debris could settle.

For FACS, the samples were triturated in AHS+2%FBS that was run through a 0.2 μm filter, and the cell suspension was passed through a Falcon 5 mL round-bottom tube fitted with a 35 μm cell strainer cap (Fisher). Samples were sorted on a SONY SH800 cell sorter gated for single cells with a fluorescence intensity exceeding that of a non-fluorescent control. Replicates of 15 cells (SS70424 and MB233B, ExR2 lines) and 80 cells (SS00027 and SS50573, EL lines) were purity sorted into 3 μL Lysis Buffer (0.2% Triton X-100, 0.1 U/μL RNAsin) and flash frozen on dry ice.

RNA-Seq: Library preparation and sequencing

One microliter of harsh lysis buffer (50 mM Tris pH 8.0, 5 mM EDTA pH 8.0, 10 mM DTT, 1% Tween-20, 1% Triton X-100, 0.1 g/L Proteinase K (Roche), 2.5 mM dNTPs (Takara), and ERCC Mix 1 (Thermo-Fisher) diluted to 1E-7) and 1 μl 10 μM barcoded RT primer were added, and the samples were incubated for 5 m at 50°C to lyse the cells, followed by 20 m at 80°C to inactivate the Proteinase K. Reverse transcription master mix (2 μL 5X RT Buffer (Thermo-Fisher), 2 μL 5M Betaine (Sigma-Aldrich), 0.2 μL 50 μM E5V6NEXT template-switch oligo (Integrated DNA Technologies), 0.1 μL 200 U/μL Maxima H-RT (Thermo-Fisher), 0.1 μL 40U/μL RNAsin (Lucigen), and 0.6 μL nuclease-free water (Thermo-Fisher) was added to the lysis reaction and incubated at 42°C for 1.5 h, followed by 10 m at 75°C to inactivate the reverse transcriptase.

PCR was performed by adding 10 μL 2X HiFi PCR Mix (Kapa Biosystems) and 0.5 μL 60 μM SINGV6 primer and incubating at 98°C for 3 m, followed by 20 cycles of 98°C for 20 s, 64°C for 15 s, 72°C for 4 m, and a final extension of 5 m at 72°C. Groups of 8 reactions were pooled to yield ∼250 μL and purified with Ampure XP Beads (0.6x ratio; Beckman Coulter), washed twice with 75% Ethanol, and eluted in 40 μL nuclease-free water. The DNA concentration of each sample was determined using Qubit High-Sensitivity DNA kit (Thermo-Fisher).

To prepare the Illumina sequencing library, 600 pg cDNA from each pooled sample was used in a modified Nextera XT library preparation (Illumina) 122 using the P5NEXTPT5 primer and unique i7 primers (Illumina) for SS70424 and MB233B, or Illumina Unique Dual Indexes for SS00027 and SS50573, and extending the tagmentation time to 15 m. The resulting libraries were purified according to the Nextera XT protocol (0.6x ratio) and quantified by qPCR using Kapa Library Quantification (Kapa Biosystems). Six to eight sequencing libraries were loaded on a NextSeq High Output flow cell reading 26 bases in Read 1, including the spacer, sample barcode and UMI, 8 bases in the i5 and i7 index reads, and 50 bases in Read 2 representing the cDNA fragment from the 3′ end of the transcript.

Sequencing adapters were trimmed from the reads with Cutadapt v2.10 123 prior to alignment with STAR v2.7.5a 124 to the Drosophila r6.34 genome assembly (Flybase). Sequencing adapters were trimmed and aligned as was done for the bulk RNA-seq data. Gene counts were generated with the STARsolo algorithm using the following additional parameters: “–soloType CB_UMI_Simple–soloCBwhitelist smartscrb_whitelist.txt–soloCBstart 2–soloCBlen 8– soloUMIstart 10–soloUMIlen 10 -soloBarcodeReadLength 0–soloCBmatchWLtype 1MM_multi_pseudocounts–soloStrand Forward–soloFeatures Gene–soloUMIdedup 1MM_All– soloUMIfiltering MultiGeneUMI–soloCellFilter None.” The full set of 384 barcodes designed for this assay was used as the allowlist. Gene counts for the subset of barcodes used in this experiment were extracted using custom R scripts.

Contributions

M.H.P., D.B.T.E, V.J. & Y.E.F. designed the study and interpreted data.

M.H.P. performed and analyzed all 2-photon experiments with assistance from D.B.T.E on the dual imaging data set.

J.C.C. performed immunostaining, confocal imaging, and analysis.

R.P.R. & D.B.T.E. performed RNA-seq experiments and analysis.

M.E. & D.B.T.E. performed EASI-FISH and analysis.

M.H.P. assisted with EASI-FISH and RNA-seq analyses.

A.L. performed the electrophysiology experiments and analysis.

M.H.P. & Y.E.F. generated the HcKCR1 transgenic line.

M.H.P. performed connectomics analysis

M.H.P. & D.B.T.E performed computational modeling

M.H.P. & Y.E.F wrote the manuscript with input from all co-authors

Acknowledgements

Fly stocks obtained from the Bloomington Drosophila Stock Center (NIH P40OD018537) were used in this study. We thank G. Rubin for the pJFRC7-20XUAS-IVS-mCD8::GFP plasmid and G. Rubin and T. Wolff for use of the EL split Gal4 fly lines prior to publication. We thank Y. Li for sharing UAS-GRAB-OA1.0 fly lines. We thank A. Shenasa for the preliminary analysis of the EASI-FISH data. Most confocal experiments were conducted at the University of California Berkeley CRL Molecular Imaging Center, RRID:SCR_017852, supported by NSF DBI-1041078. We thank H. Aaron and F. Ives for microscopy support. We thank P. Ramdya, D. Feldman, M. Feller, H. Yang, T. R. Clandinin, M. Silies, Y. Aso, A. Simon, S. Chitnis, C. Sauvola, and members of the Fisher lab for comments on the manuscript. The work by M.E., R.P.R., D.B.T.E., and V.J. was supported by Howard Hughes Medical Institute (HHMI). This work was supported by the NIH (DP2NS132373), NSF (2318081 Y.E.F. Co-PI), a Shurl and Kay Curci Foundation grant, a Seed Grant from the Brain Research Foundation, a Alfred P. Sloan Fellowship, and a Biohub, San Francisco, Investigator Award to Y.E.F.. M.H.P. is a fellow with the Jane Coffin Childs Memorial Fund for Biomedical Research. Y.E.F. is an HHMI Hanna Gray Fellow.

FUNDER INFORMATION DECLARED
National Institute of Neurological Disorders and Stroke, https://ror.org/01s5ya894, DP2NS132373
U.S. National Science Foundation, 2318081
Shurl and Kay Curci Foundation, https://ror.org/05t9fgt79
Brain Research Foundation, Seed Grant
Alfred P. Sloan Foundation, https://ror.org/052csg198
Chan Zuckerberg Biohub San Francisco, Investigator Award
Howard Hughes Medical Institute, https://ror.org/006w34k90, HHMI Hanna Gray Fellowship
Jane Coffin Childs Memorial Fund for Medical Research, https://ror.org/04yhme281
References
1.↵Petrucco, L. et al. Neural dynamics and architecture of the heading direction circuit in zebrafish. Nat. Neurosci. 26, 765–773 (2023).CrossRefPubMedGoogle Scholar
2.Ben-Yishay, E. et al. Directional tuning in the hippocampal formation of birds. Curr. Biol. 31, 2592–2602.e4 (2021).CrossRefPubMedGoogle Scholar
3.↵Seelig, J. D. & Jayaraman, V. Neural dynamics for landmark orientation and angular path integration. Nature 521, 186–191 (2015).CrossRefPubMedGoogle Scholar
4.Taube, S., Muller, U. & Ranck, B. Head-Direction Cells Recorded from the Postsubiculum Moving Rats. I. Description and Quantitative Analysis in Freely. (1990).Google Scholar
5.↵Griffiths, B. J. et al. Electrophysiological signatures of veridical head direction in humans. Nat. Hum. Behav. 8, 1334–1350 (2024).PubMedGoogle Scholar
6.↵Hulse, B. K. & Jayaraman, V. Mechanisms underlying the neural computation of head direction. Annu. Rev. Neurosci. 43, 31–54 (2020).CrossRefPubMedGoogle Scholar
7.↵Taube, J. S. The head direction signal: origins and sensory-motor integration. Annu. Rev. Neurosci. 30, 181–207 (2007).CrossRefPubMedWeb of ScienceGoogle Scholar
8.↵Green, J. et al. A neural circuit architecture for angular integration in Drosophila. Nature 546, 101–106 (2017).CrossRefPubMedGoogle Scholar
9.↵Turner-Evans*, D. B., et al. Angular velocity integration in a fly heading circuit. Elife 1–39 (2017).Google Scholar
10.Knierim, J. J., Kudrimoti, H. S. & McNaughton, B. L. Interactions between idiothetic cues and external landmarks in the control of place cells and head direction cells. J. Neurophysiol. 80, 425–446 (1998).CrossRefPubMedWeb of ScienceGoogle Scholar
11.Yoder, R. M., Peck, J. R. & Taube, J. S. Visual landmark information gains control of the head direction signal at the lateral mammillary nuclei. J. Neurosci. 35, 1354–1367 (2015).Abstract/FREE Full TextGoogle Scholar
12.Ajabi, Z., Keinath, A. T., Wei, X.-X. & Brandon, M. P. Population dynamics of head-direction neurons during drift and reorientation. Nature 615, 892–899 (2023).CrossRefPubMedGoogle Scholar
13.↵Peyrache, A., Lacroix, M. M., Petersen, P. C. & Buzsáki, G. Internally organized mechanisms of the head direction sense. Nat. Neurosci. 18, 569–575 (2015).CrossRefPubMedGoogle Scholar
14.↵Skaggs, W. E., Knierim, J. J., Kudrimoti, H. S. & McNaughton, B. L. A model of the neural basis of the rat’s sense of direction. Adv. Neural Inf. Process. Syst. 7, 173–180 (1995).CrossRefPubMedGoogle Scholar
15.↵Zhang, K. Representation of spatial orientation by the intrinsic dynamics of the head-direction cell ensemble: a theory. J. Neurosci. 16, 2112–2126 (1996).Abstract/FREE Full TextGoogle Scholar
16.↵Kim, S. S., Hermundstad, A. M., Romani, S., Abbott, L. F. & Jayaraman, V. Generation of stable heading representations in diverse visual scenes. Nature 576, 126–131 (2019).CrossRefPubMedGoogle Scholar
17.↵Fisher, Y. E., Lu, J., D’Alessandro, I. & Wilson, R. I. Sensorimotor experience remaps visual input to a heading-direction network. Nature 576, 121–125 (2019).CrossRefPubMedGoogle Scholar
18.↵Hardcastle, B. J. et al. A visual pathway for skylight polarization processing in Drosophila. Elife 1–23 (2020).Google Scholar
19.↵Omoto, J. J. et al. Visual Input to the Drosophila Central Complex by Developmentally and Functionally Distinct Neuronal Populations. Curr. Biol. 27, 1098–1110 (2017).CrossRefPubMedGoogle Scholar
20.↵Seelig, J. D. & Jayaraman, V. Feature detection and orientation tuning in the Drosophila central complex. Nature 503, 262–266 (2013).CrossRefPubMedWeb of ScienceGoogle Scholar
21.↵Okubo, T. S., Patella, P., D’Alessandro, I. & Wilson, R. I. A neural network for wind-guided compass navigation. Neuron 107, 924–940.e18 (2020).CrossRefPubMedGoogle Scholar
22.↵Garner, D. et al. Connectomic reconstruction predicts visual features used for navigation. Nature 634, 181–190 (2024).CrossRefPubMedGoogle Scholar
23.↵Haberkern, H. et al. Maintaining a stable head direction representation in naturalistic visual environments. bioRxiv 2022.05.17.492284 (2022).Google Scholar
24.↵Scheffer, L. K. et al. A connectome and analysis of the adult Drosophila central brain. Elife 9, (2020).Google Scholar
25.↵Hulse, B. K. et al. A connectome of the Drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection. Elife 10, (2021).Google Scholar
26.Hanesch, U., Fischbach, K. F. & Heisenberg, M. Neuronal architecture of the central complex in Drosophila melanogaster. Cell Tissue Res. 257, 343–366 (1989).CrossRefWeb of ScienceGoogle Scholar
27.Zhang, Z., Li, X., Guo, J., Li, Y. & Guo, A. Two clusters of GABAergic ellipsoid body neurons modulate olfactory labile memory in Drosophila. J. Neurosci. 33, 5175–5181 (2013).Abstract/FREE Full TextGoogle Scholar
28.↵Wolff, T. et al. Cell type-specific driver lines targeting the Drosophila central complex and their use to investigate neuropeptide expression and sleep regulation. Elife 14, (2025).Google Scholar
29.↵Turner-Evans, D. B. et al. The Neuroanatomical Ultrastructure and Function of a Biological Ring Attractor. Neuron 108, 145–163.e10 (2020).CrossRefPubMedGoogle Scholar
30.Homberg, U., Kingan, T. G. & Hildebrand, J. G. Immunocytochemistry of GABA in the brain and suboesophageal ganglion of Manduca sexta. Cell Tissue Res. 248, 1–24 (1987).CrossRefPubMedWeb of ScienceGoogle Scholar
31.↵Schäfer, S. & Bicker, G. Distribution of GABA-like immunoreactivity in the brain of the honeybee: GABA-LIKE IMMUNOREACTIVITY IN BEE BRAIN. J. Comp. Neurol. 246, 287–300 (1986).CrossRefPubMedWeb of ScienceGoogle Scholar
32.↵Cope, A. J., Sabo, C., Vasilaki, E., Barron, A. B. & Marshall, J. A. R. A computational model of the integration of landmarks and motion in the insect central complex. PLoS One 12, 1–19 (2017).CrossRefPubMedGoogle Scholar
33.↵Green, J. & Maimon, G. Building a heading signal from anatomically defined neuron types in the Drosophila central complex. Curr. Opin. Neurobiol. 52, 156–164 (2018).CrossRefPubMedGoogle Scholar
34.↵Dan, C., Hulse, B. K., Kappagantula, R., Jayaraman, V. & Hermundstad, A. M. A neural circuit architecture for rapid learning in goal-directed navigation. Neuron (2024).Google Scholar
35.↵Fisher, Y. E. Flexible navigational computations in the Drosophila central complex. Current Opinion in Neurobiology 73, 102514 (2022).CrossRefPubMedGoogle Scholar
36.↵Giraldo, Y. M. et al. Sun navigation requires compass neurons in Drosophila. Curr. Biol. 28, 2845–2852.e4 (2018).CrossRefPubMedGoogle Scholar
37.↵Basnak, M. A. et al. Multimodal cue integration and learning in a neural representation of head direction. Nat. Neurosci. 1–12 (2025).Google Scholar
38.↵Fisher, Y. E., Marquis, M., D’Alessandro, I. & Wilson, R. I. Dopamine promotes head direction plasticity during orienting movements. Nature 612, 316–322 (2022).CrossRefPubMedGoogle Scholar
39.↵Castillo, P. E., Chiu, C. Q. & Carroll, R. C. Long-term plasticity at inhibitory synapses. Curr. Opin. Neurobiol. 21, 328–338 (2011).CrossRefPubMedGoogle Scholar
40.↵Sjöström, P. J., Turrigiano, G. G. & Nelson, S. B. Neocortical LTD via coincident activation of presynaptic NMDA and cannabinoid receptors. Neuron 39, 641–654 (2003).CrossRefPubMedWeb of ScienceGoogle Scholar
41.Singla, S., Kreitzer, A. C. & Malenka, R. C. Mechanisms for synapse specificity during striatal long-term depression. J. Neurosci. 27, 5260–5264 (2007).Abstract/FREE Full TextGoogle Scholar
42.↵Heifets, B. D., Chevaleyre, V. & Castillo, P. E. Interneuron activity controls endocannabinoid-mediated presynaptic plasticity through calcineurin. Proc. Natl. Acad. Sci. U. S. A. 105, 10250–10255 (2008).Abstract/FREE Full TextGoogle Scholar
43.↵Woodin, M. A., Ganguly, K. & Poo, M.-M. Coincident pre- and postsynaptic activity modifies GABAergic synapses by postsynaptic changes in Cl-transporter activity. Neuron 39, 807–820 (2003).CrossRefPubMedWeb of ScienceGoogle Scholar
44.↵McPartland, J., Di Marzo, V., De Petrocellis, L., Mercer, A. & Glass, M. Cannabinoid receptors are absent in insects. J. Comp. Neurol. 436, 423–429 (2001).CrossRefPubMedGoogle Scholar
45.Vrablik, T. L. & Watts, J. L. Polyunsaturated fatty acid derived signaling in reproduction and development: insights from Caenorhabditis elegans and Drosophila melanogaster: PUFA SIGNALING INWORMS ANDFLIES. Mol. Reprod. Dev. 80, 244–259 (2013).CrossRefPubMedGoogle Scholar
46.↵Zhu, B. et al. Drosophila neurotrophins reveal a common mechanism for nervous system formation. PLoS Biol. 6, e284 (2008).CrossRefPubMedGoogle Scholar
47.↵Kuntz, S., Poeck, B. & Strauss, R. Visual working memory requires permissive and instructive NO/cGMP signaling at presynapses in the Drosophila central brain. Curr. Biol. 27, 613–623 (2017).CrossRefPubMedGoogle Scholar
48.Ueno, K. et al. Carbon monoxide, a retrograde messenger generated in postsynaptic mushroom body neurons, evokes noncanonical dopamine release. J. Neurosci. 40, 3533–3548 (2020).Abstract/FREE Full TextGoogle Scholar
49.Zatsepina, O. G. et al. Genes responsible for H2S production and metabolism are involved in learning and memory in Drosophila melanogaster. Biomolecules 12, 751 (2022).PubMedGoogle Scholar
50.Schuman, E. M. & Madison, D. V. Nitric oxide and synaptic function. Annu. Rev. Neurosci. 17, 153–183 (1994).CrossRefPubMedWeb of ScienceGoogle Scholar
51.Duan, J. et al. Nitric oxide signaling modulates cholinergic synaptic input to projection neurons in Drosophila antennal lobes. Neuroscience 219, 1–9 (2012).CrossRefPubMedGoogle Scholar
52.↵Wildemann, B. & Bicker, G. Nitric oxide and cyclic GMP induce vesicle release at Drosophila neuromuscular junction. J. Neurobiol. 39, 337–346 (1999).CrossRefPubMedWeb of ScienceGoogle Scholar
53.↵Hawkins, R. D., Abrams, T. W., Carew, T. J. & Kandel, E. R. A cellular mechanism of classical conditioning in Aplysia: activity-dependent amplification of presynaptic facilitation. Science 219, 400–405 (1983).Abstract/FREE Full TextGoogle Scholar
54.↵Waddell, S. Reinforcement signalling in Drosophila; dopamine does it all after all. Curr. Opin. Neurobiol. 23, 324–329 (2013).CrossRefPubMedGoogle Scholar
55.↵Atwood, B. K., Lovinger, D. M. & Mathur, B. N. Presynaptic long-term depression mediated by Gi/o-coupled receptors. Trends Neurosci. 37, 663–673 (2014).CrossRefPubMedGoogle Scholar
56.↵Sinakevitch, I. & Strausfeld, N. J. Comparison of octopamine-like immunoreactivity in the brains of the fruit fly and blow fly. J. Comp. Neurol. 494, 460–475 (2006).CrossRefPubMedWeb of ScienceGoogle Scholar
57.↵Bonanno, S. L. et al. Constitutive and conditional Epitope tagging of endogenous G-protein-coupled receptors in Drosophila. J. Neurosci. 44, e2377232024 (2024).Abstract/FREE Full TextGoogle Scholar
58.El-Kholy, S. et al. Expression analysis of octopamine and tyramine receptors in Drosophila. Cell Tissue Res. 361, 669–684 (2015).CrossRefPubMedGoogle Scholar
59.↵Lee, H.-G., Seong, C.-S., Kim, Y.-C., Davis, R. L. & Han, K.-A. Octopamine receptor OAMB is required for ovulation in Drosophila melanogaster. Dev. Biol. 264, 179–190 (2003).CrossRefPubMedWeb of ScienceGoogle Scholar
60.↵Kim, Y.-C., Lee, H.-G., Lim, J. & Han, K.-A. Appetitive learning requires the alpha1-like octopamine receptor OAMB in the Drosophila mushroom body neurons. J. Neurosci. 33, 1672–1677 (2013).Abstract/FREE Full TextGoogle Scholar
61.↵Eddison, M. Expansion-assisted iterative fluorescence in situ hybridization (EASI-FISH) in Drosophila CNS v1. (2022) doi:10.17504/protocols.io.5jyl8jmw7g2w/v1.CrossRefGoogle Scholar
62.↵Sun, F. et al. Next-generation GRAB sensors for monitoring dopaminergic activity in vivo. Nat. Methods 17, 1156–1166 (2020).CrossRefPubMedGoogle Scholar
63.↵Lv, M. et al. An octopamine-specific GRAB sensor reveals a monoamine relay circuitry that boosts aversive learning. Natl. Sci. Rev. 11, nwae112 (2024).PubMedGoogle Scholar
64.↵Aimon, S., Cheng, K. Y., Gjorgjieva, J. & Grunwald Kadow, I. C. Global change in brain state during spontaneous and forced walk in Drosophila is composed of combined activity patterns of different neuron classes. Elife 12, (2023).Google Scholar
65.↵Dana, H. et al. High-performance calcium sensors for imaging activity in neuronal populations and microcompartments. Nat. Methods 16, 649–657 (2019).CrossRefPubMedGoogle Scholar
66.↵Allen, A. M. et al. A high-resolution atlas of the brain predicts lineage and birth order underly neuronal identity. bioRxiv 2025.06.04.657818 (2025) doi:10.1101/2025.06.04.657818.Abstract/FREE Full TextGoogle Scholar
67.↵Zhang, Y. et al. Fast and sensitive GCaMP calcium indicators for imaging neural populations. Nature 615, 884–891 (2023).CrossRefPubMedGoogle Scholar
68.Dana, H. et al. Sensitive red protein calcium indicators for imaging neural activity. Elife 5, (2016).Google Scholar
69.↵Sun, Y. et al. Neural signatures of dynamic stimulus selection in Drosophila. Nat. Neurosci. 20, 1104–1113 (2017).CrossRefPubMedGoogle Scholar
70.↵Govorunova, E. G. et al. Kalium channelrhodopsins are natural light-gated potassium channels that mediate optogenetic inhibition. Nat. Neurosci. 25, 967–974 (2022).CrossRefPubMedGoogle Scholar
71.↵Yamada, D., Davidson, A. M. & Hige, T. Cyclic nucleotide-induced bidirectional long-term synaptic plasticity in Drosophila mushroom body. bioRxivorg (2024) doi:10.1101/2023.09.28.560058.Abstract/FREE Full TextGoogle Scholar
72.↵Handler, A. et al. Distinct Dopamine Receptor Pathways Underlie the Temporal Sensitivity of Associative Learning. Cell 178, 60–75.e19 (2019).CrossRefPubMedGoogle Scholar
73.↵Burke, C. J. et al. Layered reward signalling through octopamine and dopamine in Drosophila. Nature 492, 433–437 (2012).CrossRefPubMedGoogle Scholar
74.↵Cassenaer, S. & Laurent, G. Conditional modulation of spike-timing-dependent plasticity for olfactory learning. Nature 482, 47–52 (2012).CrossRefPubMedWeb of ScienceGoogle Scholar
75.↵Suver, M. P., Mamiya, A. & Dickinson, M. H. Octopamine neurons mediate flight-induced modulation of visual processing in drosophila. Curr. Biol. 22, 2294–2302 (2012).CrossRefPubMedGoogle Scholar
76.↵Crocker, A. & Sehgal, A. Octopamine Regulates Sleep in Drosophila through Protein Kinase A-Dependent Mechanisms. Journal of Neuroscience 28, 9377–9385 (2008).Abstract/FREE Full TextGoogle Scholar
77.↵Zhou, C. et al. Molecular genetic analysis of sexual rejection: roles of octopamine and its receptor OAMB in Drosophila courtship conditioning. J. Neurosci. 32, 14281–14287 (2012).Abstract/FREE Full TextGoogle Scholar
78.↵Youn, H., Kirkhart, C., Chia, J. & Scott, K. A subset of octopaminergic neurons that promotes feeding initiation in drosophila melanogaster. PLoS One 13, 1–16 (2018).CrossRefPubMedGoogle Scholar
79.↵Watanabe, K. et al. A circuit node that integrates convergent input from neuromodulatory and social behavior-promoting neurons to control aggression in Drosophila. Neuron 95, 1112–1128.e7 (2017).CrossRefPubMedGoogle Scholar
80.↵Koon, A. C. et al. Autoregulatory and paracrine control of synaptic and behavioral plasticity by octopaminergic signaling. Nat. Neurosci. 14, 190–199 (2011).CrossRefPubMedWeb of ScienceGoogle Scholar
81.↵Bakshinska, D. et al. Synapse-specific catecholaminergic modulation of neuronal glutamate release. Proc. Natl. Acad. Sci. U. S. A. 122, e2420496121 (2025).CrossRefPubMedGoogle Scholar
82.↵Shiozaki, H. M. & Kazama, H. Parallel encoding of recent visual experience and self-motion during navigation in Drosophila. Nat. Neurosci. 20, 1395–1403 (2017).CrossRefPubMedGoogle Scholar
83.↵Donlea, J. M. et al. Recurrent circuitry for balancing sleep need and sleep. Neuron 97, 378–389.e4 (2018).CrossRefPubMedGoogle Scholar
84.Liu, S., Liu, Q., Tabuchi, M. & Wu, M. N. Sleep Drive Is Encoded by Neural Plastic Changes in a Dedicated Circuit. Cell 165, 1347–1360 (2016).CrossRefPubMedGoogle Scholar
85.↵Pimentel, D. et al. Operation of a homeostatic sleep switch. Nature (2016).Google Scholar
86.↵Aso, Y. et al. Nitric oxide acts as a cotransmitter in a subset of dopaminergic neurons to diversify memory dynamics. Elife 8, (2019).Google Scholar
87.↵Gonzalez, K. C. et al. Synaptic basis of feature selectivity in hippocampal neurons. Nature 637, 1152–1160 (2025).CrossRefPubMedGoogle Scholar
88.↵Milstein, A. D. et al. Bidirectional synaptic plasticity rapidly modifies hippocampal representations. Elife 10, (2021).Google Scholar
89.↵Bittner, K. C., Milstein, A. D., Grienberger, C., Romani, S. & Magee, J. C. Behavioral time scale synaptic plasticity underlies CA1 place fields. Science 357, 1033–1036 (2017).Abstract/FREE Full TextGoogle Scholar
90.↵Li, Y., Briguglio, J. J., Romani, S. & Magee, J. C. Mechanisms of memory-supporting neuronal dynamics in hippocampal area CA3. Cell 187, 6804–6819.e21 (2024).CrossRefPubMedGoogle Scholar
91.↵Feldman, D. E. The Spike-Timing Dependence of Plasticity. Neuron 75, 556–571 (2012).CrossRefPubMedWeb of ScienceGoogle Scholar
92.↵Hige, T., Aso, Y., Modi, M. N., Rubin, G. M. & Turner, G. C. Heterosynaptic Plasticity Underlies Aversive Olfactory Learning in Drosophila. Neuron 88, 985–998 (2015).CrossRefPubMedGoogle Scholar
93.↵Brunelli, M., Castellucci, V. & Kandel, E. R. Synaptic facilitation and behavioral sensitization in Aplysia: possible role of serotonin and cyclic AMP. Science 194, 1178–1181 (1976).Abstract/FREE Full TextGoogle Scholar
94.↵Eschbach, C. et al. Recurrent architecture for adaptive regulation of learning in the insect brain. Nat. Neurosci. 23, (2020).Google Scholar
95.Cohn, R., Morantte, I. & Ruta, V. Coordinated and Compartmentalized Neuromodulation Shapes Sensory Processing in Drosophila. Cell 163, 1742–1755 (2015).CrossRefPubMedGoogle Scholar
96.↵Aso, Y. & Rubin, G. M. Dopaminergic neurons write and update memories with cell-type-specific rules. Elife 5, 1–15 (2016).CrossRefPubMedGoogle Scholar
97.↵Tritsch, N. X. & Sabatini, B. L. Dopaminergic modulation of synaptic transmission in cortex and striatum. Neuron 76, 33–50 (2012).CrossRefPubMedWeb of ScienceGoogle Scholar
98.↵Lesch, K.-P. & Waider, J. Serotonin in the modulation of neural plasticity and networks: implications for neurodevelopmental disorders. Neuron 76, 175–191 (2012).CrossRefPubMedWeb of ScienceGoogle Scholar
99.↵Bergles, D. E., Doze, V. A., Madison, D. V. & Smith, S. J. Excitatory actions of norepinephrine on multiple classes of hippocampal CA1 interneurons. J. Neurosci. 16, 572–585 (1996).FREE Full TextGoogle Scholar
100.Bean, B. P. Neurotransmitter inhibition of neuronal calcium currents by changes in channel voltage dependence. Nature 340, 153–156 (1989).CrossRefPubMedWeb of ScienceGoogle Scholar
101.↵Starke, K. Regulation of noradrenaline release by presynaptic receptor systems. Rev. Physiol. Biochem. Pharmacol. 77, 1–124 (1977).CrossRefPubMedWeb of ScienceGoogle Scholar
102.↵Schultz, W. Dopamine reward prediction error coding. Dialogues Clin. Neurosci. 18, 23–32 (2016).CrossRefPubMedGoogle Scholar
103.Lerner, T. N., Holloway, A. L. & Seiler, J. L. Dopamine, updated: Reward prediction error and beyond. Curr. Opin. Neurobiol. 67, 123–130 (2021).CrossRefPubMedGoogle Scholar
104.↵Sara, S. J. & Bouret, S. Orienting and reorienting: the locus coeruleus mediates cognition through arousal. Neuron 76, 130–141 (2012).CrossRefPubMedWeb of ScienceGoogle Scholar
105.↵Jensen, K. T., Hennequin, G. & Mattar, M. G. A recurrent network model of planning explains hippocampal replay and human behavior. Nat. Neurosci. 27, 1340–1348 (2024).CrossRefPubMedGoogle Scholar
106.Whittington, J. C. R. et al. Article The Tolman-Eichenbaum Machine : Unifying Space and Relational Memory through Generalization in the Hippocampal Formation ll The Tolman-Eichenbaum Machine : Unifying Space and Relational Memory through Generalization in the Hippocampal Formation. Cell 183, 1249–1263.e23 (2020).CrossRefPubMedGoogle Scholar
107.↵Chandra, S., Sharma, S., Chaudhuri, R. & Fiete, I. Episodic and associative memory from spatial scaffolds in the hippocampus. Nature 638, 739–751 (2025).CrossRefPubMedGoogle Scholar
108.↵Klapoetke, N. C. et al. Independent optical excitation of distinct neural populations. Nat. Methods 11, 338–346 (2014).CrossRefPubMedWeb of ScienceGoogle Scholar
109.↵Pfeiffer, B. D. et al. Refinement of tools for targeted gene expression in Drosophila. Genetics 186, 735–755 (2010).Abstract/FREE Full TextGoogle Scholar
110.Vogt, K. et al. Shared mushroom body circuits underlie visual and olfactory memories in Drosophila. Elife 3, e02395 (2014).CrossRefPubMedGoogle Scholar
111.Shuai, Y. et al. Driver lines for studying associative learning in Drosophila. Elife 13, (2025).Google Scholar
112.↵Nern, A., Pfeiffer, B. D. & Rubin, G. M. Optimized tools for multicolor stochastic labeling reveal diverse stereotyped cell arrangements in the fly visual system. Proc. Natl. Acad. Sci. U. S. A. 112, E2967–76 (2015).Abstract/FREE Full TextGoogle Scholar
113.↵Moore, R. J. D. et al. FicTrac: A visual method for tracking spherical motion and generating fictive animal paths. J. Neurosci. Methods 225, 106–119 (2014).CrossRefPubMedGoogle Scholar
114.↵Reiser, M. B. & Dickinson, M. H. A modular display system for insect behavioral neuroscience. J. Neurosci. Methods 167, 127–139 (2008).CrossRefPubMedWeb of ScienceGoogle Scholar
115.↵Sofroniew, N., et al. Napari: A Multi-Dimensional Image Viewer for Python. (Zenodo, 2025). doi:10.5281/ZENODO.17367124.CrossRefGoogle Scholar
116.↵Plaza, S. M. et al. neuPrint: An open access tool for EM connectomics. Front. Neuroinform. 16, 896292 (2022).PubMedGoogle Scholar
117.↵Hagberg, A. A., Schult, D. A. & Swart, P. J. Exploring network structure, dynamics, and function using NetworkX. in Proceedings of the Python in Science Conference 11–15 (SciPy, 2008). doi:10.25080/tcwv9851.CrossRefGoogle Scholar
118.↵Hulse, B. et al. A connectome of the Drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection. eLife 10, (2020).Google Scholar
119.↵Gouwens, N. W. & Wilson, R. I. Signal propagation in Drosophila central neurons. J. Neurosci. 29, 6239–6249 (2009).Abstract/FREE Full TextGoogle Scholar
120.↵Close, K., He, Y., Jeter, J., Ihrke, G. & Eddison, M. Multiplex detection of gene expression in the intact Drosophila brain using expansion-assisted iterative fluorescence in situ hybridization. J. Vis. Exp. e67656 (2025) doi:10.3791/67656.CrossRefGoogle Scholar
121.↵Meissner, G. W. et al. Mapping neurotransmitter identity in the whole-mount Drosophila brain using multiplex high-throughput fluorescence in situ hybridization. Genetics 211, 473–482 (2019).Abstract/FREE Full TextGoogle Scholar
122.↵Soumillon, M., Cacchiarelli, D., Semrau, S., van Oudenaarden, A. & Mikkelsen, T. S. Characterization of directed differentiation by high-throughput single-cell RNA-Seq. bioRxiv (2014) doi:10.1101/003236.Abstract/FREE Full TextGoogle Scholar
123.↵Martin, M. Cutadapt removes adapter sequences from high-throughput sequencing reads. EMBnet J. 17, 10 (2011).CrossRefGoogle Scholar
124.↵Dobin, A. et al. STAR: ultrafast universal RNA-seq aligner. Bioinformatics 29, 15–21 (2013).CrossRefPubMedWeb of ScienceGoogle Scholar
125.↵Clements, J. et al. neuPrint: Analysis Tools for EM Connectomics. Cold Spring Harbor Laboratory 2020.01.16.909465 (2020).Google Scholar
126.↵Dorkenwald, S. et al. FlyWire: online community for whole-brain connectomics. Nat. Methods 19, 119–128 (2022).CrossRefPubMedGoogle Scholar
 Back to top
 Previous
Next 
Posted December 15, 2025.
Download PDF
Print/Save Options
Email
Share
Citation Tools
Get QR code
Subject Area
Neuroscience

Reviews and Context

0

Comment

0

TRIP Peer Reviews

0

Community Reviews

1

Automated Services

0

Blogs/Media

0

Author Videos

Invitation to beta test

Explore references, terminology, expanded figures, and related works in the context of the original preprint.

Try Curvenote Reader  
Subject Areas
All Articles
Animal Behavior and Cognition
Biochemistry
Bioengineering
Bioinformatics
Biophysics
Cancer Biology
Cell Biology
Clinical Trials
Developmental Biology
Ecology
Epidemiology
Evolutionary Biology
Genetics
Genomics
Immunology
Microbiology
Molecular Biology
Neuroscience
Paleontology
Pathology
Pharmacology and Toxicology
Physiology
Plant Biology
Scientific Communication and Education
Synthetic Biology
Systems Biology
Zoology
Abstract
Main text
Discussion
Methods
Contributions
Acknowledgements