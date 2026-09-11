# Visually Guided Behavior and Optogenetically Induced Learning in Head-Fixed Flies Exploring a Virtual Landscape (Haberkern et al., Curr Biol 2019; doi 10.1016/j.cub.2019.04.033)

Full-text HTML captured from https://www.cell.com/current-biology/fulltext/S0960-9822(19)30431-2 (open access, CC BY-NC-ND) on 2026-09-10 via the in-app browser.

Title: Visually Guided Behavior and Optogenetically Induced Learning in Head-Fixed Flies Exploring a Virtual Landscape: Current Biology
URL: https://cell.com
Source element: <article>
---
ARTICLEVolume 29, Issue 10P1647-1659.E8May 20, 2019
Open Access
Download Full Issue
Visually Guided Behavior and Optogenetically Induced Learning in Head-Fixed Flies Exploring a Virtual Landscape
Hannah Haberkern1,2 Send email to haberkernh@janelia.hhmi.org ∙ Melanie A. Basnak1,3,5 ∙ Biafra Ahanonu1,4,6 ∙ … ∙ Mark Bolstad1 ∙ Christopher Bruns1 ∙ Vivek Jayaraman1,7 Send email to vivek@janelia.hhmi.org … Show more
Affiliations & Notes
Article Info
Linked Articles (1)
Download PDF
Outline
Share
More
Highlights
•	
2D virtual reality system for head-fixed flies emulates free walking experience
•	
Optogenetic activation of sugar-sensing neurons triggers local search behavior
•	
Flies learn to avoid visual objects associated with activation of heat sensors
Summary
Studying the intertwined roles of sensation, experience, and directed action in navigation has been facilitated by the development of virtual reality (VR) environments for head-fixed animals, allowing for quantitative measurements of behavior in well-controlled conditions. VR has long featured in studies of Drosophila melanogaster, but these experiments have typically allowed the fly to change only its heading in a visual scene and not its position. Here we explore how flies move in two dimensions (2D) using a visual VR environment that more closely captures an animal’s experience during free behavior. We show that flies’ 2D interaction with landmarks cannot be automatically derived from their orienting behavior under simpler one-dimensional (1D) conditions. Using novel paradigms, we then demonstrate that flies in 2D VR adapt their behavior in response to optogenetically delivered appetitive and aversive stimuli. Much like free-walking flies after encounters with food, head-fixed flies exploring a 2D VR respond to optogenetic activation of sugar-sensing neurons by initiating a local search, which appears not to rely on visual landmarks. Visual landmarks can, however, help flies to avoid areas in VR where they experience an aversive, optogenetically generated heat stimulus. By coupling aversive virtual heat to the flies’ presence near visual landmarks of specific shapes, we elicit selective learned avoidance of those landmarks. Thus, we demonstrate that head-fixed flies adaptively navigate in 2D virtual environments, but their reliance on visual landmarks is context dependent. These behavioral paradigms set the stage for interrogation of the fly brain circuitry underlying flexible navigation in complex multisensory environments.
Graphical Abstract
Keywords
virtual reality
Drosophila melanogaster
navigation
optogenetics
visual conditioning
search
operant learning
Introduction
Animals in their natural habitat often navigate complex visual environments to forage for food, find mates, and escape inhospitable conditions or predators. Insects, in particular, are among the animal kingdom’s most skilled navigators and have been the focus of decades of field and laboratory studies [1–6]. These studies have produced important insights into the range of navigational algorithms that insects use in different naturalistic contexts [7–9]. An important aspect of these algorithms is how much and under what conditions the animal relies on external sensory cues versus self-motion information to control its movements. Studying this interplay is challenging in natural settings, where it can be difficult to closely monitor and flexibly control an animal’s sensory experience. This shortcoming is addressed by the complementary approach of studying behavior in virtual reality (VR) [10]. VR approaches enable the creation of environments with customized rules for how the virtual sensory surroundings change in response to an animal’s actions and have found wide application in neuroscience across species [11–19]. Here we use VR to study the role of visual landmarks for navigation in Drosophila melanogaster.
In Drosophila, VR paradigms have been used to study the behavior of flying [11, 20, 21] and walking [22–24] flies. However, all past studies of navigational behaviors in tethered flies have been limited to 1D conditions in which the fly only controls its orientation relative to a fixed circular visual panorama, and its translational movements are disregarded. The conclusions drawn from the fly’s behavior in such reduced environments can be challenging to extrapolate to more realistic settings in which a fly’s location—and not just its heading—matters. Indeed, most studies of freely moving flies highlight the 3D nature of their behavior, whether in flight [25, 26] or walking [27, 28]. Generating an immersive experience for a head-fixed animal in a virtual world requires accurate estimation of the animal’s intended movements. This is challenging in tethered flying flies, but the problem is easier to solve in a tethered walking preparation, where flies can be restricted to 2D space [22, 29].
Here we present a versatile VR system that allows us to explore behavioral strategies of head-fixed flies when moving in 2D space. We exploit the flexibility of VR to investigate how flies change their interaction with visual landmarks depending on stimulus parameters, the presence of other sensory cues, and past experiences. We give flies an experience of taste and heat in an otherwise purely visual VR by activating the appropriate sensory receptors using optogenetics. While this approach does not fully substitute genuine consumption of sugar or actual heat, it has experimental advantages: it allows for experiments in which an animal’s response to such sensory experiences can be studied without affecting its satiety state or the condition of its body. Optogenetic activation of sensory neurons has previously been used to study olfactory processing [30, 31], CO2 avoidance [32], and thermotaxis [33]. Direct activation of sensory and dopaminergic neurons has also been used to replace reward or punishment in odor conditioning assays [34–37]. Further, freely moving flies were shown to avoid areas in which their bitter taste receptors were optogenetically activated, although it was not clear if flies could acquire a conditioned place preference as a result of such an experience [38]. Inspired by such studies, we developed behavioral paradigms to study adaptive, visually guided behavior in moderately complex 2D VR environments. We show that encounters with optogenetically induced sweet taste trigger exploratory behaviors in VR that are similar to the local search patterns described in freely walking flies upon encounters with real food or optogenetic substitutes [27, 39–41]. Motivated by the demonstration that freely walking flies can learn to use visual cues to navigate to a cool spot in an aversively hot 2D environment [6], we also trained head-fixed flies to avoid visual landmarks that were associated with optogenetic activation of the heat-sensing pathway. These VR paradigms for head-fixed flies clear a path toward understanding the neural underpinnings of exploratory and learned navigation in flies.
Results
A 2D Visual VR System for Head-Fixed Walking Flies
To explore 2D navigation in tethered flies, we built a VR system that combined an existing spherical treadmill for head-fixed walking flies with a projector-based panoramic visual display (Figures 1A and S1A–S1C; STAR Methods). As in past experiments [23, 24], we glued wing-clipped, head-fixed flies to a thin wire tether and suspended them above an air-supported ball such that the fly’s walking maneuvers resulted in rotations of the ball (Figures 1A [inset], 1B, and 1C; STAR Methods). These ball rotations were tracked by optical mouse sensor chips [22] and translated into simulated movement through a virtual visual environment using a custom-made C++ program (“FlyoVeR,” based on a program developed for generating a VR environment for rodents [42]; STAR Methods; Figure S1A). To validate the closed loop VR system, we tested head-fixed flies in a well-established 1D behavior that requires them to control their heading: stripe fixation [43, 44]. Flies performed this behavior successfully, albeit with genotypic differences (see STAR Methods, Figures S3A and S3B, and additional materials on www.flyfizz.org). However, the strength of our VR system is that it permits the fly to walk toward and around virtual objects in 2D environments, which can be flexibly designed with 3D-modeling software and loaded into FlyoVeR (Figure 1D; STAR Methods). For our experiments, we designed virtual environments consisting of salient visual objects distributed across a textured virtual plane. For virtual objects, we used simple, rotationally symmetric, geometric shapes such as cones and cylinders (Figures 1F, S1G, and S1I). The radial symmetry of the virtual scene permitted a compact, “object-centric” description of the fly’s position based on the fly’s distance and heading relative to a nearby object (Figures 1E and 1G). We limited the number of collisions with the impenetrable virtual objects by distributing them sparsely and avoided confining the animal inside virtual walls, as our purely visual VR cannot capture the mechanosensory experience of a collision. To increase the fly’s sampling of the visual objects, we arranged them in large periodic grids so that the fly repeatedly encountered identical visual scenes (Figure 1H). We will refer to such a world made from cone-shaped objects as a “cone forest” (Figures S1E and S1H; STAR Methods). For the analysis of walking trajectories, we exploited periodicity and sparse placement of cones to generate “collapsed” trajectories, pooling points in the VR that corresponded to the same visual environment (Figure 1I). To visually separate the objects, we used virtual fog, hiding any objects beyond a user-defined distance from the fly (Figures 1J, S1G, and S1I). We sought to use this setup to explore conditions under which walking flies might employ salient virtual objects as landmarks to guide their movements.
Figure 1 A 2D Virtual Reality (VR) System for Head-Fixed Walking Fruit Flies
Show full caption
Flies Show Similar Patterns of Interaction with Objects in VR and during Free Behavior
To verify that the absence of physical contact with virtual objects did not substantially change how flies interacted with these objects, we compared the behavior of flies navigating in our 2D VR system to that of freely walking flies. We built a large free walking arena (Figures S2A–S2C) where flies could interact with a real object under lighting conditions similar to those in VR and thus dimmer than those typically used for free walking visual behavior experiments [45]. In contrast to previous studies [46], flies could not climb on the object (STAR Methods). For these validation experiments, we chose to test hybrid flies that were constructed to be similar to flies used in subsequent optogenetic stimulation experiments (“WTB hybrid” are generated from crossing WTB and an empty-Gal4 line). We let individual flies explore the arena (Figures 2A–2C) with a single black cone placed in the center (Figure S2A) and compared their walking trajectories to those from tethered walking flies exploring the cone forest VR (Figures 2D–2F). Walking velocities were similar, but translational velocities were lower and fly-to-fly variability higher in VR (Figures S2D–S2I). Flies approached objects in both the real world and in VR (Figures 2A and 2D), and many showed a weak tendency to keep cones in their frontal field of view (FOV) when close to the object (Figures 2B, 2E, and S2F). Under both conditions, flies showed an increased residence near the cones (Figures 2C and 2F). To test whether this was a consequence of objects physically blocking the fly’s path—or, in VR, caused by object impenetrability—we exploited the flexibility of VR by generating a version of the cone forest with impenetrable, but invisible, cones. Flies showed no increased residency around invisible cones (Figure 2G), which could not be explained simply by the flies being less active (Figure 2H) or by altered walking velocities in the absence of visible objects (Figure S2J). Rather, flies made more visits to the visible objects compared to the invisible objects (Figure 2I) and stayed there for longer (Figure S2K), indicating that flies actively steered toward the cones.
Figure 2 Object Interaction in Freely Walking and Head-Fixed Flies
Show full caption
Dimensionality of World and Contrast Polarity of Visual Objects Affect Fixation Behavior
To understand how steering and approach behavior in 2D VR relates to more frequently studied orienting paradigms in 1D VR, we compared a simple visual orientation behavior, fixation of a single prominent visual landmark, in 1D (stripe VR) and 2D (cone forest VR) environments (Figure 3A). We also examined flies’ fixation preferences under different contrast polarity conditions—whether landmarks appear as dark objects on a bright background (dark-on-bright; Figures 3A [top] and 3B), like in most natural scenes, or as bright objects on a dark background (bright-on-dark; Figures 3A [bottom] and 3C), as is frequently used in fly VR experiments. Specifically, we quantified fixation by fitting a von Mises function to the relative heading distribution (see STAR Methods; Figures S3C–S3F), which allowed us to describe heading preference with two fitted parameters, one for fixation strength and one for fixation angle (Figure 3E). We used the fitted fixation strength parameter to detected trials in which flies were fixating. The scene’s contrast polarity had a strong effect on fixation: flies more frequently kept a single heading direction relative to the visual landmark (single-peaked or unimodal fixation) in bright-on-dark compared to dark-on-bright conditions (Figure 3D). The distribution of preferred fixation angles also varied with scene type: while most flies showed frontal fixation of a black stripe (Figure 3F [far left]), fixation of the bright stripe occurred across the entire FOV (Figure 3F [center right]). Unimodal fixation was more common in 1D compared to 2D scenes (Figure 3D), perhaps because translational movement toward an object in 2D pushes it out of the frontal FOV unless it is perfectly centered. Curiously, flies that showed unimodal fixation of cones in 2D scenes kept the object in their lateral FOV (Figure 3F [center left and far right]), which corresponds to a circling trajectory around the object (Figure 3C) but would correspond to maintaining a straight path if the landmarks were far away. In 2D trials, flies often showed two fixation peaks (bimodal fixation; Figures S3D and S3F; same fly as in Figure 3C; see STAR Methods for adaptation of von Mises fit), which were typically located at opposite locations within the fly’s FOV (π offset; Figure 3G). Frequently, the two fixation peaks were either in the front or back, corresponding to straight trajectories alternating approach and departure while moving from cone to cone (Figure 3B), or at the side, corresponding to counterclockwise and clockwise circling around the landmarks in this environment (Figure 3D). These features of fixation behavior were conserved across genotypes, persisted across a range of temperatures, and were not affected by manipulations aimed at rendering flies flightless (see additional materials on www.flyfizz.org). Thus, consistent with previous findings in tethered flight [47, 48], scene contrast polarity affects fixation behavior both quantitatively and qualitatively. Head-fixed flies in 2D environments did not just approach (and depart from) visual objects, but they also circled them, maintaining a consistent non-frontal heading relative to the objects. While approach behavior is consistent with 1D fixation and circling while maintaining a specific heading is consistent with recent observations in purely rotational settings [49, 50], these behaviors can only be directly established in 2D settings.
Figure 3 Fixation Behavior Is Affected by World Dimension and Contrast Polarity
Show full caption
Using Optogenetics to Study Context-Dependent Navigation
A fly’s movements and its interactions with visual objects are sensitive to context, such as the absence or presence of food [27, 39, 40, 51, 52] and environmental conditions; for example, changes in temperature [6, 24, 53]. Introducing context into a VR environment presents challenges: food can be difficult to offer to flies without leaving traces on the surface that the fly walks on, and exposure to persistently high temperature can damage flies physically. We thus sought to add context to the otherwise purely visual virtual environment by using optogenetic activation of appropriate sensory pathways [39].
Flies Initiate Local Search upon Transiently Tasting “Virtual Sugar”
Hungry flies are known to display a change in their walking pattern when they encounter a small patch of food, initiating a local search behavior that involves increased turning in the nearby area and occasional returns to the initial patch [27, 39–41]. We sought to examine whether and how the presence of visual cues influence this behavior, which has recently been suggested to involve path integration [27]. Specifically, we wanted to test if visual landmarks associated with the food patch serve as beacons, potentially allowing flies to correct for errors during path integration and more easily return to the food. To evoke local search in starved flies in VR we simulated an encounter with a food patch by transiently activating neurons expressing the Gr64f sugar taste receptor [54–56] using optogenetic stimulation (a 200 ms virtual sugar stimulus). We verified that this transient optogenetic stimulation was sufficient to induce freely walking hungry flies to slow down, a typical response to encounters with real food [57] (see STAR Methods; Figures S4A–S4C). We hypothesized that after experiencing virtual sugar in VR flies would transition to local search, exploring the space around the stimulation site, and that this behavior might be enhanced if the stimulation site was associated with a visual object. To test this, we compared responses to virtual sugar stimulation in hungry flies exploring two types of cone forest environments. In both environments, the virtual sugar stimulation was spatially restricted to a small area around cones to mimic sparse food patches, but in one case the cones were made invisible (Figure 4A and 4B [top], orange), whereas in the other case they served as a visual landmark for the stimulation site (Figure 4B [middle], magenta). We contrasted local search behavior in these two conditions with exploration of the cone forest VR in the absence of virtual sugar (Figure 4B [bottom], teal). We found that encounters with virtual sugar typically led to more tortuous walking trajectories that kept flies closer to the stimulation site than flies not exposed to optogenetic stimulation, confirming a virtual sugar-induced transition to local search behavior (Figures 4B–4E, orange and magenta lines). However, flies showed similar rates of return to the food patch regardless of the presence of landmarks (Figure 4F). Thus, virtual sugar stimulation elicits a local search behavior that is not significantly enhanced by visual objects associated with food sites and is, therefore, unlikely to rely on beaconing.
Figure 4 Local Search Behavior in VR after Optogenetic Activation of Sugar-Sensing Neurons
Show full caption
To better understand how flies accomplished local search and why visual landmarks may be dispensable, at least under these experimental conditions, we examined changes in walking pattern in more detail. Tasting virtual sugar led to higher average path curvature (Figure 4G), which was more strongly related to how much time had passed since the stimulation event than the fly’s distance from the stimulation site (Figures 4G and 4H). Further, the time course of curvature changes matched that of the changes in walking velocities (Figure 4I) and was not altered by the presence of landmarks (Figures 4G–4I, compare orange and magenta). These findings would be surprising if flies were steering back to the virtual sugar site in a directed manner. We therefore analyzed search bouts—the time period between an initial virtual sugar encounter and the departure from the simulated food patch (Figure S4D)—to assess whether turns were preferentially directed toward the virtual sugar site. None of the experimental groups showed evidence for directed turns toward the virtual sugar or landmark (Figure S4E), nor did flies clearly modulate their run length between turns according to their distance from the virtual sugar site (Figure S4F). This behavior did not measurably differ in flies that were exposed to increased durations of virtual sugar stimulation (Figures S4H–S4M). Thus, tethered flies display bouts of local exploration after tasting virtual sugar, but visual cues do not significantly improve their returns to the original virtual sugar site. Overall, these transient changes in walking pattern during foraging permit flies to sample distinct (virtual) food patches over the course of the full 20 min trial (Figure S4G).
Flies Avoid “Virtual Heat” when Walking Freely and in VR
Following the observation that the presence of landmarks did not markedly improve the accuracy of local search behavior in VR, we next sought to explore the role of visual landmarks in the avoidance of an aversive stimulus. The extensive history of fly visual learning experiments with heat, and the fact that flies have exquisite temperature sensitivity and show robust avoidance of high environmental temperatures [58], led us to explore the effects of pairing an aversive heat stimulus with our visual VR. We generated “virtual heat” stimuli by optogenetically activating heat-sensing neurons targeted by the hot cell-Gal4 (HC-Gal4) line [53] (Figure 5A). We compared responses to virtual heat stimuli for three optogenetic stimulation intensities in a free walking quadrant assay (Figures S5A–S5F). Flies robustly avoided areas with optogenetic stimulation even at low (0.27 mW/cm2) light intensities (Figures S5F and S5G), which likely only activated the peripheral HC neurons in the fly’s antenna and not the central neurons captured in the HC-Gal4 expression pattern (Figure 5A). Also, low stimulation intensity did not elicit avoidance responses in control flies (Figure S5G), suggesting that the red light was not in itself aversive. Thus, optogenetic activation of HC neurons could be used as an effective aversive stimulus in walking flies. Because virtual heat avoidance was more pronounced in male flies (Figure S5G), we performed all VR experiments in male HC-Gal4 > ChrimsonR flies.
Figure 5 Avoidance of Optogenetically Induced Virtual Heat
Show full caption
Next, we generated virtual heat zones for tethered flies in VR. Virtual heat zones were centered around either visible or invisible objects, with linearly increasing stimulation intensities (up to 0.61 mW/cm2). We used two virtual heat zone profiles that differed in their steepness (Figure 5B [top]) and compared object approaches in flies across four trials in the cone forest (Figure 5B [bottom]). In two of the trials, virtual heat zones were associated with either invisible (“Opt alone”) or visible (“Opt + object”) cones, respectively, allowing us to assess whether and how much visual landmarks increased virtual heat avoidance (landmark-assisted avoidance). We also tested flies in two trials with visible cones but no virtual heat stimulus (“Obj pre,” “Obj post”) before and after a trial in which cones were paired with virtual heat, thereby allowing us to assess whether and how much flies learned to avoid landmarks when they were associated with aversive consequences. Similar to their freely walking counterparts, flies in VR initiated turns shortly after entering virtual heat zones (Figure 5C), resulting in a decreased residency within such zones and a marked reduction in object approaches relative to trials without virtual heat (Figure 5D). We next compared the time that flies spent within the virtual heat zone in trials with and without visible landmarks (Figure 5E [top]). While landmarks appeared dispensable for the avoidance of steep virtual heat gradients (Figures 5B [top left] and 5E [top]), avoidance of shallower virtual heat gradients (Figure 5B [right]), which was generally less pronounced, was slightly improved when landmark cues were present (Figure 5E [bottom]). For shallow virtual heat gradients, entries to the virtual heat zone were also significantly reduced when these zones were paired with landmarks (Figure 5F).
Notably, we found no signs of conditioned avoidance of cones after trials in which they had been paired with virtual heat zones (Figures 5C, 5D, and 5G), potentially because the flies’ innate drive to approach these landmarks overrode any learned aversion.
Flies Distinguish between Object Shapes in VR
We reasoned that any aversive visual conditioning paradigm in VR would need to counter a fly’s strong drive to approach salient objects. Therefore, we devised a paradigm that would shift the fly’s relative preference for different object shapes rather than altering its behavior in the presence of a single object type. As a prerequisite for such a paradigm, we first established that flies could distinguish between two object shapes: a cylinder and a cone. To test flies’ naive shape preferences, we created a second type of periodic virtual world, a “cone and cylinder forest” (Figures S1H, S1I, and 6A; Video S1). Indeed, when left to explore the cone and cylinder forest, most male WTB hybrid flies showed higher visit rates to cylinders than cones (Figures 6A–6C). Thus, naive flies were able to distinguish the shapes and preferentially approached one object type.
Figure 6 Conditioning of Object Shape Preferences with Virtual Heat
Show full caption
Playback position
00:00
00:00/00:30
Open video in fullscreen mode with transcript
Settings
playback speed
Normal
quality
Auto
audio
Original English
subtitles
Off
subtitle/caption settings
keyboard shortcuts
Video (12.15 MB)
Video S1. Object Shape Preference, Related to Figure 6
Top left: trajectory of a male WTB hybrid fly walking through the cone and cylinder forest VR. Cone and cylinder locations are marked by gray triangles and rectangles, respectively. The colored dot indicates the fly’s virtual position, with the black stick pointing in the fly’s heading direction. The color of the dot changes with progression of time. Past positions of the fly in VR are marked by small dots. Bottom left: collapsed version of the trajectory. Top right: visual scene as seen from the fly’s point of view. Note that images were rendered with 120° FOV rather than 240° used in experiments. Also, images shown here were not perspective corrected as would be for the fly. Bottom right: video of the tethered fly walking on the spherical treadmill. The image on the panoramic screen can be seen in the background.
Flies in VR Alter Their Preference for Landmark Shapes Associated with Virtual Heat
We next paired the cone and cylinder forest with a virtual heat landscape that changed over the course of three consecutive trials (Figure 6D). In all trials, flies were exposed to a baseline of constant and mildly aversive low virtual heat that kept them moving through the environment enough to result in multiple visits to both object shapes. In a pre-trial phase, we let flies explore the visual environment and measured the fly’s innate shape preferences (Figure 6E [left]). On average, HC > ChrimsonR flies also had a naive preference for cylinders over cones (Figures 6E and 6F [left]), as seen previously in WTB hybrid flies. In training trials, virtual heat was increased within a small zone around cylinders (“hot zone”) and decreased around cones (“cool zone”; Figure 6D [center]; Video S2). In this anti-cylinder training protocol, flies avoided entering the hot zone, resulting in a low rate of visits to cylinders, whereas they often stopped at the edge of the cool zone near the cone, resulting in an increased residency 10–15 mm away from the cones (Figures 6E and 6F [center]). In the post-trial phase, cool and hot zones were removed, but on average flies kept visiting cones more frequently than cylinders (Figures 6D–6F [right]). Thus, pairing a virtual heat landscape with the two object shapes was sufficient to significantly and consistently alter naive shape preferences over the course of 20 min of training (Figures 6F and S6A). We also tested the reverse training protocol (anti-cone) in which cylinders were paired with cool zones and cones with hot zones (Figure 6G [left]). While flies in this paradigm showed no clear naive shape preference, the time course of the preference change mirrored that of the anti-cylinder protocol (Figure 6G). However, the shift in shape preference before and after training was not significant (Figure S6B). To further exclude the possibility that the observed shift in shape preference after anti-cylinder training had been induced by mere exposure to virtual heat, we designed a control paradigm in which the cool and hot zones were moved such that they were no longer associated with cone and cylinder positions, respectively (Figure 6H [left]). In this paradigm, we no longer observed any systematic changes in shape preference (Figures 6H and S6C). The learning effect observed in the anti-cylinder conditioning paradigm did not depend on the visit radius chosen and was primarily driven by a reduction of visits to cylinders (Figures S6D–S6F). We sought to identify changes in walking behavior that contributed to the shift in shape preference between pre- and post-trials, such as differences in the fixation of cones and cylinders (Figures S6G–S6I), but we could not find any consistent trends across flies. We therefore conclude that the shift in shape preference observed in our anti-cylinder conditioning paradigm relies on flies associating aversive and hospitable virtual heat stimuli with cylindrical objects but the underlying behavioral adjustments might vary from fly to fly.
Playback position
00:00
00:00/00:30
Open video in fullscreen mode with transcript
Settings
playback speed
Normal
quality
Auto
audio
Original English
subtitles
Off
subtitle/caption settings
keyboard shortcuts
Video (2.96 MB)
Video S2. Aversive Visual Conditioning Experiment, Related to Figure 6
Illustration of the walking trajectory of a male HC-Gal4 > ChrimsonR fly during training in the aversive visual conditioning paradigm. Top: the large colored dot indicates the fly’s position in the virtual world. The fly’s position is visualized as in Video S1, except that here the color shows the optogenetically induced virtual heat level at the respective position, and object identity is also color-coded (same color code as in Figure 6A). Bottom: visual scene as seen from the fly’s point of view. As in Video S1, images were rendered with 120° FOV rather than 240° used in experiments and not perspective corrected as would be for the fly.
Pairing Virtual Sugar with Either Object Shape Increases Attraction to Both Object Shapes
We asked whether a fly’s naive object shape preference could also be modified by selectively associating one object shape with virtual sugar stimulation. Because virtual sugar may partly—but incompletely—mimic an appetitive reward, we expected that flies might respond to such an experience by selectively increasing their interaction with the “rewarded” object shapes. As observed previously in the local search experiments, flies slowed down upon exposure to the virtual sugar (Figure S6J; increased residency around cones), which led to increased visits and interaction with objects paired with virtual sugar. However, this effect did not persist in the form of a selective increase in approaches or visits to the “rewarded” shape once the virtual sugar stimulation ceased (Figures S6K and S6L; compare training and post-trials). Flies merely showed a slight, non-specific increase in object visits (Figures S6M and S6N). Thus, virtual sugar stimulation is either insufficient to mimic key features of food reward consumption, or appetitive object conditioning requires stronger differences, such as spectral distinctions, between object appearance.
Discussion
We combined 2D visual VR and optogenetic stimulation to study how head-fixed flies modulate their walking behavior based on context. 2D VR settings, where flies can approach and walk around objects in their vicinity, reveal modes of behavior, such as approach, departure, and circling, which are consistent with fixation behaviors in angular-only VR, but cannot be directly observed in those simpler settings. We used optogenetic stimulation of thermosensory and gustatory neurons to further investigate the role of visual landmarks in guiding fly navigation in different behavioral contexts. Hungry flies exploring a visual VR responded to transient encounters with virtual sugar by changing their walking patterns much as free walking flies do—by exhibiting a local search behavior. In free-walking flies, this search behavior has been suggested to rely on path integration [27]. However, in our tethered VR setting, in which flies may not receive self-motion information as reliably, and with virtual sugar, which does not provide the multimodal experience of tasting real sugar, the most prominent behavioral changes we observed could also be explained by simpler mechanisms, such as a modulation of the rate and tightness of turns [59–61]. It is also possible that greater levels of starvation than used here could induce stronger behavioral effects, as has been observed previously [51, 52, 62]. Surprisingly, returns to the site of the encounter with virtual sugar seemed not to be increased by visual cues, opening up the possibility that local search behavior is controlled by motor control circuits that are distinct from those associated with visually guided navigation. Further, the appetitive experience of virtual sugar was insufficient to differentially condition flies to specific visual object shapes. However, we found that location-specific virtual heat was sufficient to condition head-fixed flies to alter their preferences for different object shapes, establishing that flies in 2D VR settings can be optogenetically trained to display adaptive visual behaviors. Whether the altered preference reflects a change in shape-selective approach and avoidance or simply a decrease in an existing bias for the cylinder shape remains to be seen.
Although visual place learning has been demonstrated in freely walking flies in 2D environments [6], studies of visual conditioning in head-fixed flies have relied on 1D VR, in which flies are trained to avoid aversive heat by orienting toward certain visual cues [63]. Our paradigm utilized optogenetic activation of heat-sensing neurons, but the detailed knowledge of—and genetic access to—sensory and reinforcement pathways in Drosophila should permit the generation of other “virtual” sensory stimuli using optogenetics [34, 64, 65]. Using optogenetically generated virtual stimuli offers significant advantages for experimental design by enabling the creation of sensations in flies that might otherwise affect their state of health (for example, heat, which can physically damage a fly’s body, or sugar, which might satiate it). Further, precise genetic targeting of stimulation allows the potential behavior-specific role of different pathways that may all be activated by a sensory stimulus [66] to be disambiguated. This experimental approach also allows different sensory modalities to be flexibly paired with the visual VR without the need of hardware or software modifications. Such flexibility could, if combined with automated tethering [67], permit screens in which specific pathways can be activated in isolation to identify the role of different cell types. In addition, the time course of a virtual heat or sugar stimulus is easier to control and does not rule out the use of thermogenetics to modify the activity of different neural populations [68–70].
Our operant visual conditioning paradigm required a head-fixed animal to sample its virtual environment, learn how the unconditioned stimulus related to the visual environment, and alter its behavior based on this relationship within 20 min of training. Operant learning is expected to be harder in 2D than in angular 1D environments, because, unlike in 1D, the visual scene associated with any given reinforced location is not unique and depends on the fly’s heading. Fully sampling this large space of visual stimuli paired with reinforcement requires time, making the task of learning the association significantly more challenging. This is true even in honeybees [71], insects that are well known to rely on visual learning in natural settings [72]. Training flies for longer time periods or biasing the sampling of the environment during training may further strengthen conditioning. Moreover, optogenetically generated virtual heat is likely to be experienced differently than real heat: Flies possess multiple heat sensors feeding into distinct temperature processing pathways [66], many of which may be activated in real heat reinforcement used in existing visual conditioning assays. Nevertheless, our results suggest that activation of HC neurons and their downstream partners is sufficient to induce a visual memory.
What exactly the fly learns during operant visual conditioning is an open question. Based on visual conditioning experiments in 1D visual environments [63] and observations in other free-behaving insects [73, 74], it has been proposed that insects use a snapshot-based visual learning mechanism. The idea of snapshot learning is that the animal associates a specific image template on its retina with the reinforcement rather than recognizing an individual visual feature or landmark in a spatially invariant manner. Some studies have suggested that flies learn retinal-position-invariant associations with patterns to some degree [75], which would be advantageous for visual learning in 2D environments, where the same landmark can generate a variety of different visual stimuli on the retina depending on the fly’s heading direction. This is an issue that our setup should help resolve. In 2D environments there may also be multiple valid behavioral adaptations within a given conditioning paradigm. In our paradigm, for example, flies could learn to selectively approach the non-punished landmark or avoid the punished one. Furthermore, these adaptations may be specific to certain locations within the environment: as an animal approaches a landmark, naive preferences for landmark fixation might be able to override a learned aversion as the image of the looming landmark becomes more salient. Whether flies rely on snapshots of scenes or on position-invariant object recognition for learned navigation is yet unresolved, but 2D VR again provides a tool for probing such questions.
In mammals, tracking animals moving in 2D or 3D settings while simultaneously recording from their brains has uncovered navigational strategies and neural representations thought to be involved in goal-directed navigation [76]. In smaller animals, however, neural recordings at cellular resolution require the animal to be head fixed, which poses a challenge for studying the neural basis of navigational behaviors. Our 2D VR system, which was specifically designed with two-photon calcium imaging in mind, should make it possible to study neural activity under conditions that accurately capture an animal’s visual experience during open-field navigation.
STAR★Methods
Key Resources Table
REAGENT or RESOURCE	SOURCE	IDENTIFIER
Antibodies
Mouse α-bruchpilot (nc82)	Developmental Studies Hybridoma Bank	RRID: AB_2314866
Rabbit α-HA-Tag (C29F4)	Cell Signal Technologies	Cat# 3724; RRID: AB_1549585
Deposited Data
Raw data will be deposited together with analysis code on github.	This paper	www.github.com/jayaraman-lab/HaberkernEtAl2019-2D-VR-for-flies
Experimental Models: Organisms/Strains
Hot Cell-Gal4	From T.J. Florence (Reiser lab, Janelia)	FlyBase: FBti0144107
w∗; P{UAS-mCD8::GFP.L}LL5; P{Gr64f-GAL4.9.7}1/TM3, Sb1	Bloomington Stock Center	stock #57668; RRID: BDSC_57668
pJFRC2-10XUAS-IVS-mCD8::GFP	Janelia Reseach Campus	N/A
pJFRC12-10XUAS-IVS-myr::GFP	Janelia Reseach Campus	N/A
w∗; P{Gr64f-GAL4.9.7}5/CyO; MKRS/TM2	Bloomington Stock Center	stock #57669; RRID: BDSC_57669
Software and Algorithms
FlyVeR source code and installer	This paper	https://github.com/JaneliaSciComp/FlyoVeR
Python code used for data analysis	This paper	https://github.com/jayaraman-lab/HaberkernEtAl2019-2D-VR-for-flies
Other
Website with additional information about the virtual reality system and additional supporting data.	This paper	www.flyfizz.org
Open table in a new tab
Contact for Reagent and Resource Sharing
Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, Vivek Jayaraman (vivek@janelia.hhmi.org).
Experimental Model and Subject Details
Fly strains
Three wild-type strains were used: the isogenic wild-type Berlin (WTB, donated by the Heberlein lab [77]) strain, the Dickinson laboratory (DL, gift from the Reiser lab [78]) strain and WTB hybrid flies. WTB hybrid flies were generated by crossing WTB virgins with males from an enhancerless “empty GAL4” line (pBDPGAL4U in attP2 [79]). WTB hybrid flies were chosen to approximate the genotypes used in optogenetic activation experiments, where an effector line with WTB background is crossed to GAL4 driver lines with variable genetic backgrounds. We chose a WTB background because this genotype has been used in many previous publications on various walking behaviors [45, 80]. For optogenetic stimulation experiments we crossed either Gr64f-Gal4 [54] or Hot cell (HC)-GAL4 [53] to 10xUAS-ChrimsonR-mVenus flies (trafficked in VK00005, WTB background, generated at Janelia Research Campus). The Gr64f-Gal4 line (w; Gr64f-GAL4(737-5)/CyO; Gr64f-GAL4(737-1)/TM3) was constructed from w∗; P{Gr64f-GAL4.9.7}5/CyO; MKRS/TM2 (Bloomington Stock Center, stock #57669) and w∗; P{UAS-mCD8::GFP.L}LL5; P{Gr64f-GAL4.9.7}1/TM3, Sb1 (Bloomington Stock Center, stock #57668).To confirm expression patterns of HC-Gal4 we used two driver lines: pJFRC2-10XUAS-IVS-mCD8::GFP and pJFRC12-10XUAS-IVS-myr::GFP (both Janelia Research Campus).
Fly rearing conditions
Flies were reared at 23°C in 60% relative humidity with a 16:8 light:dark cycle on fly food that was prepared according to a recipe from the University of Würzburg, Germany. To prepare 10 l of Würzburg food, 180 g yeast (inactive dry yeast, Genesee Scientific, San Diego, CA, USA), 1600 g corn meal (Quaker Yellow Corn Meal, Quaker Oats Company, Chicago, IL, USA), 100 g soy flour (Genesee Scientific, San Diego, CA, USA) and 400 g malt extract (Genesee Scientific, San Diego, CA, USA) were mixed in 10 l of water. Then 75 g agar (fly agar, Tic Gums Inc, Belcamp, MD, USA) was dissolved in 1 l of water and added to the mixture. Finally, 400 g corn syrup and an antifungal agent, Tegosept (20%, 125 ml, Genesee Scientific, San Diego, CA, USA), were added. Crosses for generating flies expressing ChrimsonR [81] were set on Würzburg food with added all-trans-retinal (0.2 mM concentration) and offspring were transferred onto food with a higher retinal concentration (0.4 mM). Flies expressing the opsin were reared in low-light condition in a blue acrylic case inside the incubator to prevent: (a) activation of ChrimsonR-expressing neurons and (b) degradation of retinal in the food. We kept flies under low-light rather than in darkness to expose the flies to visual stimuli prior to behavioral experiments, and to ensure a normal circadian rhythm. Control flies for optogenetic activation experiments were also reared inside blue cases, but on standard Würzburg food. Cornmeal and molasses in the standard Würzburg food are a potential source for all-trans-retinal [82, 83]. The exact retinal content of the standard food may vary, but we expect it to be well below 0.001 mM (based on reported retinal content of food ingredients).
Method Details
Confirmation of expression patterns
We used HC-Gal4 > mCD8::GFP (4-6 d) and HC-Gal4 > myr::GFP (6-7 d) to confirm the expression pattern of HC-GAL4. Dissections, immunolabelling and imaging were performed as described in [84]. We looked at the expression pattern in the brain (mCD8::GFP: 7 female, 5 male; myr::GFP: 4 female, 5 male) and the ventral nerve chord (VNC, mCD8::GFP: 5 female, 4 male; myr::GFP: 4 female, 4 male). The image shown in Figure 5A is a montage of maximum intensity projections of two-color stacks of the brain and the VNC.
Preparation of flies for behavior experiments
Prior to experiments, 3-5 day old flies were cold anesthetized, sorted by sex and the distal two thirds of their wings clipped. The decision to use wing-clipped flies was motivated by two observations. First, clipping the wings 1-2 days prior to experiments strongly reduced the rate of attempted take-offs or jumps of tethered flies on the ball. Second, many previous studies on visual navigation in flies have used wing-clipped flies (for example [45]), making it possible to compare our data to those results. After wing-clipping, male and female flies were kept separately and transferred into fresh food vials with a small piece of filter paper, where they were allowed to recover for 2-3 days before experiments. Experiments were performed with 5-10 day old flies. For some experiments, we used an alternative technique to render flies flightless: gluing the wings together in a relaxed position with a small drop of glue right behind the thorax. For experiments in VR, wing-clipped flies were cold-anesthetized and glued to a thin tungsten wire pin with UV-curable glue (KOA 300, KEMXERT, York, PA, USA). With an additional small droplet of glue, deposited above the neck connective, the head was fixed to the thorax, keeping it in a relaxed position. We decided to fix the head to minimize movements of the fly that would disrupt closed-loop visual stimulation. For experiments with virtual sugar stimulation, flies were wet-starved for 24 h prior to experiments by transferring wing-clipped flies to vials containing only a humidified piece of filter paper. Such wet starved flies were then tethered to a pin and used in behavioral experiments within 2 h (effective starvation 24-26 h). For all other experiments, flies were taken directly out of the food vials and tethered to the pin, but were then transferred to VR rig and tested within 3-6 h. Flies were given 10-30 min to adjust to the ball before starting an experiment.
2D visual VR
Miscellaneous hardware
On the ball, the fly was surrounded by a triangular screen formed by two 18.2 cm high and 10.2 cm wide display screens (Figures 1A and S1A–S1C). The fly was located symmetrically between the two screens, 3.1 cm behind the tip of the triangle and at one third of the screen height. The distance between the fly and the screens varied along the azimuthal direction and was smallest at 90° to either side with 2.19 cm. The composite screen spanned 119° of the fly’s azimuthal field of view (FOV) on both sides. The coverage along the vertical FOV was limited by the ball at the lower edge to 40° below the horizon line. The vertical coverage above the horizon line varied with the distance of the fly from the screen being highest where the fly was closest to the screen with 80° and lowest at the two tips of the screen with 57°. The screen was made from a single white diffuser sheet (V-HHDE-PM06-S01-D01 sample, BrightView Technologies, Durham, NC, USA) that was enforced around the edges, folded along the middle and mounted onto a custom-made metal frame. The projectors were connected to a computer via two display ports on a graphics card (GeForce GTX 770, Nvidia, Santa Clara, CA, USA) with three independent outputs. For closed-loop optogenetic stimulation in VR, we used a red LED directed at the fly on the ball (625 nm, M625F1, Thorlabs Inc, Newton, NJ, USA). We calibrated the optogenetic stimulus by measuring the light intensity with a power meter (PM100D with S130C Sensor, at 625 nm with range setting 1.3 mW) for a range of LED drives (Figure S1D). We adjusted the room temperature and humidity to maintain a temperature of around 28°C–30°C and a relative humidity of 28%–32% in the VR rig.
Spherical treadmill
We used a spherical treadmill as described in [22]. The treadmill ball was hand-milled from polyurethane foam (FR-7120, Last-A-Foam, General Plastics Manufacturing Company, Tacoma, WA, USA) and had a diameter of 9.93 mm and a weight of 37 mg. The ball was freely floating on an aircushion in a custom-made holder. The airflow to the ball was maintained at 0.45 l/min using a mass flow controller (Alicat Scientific, Tucson, AZ, USA) and humidified by passing it through a bottle humidifier (Salter Labs, Lake Forest, IL, USA). The ball surface was illuminated from below and the side with a set of four IR LEDs emphasizing the texture of the ball surface for high tracking performance. The ball motion was captured by a previously described ball tracker system [22]. The treadmill readout had arbitrary spatial units per time (au/s). To obtain a ball rotation velocity measurement in mm/s the treadmill output was calibrated using a third (calibration) camera and the same calibration procedure as described in [22]. We used a custom MATLAB script and a programmable microcontroller (Arduino Mega 2000, Figure S1A) to generate a trigger sequence for the calibration camera that was synchronized with a treadmill recording.
Projector-based visual display
The visual display consisted of a triangular screen onto which a panoramic image was back-projected by two DLP (Digital Light Processing, also referred to as digital mirror device or DMD) projectors (DepthQ WXGA 360 HD 3D Projector, developed by Anthony Leonardo, Janelia, and Lightspeed Design, Bellevue, WA, USA). The two projectors each generated an image with 720 × 1280 pixel resolution, and were aligned to generate a continuous panorama (1440 × 1280 pixel). At the closest point (90° to either side, 2.19 cm distance), a pixel subtended a visual angle of 0.74°. The furthest pixels on the screen, located in the upper back corners of the screen (10.65 cm distance), subtended an angle of 0.15°. Thus, the maximum angular pixel size in our setup is well below 5°, the approximate interommatidial angle of Drosophila melanogaster [85], ensuring that the movement of images across the screen appears smooth to the fly. The projectors we used were customized to deliver visual stimuli to the fly. The color-wheel was removed to allow the display of 8-bit gray-scale images at a frame rate of 360 Hz. This ensured a refresh-rate above the animal’s flicker fusion frequency, making the projected movements look continuous to a fly [86–88]. Furthermore, the optics were optimized for close-range projection and the lamp was replaced with a light guide to a blue LED light source (458 nm wavelength, SugarCUBE LED Illuminator, Edmund Optics Inc, Barrington, NJ, USA). Although blue light is not the ideal choice for behavioral assays, we chose this wavelength to permit easier transfer of the behavioral paradigm to commonly used two-photon calcium imaging setups in the future. We measured the irradiance of the projected image on the panoramic screen with a power meter (PM100D with S130C Sensor, Thorlabs Inc, Newton, NJ, USA, sensor facing toward the projector) for a wavelength of 459 nm (peak wavelength in previously measured spectrogram). When a bright scene with one dark landmark was projected onto the screen, we measured a light intensity of 0.52 mW/cm2 in the center of the right screen and 0.54 mW/cm2 on the left screen. The light intensity within the image of a black landmark projected onto the center of the right screen was 0.02 mW/cm2. Thus, the projected image had a Michelson contrast of about 0.93.
Software for 2D VR
The treadmill system tracked the ball’s movements at 4 kHz and this data was downsampled to 400 Hz by a custom-written C++ application (Remote Data Server, RDS) and passed on to FlyoVeR. The FlyoVeR application is a modified version of the Jovian/MouseoVeR software [42] (see www.flyfizz.org for details). We achieved a high refresh rate of the displayed images by rendering sets of three frames at a time in FlyoVeR and packing them into the red, green and blue color channel for a full color frame buffer, which were displayed sequentially and refreshed at 120 Hz. FlyoVeR computed the fly’s walking velocities from the treadmill’s ball rotation measurements as described in [22]. The walking velocities were then integrated to compute the fly’s position using two calibration factors, one for converting treadmill output from [au/s] to [pixels/s] and one to convert [pixels/s] to [mm/s] (see www.flyfizz.org for details). The calibration factors as well as the ball radius were provided to FlyoVeR through a GUI. A small square at the edge of the projected image, whose color was toggled between white and black with each newly drawn frame, served as a frame rate indicator, which could be read out with a photodiode. Data on the fly’s virtual position and velocity was logged at 360 Hz.
FlyoVeR also sent a reduced output stream (at 60 Hz) via a serial connection to a microcontroller (Arduino Mega 2000). The microcontroller then set the red stimulation LED to the light intensity specified by the reinforcement level parameter. We measured the relationship between current input (characterized in % of maximum current) and light intensity for the red stimulation light, which was, with the exception of very low input currents, approximately linear (Figure S1D). We used this empirical calibration curve to translate light intensities that worked in the free walking arena to light levels to be used in VR.
Virtual world design
Custom 3D scenes were designed in created with the free 3D modeling program Blender (version 2.73) and were exported in Collada (version 2.4) format, a standardized XML format used to describe 3D graphics. Collada files could then be loaded into FlyoVeR though the graphical user interface.
Each object within the 3D scene had a unique name and a set of properties. Properties such as the color and texture were specified in Blender as “materials” that were then assigned to the respective object. Other properties such as object visibility were communicated to FlyoVeR as part of the object’s name string (see www.flyfizz.org for details).
1D stripe fixation: For 1D stripe fixation experiments, we generated a 3D scene consisting of a cylinder centered around the fly’s virtual position. The cylinder was subdivided into 360 vertical faces, such that each face corresponded to a vertical strip of 1° angular width when seen from the cylinder center. For dark-on-bright stripe fixation experiments we used a cylinder with 20 consecutive faces colored black and all other faces white, corresponding to a 20° wide black stripe on a white background. For the bright-on-dark stripe fixation experiments the colors were reversed.
2D scenes: Virtual worlds for 2D VR experiments consisted of a large textured ground plane with sparsely distributed landmarks (Figures S1E and S1H). In most experiments, we used a scene with black landmarks on a bright background and a lightly textured ground plane, matching the conditions in the free walking assay (dark-on-bright condition). For the ground plane texture, we chose a white-noise gray scale pattern with pixels varying either between 0% and 50% black level (low contrast, see images in Figure S1F) or between 0% and 100% (high contrast). The low-contrast ground plane was used in all experiments, except when making comparisons to free walking. Landmarks were always impenetrable, that is, the fly could not move into or through the virtual landmarks. The dimensions of the virtual landmarks were chosen to match real landmarks that induced frequent approaches in freely walking flies (data from a pilot study). Free walking experiments also informed the spacing of the virtual landmarks relative to each other. The area of the virtual world that flies could explore was bounded by an invisible, impenetrable cylinder (Figures S1E and S1H). A white, flattened sphere encompassing the arena border and the ground plane served as a backdrop. The overall size of the virtual world was chosen based on pilot experiments in VR to ensure that most flies did not reach the arena border within a 10 min trial. Each visible landmark was surrounded by a slightly (0.5 mm) larger invisible object of the same shape to prevent visual artifacts when a fly came close to the surface of the landmark. In bright-on-dark trials the color of all components was inverted, i.e., we used white landmarks, black fog and the ground plane texture pattern was inverted.
We used two types of 2D scene geometries:
•	
“Cone forest”: Periodic world with only one landmark shape: 10 × 40 mm large cones. Landmarks were placed on the nodes of a triangular grid (Figures S1E and S1G). Cones were fully hidden by virtual fog at distance greater than 70 mm, gradually emerged from the fog when the fly was closer than 70 mm and came into full contrast at distances smaller than 55 mm, at which point the cones had an angular width of 10.39° at the base and an angular height of 36.03° (Figures 1J and S1G).
•	
“Cone and cylinder forest”: Periodic world with two landmark shapes: 10 × 40 mm cones and 8 × 30 mm cylinders. The two types of landmarks were alternatingly placed on the nodes of a Cartesian grid at a distance of 60 mm (Figures S1H and S1I). The virtual fog started at a distance of 15 mm and reached full coverage at a distance of 45 mm (Figure S1I).
Free-walking arena
The free-walking arena design (Figures S2A–S2C, S5C, and S5D) was inspired by a previous study [46, 81] and built to match lighting, space and landmark-interaction in VR. Specifically, the arena featured a large open space to reduce encounters with walls, and, when needed, small unclimbable objects. The arena consisted of a large circular walking platform (radius 11.4 cm) made from textured matt acrylic (TAP Plastics Inc, San Leandro, CA, USA) surrounded by an acrylic cylinder (inner diameter 22.8 cm, height 17.8 cm) mounted on a laser cut acrylic base. The walking platform could be taken out for cleaning. Coating the arena wall with a siliconizing fluid (Sigmacote from Sigma-Aldrich, St. Louis, MO, USA) prevented wing-clipped flies from walking up the wall. The arena wall was mantled with a white diffusor sheet (V-HHDE-PM06-S01-D01 sample, BrightView Technologies, Durham, NC, USA) and backlit with blue LEDs (470 nm, Super Bright LEDs Inc. St. Louis, MO, USA) mounted on a wire mesh-based scaffold that was fixed onto the arena base. A blue-colored backlight was chosen to match conditions in the VR setup. The light intensity inside the free walking arena measured with a power meter (PM100D with S130C Sensor, Thorlabs Inc, Newton, NJ, USA) for an expected wavelength of 461 nm (peak wavelength in spectrogram) was 0.115 mW/cm2 at the arena border and 0.105 mW/cm2 in the center.
Four custom-made LED panels mounted below the free walking platform, delivered infrared (IR) backlighting for high-contrast video recordings of the fly’s walking behavior (see below) and red stimulation light (627 nm) for optogenetic stimulation. Each LED panel contained spatially intercalated IR and red (LXM2-PD01-0050, LUXEON Rebel Color, Philips Lumileds Lighting Company, San Jose, CA, USA) LEDs. The four panels were mounted on a water-cooled breadboard (breadboard from Thorlabs Inc, Newton, NJ, USA, liquid cooling system from Koolance, Auburn, WA, USA) and connected to a microcontroller board built around a Teensy 2.0 processor (PJRC.com, LLC Sherwood, OR, USA). Light intensities of the IR and red stimulation LEDs were controlled from a computer using serial communication with the microcontroller. The red LEDs could be individually targeted to control illumination independently in 16 sectors. A cross-shaped light separator reduced light spreading from the illuminated to the non-illuminated LED panels (quadrants). Serial commands to the LED controller were sent through a custom-written Python (version 2.7) program, to ensure temporally precise and repeatable delivery of a light stimulation protocol. Four IR LEDs placed at the corners of the arena base plate were coupled to red illumination in the respective quadrant. These four LEDs served as indicators for the red-light stimulation in videos of the free walking arena (see below, Figure S5D). We measured the relationship between LED controller input to the red LEDs and light intensity at 627 nm (Figure S5B, Thorlabs power meter PM100D with S130C Sensor; in ON quadrant measurements range = 1.3 mW for < 10% and 13 mW above, in OFF quadrants range = 1.3 mW) in a dark room with two out of four quadrants, i.e., two out of four LED panels, switched on (Figure S5C). With 1%, 5% and 10% current we measured a light intensity of 0.27 mW/cm2 (0.01 mW/cm2), 1.13 mW/cm2 (0.05 mW/cm2) and 2.25 mW/cm2 (0.11 mW/cm2) in the illuminated quadrant, respectively (measurement in the non-illuminated quadrant in brackets).
The flies’ behavior was recorded with BIAS (Basic Image Acquisition Software, version v0p49, IO Rodeo, Pasadena, CA, USA) using a video camera (Flea3 1.3 MP Mono USB3 Vision, Point Grey, Richmond, Canada) placed 120 cm above the walking platform. A lens with 16 mm focal length, low distortion (Edmund Optics Inc, Barrington, NJ, USA, stock #63245) and a 760 nm IR filter (52 mm, Neewer Technology Ltd., Guangdong, China) were mounted to the camera. Videos were recorded at 12.3 Hz (landmark interaction validation assay) or 20 Hz (quadrant assay) with 1008 × 1008 pixel large images covering an area slightly larger than the diameter of the arena resulting in a spatial resolution of about 40 pixel/cm. The entire rig was placed inside a light-tight black enclosure and temperature and relative humidity were kept at 28°C–30°C and 28%–32%.
Behavioral assays
Fixation assay in VR
All fixation assays were performed at high room temperature (30°C) unless stated otherwise. We performed two types of assays:
•	
Black stripe fixation: One 10 min trial per fly with the dark-on-bright 20° wide stripe. Through the FlyoVeR GUI visual feedback from translational movements was disabled.
•	
Comparison of fixation in 1D and 2D scenes with contrast inversion: Each fly was tested in four 10 min trials, presented in random order. In two trials we used the dark-on-bright condition and in the other two the bright-on-dark condition. For each condition, we ran one stripe fixation (1D, translation disabled in FlyoVeR) trial and one trial with the cone forest (2D).
Validation of landmark interaction
VR experiments: Each fly was exposed to 4 trials (10 min each) in the dark-on-bright cone forest VR. In three out of the four trials the landmarks were visible, in one trial they were invisible, i.e., no visual cue was provided as to where the landmark was. The three trials with visible landmarks were always measured in a block with the invisible landmark measured either as the first or last trial.
Free walking experiments: We placed a small 3D-printed black cone, which served as a landmark, in the center of the free walking arena (Figures S2A and S2C). The cone had the same dimensions as the virtual cones used in the cone forest world (10 mm wide, 40 mm high). The surface of the object was polished to reduce surface texture. To prevent flies from climbing and resting on the cone, a coated (SurfaSil, Fisher Scientific, Thermo Fisher Scientific, Waltham, MA, USA) glass cylinder (ø = 15 mm) was placed around the cone. A single wing-clipped fly was introduced to the arena and it was given 1-2 min to explore the space before starting the video recording for a 10 min trial. After each measurement, the fly was removed from the arena and the arena floor was wiped with wet tissue paper.
“Virtual sugar” stimulation in freely walking flies
Groups of 10-15 wing-cut female Gr64f-Gal4 > ChrimsonR flies were inserted into free walking arena with ambient blue light (but no objects) and walking behavior was filmed during a 4 min long stimulation protocol. The protocol consisted of 15 pulses (200 ms long and with a light intensity of 1.58 mW/cm2), each separated by a 15 s long break. Flies were either wet starved for 24 h in an empty food vial with a humidified filter paper (starved group) or wet starved for 3 h and then transferred back on food for ∼1 h (fed group).
Quadrant assay in freely walking flies
We used a free walking quadrant assay inspired by [81] to screen stimulation paradigms for their capacity to induce avoidance behavior. HC-GAL4 > ChrimsonR flies were exposed to a stimulation protocol consisting of a 10 s long pre-stimulation period followed by 6 blocks of 30 s of red light stimulation separated by 10 s with no stimulation (Figure S5A). During the 30 s stimulation blocks, red light illumination was restricted to two opposing quadrants and the illuminated quadrants were alternated in consecutive blocks. Per trial responses of all-male or all-female groups of 12-18 wing-clipped flies were measured.
Local search in VR
In all local search experiments, we used 24h wet-starved female, wing-cut Gr64f-Gal4 > ChrimsonR flies. For all three experimental groups we used the black-on-bright cone forest VR, but landmark visibility and optogenetic stimulation differed:
•	
Opto stim: Invisible cones and optogenetic stimulation (1.29 mW/cm2).
•	
Opto stim + obj: Visible cones and optogenetic stimulation (1.29 mW/cm2).
•	
Only obj: Visible cones, but effectively no optogenetic stimulation. For convenience the level of optogenetic stimulation was set to 1%, corresponding to < 0.05 mW/cm2, so that flies were not stimulated, but the data could be analyzed in the same way as for the other two groups.
Optogenetic stimulation was triggered whenever the fly crossed the 10 mm visit radius around the center of a cone. Regardless of what the fly did, optogenetic stimulation lasted for 200 ms. After a stimulation event was triggered, a fly had to leave a 30 mm large zone around the cone at which the optogenetic stimulation had been triggered, to re-enable successive stimulation at that site. Whenever flies resided for more than 30 s within 7 mm radial distance from the center of a cone, they were teleported back to the starting position.
“Virtual heat” avoidance in VR
In “virtual heat” avoidance experiments we tested each fly in four 10 min long trials in the cone forest world. Three trials with visible landmarks were measured in a block consisting of a “Obj pre” and “Obj post” trial, in which the fly was free to explore the purely visual VR, and a “Obj + opt”, in which each landmark was paired with a virtual heat zones (Figure 5B). Either before or after this block, virtual heat avoidance was tested in world with invisible landmarks paired with virtual heat zones (“Opt” trial). Circular virtual heat zones had a radius of 40 mm.
Visual conditioning
For visual conditioning assay we used the dark-on-bright cone and cylinder forest (Figure S1H). The protocol consisted of three trials, a 10 min “Pre” trial, a 20 min “Training” trial and a 10 min “Post” trial.
Aversive visual conditioning with virtual heat: In the aversive visual conditioning experiments, we used male, 5-10d old HC-GAL4 > ChrimsonR flies. In the pre and post trial phases, flies received constant low-level optogenetic stimulation (0.35 mW/cm2) independent of their position in the VR. In the training trial virtual heat and virtual cool zones were introduced by varying optogenetic stimulation levels as a function of the fly’s position in the VR. Both zones had a radial size of 25 mm. In the cool zones the stimulation decreased from baseline to 0 mW/cm2, while in the heat zones the stimulation increased from baseline to 0.81 mW/cm2. In all trials, a fly was “teleported” to the start location if it remained within a 7 mm radius around a landmark for more than 30 s.
Appetitive visual conditioning with virtual sugar: In appetitive visual conditioning experiments, we used 5-10d old Gr64f > ChrimsonR flies. In pre and post trials, no optogenetic stimulation was provided. In training trials each visit (15 mm radius) to the reward landmark resulted in a 200 ms optogenetic stimulation of 1.29 mW/cm2.
Quantification and Statistical Analysis
Preprocessing and data selection criteria
Data from free and tethered walking experiments were treated the same way with exception of movement thresholds and sampling rate. To analyze data from VR trials (logged at 360 Hz), the log file saved by FlyoVeR was parsed with a custom Python (version 2.7) script to extract trial-specific information from the header and the time series data, which was downsampled to 20 Hz using linear interpolation. The locations of objects in the 3D scene used in the respective trial were read from the coordinate file as specified in the log file header. Most of the analysis of walking trajectories in 2D virtual worlds was performed on “collapsed” trajectories, i.e., after pooling trajectory fragments across different locations of the VR that correspond to the same sensory environment, exploiting the periodicity of the virtual world. To obtain collapsed trajectories from trials in the cone forest, trajectory fragments within a radial distance of 60 mm each of the periodically placed cone were projected onto a circular area (radius = 60 mm) around the central landmark (Figures 1H and 1I) preserving the absolute heading direction. Trajectories from trials with the cone and cylinder forest were collapsed in a similar way onto the central square formed by two cylinders and two cones (Figure S1H; Video S1). Walking trajectories from free walking experiments were extracted from video recordings using Ctrax [89]. The video frame corresponding to the beginning of the optogenetic stimulation protocol in the quadrant assay was determined for each video using custom macros in Fiji (version 2.0.0-rc-43), by monitoring the brightness of one of the indicator IR LEDs. The trajectory time series from VR and free walking experiments were further analyzed in Python (version 2.7). We classified the behavior of a fly on a per time step basis as “moving” if the instantaneous translational velocity exceeded 2 mm/s in VR experiments and 5 mm/s in free walking experiments. On a per trials basis we classify the behavior of a fly as “walking” if the fly was moving for more than 20% of the trial time.
Quantification of fixation behavior
To quantify fixation behavior, we employed the following strategy: We first selected all trials in which the fly was walking and computed the relative heading angle of the fly with respect to the stripe or the center of the landmark, i.e., the angular location of the stripe or landmark in the fly’s field of view (Figures S3C and S3D). From this we computed the frequency distribution of relative heading angles for each trial using 20° wide bins (Figures S3E and S3F). We then attempted to fit the heading distribution with a von Mises distribution (Figure S3E), which is mathematically described as
𝑓⁡(𝑥|⁢𝜇,𝜅)=
𝑒𝜅⁢cos⁡(𝑥−𝜇)
2⁢𝜋 𝐼0⁡(𝜅)
.
The von Mises distribution is unimodal, i.e., it has a single peak whose location is set by the location parameter μ∈(−𝜋,𝜋]. The height of the peak is a function of the shape parameter κ. The larger κ, the more mass is centered at the location μ. If κ = 0, the von Mises becomes a uniform circular distribution. If a good fit with a von Mises distribution could be achieved (p > 0.1 with a Kolmogorov-Smirnov test) and the fit had a shape parameter κ > 0.5, we classified a fly’s behavior as “unimodal fixation.” Some trials showed a very narrow fixation peak on top of a baseline, which is not well fitted by a von Mises. We therefore also classified a trial as unimodal fixation, if the length of the mean angular vector (PVA, population vector average) was larger than 0.5 even if no good fit was achieved. Among the heading distributions that did not match the criteria for unimodal fixation, several showed two defined peaks (Figure S3F). We therefore added a second step, in which we tried to fit the not yet classified distributions with a bimodal distribution generated by adding two von Mises that share the same shape parameter:
𝑓⁡(𝑥|⁢𝜇1,𝜇2,𝜅)=
1
2
⁢(
𝑒𝜅⁢cos⁡(𝑥−𝜇1)
2⁢𝜋 𝐼0⁡(𝜅)
+
𝑒𝜅⁢cos⁡(𝑥−𝜇2)
2⁢𝜋 𝐼0⁡(𝜅)
)
If a good fit with a shape parameter κ > 0.5 could be achieved with this bimodal distribution, the respective trial was classified as “bimodal fixation.” All remaining trials were classified as “unclassified.” In Figures 3D, 3F, and 3G, we also made a distinction between trials that were well fitted with a unimodal or bimodal von Mises distribution, respectively, but did not fulfill the fixation criteria (“Good fit, no fixation”, p < 0.1, κ < 0.5 and PVA < 0.5) as opposed to trials that matched fixation criteria (“Fixation”).
Visit analysis
We quantified “visits” to a landmark as approaches up to a radial distance of a defined “visit radius” or less. We chose a visit radius of 10 mm for local search experiments, the radius at which virtual sugar was delivered, and 15 mm for all other experiments, the radius at all landmarks but the closest ones are hidden. The visit length was defined as the time period between entering and exiting the zone defined by the visit radius.
Quantification of local search paths
Our analysis of local search after virtual sugar stimulation focused on trajectory fragments (paths) before and after a stimulation event. For Figures 4B–4D, we considered paths of 150 mm length, and ignored paths that were truncated by the beginning or the end of the trial or by preceding or following stimulation events. For the analyses in Figures 4E, 4G–4I, and S4I–S4K, we focused on paths during the 20 s following a stimulation event, again only considering paths that were not truncated. For the time-window-based analysis we first averaged paths from a single fly (median) and then across flies (median, IQR). To compute path curvature, we reparametrized the paths by their respective path lengths instead of time, such that consecutive pairs of x and y coordinates along the path were separated by a constant path distance. The path length increment was chosen such that reparametrized paths had the same number of total points as the initial time-parameterized paths. These paths were sufficiently smooth to allow curvature to be computed numerically as
𝑘=
𝑥'⁢𝑦''−𝑦'⁢𝑥''
(𝑥'2+𝑦'2)
3
2
Subsequently the computed curvature k was smoothed with a Savitzky–Golay filter (window: 15, order: 3). To assess evidence for path integration (Figure S4E, S4F, S4L, and S4M) we used measures of behaviors during search bouts, inspired by recent studies [27, 39]. A search bout lasted from the time when a fly triggered a stimulation event to when it left a 55 mm radius around the cone associated with the respective stimulation site. These bouts also defined corresponding paths. A search bout could contain additional stimulation events, which were then omitted as starting points of further search bouts. During search bouts we defined turns as path segments with an absolute curvature > 0.1. This value was chosen based on visual inspection of the data. All non-turn segments of minimal length 0.5 mm were defined as runs. Data within a 6 mm radius around virtual objects was excluded from the analysis to avoid artifacts induced by the impenetrability of virtual objects.
Statistics
Quadrant assay (Figure S5G): Two-sided one-sample t test (null hypothesis: sample mean = 0.5, ttest_1samp from scipy package, python 2.7) over the median residency per experimental repeat within the last 10 s of the stimulation block.
Stimulation	Male, + Retinal	Female, +Retinal	Male, -Retinal	Female, -Retinal
0.27 mW/cm2	p = 3.31e-17 (∗∗∗)	p = 8.39e-10 (∗∗∗)	p = 0.1853 (ns)	p = 0.5235 (ns)
1.13 mW/cm2	p = 4.47e-42 (∗∗∗)	p = 1.41e-18 (∗∗∗)	p = 3.18e-10 (∗∗∗)	p = 0.0472 (∗)
2.25 mW/cm2	p = 3.29e-37 (∗∗∗)	p = 1.32e-31 (∗∗∗)	p = 3.63e-16 (∗∗∗)	p = 0.0011 (∗∗)
Open table in a new tab
“Virtual heat” avoidance in VR (Figures 5F and 5G): We used a two-sided one-sample t test (ttest_1samp from scipy package, python 2.7) to test if the difference between the total visit counts between two trials was different from zero.
Group	Entries to virtual heat zone (visit count at 40 mm), comparing “Opt alone” and “Opt + object” trials (Figure 5F).	Comparison of object visits (15 mm radius) before (“Object pre”) and after (“Object post”) pairing of objects with virtual heat (Figure 5G).
No baseline	n = 25, t = −1.4616, p = 0.1568 (ns)	n = 25, t = −0.9269, p = 0.3632 (ns)
Baseline	n = 25, t = −2.3111, p = 0.0297 < 0.05 (∗∗)	n = 25, t = 0.9141, p = 0.3697 (ns)
Open table in a new tab
Visual conditioning in VR (Figures S6A–S6C): We used a two-sided one-sample t test (ttest_1samp from the scipy package, python 2.7) to test if the difference between the ratios of total visits in the pre and post trials (over the entire 10 min) was different from zero.
Group	Ratio of visit counts to cone-cylinders in pre – post trial
Anti-Cylinder	n = 22, t = −3.3471, p = 0.0031 < 0.005 (∗∗)
Anti-Cone	n = 11, t = 0.3290, p = 0.7489 (ns)
Control	n = 22, t = 0.5906, p = 0.5611 (ns)
Open table in a new tab
Data and Software Availability
Code availability
The FlyoVeR codebase and an installer for FlyoVeR are available at: https://github.com/JaneliaSciComp/FlyoVeR.
The analysis code is available at: https://github.com/jayaraman-lab/HaberkernEtAl2019-2D-VR-for-flies.
Data availability
The raw data is available at: https://github.com/jayaraman-lab/HaberkernEtAl2019-2D-VR-for-flies.
Additional Resources
More detailed information about the virtual reality setup, the design of virtual worlds and additional data on fixation behavior is provided on www.flyfizz.org.
Acknowledgments
We thank Brian Coop and Anthony Leonardo for help with building the projector-based display; Albert Lee for sharing the MouseoVeR code base as a basis for the FlyoVeR software; Laura Porta for pilot experiments with Gr64f; Abel Corver for help with the Gr64f conditioning experiments; TJ Florence, Ed Rogers, and Gabriella Sterne for sharing flies from their local stocks; and Michael Reiser, Eugenia Chiappe, Rebecca Yang, TJ Florence, Yoshi Aso, Tilman Triphan, Claire Eschbach, Alice Robie, Ann Hermundstad, and members of the Jayaraman lab for discussions and advice. We thank John Tuthill and David Schoppik for tweet-upgrading the title of the study. We thank Janelia’s Project Technical Resources team for dissections, immunolabelling, and imaging to confirm expression patterns. We are grateful to members of the Jayaraman lab for feedback on the manuscript. B.A. and M.A.B. were supported by the Janelia Undergraduate Scholar program. This work was supported by the Howard Hughes Medical Institute.
Author Contributions
H.H. and V.J. designed the project. B.A. built a pilot VR setup with help from J.D.C. M.B. and C.B. developed the FlyoVeR software with input from H.H., J.D.C., and V.J. H.H., with input from V.J., built the VR setup and wrote software for hardware control. H.H. designed virtual worlds, built the free walking arena, and performed optogenetically triggered local search, virtual heat avoidance, and conditioning experiments. H.H. and M.A.B. performed crosses, prepared flies, and performed fixation behavior experiments. H.H. analyzed all data. H.H. and V.J. wrote the manuscript.
Declaration of Interests
The authors declare no competing interests.
Supplemental Information (2)
Download all
PDF (16.66 MB)
Document S1. Figures S1–S6
PDF (34.49 MB)
Document S2. Article plus Supplemental Information
Related announcements
NEWS
INSPIRING SCIENTISTS
November 21, 2024
Neuroscientist Vivek Jayaraman on daring to pursue less-traveled paths in science

Exploring complex behaviors in the brains of flies with Dr. Jayaraman. 

References
1.
Frisch, K.v.
The dance language and orientation of bees
Belknap Press of Harvard University Press, Cambridge, Mass., 1967
Google Scholar
2.
Tinbergen, N. ∙ Kruyt, W.
Über die Orientierung des Bienenwolfes (Philanthus triangulum Fabr.)
Z. Vgl. Physiol. 1938; 25:292-334
Google Scholar
3.
Müller, M. ∙ Wehner, R.
Path integration in desert ants, Cataglyphis fortis
Proc. Natl. Acad. Sci. USA. 1988; 85:5287-5290
Crossref
PubMed
Google Scholar
4.
Wehner, R. ∙ Srinivasan, M.V.
Searching Behavior of Desert Ants, Genus Cataglyphis (Formicidae, Hymenoptera)
J. Comp. Physiol. 1981; 142:315-338
Crossref
Scopus (384)
Google Scholar
5.
Dacke, M. ∙ Baird, E. ∙ Byrne, M. ...
Dung beetles use the Milky Way for orientation
Curr. Biol. 2013; 23:298-300
Full Text
Full Text (PDF)
Scopus (147)
PubMed
Google Scholar
6.
Ofstad, T.A. ∙ Zuker, C.S. ∙ Reiser, M.B.
Visual place learning in Drosophila melanogaster
Nature. 2011; 474:204-207
Crossref
Scopus (300)
PubMed
Google Scholar
7.
Collett, T.S. ∙ Collett, M.
Memory use in insect visual navigation
Nat. Rev. Neurosci. 2002; 3:542-552
Crossref
Scopus (292)
PubMed
Google Scholar
8.
Wehner, R.
Desert ant navigation: how miniature brains solve complex tasks
J. Comp. Physiol. A Neuroethol. Sens. Neural Behav. Physiol. 2003; 189:579-588
Crossref
Scopus (465)
PubMed
Google Scholar
9.
Collett, M. ∙ Chittka, L. ∙ Collett, T.S.
Spatial memory in insect navigation
Curr. Biol. 2013; 23:R789-R800
Full Text
Full Text (PDF)
Scopus (242)
PubMed
Google Scholar
10.
Dombeck, D.A. ∙ Reiser, M.B.
Real neuroscience in virtual worlds
Curr. Opin. Neurobiol. 2012; 22:3-10
Crossref
Scopus (76)
PubMed
Google Scholar
11.
Stowers, J.R. ∙ Hofbauer, M. ∙ Bastien, R. ...
Virtual reality for freely moving animals
Nat. Methods. 2017; 14:995-1002
Crossref
Scopus (155)
PubMed
Google Scholar
12.
Hölscher, C. ∙ Schnee, A. ∙ Dahmen, H. ...
Rats are able to navigate in virtual environments
J. Exp. Biol. 2005; 208:561-569
Crossref
Scopus (147)
PubMed
Google Scholar
13.
Dombeck, D.A. ∙ Harvey, C.D. ∙ Tian, L. ...
Functional imaging of hippocampal place cells at cellular resolution during virtual navigation
Nat. Neurosci. 2010; 13:1433-1440
Crossref
Scopus (567)
PubMed
Google Scholar
14.
Aronov, D. ∙ Tank, D.W.
Engagement of neural circuits underlying 2D spatial navigation in a rodent virtual reality system
Neuron. 2014; 84:442-456
Full Text
Full Text (PDF)
Scopus (166)
PubMed
Google Scholar
15.
Acharya, L. ∙ Aghajan, Z.M. ∙ Vuong, C. ...
Causal Influence of Visual Cues on Hippocampal Directional Selectivity
Cell. 2016; 164:197-207
Full Text
Full Text (PDF)
Scopus (89)
PubMed
Google Scholar
16.
Gray, J.R. ∙ Pawlowski, V. ∙ Willis, M.A.
A method for recording behavior and multineuronal CNS activity from tethered insects flying in virtual space
J. Neurosci. Methods. 2002; 120:211-223
Crossref
Scopus (39)
PubMed
Google Scholar
17.
Takalo, J. ∙ Piironen, A. ∙ Honkanen, A. ...
A fast and flexible panoramic virtual reality system for behavioural and electrophysiological experiments
Sci. Rep. 2012; 2:324
Crossref
Scopus (27)
PubMed
Google Scholar
18.
Kaupert, U. ∙ Thurley, K. ∙ Frei, K. ...
Spatial cognition in a virtual reality home-cage extension for freely moving rodents
J. Neurophysiol. 2017; 117:1736-1748
Crossref
Scopus (13)
PubMed
Google Scholar
19.
Jouary, A. ∙ Haudrechy, M. ∙ Candelier, R. ...
A 2D virtual reality system for visual goal-driven navigation in zebrafish larvae
Sci. Rep. 2016; 6:34015
Crossref
Scopus (21)
PubMed
Google Scholar
20.
Wolf, R. ∙ Heisenberg, M.
Visual control of straight flight in Drosophila melanogaster
J. Comp. Physiol. A Neuroethol. Sens. Neural Behav. Physiol. 1990; 167:269-283
Crossref
Scopus (68)
PubMed
Google Scholar
21.
Maimon, G. ∙ Straw, A.D. ∙ Dickinson, M.H.
A simple vision-based algorithm for decision making in flying Drosophila
Curr. Biol. 2008; 18:464-470
Full Text
Full Text (PDF)
Scopus (135)
PubMed
Google Scholar
22.
Seelig, J.D. ∙ Chiappe, M.E. ∙ Lott, G.K. ...
Two-photon calcium imaging from head-fixed Drosophila during optomotor walking behavior
Nat. Methods. 2010; 7:535-540
Crossref
Scopus (230)
PubMed
Google Scholar
23.
Buchner, E.
Elementary movement detectors in an insect visual system
Biol. Cybern. 1976; 24:85-101
Crossref
Scopus (250)
Google Scholar
24.
Bahl, A. ∙ Ammer, G. ∙ Schilling, T. ...
Object tracking in motion-blind flies
Nat. Neurosci. 2013; 16:730-738
Crossref
Scopus (112)
PubMed
Google Scholar
25.
van Breugel, F. ∙ Dickinson, M.H.
The visual control of landing and obstacle avoidance in the fruit fly Drosophila melanogaster
J. Exp. Biol. 2012; 215:1783-1798
Crossref
Scopus (110)
PubMed
Google Scholar
26.
Saxena, N. ∙ Natesan, D. ∙ Sane, S.P.
Odor source localization in complex visual environments by fruit flies
J. Exp. Biol. 2018; 221:172023
Crossref
Scopus (32)
Google Scholar
27.
Kim, I.S. ∙ Dickinson, M.H.
Idiothetic Path Integration in the Fruit Fly Drosophila melanogaster
Curr. Biol. 2017; 27:2227-2238.e3, e2223
Full Text
Full Text (PDF)
Scopus (83)
PubMed
Google Scholar
28.
Álvarez-Salvado, E. ∙ Licata, A.M. ∙ Connor, E.G. ...
Elementary sensory-motor transformations underlying olfactory navigation in walking fruit-flies
eLife. 2018; 7:e37815
Crossref
Scopus (72)
PubMed
Google Scholar
29.
Moore, R.J. ∙ Taylor, G.J. ∙ Paulk, A.C. ...
FicTrac: a visual method for tracking spherical motion and generating fictive animal paths
J. Neurosci. Methods. 2014; 225:106-119
Crossref
Scopus (66)
PubMed
Google Scholar
30.
Bell, J.S. ∙ Wilson, R.I.
Behavior Reveals Selective Summation and Max Pooling among Olfactory Processing Channels
Neuron. 2016; 91:425-438
Full Text
Full Text (PDF)
Scopus (51)
PubMed
Google Scholar
31.
Schulze, A. ∙ Gomez-Marin, A. ∙ Rajendran, V.G. ...
Dynamical feature extraction at the sensory periphery guides chemotaxis
eLife. 2015; 4:e06694
Crossref
Scopus (72)
Google Scholar
32.
Lin, H.-H. ∙ Chu, L.-A. ∙ Fu, T.-F. ...
Parallel neural pathways mediate CO2 avoidance responses in Drosophila
Science. 2013; 340:1338-1341
Crossref
Scopus (51)
PubMed
Google Scholar
33.
Klein, M. ∙ Afonso, B. ∙ Vonner, A.J. ...
Sensory determinants of behavioral dynamics in Drosophila thermotaxis
Proc. Natl. Acad. Sci. USA. 2015; 112:E220-E229
Crossref
Scopus (104)
PubMed
Google Scholar
34.
Claridge-Chang, A. ∙ Roorda, R.D. ∙ Vrontou, E. ...
Writing memories with light-addressable reinforcement circuitry
Cell. 2009; 139:405-415
Full Text
Full Text (PDF)
Scopus (359)
PubMed
Google Scholar
35.
Riemensperger, T. ∙ Kittel, R.J. ∙ Fiala, A.
Optogenetics in Drosophila Neuroscience
Methods Mol. Biol. 2016; 1408:167-175
Crossref
Scopus (20)
PubMed
Google Scholar
36.
Aso, Y. ∙ Rubin, G.M.
Dopaminergic neurons write and update memories with cell-type-specific rules
eLife. 2016; 5
e16135–e16135
Crossref
Scopus (153)
PubMed
Google Scholar
37.
Keene, A.C. ∙ Masek, P.
Optogenetic induction of aversive taste memory
Neuroscience. 2012; 222:173-180
Crossref
Scopus (39)
PubMed
Google Scholar
38.
Stern, U. ∙ Yang, C.-H.
SkinnerTrax: high-throughput behavior-dependent optogenetic stimulation of Drosophila
bioRxiv. 2017;
Crossref
Google Scholar
39.
Corfas, R.A. ∙ Dickinson, M.H.
Diverse food-sensing neurons trigger idiothetic local search in Drosophila
bioRxiv. 2018;
Crossref
Google Scholar
40.
Brockmann, A. ∙ Murata, S. ∙ Murashima, N. ...
Sugar intake elicits a small-scale search behavior in flies and honey bees that involves capabilities found in large-scale navigation
bioRxiv. 2017;
Crossref
Google Scholar
41.
Murata, S. ∙ Brockmann, A. ∙ Tanimura, T.
Pharyngeal stimulation with sugar triggers local searching behavior in Drosophila
J. Exp. Biol. 2017; 220:3231-3237
Crossref
Scopus (22)
PubMed
Google Scholar
42.
Cohen, J.D. ∙ Bolstad, M. ∙ Lee, A.K.
Experience-dependent shaping of hippocampal CA1 intracellular activity in novel and familiar environments
eLife. 2017; 6:e23040
Crossref
Scopus (70)
PubMed
Google Scholar
43.
Bülthoff, H. ∙ Götz, K.G. ∙ Herre, M.
Recurrent Inversion of Visual Orientation in the Walking Fly, Drosophila melanogaster
J. Comp. Physiol. 1982; 148:471-481
Crossref
Scopus (53)
Google Scholar
44.
Reichardt, W. ∙ Poggio, T.
Visual control of orientation behaviour in the fly. Part I. A quantitative analysis
Q. Rev. Biophys. 1976; 9:311-375
428–438
Crossref
Scopus (319)
PubMed
Google Scholar
45.
Schuster, S. ∙ Strauss, R. ∙ Götz, K.G.
Virtual-reality techniques resolve the visual cues used by fruit flies to evaluate object distances
Curr. Biol. 2002; 12:1591-1594
Full Text
Full Text (PDF)
Scopus (62)
PubMed
Google Scholar
46.
Robie, A.A. ∙ Straw, A.D. ∙ Dickinson, M.H.
Object preference by walking fruit flies, Drosophila melanogaster, is mediated by vision and graviperception
J. Exp. Biol. 2010; 213:2494-2506
Crossref
Scopus (50)
PubMed
Google Scholar
47.
Reiser, M.B. ∙ Dickinson, M.H.
A modular display system for insect behavioral neuroscience
J. Neurosci. Methods. 2008; 167:127-139
Crossref
Scopus (198)
PubMed
Google Scholar
48.
Heisenberg, M. ∙ Buchner, E.
Role of Retinula Cell-Types in Visual Behavior of Drosophila-Melanogaster
J. Comp. Physiol. 1977; 117:127-162
Crossref
Scopus (227)
Google Scholar
49.
Giraldo, Y.M. ∙ Leitch, K.J. ∙ Ros, I.G. ...
Sun Navigation Requires Compass Neurons in Drosophila
Curr. Biol. 2018; 28:2845-2852.e4
e2844
Full Text
Full Text (PDF)
Scopus (91)
PubMed
Google Scholar
50.
Green, J. ∙ Vijayan, V. ∙ Mussells Pires, P. ...
Walking Drosophila aim to maintain a neural heading estimate at an internal goal angle
bioRxiv. 2018;
Crossref
Google Scholar
51.
Dethier, V.G.
Communication by Insects: Physiology of Dancing
Science. 1957; 125:331-336
Crossref
Scopus (66)
PubMed
Google Scholar
52.
Bell, W.J.
Sources of information controlling motor patterns in arthropod local search orientation
J. Insect Physiol. 1985; 31:837-847
Crossref
Scopus (85)
Google Scholar
53.
Gallio, M. ∙ Ofstad, T.A. ∙ Macpherson, L.J. ...
The coding of temperature in the Drosophila brain
Cell. 2011; 144:614-624
Full Text
Full Text (PDF)
Scopus (185)
PubMed
Google Scholar
54.
Weiss, L.A. ∙ Dahanukar, A. ∙ Kwon, J.Y. ...
The molecular and cellular basis of bitter taste in Drosophila
Neuron. 2011; 69:258-272
Full Text
Full Text (PDF)
Scopus (296)
PubMed
Google Scholar
55.
Dahanukar, A. ∙ Lei, Y.T. ∙ Kwon, J.Y. ...
Two Gr genes underlie sugar reception in Drosophila
Neuron. 2007; 56:503-516
Full Text
Full Text (PDF)
Scopus (317)
PubMed
Google Scholar
56.
Fujii, S. ∙ Yavuz, A. ∙ Slone, J. ...
Drosophila sugar receptors in sweet taste perception, olfaction, and internal nutrient sensing
Curr. Biol. 2015; 25:621-627
Full Text
Full Text (PDF)
Scopus (144)
PubMed
Google Scholar
57.
Dethier, V.G.
The hungry fly: a physiological study of the behavior associated with feeding
Harvard University Press, Cambridge, Mass., 1976
Google Scholar
58.
Barbagallo, B. ∙ Garrity, P.A.
Temperature sensation in Drosophila
Curr. Opin. Neurobiol. 2015; 34:8-13
Crossref
Scopus (34)
PubMed
Google Scholar
59.
Ward, S.
Chemotaxis by the nematode Caenorhabditis elegans: identification of attractants and analysis of the response by use of mutants
Proc. Natl. Acad. Sci. USA. 1973; 70:817-821
Crossref
Scopus (422)
PubMed
Google Scholar
60.
Pierce-Shimomura, J.T. ∙ Morse, T.M. ∙ Lockery, S.R.
The fundamental role of pirouettes in Caenorhabditis elegans chemotaxis
J. Neurosci. 1999; 19:9557-9569
Crossref
PubMed
Google Scholar
61.
Berg, H.C. ∙ Brown, D.A.
Chemotaxis in Escherichia coli analysed by three-dimensional tracking
Nature. 1972; 239:500-504
Crossref
Scopus (1585)
PubMed
Google Scholar
62.
Corrales-Carvajal, V.M. ∙ Faisal, A.A. ∙ Ribeiro, C.
Internal states drive nutrient homeostasis by modulating exploration-exploitation trade-off
eLife. 2016; 5:e19920
Crossref
PubMed
Google Scholar
63.
Dill, M. ∙ Wolf, R. ∙ Heisenberg, M.
Visual pattern recognition in Drosophila involves retinotopic matching
Nature. 1993; 365:751-753
Crossref
Scopus (107)
PubMed
Google Scholar
64.
Aso, Y. ∙ Sitaraman, D. ∙ Ichinose, T. ...
Mushroom body output neurons encode valence and guide memory-based action selection in Drosophila
eLife. 2014; 3:e04580
Crossref
Scopus (436)
PubMed
Google Scholar
65.
Nuwal, N. ∙ Stock, P. ∙ Hiemeyer, J. ...
Avoidance of heat and attraction to optogenetically induced sugar sensation as operant behavior in adult Drosophila
J. Neurogenet. 2012; 26:298-305
Crossref
Scopus (7)
PubMed
Google Scholar
66.
Barbagallo, B. ∙ Garrity, P.A.
Temperature sensation in Drosophila
Curr Opin Neurobiol. 2015; 34:8-13
Crossref
Scopus (70)
PubMed
Google Scholar
67.
Savall, J. ∙ Ho, E.T.W. ∙ Huang, C. ...
Dexterous robotic manipulation of alert adult Drosophila for high-content experimentation
Nat. Methods. 2015; 12:657-660
Crossref
Scopus (13)
PubMed
Google Scholar
68.
Hamada, F.N. ∙ Rosenzweig, M. ∙ Kang, K. ...
An internal thermal sensor controlling temperature preference in Drosophila
Nature. 2008; 454:217-220
Crossref
Scopus (738)
PubMed
Google Scholar
69.
Kitamoto, T.
Conditional modification of behavior in Drosophila by targeted expression of a temperature-sensitive shibire allele in defined neurons
J. Neurobiol. 2001; 47:81-92
Crossref
Scopus (647)
PubMed
Google Scholar
70.
Parisky, K.M. ∙ Agosto, J. ∙ Pulver, S.R. ...
PDF cells are a GABA-responsive wake-promoting component of the Drosophila sleep circuit
Neuron. 2008; 60:672-682
Full Text
Full Text (PDF)
Scopus (312)
PubMed
Google Scholar
71.
Fry, S.N. ∙ Wehner, R.
Look and turn: landmark-based goal navigation in honey bees
J. Exp. Biol. 2005; 208:3945-3955
Crossref
Scopus (30)
PubMed
Google Scholar
72.
Cheng, K. ∙ Collett, T.S. ∙ Pickhard, A. ...
The use of visual landmarks by honeybees: Bees weight landmarks according to their distance from the goal
J Comp Physiol A. 1987; 161:469-475
Crossref
Scopus (141)
Google Scholar
73.
Zhang, S.W. ∙ Lehrer, M. ∙ Srinivasan, M.V.
Honeybee memory: navigation by associative grouping and recall of visual stimuli
Neurobiol. Learn. Mem. 1999; 72:180-201
Crossref
Scopus (75)
PubMed
Google Scholar
74.
Judd, S.P.D. ∙ Collett, T.S.
Multiple stored views and landmark guidance in ants
Nature. 1998; 392:710-714
Crossref
Scopus (175)
Google Scholar
75.
Tang, S. ∙ Wolf, R. ∙ Xu, S. ...
Visual pattern recognition in Drosophila is invariant for retinal position
Science. 2004; 305:1020-1022
Crossref
Scopus (71)
PubMed
Google Scholar
76.
Geva-Sagiv, M. ∙ Las, L. ∙ Yovel, Y. ...
Spatial cognition in bats and rats: from sensory acquisition to multiscale maps and navigation
Nat. Rev. Neurosci. 2015; 16:94-108
Crossref
Scopus (178)
PubMed
Google Scholar
77.
Azanchi, R. ∙ Kaun, K.R. ∙ Heberlein, U.
Competing dopamine neurons drive oviposition choice for ethanol in Drosophila
Proc. Natl. Acad. Sci. USA. 2013; 110:21153-21158
Crossref
Scopus (72)
PubMed
Google Scholar
78.
Tuthill, J.C. ∙ Nern, A. ∙ Holtz, S.L. ...
Contributions of the 12 neuron classes in the fly lamina to motion vision
Neuron. 2013; 79:128-140
Full Text
Full Text (PDF)
Scopus (146)
PubMed
Google Scholar
79.
Pfeiffer, B.D. ∙ Ngo, T.T.B. ∙ Hibbard, K.L. ...
Refinement of tools for targeted gene expression in Drosophila
Genetics. 2010; 186:735-755
Crossref
Scopus (724)
PubMed
Google Scholar
80.
Triphan, T. ∙ Poeck, B. ∙ Neuser, K. ...
Visual targeting of motor actions in climbing Drosophila
Curr. Biol. 2010; 20:663-668
Full Text
Full Text (PDF)
Scopus (76)
PubMed
Google Scholar
81.
Klapoetke, N.C. ∙ Murata, Y. ∙ Kim, S.S. ...
Independent optical excitation of distinct neural populations
Nat. Methods. 2014; 11:338-346
Crossref
Scopus (1415)
PubMed
Google Scholar
82.
Isono, K. ∙ Tanimura, T. ∙ Oda, Y. ...
Dependency on light and vitamin A derivatives of the biogenesis of 3-hydroxyretinal and visual pigment in the compound eyes of Drosophila melanogaster
J. Gen. Physiol. 1988; 92:587-600
Crossref
Scopus (43)
PubMed
Google Scholar
83.
Wang, X. ∙ Wang, T. ∙ Ni, J.D. ...
The Drosophila visual cycle and de novo chromophore synthesis depends on rdhB
J. Neurosci. 2012; 32:3485-3491
Crossref
Scopus (39)
PubMed
Google Scholar
84.
Aso, Y. ∙ Hattori, D. ∙ Yu, Y. ...
The neuronal architecture of the mushroom body provides a logic for associative learning
eLife. 2014; 3:e04577
Crossref
Scopus (609)
PubMed
Google Scholar
85.
Land, M.F.
Visual acuity in insects
Annu. Rev. Entomol. 1997; 42:147-177
Crossref
Scopus (469)
PubMed
Google Scholar
86.
Autrum, H.
Electrophysiological analysis of the visual systems in insects
Exp. Cell Res. 1958; 14(Suppl 5):426-439
PubMed
Google Scholar
87.
Cosens, D. ∙ Spatz, H.C.
Flicker Fusion Studies in Lamina and Receptor Region of Drosophila Eye
J. Insect Physiol. 1978; 24:587
Crossref
Scopus (14)
Google Scholar
88.
Miall, R.C.
The flicker fusion frequencies of six laboratory insects, and the response of the compound eye to mains fluorescent ‘ripple’
Physiol. Entomol. 1978; 3:99-106
Crossref
Scopus (48)
Google Scholar
89.
Branson, K. ∙ Robie, A.A. ∙ Bender, J. ...
High-throughput ethomics in large groups of Drosophila
Nat. Methods. 2009; 6:451-457
Crossref
Scopus (544)
PubMed
Google Scholar
Article metrics
Related Articles