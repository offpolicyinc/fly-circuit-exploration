# Flores-Valle et al. — "Goal learning, memory, and drift in the Drosophila head direction system" — bioRxiv 10.1101/2025.03.20.644317v1

Captured 2026-09-10 via in-app browser get_page_text from https://www.biorxiv.org/content/10.1101/2025.03.20.644317v1.full. Figures not saved.


ABSTRACT

Selecting and memorizing goal direction are essential for navigation behavior. Heading information is represented in the head direction systems across species, including Drosophila. However, how navigation decisions are made and how goal memories are represented in these systems is little understood. Here, using a navigation learning assay for flies walking in virtual reality during two-photon imaging, we describe neural dynamics for direction selection and memory. We find that neurons which encode walking direction in the fan-shaped body, a navigation and learning related area in the center of the fly brain, show continuing autonomous activity or directional drift when the animal is at rest. Drift during rest centers around opposite directions to activity during walking, suggesting different computations between these two behavioral states. Targeted optogenetic activation of these neurons during rest is sufficient to induce a subsequent directional navigation preference. Learning leads to changes in drift distributions during rest depending on goal direction, revealing a memory in the network. The fly’s head direction system thus offers a compact architecture for direction selection, learning, and memory. Changes in neural representations due to goal learning and between rest and walking suggest similarities in navigation circuits across species.

Animal movement is shaped by memory across species1. Many animals, including a variety of insects2, navigate over long distances relying on memories of visual cues and the features attributed to these memories are key for decision making1–4. Navigation towards visual cues or goals requires selecting and maintaining a goal in memory during behavior2,5,6. An animal’s orientation with respect to visual cues is represented in the head direction system7–11. Goal related navigation circuits have been described in bats12, rats5,6, and insects, including Drosophila8,13–17. While mammalian place and grid cells change their spatial arrangement during goal learning5,6,8,18, less is known about head direction cells. In mammalian circuits, decision making and learning are additionally accompanied by navigation-related activity during rest and sleep, such as reactivation19–24.

In Drosophila, memories for visual navigation behavior have been located in the central complex (CX)25–29, a brain area at the center of sensorimotor integration. The CX contains the fly’s head direction system with circuits that share features of ring attractor networks9,10,30–34. Head direction circuits, including neurons that determine goal direction14, have been investigated using two-photon imaging in flies during learning behavior35,36.

Behavior, physiology, and computational modeling point to the importance of of the fan-shaped body, a substructure of the CX, for the encoding of memory, and propose mechanisms for direction selection6,8,10,16,17,37. However, where behavioral decisions, such as a choice of navigation direction, occur in the network, and how selected goals are memorized and shape locomotion remains poorly understood6,38,39.

Here we describe direction selection and memory formation in the Drosophila fan-shaped body. We use imaging and optogenetics in head-fixed walking flies navigating in a mechanically actuated virtual reality arena40,41to show that a navigation-related population of columnar fan-shaped body neurons (PFR neurons) is critical for direction selection. PFR neurons track traveling direction during walking as previously described42–44. However, we find that different from other columnar CX neurons, PFR neurons show continuing drift of activity over columns or directions while the animal is at rest, either standing still or grooming. Drift during rest centers around directions opposite to activity during walking, indicating a difference in computations between rest and walking states. Optogenetic activation during rest is sufficient to change drift distributions and to guide subsequent behavior. Learning shapes drift distributions depending on goal direction, revealing a lasting memory in the network. Additionally, we find that fan-shaped body layers are activated by the reinforcing temperature stimulus. These experiments reveal dynamics for direction selection, learning, and memory during rest and navigation in the fly brain.

PFR neurons show drift during rest

For imaging neural activity in navigating flies, we combined a virtual mechanical arena with a diameter of 0.5 meters (Fig. 1a and Supplementary Fig. S1a) in which flies can perform spatial learning40 with two-photon calcium imaging47,48. In this setup tethered flies navigate on an air supported ball and the read-out of ball motion serves to rotate and translate the arena in two dimensions (Fig. 1b, see Methods)40. The relative positions and orientations of the fly with respect to the arena remain thus similar to those of an animal walking freely in a stationary arena. In these experiments, the arena featured a single bright vertical stripe on an otherwise dark background (Fig. 1a and b). Flies could freely explore the arena (in closed loop) for 5 minutes in 3 trials starting at the center of the arena.

Download figureOpen in new tab
Figure 1.

Virtual reality setup and PFR drift. a Mechanical virtual reality (colors for visualization). Cube of 100 mm length is shown for scale. A smaller version of the mechanical arena as well as place learning behavior without imaging are described in40 and in Methods. b A fly walks on an air-suspended ball inside the moving cylindrical arena, enabling 2D navigation (translation in x, y and rotation around θ). The arena, shown here with a bright stripe on a black background, moves while the fly remains stationary during two-photon imaging. c PFRa neurons, a subpopulation of PFR neurons (see Supplementary Information), projecting to the FB, each in a different color. Image downloaded from45,46 d Expression of calcium indicator in PFR neurons with 27G06-GAL4 (average of 500 frames), which also labels other populations (in the ellipsoid body). Right: ROIs across the FB. e Example of PFR calcium activity during navigation. Top: fly velocity. Middle: PFR activity across 16 ROIs (panel d) during rest (green) and walking (black). Bottom: PFR phase during rest (green) and walking (black), and fly orientation in the arena (orange). f PFR phase distribution during rest (top) and walking (middle), and fly orientation distribution in VR across 16 bins (bottom) for the fly in e. g Example of PFR calcium activity during 30 seconds of rest. Top: PFR activity across 16 ROIs. Bottom: PFR phase during rest (green) and fly orientation in the arena (orange). h Absolute PFR phase displacement from 24 flies during continuous rest (green) and walking (black) epochs, with red lines representing the linear fit (see Methods). i PFR phase velocity during rest (green) and walking (black) in cycles per second (cycles across the 16 ROIs) for 24 flies. Three asterisks show statistical significance based on a paired t-test across flies (p < 0.00005). j PFR phase density during rest for all flies, with maximum aligned to 270 degrees. k PFR phase density and l fly orientation during walking across 16 bins aligned to their PFR phase density peak during rest. m Fly trajectories (left) and position density binned in a 30 mm grid in the arena (right), aligned by PFR phase density peak during rest for all flies. n Arena azimuth angle across 16 bins (see angles in panel m, left) of all flies aligned based on their PFR phase density peak during rest. Asterisks in density panels (h, i, and k) indicate significant differences between 90° and 270° (Kolmogorov-Smirnov test: p < 0.005 (**), p < 0.0005 (***)).

PFR neurons project into different FB columns (Fig. 1c, see Methods) and receive input from hΔB neurons, which encode the traveling direction of the fly in allocentric coordinates (Supplementary Fig. S5a)42–44. PFR neurons therefore show similar dynamics to hΔB neurons44. To record activity during navigation we expressed the calcium indicator GCaMP8m49 in PFR neurons using the GAL4 line R27G0650 (R27G06-GAL4 > UAS-GCaMP8m, Fig. 1d).

PFR activity formed a moving bump or cosine-like profile across the FB during walking (see Supplementary Fig. S2d and Methods) with its phase (see Methods) tracking traveling direction relative to the bright stripe as previously described42–44. Heading direction signals display an arbitrary offset relative to landmarks30 and the offset between the bright stripe position and PFR phase was removed (see Methods and Fig. 1e, black). We occasionally observed phase jumps, which could indicated different traveling directions, such as diagonal, sideways, or backward walking43,44.

We found that when the fly is standing still, PFR activity nevertheless drifts (Fig. 1e, green)51, maintaining a cosine-like activity profile similar to that during walking (see Supplementary Fig. S2d and Methods). This differs from other head direction cells, where bump position is stable during periods of rest over tens of seconds30. Drift in PFR neurons has been observed anecdotally44, but we find that drift persists over long bouts of immobility (Fig. 1g). Drift activity moved at about twice the speed of activity observed during walking (Fig. 1h and i, see Methods).

PFR phase shifts by 180 degree between rest and walking

Comparing PFR activity during rest and walking epochs in a trial of 5 minutes of navigation (Fig. 1e) shows that the distribution of PFR phase drift during rest is approximately inverse to the phase distribution during walking (Fig. 1f), that is, highest in FB columns that are inactive during walking and vice versa. Since PFR phase corresponds to traveling direction of the fly in the arena during walking, orientation in the arena is also inverse to the distribution during rest (Fig. 1f, orange).

To compare activity distributions across trials and flies, we first removed the arbitrary phase offset intrinsic to heading direction signals (see Methods). We aligned the imaging data based on their phase distribution during rest and with the peak of the distribution arbitrarily defined as 270 degrees (called ’rest-phase offset’ in the following, Fig. 1j). After aligning, the PFR phase distribution during walking was shifted by 180 degrees compared to that during rest (centered around 90 degrees, Fig. 1k), consistently revealing a 180-degree offset across flies.

Similarly, after aligning all orientations and walking trajectories in the arena by rotating them by the rest-phase offset, we found that the orientation of flies was shifted by 180 degrees compared to the peak of the PFR phase distribution during rest (Fig. 1l, centered around 90 degrees). In these experiments, flies mostly walked outwards from the center of the arena at the beginning of the trial towards the rim of the arena at the end of the trial. Therefore, after aligning the trajectories by rotating them by the rest-phase offset, flies mostly walked in the direction opposite to the peak PFR phase distribution at rest (Fig. 1m and n, centered around 90 degrees). This shows that the 180 degree phase shift between walking and rest also occurs during directional walking. Thus, PFR activity during rest is shifted by 180 degrees compared to activity during walking, orientation in the arena, and travel direction, suggesting different computations between rest and walking.

Optogenetic writing of navigation direction during rest

Neural activity during immobility is important for decision making, planning, memory consolidation, and learning in mammalian navigation circuits19–24 and could also play a similar role in the fly. We therefore asked whether PFR activity during walking was driving activity during rest or if vice versa PFR activity during rest was influencing subsequent activity during walking and behavior.

To monitor and perturb activity at the same time, we combined two-photon imaging with optogenetics (Fig. 2a, see Methods)33,52. We expressed the calcium indicator jGCaMP8m49 together with CsChrimson53 and used a red laser and a spatial light modulator for targeted neuronal activation (Fig. 2a, see Methods)52. This approach avoided GCaMP8m excitation due to optogenetic activation, ensuring that fluorescence changes during activation only reflected changes in calcium activity.

Download figureOpen in new tab
Figure 2.

Optogenetic activation during rest drives subsequent behavior. a Setup for combined local optogenetic activation and two-photon calcium imaging in behaving flies. A red laser is reflected off an SLM and activation patterns as well as a laser for two-photon imaging a targeted to the fly brain. b Optogenetic activation of PFR columns during rest in navigating flies. Top: laser for optogenetics is only switched on when the fly rests (walking velocity is zero). First row: walking velocity of the fly. Second row: fluorescence from 16 ROIs defined in the FB. Optogenetic activation was performed in columns on one side of the FB (shown on the left). Third row: phase of PFR neurons (see Methods), during walking (black) and rest (green). Orange: fly orientation in the mechanical virtual reality. c Top: PFR phase distribution during rest. Red triangle indicates corresponding optogenetic activation site. Center and bottom: PFR phase and fly orientation distributions across 16 bins during walking, respectively. d Left: PFR distribution during rest (green) and walking (black) for flies expressing CsChrimson (top) and for control flies (bottom). Activation was performed on the right side of the FB (red arrow). Right: same as left, but for activation on the left side of the FB. e Distributions of fly orientation in the arena across 16 bins during activation on the right side of the FB (left) and left side of the FB (right) for flies expressing CsChrimson (top) and control flies (bottom). f Top: trajectories of flies expressing CsChrimson in mechanical VR during activation on the right side of FB (left) and activation on the left side of FB (right). Bottom: position density of all flies in the arena, binned in a 30 mm square grid for right-side (left) and left-side (right) activation. g Same as f, but for control flies. For clarity, only the last 5 minutes of the 10-minute trials are shown in the trajectories (top part of panels f and g). h Same as e but showing azimuth angle distributions in mechanical VR across 16 bins.

In these experiments, flies could again freely explore the arena (closed loop) with a single bright stripe. Rest was detected in real-time, and activation of a subset of columns of PFR neurons during rest (Fig. 2b, top and second) resulted in an increase in calcium at the activated site (Fig. 2c, green). Activation ended as soon as the fly resumed walking. During subsequent walking, neurons tracked walking direction as expected.

The PFR phase distribution and the distribution of the orientation of the fly in the arena during walking following activation during rest were opposite to the activated direction (Fig. 2c, black and yellow, respectively). Across flies, activation on either the left or right side of the FB during rest (see Methods) caused a 180-degree shift in the phase distribution during subsequent walking (Fig. 2d). Following left or right activation flies were oriented in opposite directions relative to the activation site (Fig. 2e), and also walked in opposite directions in the arena (Fig. 2f). As a result, flies occupied the opposite direction in the arena relative to the activation site (Fig. 2h). These effects were not observed in control flies (Fig. 2g, h). Thus, optogenetics activation of PFR neurons during rest was sufficient to drive behavior in the opposite direction of the activation site.

Goal memory emerges during learning

We next asked whether directional learning would lead to changes in PFR drift. Given that drift activity during rest can influence subsequent behavior (Fig. 2), we reasoned that vice versa learning and memory which results in directed navigation behavior could lead to changes in drift distributions during rest. We combined an assay for tethered place learning (Fig. 3a, b)40, similar to place learning in freely walking flies28, with two-photon calcium imaging. In these experiments, flies learned to find a cool area in the mechanical virtual reality with two visual landmarks, one bright (yellow in Fig. 3a) and one dim (gray in Fig. 3a, see Methods). To simulate the cool area, the fly was heated with an IR laser (Fig. 3b) unless it entered the cool area (green area in Fig. 3a, left), where the IR laser switched off. Flies were trained for 10 trials and each trial lasted until the fly stayed inside the cool area for at least 10 s. The position of the bright and dim stripes were then swapped, the cool area staying with the same stripe, thus repositioning the fly and the goal to opposite sides of the arena. The next trial then started with the fly again navigating in closed loop to the cool area (Fig. 3a, right). If the fly did not find the cool area within 15 minutes during a trial, a new trial started (again after swapping dim and bright stripe position as well as the cool area, see Methods).

Download figureOpen in new tab
Figure 3.

PFR activity during learning. a Schematic of behavior protocol for place learning experiment: flies are trained over 10 trials in a mechanical arena with two stripes (one dim, one bright, see Methods). a. First trial: fly starts at center of arena, has to reach cool area, and stay there for 10 seconds (red line). The two stripes switch positions, and the cool area moves to the other side. The fly has to reorient and find the cool area again. This pattern repeats for all trials, with the cool area and stripes switching upon trial completion. b The aversive heat stimulus is delivered with an IR laser, focused on the thorax of the fly using a mirror. The laser is switched off in the cool area. c Left: time taken for all flies to reach the cool area, positioned in front of the bright stripe for 10 trials. Right: time to reach the cool area after a 20 minute-break. d: Same as c, but with the cool area in front of the dim stripe. e First row: fly trajectories over trials 1, 4, 7, and 10 when trained with cool area in front of the bright stripe (protocol schematic in first column). Second row: same as previous, but with the cool area in front of the dim stripe. f Example of place learning during imaging for a single fly. Top row: trial number. First row: walking velocity. Second row: fluorescence in the FB during walking (black) and resting (green). Third row: fly orientation (orange) and PFR phase during walking (black) and rest (green). The offset between PFR phase and arena orientation is corrected so that fluorescence and PFR phase during walking align with fly orientation (see Methods). g PFR phase density during rest across trials for the fly in panel f. The green rectangle indicates the direction of the cool area (90 degrees for the bright stripe). h Top: PFR phase density during rest across trials 1-3 (left), 3-7 (center), and 7-10 (right) for all flies trained with the cool area in front of the bright stripe (at a 90-degree direction, schematic on left). On the right, PFR phase density during rest over 1 trial after the 20-minute break. Bottom: same as top, but with cool area in front of the dim stripe (at 270-degree direction). Light green traces represent individual flies; thick green lines show averages. i Same as panel h but for PFR phase density during walk. Asterisks in panels h and i indicate statistical significance between distribution sets, determined using a t-test on the reduced distribution for each fly (projected to one dimension via PCA, see Methods). Significance levels: p < 0.05 (*), p < 0.005 (**), p < 0.0005 (***).

Flies could learn to navigate to the cool area located both in front of the bright (Fig. 3c, left side) or dim stripe (Fig. 3d, left side) during two-photon imaging, although with better learning performance for the bright stripe. Fig. 3e shows trajectories of all flies during a subset of trials. An example of a fly that learns to locate the cool area positioned in front of the bright stripe across 10 trials is shown in Fig. 3f. All imaging data were aligned to the orientation of the fly in the arena to correct for the offset between arena orientation and PFR phase (see Methods). Learning led to a shift in the PFR phase distribution during rest over multiple trials in the direction opposite to that of the cool area (Fig. 3g). Similarly, across flies learning induced a shift in the PFR phase distribution during rest, with a peak in the PFR phase distribution opposite to goal location in the last trials (Fig. 3h and Methods). This shift was observed in experiments with both, the bright stripe or the dim stripe indicating goal location (Fig. 3g, top and bottom, respectively). During walking, the PFR phase was more strongly centered around the goal direction (Fig. 3i), consistent with the expected 180-degree shift between walking and resting, as well as the learned goal-directed behavior.

After 10 trials, flies rested for 20 minutes, after which their memory for the location of the cool area was tested again with an additional trial. Flies trained with the cool area in front of the bright stripe still remembered its location (Fig. 3c, e right side). Similarly, the signature of memory in the drift distribution during rest and PFR phase during walking still persisted after 20 minutes (Fig. 3h and i, top right). Flies trained with the cool area in front of the dim stripe, which led to poorer learning performance, could not reliably memorize the position of the cool area (Fig. 3d and e right side), nor did the drift distribution during rest show memory (Fig. 3h, bottom right). Together, these experiments show that direction learning results in lasting changes in the CX network which are reflected in the distribution of the PFR phase during rest. Additionally, since rest activity drives subsequent behavior (Fig. 2), drift activity during rest may play a role in guiding fly behavior toward the memorized goal.

The FB is thought to encode attributes for directions in tangential neurons4,6,16,54,55. We identified a population of tangential neurons in dorsal FB layers which respond to the change in temperature of the cool area (see Supplementary Fig. S3 and Supplementary Information). This shows that in addition to direction information, also changes in temperature are encoded in the FB network which could serve to reinforce preferred directions.

Model of drift and phase switching

A simplified computational model can describe drift in PFR neurons during rest (Fig. 1g) and the 180-degree phase shift between rest and walking. We first assume that PFR neurons are part of a ring attractor network. PFR neurons receive input from Δ7 neurons in the protocerebral bridge (PB), which follow a sinusoidal connectivity pattern, as proposed in ring attractor network models16,17,56,57. In ring attractors, activity can drift due to asymmetries in connectivity or noise in background input58–60. We model a ring attractor with synaptic depression58 and background noise, which induces continuous drift. Drift in the model results from the most active neuron inhibiting all others, but sustained activity leading to synaptic depression of the output of the dominant neuron over time. As activity decays, another neuron becomes dominant, repeating the cycle (see Supplementary Fig. S4a and Supplementary Information).

During walking, strong input from hΔB neurons, which encode traveling direction43,44, drives the network and overcomes drift (Supplementary Fig. S4b, blue and black). We assume that hΔB neurons are inactive during rest, since no drift has been reported in these neurons during rest44. As a result, synaptic depression dynamics become dominant, leading to drift activity in PFR neurons. The activity shifts toward neurons that were less active during walking (Supplementary Fig. S4b, right side in green), producing a 180-degree activity shift between walking and rest (Supplementary Fig. S4c).

The developed model suggests that the 180-degree shift in the PFR phase distribution between rest and walking is driven by synaptic depression. Furthermore, synaptic depression and background input noise produce fluctuations during rest. Downstream neurons, such as hΔA neurons, could exploit this drift and phase shift to reactivate FB circuits during rest, facilitating memory consolidation (see Supplementary Information for details of connectivity and model implementation). Alternatively, the 180-degree shift in the distribution of PFR neurons during rest combined with anti-Hebbian plasticity could weaken connections in the columns opposite to those active during walking, thereby suppressing undesired directions. A 180-degree shift in distribution during rest could also represent components of the ‘home vector’, a goal vector that is thought to be encoded with a 180-degree shift compared to the traveling direction of the fly16,17.

Discussion

The importance of the CX for navigation learning and memory has long been recognized25–29,61 and corresponding circuit mechanisms have been propose based on computational models as well as behavior, physiology, and connectivity data4,8,16,54,55. We found that a population of PFR neurons is sufficient for driving direction selection. Direction memory emerges during learning over time through changes in drift during rest. The inverted drift distributions between rest and walking points to a dedicated computational role of rest states for navigation. Thus, the CX offers an architecture for the close interaction of head direction, direction selection, and memory during rest and walking.

Neural representations underlying visual memory behavior have been investigated using two-photon imaging in tethered flies during behavior14,35,36. These experiments show that neurons across CX substructures are important for learning, such as ring neurons that detect visual features35,62,63, or EPG neurons14,36 which represent the fly’s heading angle30. Goal-related columnar neurons in the fan-shaped body have been identified using optogenetics14. However, the connectome shows only weak direct interactions between these and PFR neurons which could point to the integration of multiple neural populations for goal-directed navigation. Supporting this, PFL neurons, which compute the error between the current heading and goal direction, driving rotational movements to orient the fly towards its target14,15, receive input from various columnar neurons in the FB, including indirect input from PFR neurons through hΔA17 (see Supplementary Fig. S5).

Computational models propose that different directions could be learned and selected depending on behavioral needs4,16,54,55. In addition to the tangential FB neurons identified here that respond to cooler temperatures, other tangential neurons signal hunger52, with dynamics similar to goal encoding neurons in the orbitofrontal cortex, but over longer timescales39,64. Learning-related changes for direction could also support alterations in foraging behavior, which is regulated by tangential neurons65. Temperature-sensitive neurons likely do not connect directly to PFR neurons, as they arborize in the dorsal layers of the FB, while PFR neurons arborize in the central layers. However, indirect connections between these populations may occur through neurons such as vΔ or nearby tangential neurons.

Grid and place cells move towards goal locations following learning5,6,8,18. Such distortions could originate from local modifications of “Mexican hat” connectivity patterns18. Similarly, local modification of connectivity could result in the shaping of drift distributions observed here. In mice, changes in head direction dynamics have been observed during walking in darkness, revealing a memory of the direction of a previous visual stimulus66. This suggests that potentially similar representations could be used across species to remember salient or behaviorally important directions.

Activity during rest has been described in other Drosophila neurons67 and glia52. Reactivation of neurons in the FB after learning has also been associated with memory consolidation68. In mammals, head direction representations drift during sleep69,70. Neural populations involved in particular in navigation show autonomous activity during rest and sleep, which plays a role in planning, decision-making, and learning19–21,23,24,71. More broadly, drift or variability could support reinforcement learning36,72,73. In the proposed computational model, PFR reactivation could support learning by reactivating the same neurons that were active during walking74,75.

Together, our data reveal the interactions of memory, direction selection, and navigation in a single cell type. These results suggest similarities between mammalian and insect navigation systems beyond basic ring attractor dynamics75–77, including drift, changes in spatial representations following goal learning, and changes in dynamics between rest and walking5,18,66. In the future, integrating connectome information with functional data will enable the development of detailed circuit models underlying the interactions between memory formation, decision-making, and head direction networks.

Funding

Max Planck Society, Max Planck Institute for Neurobiology of Behavior – caesar (MPINB). Netzwerke 2021, Ministry of Culture and Science of the State of Northrhine Westphalia.

Author contributions

AFV and JDS designed the study and wrote the manuscript. All authors designed and built the setup, RH built mechanical arena, AFV built automation and control. AFV performed experiments, data analysis, and computational modeling.

Disclosures

The authors declare that there are no conflicts of interest related to this article.

Methods
Drosophila preparation

All flies used for experiments were reared in an incubator at a temperature of 22 degrees Celsius and under a 12-hour light/dark cycle. Flies between 3 and 8 days of age expressing jGCaMP8m in PFR neurons (UAS-jGCaMP8m;27G06-GAL4) were used for imaging. The dissection of the flies for inserting a transparent window into the cuticle was performed as described41. First, a window was cut in the head using a laser. Then the cuticle and air sacks were removed under a dissection microscope using a microrobotic arm41 or manually. The opening was then sealed with a drop of transparent UV glue (Freeform, UV fixgel composite, purchased before 2023, or NOA68 optical glue). Usually, between 3 and 5 flies were dissected at a time. Flies were allowed to recover after the dissection in isolation, in vials with food for 2 to 3 days before imaging. The flies were then glued to a glass slide with UV glue and transferred to the mechanical VR setup and placed under the two-photon microscope47. Flies that did not show the desired imaging quality (as assessed by the visibility of FB) or behavior were discarded at this step.

Mechanical virtual reality

We combined a mechanical virtual reality (VR) setup similar to the one described in40 with a custom two-photon microscope (as described in41,78) for recording neural activity during learning.

The mechanical VR allows flies to navigate within a cylindrical arena that both translates and rotates around the fly. It consists of two main components: a rotational stage with a slip ring for continuous rotation and a translation stage that offsets the arena along two dimensions. We used a cylindrical arena twice the size of that in40, with a diameter of 500 mm and a height of 250 mm (Fig. 1a and b). For translation, we employed the same Nema 17 stepper motors with encoders as in40. However, for rotation, we used a T-Motor AK10-9 V2.0 (60kv Brushless Motor) instead, to accommodate the increased inertia of the larger arena. Additionally, the translation stage was extended in both dimensions to support the required larger translations. The setup is shown in Fig. 1a, b, and Supplementary Fig. S1a. To prevent vibrations from the motors to interfere with fly behavior or two-photon imaging, the mechanical VR was mechanically isolated by placing it on a table that was mechanically decoupled from the optical table, as described in40.

The cylindrical arena contained either a single vertical stripe (Figs. 1 and 2), measuring 40 mm in width and 200 mm in height, or two identical vertical stripes positioned 180 degrees apart for learning experiments (Fig. 3a). The stripes could be illuminated from the back of the cylinder using white LEDs. The LED light was diffused through white paper and filtered using colored long-pass filters (Thorlabs, FGL550S) to prevent interference with the photomultiplier tube (PMT) used for fluorescence detection. During the learning experiment (Fig. 3a), the LEDs illuminating each stripe were independently controlled via an Arduino UNO.

For imaging experiments, flies were glued to a cover slip and positioned on an air-suspended ball using a custom aluminum fly holder (Supplementary Fig. S1b). The ball was placed 150 mm above the bottom of the cylindrical arena (Fig. 1b). Fly movement was tracked using an optic flow-based algorithm79, which analyzed ball motion via a small mirror from the back and a camera from below, as described in40. To prevent collisions between the objective and the cylinder walls, a walking limit with a 270 mm diameter was set in the mechanical VR, as in40. Thus, the effective walking area for the flies was confined to a circular region of 270 mm diameter. The rotational gain of the arena was set to 0.3 to prevent excessively fast turns in the mechanical virtual reality, while the translational gain was set to 1. Despite the low rotational gain, most flies were able to track the position of the stripe (Fig. 1e). Flies that were not able to track the stripe were discarded (see sections below for details).

Two-photon microscope

We used a custom two-photon microscope setup similar to the one described in41,78. This setup contains two axially offset beams with independently controlled focal planes that were offset in time by 6 ns to additionally detect them independently using temporal multiplexing. This setup configuration allows estimating and correcting axial motion78. Here we considered both beams as once combined excitation volume with an effective extended focal length, allowing us to record volumetric calcium activity while decreasing two-photon laser power for imaging. Axial motion estimation and correction were therefore not considered here, as axial motion during imaging produced little fluorescence changes in the recorded neurons.

Data acquisition

Behavioral data from the mechanical VR was obtained at 100 Hz, providing the time stamps of the experiment, the ball tracking data, and the position and orientation of the mechanical arena. The time stamps were sent through ROS 1 (Robot Operating System Version 1) and through the local network to the computer running Scanimage that controlled the two-photon microscope. These time stamps were stored together with each recorded frame from the microscope and were later used to synchronize the behavior and imaging data. The imaging data were obtained at a resolution of 256 × 256 pixels at approximately 60 Hz continuously during the whole experiment.

Analysis of behavior data

The linear velocity of the fly was first computed from the recorded ball velocity. We then thresholded the linear velocity to define bouts of rest (with zero linear velocity) or walking for each fly. This threshold was set tp 0.125 mm/sec, which was adjusted to be right above the linear velocity noise level.

Analysis of imaging data

For each fly, all recorded imaging frames were aligned to a common template to correct for lateral motion using cross-correlation. Once every frame was aligned, we defined a total of 16 regions of interest (ROIs) along the expression pattern in the FB (Fig. 1d) and computed the total intensity Ii(t) within each ROI i and for each frame, associated with a time stamp t. Then, the fluorescence over the frames for each ROI was computed as
where  is the 0.1 quantile of the intensity Ii(t), calculated using a sliding window containing intensity data over 300 seconds. The window was continuously shifted along the timeline to compute a dynamic baseline, enhancing the signal of the activity bump compared to using a fixed baseline over the entire experiment.

Once fluorescence data was obtained for each ROI, we created a fluorescence matrix with dimensions T 16, where T is the total number of recorded frames for one fly. The matrix was filtered using a Gaussian filter. To do this, we first extended the fluorescence matrix along the second dimension, resulting in a matrix of size T× 48 and a Gaussian filter with a size of 1× 1 was applied. Finally, we extracted the 16 ROIs from the center slices (8 to 32) of the extended fluorescence matrix (T × 16 : 32). This approach ensured that the Gaussian filtering was applied in a circular manner, effectively filtering together ROI 1 and ROI 16.

PFR phase calculation

We calculated the PFR phase from the fluorescence signals of 16 defined ROIs in the FB (Fig. 1d). This was done by sliding a cosine function across the 16 ROIs, shifting one ROI at a time, and computing the Pearson correlation between the cosine function and the fluorescence profile of the ROIs at each frame. The PFR phase was determined as the cosine offset with the highest correlation. Finally, the phase was converted to degrees by multiplying by 360/16. The PFR phase was further smoothed using a mean circular filter, calculated with a sliding window of 0.5 seconds.

Orientation-PFR phase offset correction

The PFR phase during walking reflects the fly’s traveling direction relative to visual landmarks but exhibits an arbitrary offset across individual flies30. To align the neural data with the orientation of the fly, we calculated the offset by first focusing on the PFR phase during walking epochs, since the PFR phase drifts during rest while the orientation of the fly remains constant. Therefore, we only considered the PFR phase during active walking for offset computation.

The offset at any given moment is calculated as the difference between the PFR phase and the mechanical VR orientation:

This offset is filtered using a circular mean filter with a sliding window of 15 seconds to smooth out noise and reduce variability.

In some flies, we observed that the offset remained relatively constant for extended periods, but switched during certain portions of the experiment. This phenomenon of offset switching has been observed when different visual cues are presented in virtual reality30, or in real-world virtual environments80. Given that our mechanical virtual reality system has a low rotational gain of 0.3 (i.e., the VR rotates 0.3 revolutions for every full rotation of the fly), it is possible that this low gain contributed to the offset switching observed in some trials. Additionally in learning experiments, the mechanical VR contained two visual cues (dim and bright stripe, see later section) which could also contribute to the offset switching.

To model this switching offset, we allowed for a maximum of three switches during each experiment and aimed to divide the filtered offset into 3 distinct constant segments. The optimization approach we used for this task is based on minimizing the error between the filtered offset and the 3-segment model of the offset. Specifically, we optimized the positions of two breakpoints in time, t1 and t2, that divide the experiment into 3 segments:

The first segment spans from the start of the experiment (tmin) to time t1.

The second segment spans from time t1 to time t2.

The third segment spans from time t2 to the end of the experiment (tmax).

We modeled the offset in each segment as a constant value, so that the offset at any time t is give by:
where µi is the mean offset in the i-sh segment. For each segment, the mean offset µi is computed as the circular average of the filtered offset between the defined times.

The optimization objective is to minimize the total error between the original filtered offset and the 3 segment offset model (E(t1,t2)), defined as:

The breakpoints t1 and t2 are therefore found by minimizing the error:

This minimization was performed using the Powell method via the minimize function from the Scipy package.

Once the optimal breakpoints are identified, the offset is segmented into three parts, each with its respective constant mean offset. In experiments where no offset switching occurs, this method results in three segments with identical offset values, reflecting the stability of the offset throughout the trial.

Correlation between PFR phase and VR orientation

In some flies, the PFR neurons were unable to reliably track the orientation of the arena. This could be due to various factors, such as the inability of flies to track the low-gain mechanical VR, or variations in fly surgery. To ensure accurate tracking, we discarded flies that did not show good alignment between the PFR phase and the mechanical arena orientation. This was determined by computing the correlation between the PFR phase and the arena orientation during walking.

For this, we first aligned the PFR phase with the mechanical arena orientation using the 3-segment offset fit described in the previous section. We then calculated the Pearson correlation coefficient between the arena orientation and the offset PFR phase. Flies with a correlation coefficient lower than 0.2 were excluded. Flies walking always forward would show a very high correlation, close to 1. However, in flies that occasionally walked backward or sideways, the PFR phase would jump by 180 or 90 degrees, respectively43,44. These jumps caused a reduction in correlation, which is why we set the threshold at 0.2, allowing to account for walking patterns that did not align directly with the heading direction of the fly.

PFR activity profile during walking and rest

PFR activity shows spontaneous fluctuations during immobility or grooming, which we define as rest (Fig. 1g). We analyzed the activity profile of PFR neurons at a given time point during rest and compared it to the activity during walking. We first selected flies with at least 5 distinct rest and walk epochs, each lasting a minimum of 5 seconds. Out of 32 flies, 24 met these criteria. We then combined and normalized the PFR activity from all flies across the 16 ROIs in the FB for both states. Normalization was done by subtracting the average activity of the 16 ROIs at each time point and dividing by their standard deviation. Principal component analysis (PCA) was applied to reduce the 16-dimensional data to 2 dimensions. We separated the reduced data into two groups: one corresponding to walking (Supplementary Fig. S2a, black) and the other to rest (Supplementary Fig. S2a, green). In both states, the data points formed a ring-like structure along the two principal components. We then defined a circular trajectory (Supplementary Fig. S2a, red line) and mapped 500 points along this trajectory back to the original 16-ROI normalized fluorescence data for both walking (Supplementary Fig. S2b, black) and resting (Supplementary Fig. S2b, green). This circular pattern in PCA space corresponded to a continuous activity bump across the 16 ROIs. We also mapped the PCA trajectory to the original fluorescence data (without normalization) for both states (Supplementary Fig. S2c), yielding similar results. Finally, we aligned the 500 points based on their phase in PCA space, resulting in a cosine-like activity profile across ROIs for both walking (Supplementary Fig. S2d, black) and rest (Supplementary Fig. S2d, green), although the amplitude was lower during rest than during walking. Additionally, the PCA representation contained points near the center. When a circular trajectory with a smaller radius was considered (Supplementary Fig. S2e) and mapped back to both normalized (Supplementary Fig. S2f) and non-normalized fluorescence data (Supplementary Fig. S2g), we observed a cosine-like profile (Supplementary Fig. S2h), but with a more diluted and lower amplitude. This indicates that the PFR activity profile exhibits a cosine-like pattern both during rest and walking, though with varying amplitudes across time.

PFR phase velocity during walking and rest

To quantify the PFR drift during rest (Fig. 1g) and to compare it to the PFR phase during walking, we computed the absolute PFR phase displacement for both states. The displacement was calculated as the absolute difference between consecutive PFR phase time points during epochs lasting 5 to 30 seconds in both rest and walking periods. We selected flies with at least 5 distinct rest and walk epochs of at least 5 seconds each (24 out of 32 flies met these criteria). Figure 1h shows the combined data from all 24 flies, with PFR phase displacement during rest (green) and walking (black), along with a linear fit (red). Figure 1i presents the slope of the fit (PFR phase velocity) during rest and walking for each fly, with statistical significance assessed via a paired t-test. On average, the PFR phase velocity during rest was about twice as fast as during walking. Although the mechanical VR had a low rotational gain (0.3), rapid PFR phase shifts were still observed during walk epochs, particularly when flies walked backwards or sideways. These results suggest that the PFR phase velocity during walking is more influenced by the fly’s walking patterns than by the mechanical VR gain (e.g., PFR phase jumps during walking in Fig. 1e).

PFR phase distribution during walking and rest

To analyze the PFR phase distribution during rest and walking, we first computed the PFR phase distribution during rest over a 5-minute trial in the mechanical VR. Only flies with at least 10 seconds of rest and 60 seconds of walking duration were included in the analysis, resulting in a total of 32 flies. For each fly we first computed the PFR phase distribution during rest. We then identified the peak of the distribution and offset it so that the peak was aligned with 270 degrees. Fig. 1j shows the aligned PFR phase distribution during rest for all 32 flies. We also calculated the PFR phase distribution during walking and offset it based on the peak offset of the rest-phase distribution aligned to 270 degrees. This resulted in a distribution that peaked around 90 degrees for all flies (Fig. 1k). A statistical comparison with a t-test revealed a significant difference between the PFR phase distribution during walking at 90 and 270 degrees. The peak of the PFR phase distribution during walking therefore corresponds to a 180-degree shift from the distribution during rest.

Next, we aligned the orientation of each fly in the arena to the PFR phase during walking using the 3-segment offset model described above. We then computed the orientation distribution and offset it based on the alignment of the PFR phase distribution during rest. As expected, the orientation distribution for all flies peaked around 90 degrees (Fig. 1l), consistent with the PFR phase tracking the arena orientation during walking. A t-test was used to assess the statistical significance between the values at 90 and 270 degrees for the arena orientation distribution.

We also examined the trajectories of the flies in the mechanical VR. To align the trajectories with the PFR phase, we first rotated them according to the 3-segment offset model, so that if the PFR phase during walking was predominantly at 90 degrees, it would indicate that the fly was walking towards the 90-degree direction in the mechanical arena. We then further rotated the trajectories based on the offset of the PFR phase peak during rest. This alignment showed that all trajectories were consistently oriented towards the 90-degree direction of the arena (Fig. 1m, left), which was expected given the PFR phase distribution during walking. Next, we computed the position density of all 32 flies within the arena using a grid with a square length of 30 mm (Fig. 1m, right). The fly’s azimuth angle in the area, from the position in polar coordinates (Fig. 1m, left, see angles), showed a distribution that peaked around 90 degrees. A statistical comparison with a t-test revealed that the values at 90 degrees were significantly different from those at 270 degrees, as expected (Fig. 1n). These results demonstrate that the behavior of flies was shifted by approximately 180 degrees from the PFR phase distribution observed during rest when the flies were aligned based on the peak of the PFR phase distribution during rest. Consequently, the PFR phase distribution during walking was also offset by 180 degrees.

Optogenetics setup

Optogenetic activation was performed by illuminating specific FB regions with computer-generated holograms projected using a red laser (640 nm, Toptica, iBEAM-SMART-640-S-HP) and a phase-SLM (Meadowlark Optics, HSP1920-1064-HSP8). The setup is described in52. A laser beam was expanded and modulated by a phase-SLM before being combined with the fluorescence illumination using a dichroic mirror. The phase-SLM, which generated the holograms, was positioned at a conjugate plane with the microscope’s back focal plane (see Fig. 2a). The Gerchberg-Saxton algorithm81 was used to generate phase modulation for the desired activation pattern. A custom GUI integrated with Scanimage82 allowed users to select activation regions in the two-photon field of view. Calibration for precise alignment between the FOV and the SLM-illuminated area was done using a camera (Basler acA640-750um) imaging reflected and fluorescent light.

Optogenetics activation during rest

Optogenetic activation was triggered by an Arduino UNO, which controlled a red laser based on real-time ball velocity tracking of the fly. The power of the laser was set to 30µW . When the velocity of the fly dropped below a defined threshold, determined by baseline noise from the ball tracking algorithm, the laser was turned on after a 0.5-second delay. When the fly resumed walking and exceeded the threshold, the laser was switched off. During rest periods, the laser alternated between 0.1-second ON and OFF cycles.

We used flies expressing CsChrimson and GCaMP8m in PFR neurons (GAL4-R27G06; UAS-CSChrimson; UAS-jGCaMP8m). Control flies lacked CsChrimson expression (GAL4-R27G06; UAS-jGCaMP8m). To avoid excessive activation from the two-photon laser, which interfered with calcium imaging, we did not feed flies retinal food.

The optogenetic activation occurred in two separate 10 minute trials. In one trial, the right side of the FB was activated by defining a small circular activation mask on the right side (Fig. 2a), while in the second trial, the left side was activated using a similar mask on the left side. The order of activation varied across flies: some had the right side activated first, followed by the left, while others were activated in reverse. After each 10-minute trial, flies were given a 5-minute recovery period without optogenetic activation. The mechanical VR was reset at the start of each trial, ensuring the fly’s position was at the center. Fig. 2b shows an example of a 10 minute trial in which the FB was activated on the left side during rest.

PFR phase during rest-optogenetics activation

We first analyzed the PFR phase distribution during rest (i.e., during optogenetic activation) using a laser power of 0.3 µW across all flies. However, in some cases, this power was insufficient to counteract the natural drift of the PFR phase, leading to weak centering around the activated FB region. Variability in CSChrimson expression or differences in surgical conditions may have contributed to this. To ensure robust activation, we filtered out trials where the standard deviation of the PFR phase distribution during rest (activation period) exceeded 100 degrees, retaining only those with strong, localized activation. In some cases, a trial with left-side activation was discarded due to broad optogenetic activation, while the right-side activation trial for the same fly was retained. Because some flies only had valid data for one activation side, we did not analyze the data as pairwise distributions for each fly. Instead, we grouped all flies with left-side activation together and all flies with right-side activation together for analysis.

Additionally, we excluded flies that did not exhibit a reliable correlation between arena orientation and PFR phase during walking, as described in a previous section. We noted that flies expressing CSChrimson showed lower orientation-phase correlations, likely due to activation from the two-photon laser during calcium imaging. For the final analysis, we only considered trials where flies rested and received optogenetic stimulation for at least 20 seconds and walked for at least 20 seconds.

The fly’s orientation was aligned to the PFR phase during walking using the 3-segment offset model, and its trajectory was similarly rotated to ensure neural and behavioral data were aligned. This alignment allowed the PFR phase during walking to reflect the fly’s heading and walking direction in the arena. We found that optogenetic activation on one side of the FB during rest influenced the PFR phase distribution during walking, as well as the fly’s orientation, shifting them approximately 180 degrees from the activation site (Fig. 2d, e, first row). In control flies lacking CsChrimson, PFR phase distributions during rest were spread across the FB without a directional preference (Fig. 2d, e, second row). Statistical significance between PFR phase distributions during rest and walking was assessed using dimensionality reduction: PCA reduced the 16-bin distributions to a single dimension, followed by a t-test. This analysis showed a significant effect in CsChrimson-expressing flies but not in controls (Fig. 2e). A similar approach was used to compare orientation distributions between left and right activation sites.

Aligned trajectories revealed that flies preferred the side of the arena opposite to the optogenetic activation site. Fig. 2f and g (first row) show the last 5 minutes of the 10-minute activation trial (for clarity) for left and right activation in CsChrimson-expressing flies (panel f) and controls (panel g). The second row presents position density maps for all flies over the full 10-minute trial, using a 30 mm grid. To quantify directional preference, we analyzed the fly’s azimuth angle (from position in polar coordinates) using PCA-based dimensionality reduction again. This showed a statistically significant shift in orientation opposite to the activation site in CsChrimson flies (Fig. 2h, first row), an effect absent in controls (Fig. 2h, bottom row).

Spatial learning task

We adapted a spatial learning assay from previous studies28,40, where flies had to locate a cool area positioned in front of a visual landmark (Fig. 3a). Arena temperature was controlled using an IR laser targeted at the fly’s thorax, which switched off when the fly entered the cool area (Fig. 3b, Supplementary Fig. S1b). Unlike in previous experiments with a single bright stripe, in this task the arena contained two vertical stripes: a self-illuminated “bright” stripe and a “dim” stripe passively lit by the first. Flies were trained in two groups: one with the cool area in front of the bright stripe and another with the cool area in front of the dim stripe (Fig. 3d).

Aversive stimulus during learning

An infrared (IR) laser (Toptica, ibeam-smart-785-S-HP with pulse option, 785 nm) was used to deliver an aversive heat stimulus, similar to the method described in40. The laser beam was focused onto the fly’s thorax using a lens and directed with a small mirror (Thorlabs, MRA05-P01) placed behind the fly holder (Fig. 3b and Supplementary Fig. S1b). Since each fly was attached slightly differently to the slide, a camera was used at the beginning of the experiment to adjust the position of the IR laser after placing the fly on the ball with a kinematic mirror mount. During the learning experiment, the IR laser power was set to 30 mW, and an Arduino UNO was used to pulse the laser at a frequency of 0.2 Hz.

Analysis of learning behavior

Flies explored the arena freely for 5–20 minutes before training, which consisted of 10 trials. At the start of the first trial, the mechanical VR reset to the center with a random orientation. An aversive IR laser delivered 0.1-second pulses of “heat” everywhere except the cool area. To prevent prolonged grooming or resting epochs, the air supply to the ball was momentarily turned off for 0.1 seconds if flies rested continuously for over 10 seconds, stimulating them to resume walking. The air valve was triggered by tracking of the velocity of the ball in real time79.

Once a fly remained in the cool area for 10 seconds, the next trial began. The bright stripe switched to the opposite side of the arena, and the cool area moved accordingly. This effectively caused an instant 180-degree rotation of the arena from the fly’s perspective, similar to previous place-learning assays in freely moving flies28. Each time the fly found the cool area, the stripe and cool area shifted 180 degrees, repeating this cycle until all 10 trials were completed. If a fly failed to find the cool area within 15 minutes, a new trial began, and both the cool area and bright stripe were shifted to the opposite side accordingly. In some cases, flies happened to be in the location where the cool area moved, allowing them to immediately “find” it in the next trial by chance. This may have helped some flies navigate back to the cool area in later trials.

We selected flies that met a minimum required PFR phase-orientation correlation, as in previous experiments (see prior section). Additionally, flies that did not demonstrate learning were excluded.

To assess learning, we calculated a learning index, which quantifies how much faster a fly finds the cool area in later trials (7–10) compared to earlier trials (1–6):

Flies with a learning index below 1 (indicating they took longer in later trials than in early ones) were discarded, as they were considered not to have learned. This also excluded flies that had a strong initial preference for the cool area’s location (either the bright or dim stripe) and quickly found the cool area in the first trials. Based on this criterion, 11 flies were considered to have learned the location of the cool area in front of the bright stripe (Fig. 3c), while 7 flies were included that learned the location of the cool area in front of the dim stripe (Fig. 3d). In both cases, flies improved their time to find the cool area across trials, as evidenced by the statistically significant difference between the first trial and subsequent trials, as determined by a t-test (Fig. 3c and d). The trajectories of all flies for specific trials are shown in Fig. 3e.

After finishing 10 training trials, the mechanical arena was reset to the central position, and the flies were given 20 minutes to navigate or rest with the IR laser switched off. Following the 20-minute break, memory was tested in a single trial where the flies had to locate the cool area again. Only flies that had learned the location of the cool area in front of the bright stripe successfully remembered its position, as indicated by the reduced time it took them to find the cool area compared to the initial trial (Fig. 3c, right side). In contrast, flies that learned to find the cool area in front of the dim stripe did not reliably remember its location, as shown by the lack of significant difference between the times taken in the first trial and the probe trial after the 20-minute break (Fig. 3d, right side).

PFR phase during learning

We trained flies expressing GCaMP8m in PFR neurons using GAL4-R27G06; UAS-jGCaMP8m, which allowed recording calcium activity during the learning task. To analyze the data, we aligned the fluorescence ROIs and PFR phase to the arena orientation using the 3-segment offset model, ensuring that the PFR phase corresponded to the fly’s orientation in the arena. Fig. 3f shows the recorded imaging data from a fly trained with the cool area in front of the bright stripe.

For each fly, we calculated the PFR phase distribution during rest for trials with at least 10 seconds of resting time. Fig. 3g shows the distribution of PFR phase during rest for the fly shown in Fig. 3f across 10 trials, with the cool area located around the 90-degree direction. We observed that the PFR phase distribution during rest shifted across trials, centering around 180 degrees opposite to the cool area direction. We grouped the distributions of PFR phase during rest into three sets: trials 1-3, trials 4-7, and trials 8-10 to calculate distributions over extended rest periods. Fig. 3h compares the PFR phase distributions during rest for flies trained with the cool area in front of the bright stripe (top) and the dim stripe (bottom). We used PCA to reduce each fly’s distribution to a single dimension and applied a t-test to assess statistical significance (Fig. 3h). Statistically significant differences emerged in the last trials (8-10), with the PFR phase distribution peaking approximately 180 degrees from the direction of the cool area. After the 20-minute break, the distributions of PFR phase during rest remained statistically different (Fig. 3h, right), although the distributions were somewhat distorted compared to the last 8-10 trials and the peak of the distributions were no longer centered 180 apart from the cool area, for example in the case of the flies trained towards the dim stripe. The distribution in flies trained toward the bright stripe still showed a minimum at the location of the cool area (at 90 degrees).

We also calculated the distributions of PFR phase during walking for the three trial sets (Fig. 3i). As with the distributions during rest, the PFR phase distributions during walking became statistically significant in the last trials (8-10). After the 20-minute break, these distributions remained significantly different (Fig. 3i on the right). Flies trained with the cool area in front of the bright stripe showed a strong preference for the bright stripe, while flies trained with the cool area in front of the dim stripe did not exhibit this preference, consistent with the behavior analysis showing that these flies had poorer memory of the cool area location.

Supplementary Information
FB layers respond to change in temperature

Computational models predict that such learning could occur through plasticity between FB layers and FB columnar neurons4,16,54. Based on the anatomical arrangement of CX, computational models typically assume that a reinforcing signal should be present in layers of the fan-shaped body. FB neurons respond to taste83 feeding65, odors54, and hunger52, and could support the selection of directions associated with these behavioral needs after learning4,16,54. We therefore asked whether similarly temperature would be encoded in FB tangential layers.

We found that dorsal tangential neurons respond to temperature changes. These neurons were labeled using the GAL4-72G07 and expressed GCaMP8m (GAL4-72G07; UAS-jGCaMP8m, Supplementary Fig. S3a, left). Using Neurobridge84, we confirmed that they innervate layers 6 and 7 of the FB. We defined 16 regions of interest (ROIs) across the FB, similar to the analysis of PFR neurons (Supplementary Fig. S3a, right). Flies were then trained in the learning task as described in Methods. However, their performance was generally worse than that observed in flies during PFR neuron recordings and we did not analyze their learning behavior in relation to neural activity changes. However, in all flies activity increased whenever they entered the cool area. Supplementary Fig. S3b displays the average fluorescence of 468 traces recorded from defined FB ROIs in 21 flies over 10 training trials, aligned to the moment flies enter the cool area. If flies entered the cool area but stayed for less than 10 seconds during training, the event was cut off at the point they exited the cool area. If flies remained in the cool area for 10 seconds, a new trial began, during which the cool area was switched. Therefore, the maximum time spent by flies in the cool area was limited to 10 seconds. The increase in activity was observed across all FB columns, confirming that the signal spanned the entire FB and corresponded to tangential FB neurons. To further investigate this, we calculated the total fluorescence signal in the FB for each fly, mapping activity across the arena in 15 mm grid bins and averaging across all flies. Supplementary Fig. S3c (left and center panels) shows that the increased activity precisely aligned with the cool area in the arena. To ensure this activity was specific to the cool area, we recorded an additional seven flies navigating the arena for one hour without the IR laser, that is, in the absence of a cool area. In this case, activity remained flat across the arena (Supplementary Fig. S3c, right panel). This confirms that the cool area, that is, the change in temperature, triggered activity in the dorsal FB layers. When fluorescence signals were aligned to the time flies entered the cool area (468 events from 21 flies) and compared to control flies that entered the same location without the IR laser (78 events from 7 flies), we observed a statistically significant increase in fluorescence in the experimental group (Supplementary Fig. S3d, t-test). Again, if flies entered the cool area but remained for less than 10 seconds, the event was truncated to the time when they exited the cool area.

Additionally, we found that these neurons exhibited spontaneous spiking activity during rest epochs (Supplementary Fig. S3g). Using a threshold to identify spikes, we observed that these events were sparse, typically ranging from 2 to 10 spikes per minute (Supplementary Fig. S3h).

These findings demonstrate that a temperature dependent signal which could serve for reinforcement during the spatial learning task is indeed transmitted to the FB. While these dorsal tangential neurons innervate the upper FB layers, PFR neurons primarily target the central FB, specifically layers 4 and 5. This suggests that direct connectivity between these tangential FB neurons and PFR neurons is unlikely and may rely on intermediate neural populations.

PFR neurons and connectome analysis

PFR neurons are columnar neurons that project to the PB, FB, and ROB (round body), as illustrated in Fig. 1c. Based on the connectome, there are two types of PFR neurons: PFRa and PFRb17. PFRa neurons remain in the same column across the PB and FB, while PFRb neurons shift by one column between these regions. This suggests that PFRb neurons might help shift neural activity in the FB, though their exact function remains unclear. We classify the neurons investigated here as PFRa based on matching analysis using Neurobridge84 (not shown), though the R27G06-GAL4 line may include other neuron types. According to the connectome, PFRa neurons are classified as dopaminergic from electron microscopy images85.

Both PFRa and PFRb neurons receive strong input from hΔB neurons, which encode the fly’s traveling direction in allocentric coordinates43,44. In fact, PFR activity has been used as a proxy for recording the output of hΔb neurons44.

Supplementary Fig. S5a shows the connectivity between hΔb neurons and PFRa neurons, obtained from the hemibrain connectome17. In the top-left corner, we display the synapse locations in the FB, with each color representing a distinct presynaptic neuron from the hΔB population. These neurons are sorted based on their output arborization across the FB columns (from left to right). In the bottom-left corner, we show the same synapse locations, but now color-coded according to the postsynaptic neurons, sorted by their output (axonal) arborization in the FB columns. On the right side, we present the connectivity matrix for pre- and postsynaptic neurons in the FB columns, with the number of synapses indicated. As shown in this figure, the hΔb phase is not expected to shift when it is passed to PFRa neurons, with each column connecting to the same corresponding column.

One of the key outputs of PFRa neurons is to hΔA neurons, another type of columnar neuron in the FB. The connectome shows that hΔA neurons receive input from PFR neurons in two distinct columns, offset by half the width of the fan-shaped body, corresponding to a 180-degree phase shift. This is evident in the connectivity matrix between PFR and hΔA neurons, which displays two diagonals: the main diagonal, where no transformation occurs (input from one column produces output in the same column), and an off-diagonal, shifted by 4 columns, representing a 180-degree input-output transformation (Supplementary Fig. S5c). Interestingly, this does not apply to hΔB neurons, which exclusively connect to hΔA neurons along the main diagonal, without any phase shift (Supplementary Fig. S5b). hΔA neurons also project back to PFRa neurons, maintaining their phase without any shift across the FB, as shown by a single diagonal in Supplementary Fig. S5d.

While some neurons, such as hΔB neurons, connect to hΔA neurons without causing a phase shift (Supplementary Fig. S5b), certain tangential FB neurons establish connections with hΔA neurons across FB columns through a 180-degree offset diagonal (Supplementary Fig. S5e and f). This suggests that inputs to hΔA neurons can be coordinated, with either the main diagonal (0-degree phase shift) or the off-diagonal (180-degree phase shift) being functionally active depending on the context (see next section).

Finally, hΔA neurons provide strong input to both PFL2 and PFL3 neurons without phase shift (Supplementary Fig. S5g and h, respectively), and these PFL2 and PFL3 neurons drive turning behavior to orient the fly towards a goal14,15. Thus, PFRa neurons are positioned upstream of the turning PFL neurons, with hΔA neurons in between. Interestingly, the synaptic patterns in hΔA neurons could potentially correct the phase shift of PFRa neurons observed during rest.

Mechanism for correcting the phase shift of PFR neurons during rest

The 180-degree shift in the PFR phase distribution during rest could be corrected by FB circuits, restoring the original phase distribution observed during walking. This correction would allow the reactivation of the FB columns active during walking to occur during rest, potentially supporting memory consolidation. Such a mechanism is consistent with the connectivity between PFR and hΔA neurons, which includes two diagonals (Supplementary Fig. S5c), and the way hΔA neurons receive input from both the main diagonal (e.g., hΔB neurons, Supplementary Fig. S5b) and the off-diagonal (e.g., FB4Y and FB5X tangential neurons, Supplementary Fig. S5e and f).

View inlineView popup
Table S1.
Parameter values used in the simulation of the ring attractor in Supplementary Fig. S4b

During walking, PFRa and hΔB neurons could provide stronger input to hΔA neurons through the main diagonal, resulting in no phase shift. However, during rest, if hΔB neurons become inactive and tangential neurons are active alongside PFRa neurons, the off-diagonal will receive stronger input than the main diagonal, inducing a 180-degree phase shift between PFRa and hΔA neurons. This shift allows for the correction of the PFRa phase during rest. This corrected phase could subsequently be transmitted by hΔA neurons to downstream circuits for memory consolidation.

Ring attractor model

Based on the connectivity between PFR neurons and Δ7 neurons in the PB, which exhibit sinusoidal connectivity similar to the hypothesized ring attractor network17, along with the cosine-like activity profile of PFR neurons during rest and walking (Supplementary Fig. S2), we propose that PFR neurons may be part of a ring attractor network, as also assumed for other FB columnar neurons16. In such networks, activity drift is typically driven by connectivity heterogeneities or noise, which could explain our observations58–60.

We employed a rate-based model to simulate a ring attractor network consisting of N = 8 neurons, each representing one of the eight columns in the fan-shaped body (FB)86. The dynamics of the network are described by the following equation:
where ri represents the activity of the i-th neuron in the ring attractor, and τ is the time constant of the neurons. The recurrent connectivity matrix, wi j, depends on the distance between neurons i and j around the ring, and it reflects the interaction between PFR neurons. This connectivity is potentially mediated by Δ7 neurons. The term wI represents global inhibition within the network, θ is a constant background input, Δi is the input from hΔB neurons to the i-th column, and ε represents random noise input sampled from a normal distribution. The term [· ]+ threshold-linear function to ensure positive-valued firing rates.

We assume synaptic depression in the wi j weight matrix, which is described by the following equation:
where τw represents the time constant of synaptic depression,  represents the baseline synaptic weight in the absence of activity-dependent depression, U is a constant governing the strength of synaptic depression, and r j(t) is the activity of the presynaptic neuron j. High presynaptic activity leads to neurotransmitter depletion, which in turn reduces the synaptic strength, making the depression dependent on the presynaptic neuron’s activity.

The baseline synaptic weight, ,is defined with a Gaussian-like function that depends on the distance between i and j neurons in the ring:
where wE represents the magnitude of synaptic weights and σE determines the width of the synaptic connectivity pattern, influencing how the connectivity strength decreases with distance between neurons in the ring. All parameter values used for the ring attractor simulation are shown in Table S1.

Synaptic depression in the model, along with random input noise, ε, induces drift in the ring attractor. When a neuron reaches peak activity, it inhibits other neurons through sustained activity, which leads to synaptic depression. This sustained activity diminishes the active neuron’s influence over time, causing it to lose dominance. Consequently, the peak activity shifts to a different neuron with a non-depressed synaptic weight (i.e., with more available resources). As the depleted neuron becomes fully inhibited and its activity drops to zero, its resources recover, while the newly active neuron weakens, continuing the cycle (Supplementary Fig. S4a and b, left green side).

In our model, we assume that during walking, the ring attractor network receives strong input from walking direction neurons, hΔB, denoted as Δi(t). We model the activity of hΔB neurons with a sine-like pattern over time, as shown in Supplementary Fig. S4b (blue), using the following equation:

Here, I represents the maximum activity of hΔB neurons, σI defines the standard deviation of the activity across the FB columns, and m(t) represents the sine trajectory across the FB, given by:

In this equation, C is the column along which the sine-like input trajectory oscillates (set to C = 4), and T is the oscillation period, with T = 5 seconds.

This strong input helps the ring attractor counteract drift and accurately track the directional signal (Supplementary Fig. S4b, black), even in the presence of synaptic depression (Supplementary Fig. S4b, bottom). We then simulate the fly at rest by setting the input from hΔB neurons to zero. As a result, the peak of activity in the network drifts, governed by the dynamics of synaptic depression (Supplementary Fig. S4b, bottom). Consequently, the activity shifts toward the neurons that were less active during walking (Supplementary Fig. S4b, right green side). This results in a 180-degree phase shift in the distribution between rest and walking within the ring attractor network (Supplementary Fig. S4c). This model suggests that the 180-degree shift in the PFR phase distribution between rest and walking is driven by synaptic depression, while drift is influenced by both random noise and synaptic depression.

To account for the activity of PFR neurons during rest, we hypothesize that this 180-degree shift is corrected by hΔA neurons. During walking, hΔA neurons do not modify the PFR phase, meaning only the main diagonal of the connectivity matrix between PFR and hΔA neurons is functional. However, during rest, hΔA neurons may shift the PFR phase by 180 degrees, by using the off-diagonal in the connectivity matrix (see Supplementary Fig. S5c). This shift corrects the observed drift in the PFR distribution during rest, ensuring that the same FB columns active during walking are reactivated during rest in downstream neurons of hΔA. The mechanism behind this functional shift in hΔA connectivity is discussed in the previous section.

Thus, through the drifting dynamics, hΔA neurons may correct the shift and reactivate downstream neurons, such as tangential FB neurons, to support memory consolidation during rest. This consolidation, in turn, influences subsequent behavior, as seen in optogenetic experiments (Fig. 2). Overall, our model provides a mechanistic explanation for both the drift and 180-degree phase shift, and suggests how neural circuits could leverage this drift to facilitate memory consolidation during rest.

Download figureOpen in new tab
Figure S1.

a Mechanical virtual reality setup from two different views, colors are for visualization. The setup is described in detail in40. b A fly glued to a cover slide is attached to the fly holder and placed between the air-supported ball and the objective. The IR laser used as an aversive stimulus is focused on the back of the fly through an opening in the fly holder (visible on the left side) and with the help of a small mirror.

Download figureOpen in new tab
Figure S2.

Activity profile of PFR neurons during rest and walking. a Fluorescence data from all flies (24 flies total) were combined and normalized (see Methods), resulting in 299,637 fluorescence traces for each of the 16 ROIs in the FB. Principal component analysis (PCA) was applied to reduce the 16-dimensional data to two dimensions, with data points during walking (black, left panel) and resting (green, right panel) displayed along the principal components. b A circular trajectory was defined along the reduced data (red line in panel a), with 500 points along the trajectory mapped back to the normalized fluorescence data across the 16 ROIs during walking (black) and rest (green). c The same as panel b, but the circular trajectory was mapped to the original (non-normalized) fluorescence data. d The 500 data traces from panel c are aligned based on their phase during walking (left, black) and rest (right, green), showing a cosine-like profile (red line) across the ROIs of the FB. e-h Same as panels a-d but for a circular trajectory defined in panel e with a smaller radius in the reduced 2D PCA dimensions.

Download figureOpen in new tab
Figure S3.

Temperature sensitive neurons in FB. a Neurons labeled with 72G07-GAL4 innervate the dorsal layers of the FB (top). Regions of interest in the FB (bottom). b Average fluorescence FB from 21 flies crossing the cool area 242 times, aligned to the time point they enter the cool area. Events where flies entered the cool area but did not remain for 10 seconds during training were truncated to the time they exited the cool area. Events where flies stayed in the cool area for 10 seconds triggered the start of a new trial, during which the cool area switched. As a result, flies were in the cool area for a maximum of 10 seconds. c Left: arena with cool area. Center: fluorescence of dorsal FB layer neurons at each position in the arena (arena position binned in 15 mm increments). Right: same as center panel but for flies where the IR laser was not used. d Amplitude of dorsal FB layer fluorescence when crossing the cool area, comparing conditions where the IR laser was used (blue line) versus when it was not used (control, black line). Thick lines represent average, while shaded areas indicate the standard error of the mean (SEM). Events where flies entered the cool area but stayed for less than 10 seconds during training were truncated to the time they exited the cool area. e Fluorescence levels of dorsal FB layer neurons in the cool area for flies with laser activation (blue, 21 flies) and without laser activation (black, 7 flies).

Download figureOpen in new tab
Figure S4.

The ring attractor model generates drift and a 180-degree shift in the activity distribution. a Left: neurons forming the ring attractor, with color indicating their activity levels. Orange wedges represent neurotransmitter availability. As time progresses, sustained activity from a neuron leads to synaptic depression (indicated by red arrows in the second panel). This causes the activity peak to shift toward another neuron with available neurotransmitters (third panel). The previously active neuron becomes inhibited, and neurotransmitter availability recovers (blue arrows in the fourth panel). b In this simulation, input to the ring attractor, representing hΔB neurons, is active during walking (first panel, in blue). The ring attractor exhibits spontaneous fluctuations without input (green, second panel), similar to the activity of PFRa neurons. During walking, PFRa neurons track the input from hΔB neurons. In the subsequent rest period, the ring attractor is most active in neurons that were inactive during walking. Third panel: synaptic depression in each neuron of the ring attractor. c Activity distribution in the ring attractor during walking (top) and subsequent rest (bottom).

Download figureOpen in new tab
Figure S5.

Neural connectivity according to the hemibrain connectome17,45,46. a Top left: Each point represents a synapse in the FB, with color indicating the presynaptic neuron from hΔB population. Neurons are arranged from left to right based on their axonal (output) arborization in the FB. Bottom right: The same synapses as in the top left panel, now colored according to their corresponding postsynaptic PFRa neurons, which are also sorted by axonal arborization in the FB. Right panel: The number of synapses between hΔB and PFRa neurons across the eight columns of the FB. b-h Same as b but for other populations indicated at the top of each panel.

Acknowledgements

We thank Anna Kaatz for fly crosses and dissections for imaging experiments. We thank Ivan Vishniakou for technical support. We thank Gülin Öykü Tabel for fly crosse, Jasmin Beinert, Anne Buecker, and her team for help with maintaining flies, and Vivek Jayaraman for Chrimson flies. We thank Jason Kerr for the Mai Tai Laser as well as other equipment, and Anne Buecker, Christoph Geisen, Alexandr Klioutchnikov, and Yasiz Rachad for helpful discussions. We thank the MPINB mechanical and electronics workshops for support with building instrumentation.

Footnotes

↵* andres.flores{at}mpinb.mpg.de

References
1.↵Fagan, W. F. et al. Spatial memory and animal movement. Ecol. letters 16, 1316–1329 (2013).CrossRefGoogle Scholar
2.↵Collett, M., Chittka, L. & Collett, T. S. Spatial memory in insect navigation. Curr. Biol. 23, R789–R800 (2013).CrossRefPubMedGoogle Scholar
3.Eichenbaum, H. The role of the hippocampus in navigation is memory. J. neurophysiology 117, 1785–1796 (2017).CrossRefPubMedGoogle Scholar
4.↵Le Moël, F., Stone, T., Lihoreau, M., Wystrach, A. & Webb, B. The central complex as a potential substrate for vector based navigation. Front. psychology 10, 690 (2019).CrossRefGoogle Scholar
5.↵Sosa, M. & Giocomo, L. M. Navigating for reward. Nat. Rev. Neurosci. 22, 472–487 (2021).CrossRefPubMedGoogle Scholar
6.↵Basu, J. & Nagel, K. Neural circuits for goal-directed navigation across species. Trends Neurosci. (2024).Google Scholar
7.↵Taube, J. S. The head direction signal: origins and sensory-motor integration. Annu. Rev. Neurosci. 30, 181–207 (2007).CrossRefPubMedWeb of ScienceGoogle Scholar
8.↵Webb, B. The internal maps of insects. J. Exp. Biol. 222, jeb188094 (2019).Abstract/FREE Full TextGoogle Scholar
9.↵Hulse, B. K. & Jayaraman, V. Mechanisms underlying the neural computation of head direction. Annu. review neuroscience 43, 31–54 (2020).CrossRefGoogle Scholar
10.↵Wilson, R. I. Neural networks for navigation: From connections to computations. Annu. Rev. Neurosci. 46, 403–423 (2023).CrossRefPubMedGoogle Scholar
11.↵Petrucco, L. et al. Neural dynamics and architecture of the heading direction circuit in zebrafish. Nat. neuroscience 26, 765–773 (2023).CrossRefPubMedGoogle Scholar
12.↵Sarel, A., Finkelstein, A., Las, L. & Ulanovsky, N. Vectorial representation of spatial goals in the hippocampus of bats. Science 355, 176–180 (2017).Abstract/FREE Full TextGoogle Scholar
13.↵Beetz, M. J., Kraus, C. & El Jundi, B. Neural representation of goal direction in the monarch butterfly brain. Nat. Commun. 14, 5859 (2023).CrossRefPubMedGoogle Scholar
14.↵Mussells Pires, P., Zhang, L., Parache, V., Abbott, L. & Maimon, G. Converting an allocentric goal into an egocentric steering signal. Nature 626, 808–818 (2024).CrossRefPubMedGoogle Scholar
15.↵Westeinde, E. A. et al. Transforming a head direction signal into a goal-oriented steering command. Nature 626, 819–826 (2024).CrossRefPubMedGoogle Scholar
16.↵Goulard, R., Heinze, S. & Webb, B. Emergent spatial goals in an integrative model of the insect central complex. PLOS Comput. Biol. 19, e1011480 (2023).CrossRefPubMedGoogle Scholar
17.↵Hulse, B. K. et al. A connectome of the drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection. Biorxiv 2020–12 (2020).Google Scholar
18.↵Ginosar, G., Aljadeff, J., Las, L., Derdikman, D. & Ulanovsky, N. Are grid cells used for navigation? on local metrics, subjective spaces, and black holes. Neuron 111, 1858–1875 (2023).CrossRefPubMedGoogle Scholar
19.↵Redish, A. D. Vicarious trial and error. Nat. Rev. Neurosci. 17, 147–159 (2016).CrossRefPubMedGoogle Scholar
20.Buzsáki, G., McKenzie, S. & Davachi, L. Neurophysiology of remembering. Annu. review psychology 73, 187–215 (2022).CrossRefGoogle Scholar
21.↵Tang, W. & Jadhav, S. P. Multiple-timescale representations of space: Linking memory to navigation. Annu. review neuroscience 45, 1–21 (2022).CrossRefGoogle Scholar
22.Mattar, M. G. & Lengyel, M. Planning in the brain. Neuron (2022).Google Scholar
23.↵Jones, E. A. A. & Giocomo, L. M. Neural ensembles in navigation: From single cells to population codes. Curr. Opin. Neurobiol. 78, 102665 (2023).CrossRefPubMedGoogle Scholar
24.↵Brodt, S., Inostroza, M., Niethard, N. & Born, J. Sleep—a brain-state serving systems memory consolidation. Neuron 111, 1050–1075 (2023).CrossRefPubMedGoogle Scholar
25.↵Guo, A. et al. Conditioned visual flight orientation in drosophila: dependence on age, practice, and diet. Learn. & Mem. 3, 49–59 (1996).Abstract/FREE Full TextGoogle Scholar
26.Liu, G. et al. Distinct memory traces for two visual features in the drosophila brain. Nature 439, 551–556 (2006).CrossRefPubMedWeb of ScienceGoogle Scholar
27.Pan, Y. et al. Differential roles of the fan-shaped body and the ellipsoid body in drosophila visual pattern memory. Learn. & Mem. 16, 289–295 (2009).Abstract/FREE Full TextGoogle Scholar
28.↵Ofstad, T. A., Zuker, C. S. & Reiser, M. B. Visual place learning in drosophila melanogaster. Nature 474, 204–207 (2011).CrossRefPubMedWeb of ScienceGoogle Scholar
29.↵Fisher, Y. E. Flexible navigational computations in the drosophila central complex. Curr. opinion neurobiology 73, 102514 (2022).CrossRefGoogle Scholar
30.↵Seelig, J. D. & Jayaraman, V. Neural dynamics for landmark orientation and angular path integration. Nature 521, 186–191 (2015).CrossRefPubMedGoogle Scholar
31.Turner-Evans, D. et al. Angular velocity integration in a fly heading circuit. Elife 6, e23496 (2017).CrossRefPubMedGoogle Scholar
32.Green, J. et al. A neural circuit architecture for angular integration in drosophila. Nature 546, 101–106 (2017).CrossRefPubMedGoogle Scholar
33.↵Kim, S. S., Rouault, H., Druckmann, S. & Jayaraman, V. Ring attractor dynamics in the drosophila central brain. Science 356, 849–853 (2017).Abstract/FREE Full TextGoogle Scholar
34.↵Turner-Evans, D. B. et al. The neuroanatomical ultrastructure and function of a biological ring attractor. Neuron 108, 145–163 (2020).CrossRefPubMedGoogle Scholar
35.↵Grover, D. et al. Differential mechanisms underlie trace and delay conditioning in drosophila. Nature 603, 302–308 (2022).CrossRefPubMedGoogle Scholar
36.↵Dan, C., Hulse, B. K., Kappagantula, R., Jayaraman, V. & Hermundstad, A. M. A neural circuit architecture for rapid learning in goal-directed navigation. Neuron (2024).Google Scholar
37.↵Collett, T., Graham, P. & Heinze, S. The neuroethology of ant navigation. Curr. Biol. 35, R110–R124 (2025).CrossRefPubMedGoogle Scholar
38.↵Cheong, H. S., Siwanowicz, I. & Card, G. M. Multi-regional circuits underlying visually guided decision-making in drosophila. Curr. Opin. Neurobiol. 65, 77–87 (2020).CrossRefPubMedGoogle Scholar
39.↵Basu, R. & Ito, H. T. A goal pointer for a cognitive map in the orbitofrontal cortex. Curr. Opin. Neurobiol. 83, 102803 (2023).CrossRefPubMedGoogle Scholar
40.↵Flores-Valle, A. & Seelig, J. D. A place learning assay for tethered walking drosophila. J. Neurosci. Methods 378, 109657 (2022).CrossRefPubMedGoogle Scholar
41.↵Flores-Valle, A., Honnef, R. & Seelig, J. D. Automated long-term two-photon imaging in head-fixed walking drosophila. J. neuroscience methods 368, 109432 (2022).CrossRefPubMedGoogle Scholar
42.↵Shiozaki, H. M., Ohta, K. & Kazama, H. A multi-regional network encoding heading and steering maneuvers in drosophila. Neuron 106, 126–141 (2020).CrossRefPubMedGoogle Scholar
43.↵Lu, J. et al. Transforming representations of movement from body-to world-centric space. Nature 601, 98–104 (2022).CrossRefPubMedGoogle Scholar
44.↵Lyu, C., Abbott, L. & Maimon, G. Building an allocentric travelling direction signal via vector computation. Nature 601, 92–97 (2022).CrossRefPubMedGoogle Scholar
45.↵Xu, C. S. et al. A connectome of the adult drosophila central brain. BioRxiv 2020–01 (2020).Google Scholar
46.↵Plaza, S. M. et al. neu print: An open access tool for em connectomics. Front. Neuroinformatics 16, 896292 (2022).CrossRefGoogle Scholar
47.↵Denk, W., Strickler, J. H. & Webb, W. W. Two-photon laser scanning fluorescence microscopy. Science 248, 73–76 (1990).Abstract/FREE Full TextGoogle Scholar
48.↵Seelig, J. D. et al. Two-photon calcium imaging from head-fixed drosophila during optomotor walking behavior. Nat. methods 7, 535–540 (2010).CrossRefPubMedWeb of ScienceGoogle Scholar
49.↵Zhang, Y. et al. Fast and sensitive gcamp calcium indicators for imaging neural populations. Nature 615, 884–891 (2023).CrossRefPubMedGoogle Scholar
50.↵Jenett, A. et al. A gal4-driver line resource for drosophila neurobiology. Cell reports 2, 991–1001 (2012).CrossRefPubMedGoogle Scholar
51.↵Flores-Valle, A. Sleep and navigation in Drosophila. Ph.D. thesis, Universitäts-und Landesbibliothek Bonn (2023).Google Scholar
52.↵Flores-Valle, A. & Seelig, J. D. Dynamics of a sleep homeostat observed in glia during behavior. bioRxiv 2022–07 (2022).Google Scholar
53.↵Klapoetke, N. C. et al. Independent optical excitation of distinct neural populations. Nat. methods 11, 338–346 (2014).CrossRefPubMedWeb of ScienceGoogle Scholar
54.↵Matheson, A. M. et al. A neural circuit for wind-guided olfactory navigation. Nat. communications 13, 4613 (2022).CrossRefGoogle Scholar
55.↵Kathman, N. D., Lanz, A. J., Freed, J. D. & Nagel, K. I. Neural dynamics for working memory and evidence integration during olfactory navigation in drosophila. bioRxiv 2024–10 (2024).Google Scholar
56.↵Green, J. & Maimon, G. Building a heading signal from anatomically defined neuron types in the drosophila central complex. Curr. opinion neurobiology 52, 156–164 (2018).CrossRefGoogle Scholar
57.↵Pisokas, I., Heinze, S. & Webb, B. The head direction circuit of two insect species. Elife 9, e53985 (2020).CrossRefPubMedGoogle Scholar
58.↵Seeholzer, A., Deger, M. & Gerstner, W. Stability of working memory in continuous attractor networks under the control of short-term plasticity. PLoS computational biology 15, e1006928 (2019).CrossRefGoogle Scholar
59.Flores-Valle, A., Gonçalves, P. J. & Seelig, J. D. Integration of sleep homeostasis and navigation in drosophila. PLoS Comput. Biol. 17, e1009088 (2021).CrossRefPubMedGoogle Scholar
60.↵Chechelnizki, G., Shaham, N., Salhov, A. & Burak, Y. Stabilization of memory on neural manifolds through multiple synaptic time scales. bioRxiv 2025–01 (2025).Google Scholar
61.↵Neuser, K., Triphan, T., Mronz, M., Poeck, B. & Strauss, R. Analysis of a spatial orientation memory in drosophila. Nature 453, 1244–1247 (2008).CrossRefPubMedWeb of ScienceGoogle Scholar
62.↵Seelig, J. D. & Jayaraman, V. Feature detection and orientation tuning in the drosophila central complex. Nature 503, 262–266 (2013).CrossRefPubMedWeb of ScienceGoogle Scholar
63.↵Garner, D. et al. Connectomic reconstruction predicts visual features used for navigation. Nature 634, 181–190 (2024).CrossRefPubMedGoogle Scholar
64.↵Basu, R. et al. The orbitofrontal cortex maps future navigational goals. Nature 599, 449–452 (2021).CrossRefPubMedGoogle Scholar
65.↵Goldschmidt, D. et al. A neuronal substrate for translating nutrient state and resource density estimations into foraging decisions. BioRxiv 2023–07 (2023).Google Scholar
66.↵Ajabi, Z., Keinath, A. T., Wei, X.-X. & Brandon, M. P. Population dynamics of head-direction neurons during drift and reorientation. Nature 1–8 (2023).Google Scholar
67.↵Yap, M. H. et al. Oscillatory brain activity in spontaneous and induced sleep stages in flies. Nat. communications 8, 1815 (2017).CrossRefGoogle Scholar
68.↵Dag, U. et al. Neuronal reactivation during post-learning sleep consolidates long-term memory in drosophila. Elife 8, e42786 (2019).CrossRefPubMedGoogle Scholar
69.↵Peyrache, A., Lacroix, M. M., Petersen, P. C. & Buzsáki, G. Internally organized mechanisms of the head direction sense. Nat. neuroscience 18, 569–575 (2015).CrossRefPubMedGoogle Scholar
70.↵Chaudhuri, R., Gerçek, B., Pandey, B., Peyrache, A. & Fiete, I. The intrinsic attractor manifold and population dynamics of a canonical cognitive circuit across waking and sleep. Nat. neuroscience 22, 1512–1520 (2019).CrossRefPubMedGoogle Scholar
71.↵Chen, Z. S. & Wilson, M. A. How our understanding of memory replay evolves. J. Neurophysiol. 129, 552–580 (2023).CrossRefPubMedGoogle Scholar
72.↵Fee, M. S. & Goldberg, J. H. A hypothesis for basal ganglia-dependent reinforcement learning in the songbird. Neuroscience 198, 152–170 (2011).CrossRefPubMedWeb of ScienceGoogle Scholar
73.↵Momennejad, I. Learning structures: predictive representations, replay, and generalization. Curr. Opin. Behav. Sci. 32, 155–166 (2020).CrossRefPubMedGoogle Scholar
74.↵Wang, X.-J. Neural dynamics and circuit mechanisms of decision-making. Curr. opinion neurobiology 22, 1039–1046 (2012).CrossRefGoogle Scholar
75.↵Khona, M. & Fiete, I. R. Attractor and integrator networks in the brain. Nat. Rev. Neurosci. 1–23 (2022).Google Scholar
76.Langdon, C., Genkin, M. & Engel, T. A. A unifying perspective on neural manifolds and circuits for cognition. Nat. Rev. Neurosci. 24, 363–377 (2023).PubMedGoogle Scholar
77.↵Clark, D. G., Abbott, L. & Sompolinsky, H. Symmetries and continuous attractors in disordered neural circuits. bioRxiv 2025–01 (2025).Google Scholar
78.↵Flores-Valle, A. & Seelig, J. D. Axial motion estimation and correction for simultaneous multi-plane two-photon calcium imaging. Biomed. Opt. Express 13, 2035–2049 (2022).CrossRefPubMedGoogle Scholar
79.↵Vishniakou, I., Plöger, P. G. & Seelig, J. D. Virtual reality for animal navigation with camera-based optical flow tracking. J. neuroscience methods 327, 108403 (2019).CrossRefPubMedGoogle Scholar
80.↵Haberkern, H. et al. Maintaining a stable head direction representation in naturalistic visual environments. bioRxiv 2022–05 (2022).Google Scholar
81.↵Gerchberg, R. W. & Saxton, W. O. A practical algorithm for the determination of the phase from image and diffraction plane pictures. Optik 35, 237–246 (1972).Google Scholar
82.↵Pologruto, T. A., Sabatini, B. L. & Svoboda, K. Scanimage: flexible software for operating laser scanning microscopes. Biomed. engineering online 2, 1–9 (2003).CrossRefGoogle Scholar
83.↵Sareen, P. F., McCurdy, L. Y. & Nitabach, M. N. A neuronal ensemble encoding adaptive choice during sensory conflict in drosophila. Nat. communications 12, 4131 (2021).CrossRefGoogle Scholar
84.↵Clements, J. et al. Neuronbridge: an intuitive web application for neuronal morphology search across large data sets. BMC bioinformatics 25, 114 (2024).CrossRefPubMedGoogle Scholar
85.↵Eckstein, N. et al. Neurotransmitter classification from electron microscopy images at synaptic sites in drosophila melanogaster. Cell 187, 2574–2594 (2024).CrossRefPubMedGoogle Scholar
86.↵Wolff, T. & Rubin, G. M. Neuroarchitecture of the drosophila central complex: A catalog of nodulus and asymmetrical body neurons and a revision of the protocerebral bridge catalog. J. Comp. Neurol. 526, 2585–2611 (2018).CrossRefPubMedGoogle Scholar
 Back to top
 Previous
Next 
Posted March 24, 2025.
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
ABSTRACT
Discussion
Funding
Author contributions
Disclosures
Methods
Supplementary Information
Acknowledgements
Footnotes