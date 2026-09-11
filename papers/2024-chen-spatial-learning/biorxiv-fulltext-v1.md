# Chen et al. — "Spatial learning in feature-impoverished environments in Drosophila" — bioRxiv 10.1101/2024.09.28.615625v1

Captured 2026-09-10 via in-app browser get_page_text from https://www.biorxiv.org/content/10.1101/2024.09.28.615625v1.full. Figures not saved.


Abstract

The ability to return to memorized goal locations is essential for animal survival. While it is well documented that animals use visual landmarks to locate goals1,2, how they navigate spatial learning tasks in environments lacking such landmarks remains poorly understood. Here, using a high-throughput spatial learning task we developed to investigate this question in Drosophila, we found that Drosophila can simultaneously use self-generated olfactory cues and self-motion cues to learn a spatial goal under visually challenging conditions. Specifically, flies mark a rewarded goal location with self-deposited scents, to which they assign a positive value to, and use these scents and their self-motion cues to guide them back to the goal. This learning process is mediated by the mushroom body(MB) – an olfactory learning center responsible for associating odors with reinforcement3 –and by PFN neurons, which encode egocentric translational velocity4,5, a self-motion cue. Intriguingly, when the environment is enriched with prominent external olfactory landmarks, flies shift their strategy, prioritizing these landmarks over self-generated cues. Our findings demonstrate that Drosophila can dynamically adapt to environmental complexities when solving spatial learning tasks by creating and integrating internal and external cues, revealing an unexpected level of sophistication in their cognitive capacities.

Introduction

The capacity for returning to memorized goal locations in darkness or without any guidance from prominent visual landmarks is critical for animals to survive in nature, especially for nocturnal animals and animals with no or limited vision. Identifying the behavioral strategies and neural circuits that support navigation in such challenging conditions will provide important insights into the neural basis of simple cognition. In principle, animals can rely purely on self-motion cues to estimate their relative distance and angle to a goal location – i.e., to calculate a home vector – in a process known as path integration, and then use the vector to guide their return to the goal6,7. For example, desert ants have been shown to be able to gauge whether they have reached the goal by “counting” the number of steps they have taken8. In addition, mammals such as rats9, mice10, bats11, and dogs12, and insects such as bees13–16, dung beetles17–19, and fruit flies20–23 have all been implicated to use path integration for navigation. The exact neural mechanism by which path integration is implemented in the brain remains poorly understood, but self-motion-sensitive spatially selective neurons, such as heading direction cells24, likely play a critical role.

In addition to self-motion cues, olfactory cues constitute another major source of information animals could utilize when navigating without access to prominent visual cues. Odors can aid successful navigation to goals in at least two ways. First, animals can return to the goal location by simply following the odor plume – i.e., by beaconing – if the goal happens to emit some innately attractive odors, such as those from a food source25–29. Second, animals can also use odors present at fixed locations away from the goal to reset the path integrator30–32. For example, a recent study suggests that mice can use odors delivered consistently at specific locations along a linear path to the goal to estimate their relative position to the goal32. The circuit mechanism responsible for the first strategy should be relatively straightforward, while that for the second requires integration of olfactory cues and self-motion cues in the path-integration circuit.

In this study, we set out to uncover behavioral and neural strategies animals might adopt when searching for a memorized spatial goal in environments that lack both prominent external landmarks, using Drosophila melanogaster as our model. Drosophila has been shown to be able to perform visual cues-based spatial learning and path integration, and, importantly, possesses several classes of spatially selective neurons (e.g., head direction cells) in its compact brain4,5,33–36. Using a high-throughput spatial learning paradigm we developed where an optogenetically delivered reward was placed in an essentially featureless arena, we found that flies were able to learn the location of the rewarded goal relatively quickly. Interestingly, in addition to making use of self-motion cues, our results suggest that, in parallel, they also exploited scent(s) from substances they deposited themselves, assigning it with a positive valence to help them memorize and locate the goal. Moreover, they adjusted the relative reliance on the two strategies depending on whether salient external olfactory landmarks were available in the environment. Our results highlight this model organism’s “creativity” and flexibility in solving a spatial task in landmark-impoverished environments, paving the way for future studies into the underlying molecular and neural mechanisms.

Results
Flies can learn the location of a spatial goal without relying on prominent visual cues

To test whether flies can learn a spatial goal location without using prominent visual cues, we designed a spatial learning task where a fly can collect virtual rewards at a goal location in a rectangularly shaped and otherwise “featureless” arena (“flat chamber”) that lacks clear visual landmarks (Fig.1a). The task was conducted in a custom-designed high-throughput system (SkinnerSys) – comprising hardware and software (SkinnerTrax37) – for behavior-dependent optogenetic stimulation of many flies independently and in parallel. The apparati we used each housed 40 individual flies in separate arenas (Fig. 1b). We customized SkinnerTrax to place the goal location – shaped as a small (and invisible) circle – at the center of the arena so that it was not directly associated with specific spatial features (e.g., arena corners) (Fig. 1a). Rewards were delivered optogenetically. Specifically, each time the fly crossed over the border of the reward circle from the outside, a 250-ms pulse of light was delivered to optogenetically activate a group of neurons (labeled by 0273-Gal4) that have been previously shown to be a strong positive reinforcer 38,39 (Fig. 1c, Video S1). Two features of our design are noteworthy. First, to collect additional rewards, the fly must leave the reward circle and then reenter it, as staying inside will not trigger any rewards (Fig. 1c). As such, to continually forage for more rewards, flies likely need to have some memory of the reward location. Second, we paired each experimental fly with a yoked control fly that received a reward at the same time as its experimental fly, but whose positions had no influence over reward delivery (Fig. 1d).

Download figureOpen in new tab
Fig. 1
Flies can learn a spatial goal without using visual cues.

a, Schematic of a featureless flat arena (16mm x 10mm x 3mm) that houses a single fly. During training sessions, the computer would designate a reward circle (d = 2.6mm) at the center of the arena as the goal location. b, The high-throughput setup we developed for administering our spatial task. Each setup contains two cameras, one LED board, one infrared back light, and a holder that houses 40 individual arenas. c, Our reward rule during the training sessions: only when the fly enters the reward circle from the outside can trigger 1 pulse of light (250ms, 17µW/mm2, 527nm). d, Top: Temporal design of the spatial task. Flies can only receive rewards during the training sessions. Bottom: Positional heatmaps of 20 experimental flies with their 20 yoked control flies at the end of each training session. The fly ‘E1’ is paired with the fly ‘Y1’, ‘E2’ is paired with ‘Y2’, etc. e, The reward index (RI) of experimental flies and their paired yoked control flies (0273-Gal4>CsChrimson) at each sync bucket (10 mins, see Methods) during the three training sessions. Inset is the schematic of the flat chamber with the reward circle and the control circle (d = 13mm) labeled. Note that we only used males in this study so as to reduce the potential impact of mating experience (virgin vs. mated) and reproductive state (actively egg-laying vs. not) on learning. f, The RI difference between experimental and their paired yoked control flies (0273-Gal4>CsChrimson) at each syn bucket during training sessions. g, Spatial learning index (SLI) of “sighted” (0273-Gal4>CsChrimson) flies (n = 83). h, SLI of blind (norpA; 0273-Gal4>CsChrimson) flies (n = 75). Unless otherwise mentioned, all line plots show means and 95% confidence intervals (shaded), and the numbers above the lines are the sample size at each sync bucket. Error bars in all scatter plots are mean ± S.E.M. One-sample t-test (two-tailed) against 0 was used in f - h. Note that throughout the paper *: p<0.05; **: p<0.01; ***: p<0.001; ****: p<0.0001.

The length of the task was 4 hours with three 1-hour training sessions (Fig. 1d). Rewards were available only during the training sessions, but not in the pre- or post-training sessions. To assess the spatial learning performance of flies, we first plotted the mean reward index (RI) of the flies over time to quantify their preference for the rewarded circle over a larger control circle (Fig. 1e). We found that whereas the RI of yoked controls stayed relatively constant, the RI of the experimental flies increased as the training progressed (Fig. 1e), indicating a learned preference for the rewarded location. To visualize flies’ learning performance more stringently, we calculated the RI differences between each experimental fly and its paired yoked control fly (Fig. 1f), aiming to eliminate impacts on RI from non-associative biases induced by repeated reward exposures. As in the case of the RI of the experimental flies, the RI difference between experimental and yoked flies also increased as training progressed (Fig. 1f). To simplify the representation of learning performance and its comparisons across genotypes or other manipulations, we introduced the spatial learning index (SLI) – the RI difference between the experimental and yoked flies in the last 10-min sync bucket of training session 3 (see Methods for our sync bucket definition). We found that both sighted and blind (norpA mutant) flies exhibited a positive SLI in our featureless arenas (Fig. 1g, h). Interestingly, learning performance of individual flies did not clearly correlate with their reward preference (Light PI, see Methods) and locomotion speed (Extended Data Fig. 1). These results suggest flies can learn the goal location in our arenas without relying on any salient visual landmarks.

Download figureOpen in new tab
Extended Data Fig. 1
SLI of 0273-Gal4>CsChrimson flies showed weak negative correlation with average locomotion speed and no correlation with Light PI.

a, Average locomotion speed during the spatial learning task for experimental versus yoked control flies expressing 0273-Gal4>CsChrimson (n = 83). b, 0273-Gal4>CsChrimson (n = 83) flies showed a very weak negative correlation between average locomotion speed and SLI. c, Top: Temporal structure of the open-loop light (reward) preference assay (see Methods). Bottom: Schematic representation of the flat chamber during the light assay, with the upper half illuminated during light-on periods. d, The positional preference index (Light PI) for illuminated side in 0273-Gal4>CsChrimson (n = 36) flies. e, Light PI of 0273-GAL4>CsChrimson (n = 37) flies in norpA mutant background. f, 0273-Gal4>CsChrimson (n = 70) flies showed no correlation between Light PI and SLI.

Self-motion cues play a role in supporting spatial learning in the absence of prominent visual cues

To begin to identify the potential non-visual cues flies might have used for returning to the unmarked goal location to collect more rewards, we tested the involvement of self-motion cues. Previous studies have suggested that flies can perform path integration21–23, a strategy where animals rely principally on self-motion cues to calculate the angle and distance (i.e., a vector) they have traveled from a reference location, and then use the vector to guide them back to the location. The first indication that flies might have used self-motion cues for locating the goal in our task came from an examination of animals’ trajectories in between rewards (Fig. 2a). Specifically, we calculated the proportion of rewards individual animals collected without touching the arena walls. Matching our SLI calculation, we then calculated the difference in these proportions between experimental flies and their paired yoked controls for the last sync bucket of the training session 3, naming this measure the “no wall contact index.” We found that compared to yoked controls, experimental flies were able to collect a significantly higher proportion of rewards without touching – and therefore without using – the arena walls, as the mean value was significantly higher than 0 (Fig. 2b).

Download figureOpen in new tab
Fig. 2
Flies rely on neurons that signal egocentric translational velocity to learn the task well.

a, Left: An in-between reward trajectory with many wall contacts. Right: An in-between reward trajectory without any wall contact. b, The no wall contact index of regular flies (0273-Gal4>CsChrimson, n = 80). c, Expression pattern of the LexA driver line that labels PFNd neurons (GMR16D01-LexA). Inset is schematic of PFNd neurons. d, Left: SLI of Ctrl>Kir (n = 74) versus PFNd>Kir (n = 68) flies. Right: The no wall contact index of Ctrl>Kir (n = 74) versus PFNd>Kir (n= 66) flies. Green-filled arena schematic indicates that PFNd neurons were silenced everywhere. Note that throughout this work, we used 0273-GAL4>CsChrimson as controls and introduced various transgenes into this background to manipulate different neurons. Here, Ctrl>Kir flies carried the additional transgenes of empty-lexA and lexAop-Kir whereas PFNd>Kir flies carried the additional transgenes of 16D01-lexA, and lexAop-Kir. e, Left: SLI of Ctrl>GtACR1 (n = 41) versus PFNd>GtACR1 (n = 75) flies. Right: The no wall contact index of Ctrl>GtACR1 (n = 41) versus PFNd>GtACR1 (n = 74) flies. The green disc in the arena schematic indicates that PFNd neurons were silenced only when flies received rewards. Note that throughout the paper, we used arenas with either color-filled backgrounds or center-only circle marks to depict conditions under which neurons of interest were either chronically or transiently manipulated at the reward circle, respectively. f, Confocal image and schematic showing the expression pattern of the split-Gal4 driver that labels the PFNd neurons (SS00078). g, Left: SLI of Ctrl>CsChrimson (n = 119) versus PFNd>CsChrimson (n = 118) flies. Right: The no wall contact index of Ctrl>CsChrimson (n = 117) versus PFNd>CsChrimson (n = 114) flies. h, Confocal image and schematic showing the expression pattern of the split-Gal4 driver that labels PFNv neurons (SS52628). i, Left: SLI of Ctrl>CsChrimson (n = 98) versus PFNv>CsChrimson (n = 119) flies. Right: The no wall contact index of Ctrl>CsChrimson (n = 98) versus PFNv>CsChrimson (n = 117) flies. j, Confocal image and schematic showing the expression pattern of the LexA driver line that labels EPG neurons (GMR60D05-LexA). k, SLI of Ctrl>Kir (n = 74) versus EPG>Kir (n = 72) flies. l, SLI of Ctrl>GtACR1 (n = 81) versus EPG>GtACR1 (n = 62) flies. m, Confocal image and schematic showing the expression pattern of the split-Gal4 driver line that labels EPG neurons (SS00090). n, Left: SLI of Ctrl>CsChrimson (n = 119, same as the Ctrl for PFNd>CsChrimson) versus EPG>CsChrimson (n = 106) flies. Unless otherwise mentioned, unpaired two-tailed t-test with Welch’s correction was used in all paired comparisons in this paper.

To further confirm flies’ use of self-motion cues for goal locating, we tested the necessity of proper activities of PFN neurons – a class of spatially selective neurons that comprises two spatially selective subgroups (PFNd and PFNv) whose populational activities have been shown to track a fly’s egocentric translational velocity4,5 and to be required for proper local search5. We first silenced the activities of PFNd neurons chronically (by expressing in them the Kir2.1 channel) and found that this manipulation significantly decreased learning performance, as well as the proportion of rewards flies collected without wall contacts (Fig. 2c, d). Moreover, we also optogenetically manipulated PFN activity transiently at the goal location via the 250-ms reward delivery light pulses, as green light is capable of activating both CsChrimson and the light-gated chloride channel GtACR140. Transiently silencing PFNd neurons, transiently activating them – which should also disrupt their spatial selectivity – as well as transiently activating PFNv neurons all reduced learning performance (Fig. 2e-i). These manipulations of PFN neurons did not cause a consistent change in the reward preference or the locomotion speed (Extended Data Fig. 2). It is also worth mentioning that the SLI we use to represent learning should be less sensitive to unintended consequences of various manipulation, as it indicates the performance difference between an experimental fly and its paired yoked control, both of which underwent the same manipulation.

Download figureOpen in new tab
Extended Data Fig. 2
Flies with defective PFNd neurons showed no consistent changes in reward preference (Light PI) or locomotion speed during the spatial learning task.

a, Left: Average locomotion speed of Ctrl>Kir (n = 74) versus PFNd>Kir (n = 68) flies. Right: Light PI of Ctrl>Kir (n = 39) versus PFNd>Kir (n = 31) flies. b, Left: Average locomotion speed of Ctrl>GtACR1 (n = 41) versus PFNd>GtACR1 (n = 75) flies. Right: Light PI of Ctrl>GtACR1 (n = 39) versus PFNd>GtACR1 (n = 64) flies. c, Left: Average locomotion speed of Ctrl>CsChrimson (n = 119) versus PFNd>CsChrimson (n = 118) flies. Right: Light PI of Ctrl>CsChrimson (n = 60) versus PFNd>CsChrimson (n = 60) flies. d, Left: Average locomotion speed of Ctrl>CsChrimson (n = 98) versus PFNv>CsChrimson (n = 119) flies. Right: Light PI of Ctrl>CsChrimson (n = 40) versus PFNv>CsChrimson (n = 39) flies.

We also tested whether EPG neurons may play a role. EPG neurons signal heading direction and represent a major input into PFN neurons4,5,35. Surprisingly, chronically silencing EPG neurons had no impact on performance (Fig. 2j, k). Similarly, transiently silencing or activating EPG neurons at the goal location did not cause any significant impacts either (Fig. 2l-n). (As in the case of PFNs, we assumed activating the entire EPG population may disrupt its spatial selectivity.) Thus, the proper heading direction signal represented by the population activities of EPG neurons appeared unessential for flies to locate the goal in our task, which is consistent with the finding that EPG neurons are dispensable for local search behavior41. Additionally, proper activities of another type of spatially selective neurons that signal allocentric translational velocity, PFR neurons4, also appeared to be dispensable (Extended Data Fig. 3). Together, our results suggest that flies use cues that signal egocentric movements but not cues that signal allocentric orientation or movements to learn our spatial task.

Download figureOpen in new tab
Extended Data Fig. 3
Proper activity of allocentric translational velocity-signaling PFR neurons was dispensable for our spatial task.

a, Confocal image and schematic showing the expression pattern of the LexA driver that labels PFR neurons (GMR37G12-LexA). b, SLI of Ctrl>Kir (n = 74, same as the Ctrl for EPG>Kir) versus PFR>Kir (n = 57) flies. c, SLI of Ctrl>GtACR1 (n = 79) versus PFR>GtACR1 flies (n = 112). d, Confocal image and schematic showing the expression pattern of the split-GAL4 driver that labels the PFR neurons (SS54549). e, SLI of Ctrl>CsChrimson (n = 140) versus PFR>CsChrimson (n = 139) flies.

Olfaction plays a role in supporting spatial learning in the absence of external odor landmarks and prominent visual cues

Next, we tested whether flies could use strategies other than ones that depend on self-motion cues, given that flies with inactivated PFN neurons were still capable of learning, albeit at a lower level (Fig. 2c-i). The flies’ antennae are a sensory organ that can detect external non-visual cues including mechanosensory and olfactory ones. To test if antennae-sensed cues were used for learning of our task, we first covered both antennae with UV-cured glue. These flies showed a significant decrease in their learning performance, as did flies with the 3rd segment of both their antennae surgically removed (Fig. 3a), suggesting the importance of one or more of the antennae-detected cues in enabling learning. To differentiate the relative contributions of mechanosensory vs. olfactory antennal inputs, we next removed bilaterally just the arista, the long hair-like structure at the tip of the 3rd antennal segment critical for detecting mechanosensory but not olfactory cues, and found that these arista-less flies learned normally (Fig. 3a). These results suggest that, surprisingly, olfactory cues appear to be the relevant antennae-detected cues that promote learning in a task where no external olfactory landmarks were supplied.

Download figureOpen in new tab
Fig. 3
Flies rely on self-deposited chemicals as olfactory landmarks for learning the goal.

a, SLI of Ctrl (n = 83, same as flies in Fig1. g), antenna glued (n = 66), 3rd segment of antenna removed (n = 105), and arista removed (n = 56) flies. b, SLI of Orco2/+ (n = 98) versus Orco1/Orco2 (n = 92) flies. c, SLI of control groups Ir25a & Orco-QF only (n = 59), QUAS-Kir only (n = 88) vs. Ir25a & Orco-QF>Kir flies (n = 90). d, Steps of collecting deposit samples from the center of the flat chambers. Gray circle area in the center of the flat chamber indicates the transparent film that was used for collecting the odors (see Methods). e, GC-MS identified several cuticular hydrocarbons that were unique for both experimental and yoked control flies not presented in blank controls (odor samples from empty flat arenas). Triangle mark indicates peak present in the blank control. f, SLI of Ctrl (n = 157), hind tarsi removed (n = 146), genitalia glued (n = 103), and hind tarsi removed with genitalia glued simultaneously (n = 104) flies. g, Schematic of an analysis that assesses how likely a fly will make a sharp turn (> 90°) within 0.75s arriving at different distances (2 to 6 mm) from the midline of the arena when it moves in a direction away from the goal (see Methods). h, Comparing the probabilities that such sharp turns were made between the experimental and yoked control flies at different distances during pre-training (Pre, n = 75) and the last sync bucket of training 3 (T3-LSB, n = 76). i, Images showing the expression pattern of the LexA driver lines we used to label MBKCs. Top: GMR19B03-LexA; Bottom: GMR26E07-LexA. j, Left: SLI of Ctrl>Kir (n = 113) versus MBKC-1>Kir (n = 102) flies. Right: SLI of Ctrl>Kir (n = 74, same as the Ctrl for PFNd>Kir) versus MBKC-2>Kir (n = 66) flies. k, Left: SLI of Ctrl>GtACR1 (n = 82) versus MBKC-1>GtACR1 (n = 144) flies. Right: SLI of Ctrl>GtACR1 (n = 82, same as the Ctrl for MBKC-1>GtACR1) versus MBKC-2>GtACR1 (n = 153) flies. Welch ANOVA tests with Games-Howell post-hoc test was used for multiple comparisons in panel a, c, f.

To verify that olfactory cues were indeed used for learning, we then tested the performance of Orco mutant flies and found that they had decreased learning performance as compared to that of controls (Fig. 3b). Orco mutants are known to be defective in olfaction as the Orco channel is an obligatory co-receptor for many odorant receptors42. The impact of Orco mutation on learning seemed less than that of removing the 3rd segment of the antennae, possibly because Orco is expressed in only ∼78% of total olfactory neurons43. In a separate attempt to block the olfactory inputs, we expressed Kir2.1 in the Orco- and the IR25a-expressing neurons simultaneously, which should disrupt the function of more olfactory neurons43, and also found a clear decrease in performance (Fig. 3c). Again, the olfaction-defective flies we tested did not show a consistent change in reward preference or locomotion speed (Extended Data Fig. 4).

Download figureOpen in new tab
Extended Data Fig. 4
Flies with disrupted olfactory learning circuit did not show consistent changes in locomotion speed or reward preference.

a, Left: Average locomotion speed of Ctrl (n = 83), antenna glued (n = 66), 3rd segment of antenna removed (n = 105), and arista removed (n = 56) flies. Right: Light PI of Ctrl (n = 36), antenna glued (n = 39), 3rd segment of antenna removed (n = 36), and arista removed (n = 38) flies. b, Left: Average locomotion speed of Orco2/+ (n = 98) versus Orco1/Orco2 (n = 92) flies. Right: Light PI of Orco2/+ (n = 38) versus Orco1/Orco2 (n = 37) flies. c, Left: Average locomotion speed of control groups Ir25a & Orco-QF only (n = 59) and QUAS-Kir only (n =88) vs. Ir25a & Orco-QF>Kir (n = 90) flies. Right: Light PI of control groups Ir25a & Orco-QF only (n = 38) and QUAS-Kir only (n =53) vs. Ir25a & Orco-QF>Kir (n = 56) flies. d, Left: Average locomotion speed of Ctrl (n = 157), hind tarsi removed (n = 146), genitalia glued (n = 103), and flies with both manipulations (n = 104). Right: Light PI of Ctrl (n = 68), hind tarsi removed (n = 75), genitalia glued (n = 76), and flies with both manipulations (n = 57). e, Left: Average locomotion speed of Ctrl>Kir (n = 113) versus MBKC-1>Kir (n = 102) flies. Right: Light PI of Ctrl>Kir (n = 38) versus MBKC-1>Kir (n = 37) flies. f, Left: Average locomotion speed of Ctrl>Kir (n = 74, same as the Ctrl for PFNd>Kir) versus MBKC-2>Kir (n = 66) flies. Right: Light PI of Ctrl>Kir (n = 39, same as the Ctrl for PFNd>Kir) versus MBKC-2>Kir (n = 34) flies. g, Left: Average locomotion speed of Ctrl>GtACR1 (n = 82) versus MBKC-1>GtACR1 (n = 144) flies. Right: Light PI of Ctrl>GtACR1 (n = 39) versus MBKC-1>GtACR1 (n = 36) flies. h, Left: Average locomotion speed of Ctrl>GtACR1 (n = 82, same as the Ctrl for MBKC-1>GtACR1) versus MBKC-2>GtACR1 (n = 153) flies. Right: Light PI of Ctrl>GtACR1 (n = 39, same as the Ctrl for MBKC-1>GtACR1) versus MBKC-2>GtACR1 (n = 40) flies. Welch ANOVA tests with Games-Howell post-hoc test was used for multiple comparisons in panel a, c, and d.

But what might be the source of the odor(s)? Given we did not supply any external odors and cleaned the arenas thoroughly prior to each experiment, we suspected the odor flies used for learning might be from deposits they made. To test this idea, we collected samples from the center of many arenas after the flies had completed the task and sent them for gas chromatography-mass spectrometry (GC-MS) analysis (Fig. 3d). Indeed, several tricosene isomers, cyclotetracosane, and pentacosene isomers were detected in samples collected from arenas where flies had undergone training, but not from the clean arenas (Fig. 3e, Table 1). Tricosene and pentacosene are known pheromones for flies44,45. These results show that while we did not provide scents in the arenas, they were not necessarily odorless. To lend further support to the idea that self-scenting might be important for supporting learning, we attempted to reduce the transferring of scented substances from flies’ bodies onto the arena floor by removing flies’ hind tarsi and covering their genitalia with UV-cured glue. We found that while removal of hind tarsi did not cause a significant decrease in performance, gluing the genitalia did, and the decrease was more pronounced when we simultaneously compromised both (Fig. 3f). Together these results suggest that, in addition to using self-motion cues, flies can also use “scent-marking” as a strategy for returning to the goal location in an environment that lacks prominent visual and external odor landmarks.

View inlineView popup
Table 1.
List of Putative Observed Compounds identified by GC-MS
Functional MB is important for learning the spatial goal in the absence of external odor landmarks and prominent visual cues

Having found that flies deposited potentially scented substances during learning and that learning depended on a functional olfactory system, we next asked how the scents might be used for locating the goal. One possibility is that these scents were enriched near the goal such that flies may find the goal by following scent gradients. Consistent with this idea, we found that the tendency of flies to make a sharp turn that brings them closer to the goal increased as they were walking further away from the goal (Fig. 3g, h). Importantly, the tendency reduced when we compromised flies’ olfaction or made them less capable of scent marking the arena (Extended Data Fig. 5). Further, we found that naïve flies that had never experienced any trainings did not show any preference for the goal location when placed in arenas just “scented” by trained flies (Extended Data Fig. 6), suggesting that the deposited scented substances around the goal were not innately attractive and possibly were afforded positive valence by the presence of reward.

Download figureOpen in new tab
Extended Data Fig. 5
Flies with disrupted olfactory inputs or scent deposition showed reduced sharp turns toward the goal location.

a, Left: Schematic of two boundary crossing events. Middle: Schematic of a sharp turn event. Right: Example trajectories of sharp turn and non-sharp turn events as the fly crossed boundaries at a given distance from the goal. b-j, Comparison of sharp turn probabilities toward the goal at different distances from the midline for different groups of flies. b, Ctrl (n = 76) versus antenna glued (n = 64) flies. The same controls were used for the next two panels. c, Ctrl (n = 76) versus 3rd segment of antenna removed (n = 102) flies. d, Ctrl (n = 76) versus arista removed (n = 55) flies. e, Orco2/+ (n = 98) versus Orco1/Orco2 (n = 89) flies. f, Left: Ir25a- & Orco-QF only (n = 58) versus Ir25a-QF & Orco-QF>Kir (n = 90) flies. Right: QUAS-Kir only (n = 88) versus Ir25a- & Orco-QF>Kir (n = 90) flies. g, Ctrl (n = 129) versus hind tarsi removed (n = 72) flies. The same controls were used for the next two panels. h, Ctrl (n = 129) versus genitalia glued (n = 93) flies. i, Ctrl (n = 129) versus both hind tarsi removed and genitalia glued (n = 59) flies.

Download figureOpen in new tab
Extended Data Fig. 6
Deposited scents were not attractive for naïve flies.

a, Proportion of time naïve flies spent in the 2.5mm radius circle concentric to the reward circle in clean flat chambers (n = 76) versus the same flies trained after 3 training sessions. b, Proportion of time naïve flies spent in the 2.5mm radius circle concentric to the reward circle in clean flat chambers (n = 76) versus “used” chambers previously occupied by flies that had just completed 3 training sessions (n = 104). The duration of this preference assay was 3 minutes.

To test the idea that flies could learn to use initially neutral scents from self-deposits for locating the rewarded goal, we next manipulated the mushroom body (MB), the olfactory conditioning center where odors can acquire valence by association3,46. First, we chemically ablated the Kenyon cells (KCs), the principal neurons of the MB, by hydroxyurea47 and found that flies with a significant portion of their MB ablated showed a substantial decrease in learning (Extended Data Fig. 7). To rule out the possibility that such decrease might be caused by unintended ablation of brain areas outside of the MB, we also took a genetic approach to selectively inhibit the KCs. Chronic inhibition of KCs using two different genetic drivers caused a clear decrease in learning performance in both cases (Fig. 3i-j). Interestingly, transiently silencing KCs specifically at the goal location (again via the 250-ms reward delivery light pulses) also caused a significant decrease (Fig. 3k), in keeping with the notion that flies might be using MB to associate scents from self-deposits with reward at the goal location. In addition, similar to the olfaction-defective flies, KCs-silenced flies also showed a decrease in their tendency to make a sharp turn towards the goal as they moved in a direction away from the goal (Extended Data Fig. 8). Lastly, as with the other manipulated flies we have described thus far, flies with non-functional olfactory learning circuit did not show a consistent change in their preference for reward or locomotion speed (Extended Data Fig. 4e-h). Together, these results suggest that when the goal is in an environment that lacks prominent external features, flies might mark the rewarded location with scented deposits, and then use the olfactory learning circuit to stamp the scents with a positive valence to guide them back to the goal.

Download figureOpen in new tab
Extended Data Fig. 7
Flies with HU-ablated mushroom body (MB) showed strongly reduced learning performance.

a, Top: Fas-2 staining in the MB lobes of an untreated fly. Bottom: Fas-2 staining in the MB lobes of a hydroxyurea (HU) treated fly. b, SLI of Ctrl (n = 62) versus MB-ablated (n = 39) flies. c, Light PI of Ctrl (n = 20) versus MB-ablated (n = 20) flies. d, Average locomotion speed of Ctrl (n = 62) versus MB-ablated (n = 39) flies.

Download figureOpen in new tab
Extended Data Fig. 8
Flies with silenced MBKCs showed reduced sharp turns toward the goal location.

a, Left: Turn probability of Ctrl>Kir (n = 110) versus MBKC-1>Kir (n = 101) flies. Right: Turn probability of Ctrl>Kir (n = 73) flies versus MBKC-2>Kir (n = 66) flies. b, Left: Turn probability of Ctrl>GtACR1 (n = 81) flies versus MBKC-1>GtACR1 (n = 142) flies. Right: Turn probability of Ctrl>GtACR1 (n = 81, same as the Ctrl for MBKC-1>GtACR1) flies versus MBKC-2>GtACR1 (n = 153) flies.

Salient external olfactory landmarks can further improve spatial learning performance

Given that flies are likely able to scent mark the goal in an otherwise odorless environment, we next wondered whether flies could also use salient external odor landmarks away from the goal to further improve their chances of locating the goal. To answer this question, we enriched the arena by placing strips of 1% agarose into troughs located at the two edges of the arena, away from the goal location (Fig. 4a, Video S2) (“agarose chamber”). We found that flies significantly improved their learning performance in the agarose chamber as compared to learning in the flat chamber (Fig. 4b-f). Importantly, the enhanced performance was not caused by flies’ restricting their search area due to strong innate avoidance of the agarose strips (Extended Data Fig. 9). This result suggests flies are able to use salient external landmarks that are consistently “anti-correlated” with the goal to help with locating the goal.

Download figureOpen in new tab
Extended Data Fig. 9
Learning induced avoidance of agarose-occupied areas at the end of the task.

a, Schematic of agarose-equivalent areas in the flat chamber (left) and agarose areas in the agarose chamber (right). b, Left two columns: Percentage of time flies spent in agarose-equivalent areas in the flat chamber (n = 113) versus agarose areas in the agarose chamber (n = 115) during the pre-training session. The difference was statistically significant but mild. Right two columns: Percentage of time flies spent in agarose-equivalent areas in the flat chamber (n = 83) versus agarose areas in the agarose chamber (n = 105) during the last sync bucket (10 mins) of the training 3. Two-way ANOVA was used to calculate the interaction between chamber types and learning task sessions on the percentage of time flies spent in agarose-equivalent areas. Šídák’s multiple comparisons test was used to compare values between the flat and agarose chambers at the given session of the task.

Download figureOpen in new tab
Fig. 4
Flies can use salient external olfactory landmarks to significantly improve their spatial learning performance.

a, Schematic of our default featureless flat chamber and our agarose chamber enriched with two strips of 1% agarose away from the goal location. b, The positional heatmaps of experimental and yoked control flies at the end of the three training sessions administered in the agarose chamber. c, RI difference between experimental and yoked control flies during training in the flat chamber versus the agarose chamber. d, SLI of the flies from panel c (n = 83, 105). e, RI difference between blind (norpA) experimental and yoked control flies during training in the flat chamber versus agarose chamber. f, SLI of blind flies from panel e (n = 75, 77). g, SLI of Ctrl (n = 105), antenna glued (n = 51), 3rd antenna segments removed (n = 67), and arista removed (n = 58) flies in the agarose chamber. h, SLI of Orco2/+ (n = 79) versus Orco1/Orco2 (n = 76) flies in the agarose chamber. i, SLI of Ir25a-QF & Orco-QF only (n = 67), QUAS-Kir only (n = 74), and Ir25a & Orco-QF>Kir (n = 74) flies in the agarose chamber. j, SLI of Ctrl (n = 88), hind tarsi removed (n = 69), genitalia glued (n = 78), and hind tarsi removed with genitalia glued simultaneously (n = 90) flies. k, Left: SLI of Ctrl>Kir (n = 75) versus MBKC-1>Kir (n = 47). Right: SLI of Ctrl>Kir (n = 54) versus MBKC-2>Kir (n = 50) flies in the agarose chamber. l, Left: SLI of Ctrl>GtACR1 (n = 98) versus MBKC-1>GtACR1 (n = 116) flies. Right: SLI of Ctrl>GtACR1 (n = 98, same as the Ctrl for MBKC-1>GtACR1) versus MBKC-2>GtACR1 (n = 144) flies in the agarose chamber. Welch ANOVA tests with Games-Howell post-hoc test was used for multiple comparisons in panel g, i, j.

Since agarose can provide both mechanosensory and olfactory cues, we then determined which one of them was responsible for enhancing performance. One observation is consistent with flies using agarose as an olfactory landmark: we found that as the training progressed, the first large turn the flies took towards the goal as they moved away from the goal after receiving a reward, increasingly occurred before physically contacting the agarose (Extended Data Fig. 10c-d), suggesting flies might be sensing the agarose from a distance.

Download figureOpen in new tab
Extended Data Fig. 10
Flies use agarose areas as olfactory landmarks to learn the spatial task.

a, Left two columns: SLI of Ctrl (n = 83) versus 3rd segment of antenna removed (n = 105) flies in the flat chamber. Right two columns: SLI of Ctrl (n = 105) versus 3rd segment of antenna removed (n = 67) flies in the agarose chamber. Two-way ANOVA was used to calculate the interaction between 3rd segment removal and chamber type on SLI. Šídák’s multiple comparisons test was used to compare SLI between Ctrl and antenna removed flies for each given chamber type. b, Left three columns: SLI of control groups Ir25a & Orco-QF only (n = 59) and QUAS-Kir only (n = 88) versus Ir25a & Orco-QF>Kir flies (n = 90) in the flat chamber. Right three columns: SLI of control groups Ir25a & Orco-QF only (n = 67) and QUAS-Kir only (n = 74) versus Ir25a & Orco-QF>Kir flies (n = 74) in the agarose chamber. Two-way ANOVA was used to calculate the interaction between silencing Ir25a & Orco-expressing OSNs and chamber type on SLI. Šídák’s multiple comparisons test was used to compare SLI between control groups and Ir25a & Orco-QF>Kir flies for each chamber type. c, Schematic of the analysis determining the distribution of distances where flies initiated their first large turn after departing from the reward circle (see Methods). d, Distribution of distances where flies initiated their first large turn after departing from the reward circle in training session 1 versus session 3 (n = 113) in the agarose chamber. The dotted blue line shows the shortest distance from the reward circle to positions where the fly could physically contact the agarose area. Paired two-tailed t-test was used to compare mean distances from the reward circle between the two groups. e-g, Distribution of distances where flies initiated their first large turn departing from the reward circle goal for different groups of flies in the agarose chamber. e, Ctrl (n = 114) versus 3rd segment of antenna removed (n = 82) flies. f, Orco2/+ (n = 80) versus Orco1/Orco2 (n = 77) flies. g, Left: Ir25a-QF & Orco-QF only (n = 73) versus Ir25a & Orco-QF>Kir (n = 83) flies. Right: QUAS-Kir only (n = 79) versus Ir25a & Orco-QF>Kir (n = 83) flies. Stars above each bin show the result of unpaired two-tailed t-tests with Welch’s correction for frequency distribution in each bin. Welch’s corrected unpaired two-tailed t-tests were also used to compare mean distances from the reward circle during the training session for each fly between groups.

To test the idea more directly, we disrupted flies’ ability to sense odors by manipulating their antennae, removing their Orco channel, and silencing their olfactory neurons. We found that agarose-induced learning improvement was significantly reduced in all conditions, albeit to different degrees (Fig. 4g-I, Extended Data Fig. 10a, b). Inactivating MB severely compromised the agarose-induced performance improvement (Fig. 4k, l), too, suggesting MB contributes to learning the goal location by associating agarose odor(s) with value. Further, flies with defective odor-learning systems tended to initiate the first large turn further away from the goal location (when departing from the goal after receipt of a reward) as compared to controls (Extended Data Fig. 10e-g), lending support to the notion that flies might have learned to treat the agarose-emitted odors as aversive because they were consistently detected in the absence of reward, thereby limiting the area they needed to search for the goal. Tagging agarose-emitted odors as aversive is in keeping with an earlier finding that odors that are delivered to flies consistently after reward can acquire an aversive quality48. Lastly, we found that simultaneously removing flies’ hind tarsi and gluing their genitalia no longer significantly impacted learning (Fig. 4j), which is quite different from the large decrease in learning performance observed in the flat chamber, indicating that presence of salient external olfactory landmarks can “rescue” flies’ learning performance when they were less capable of depositing scents near the goal.

Flies can flexibly adjust their reliance on self-motion cues for learning depending on the availability of external olfactory landmarks in the environment

We have so far shown that flies were able to use both self-motion cues and odor cues from self-deposits for locating the goal in a relatively featureless arena, and to improve their performance when the arena became enriched with external olfactory landmarks. Next, we were curious if flies might adjust their strategies in these two types of arenas where the available spatial cues differ. To begin, we ascertained the parallel nature of the self-motion cues- and olfactory cues-based strategies for locating the goal in the flat chamber by asking whether flies with disabled PFN neurons showed further decreased performance upon their antennae being blocked, and vice versa. Indeed, we found that inhibition of PFN caused a further learning decrease in antennae-glued flies (Fig. 5a). Similarly, gluing the antennae caused a further learning decrease in flies with inhibited PFN neurons (Fig. 5b). When removing the antennae instead of gluing them, similar results were also found in antennae-removed and PFNd-silenced flies (Extended Data Fig. 11a, b). These results support the parallel nature and flies’ concurrent adoption of self-motion cue-based and olfactory landmark-based strategies for locating the spatial goal in the “featureless” flat chamber.

Download figureOpen in new tab
Extended Data Fig. 11
Olfactory cues and self-motion cues independently contribute to spatial learning, with flexible adjustment in cue usage.

a, SLI of PFNd>Kir (n = 68) versus PFNd>Kir with 3rd segment of antenna removed (n = 105) flies in the flat chamber. b, Ctrl>Kir with 3rd segment of antenna removed (n = 161) versus PFNd>Kir with 3rd segment of antenna removed (n = 105) flies in the flat chamber. c, Left two columns: SLI of Ctrl>Kir (n = 110) versus PFNd>Kir (n = 99) flies in the agarose chamber. Right two columns: SLI of Ctrl>Kir with 3rd segment of antenna removed (n = 51) versus PFNd>Kir with 3rd segment of antenna removed (n = 68) flies in the agarose chamber. Two-way ANOVA was used to calculate the interaction between silencing PFNd neurons and antenna removal on SLI. Šídák’s multiple comparisons test was used to compare the SLI between Ctrl>Kir and PFNd>Kir flies with normal and 3rd segment of antenna removed flies.

Download figureOpen in new tab
Fig. 5
Flies can flexibly adjust their strategies for learning the spatial goal depending on the availability of landmarks in the environment.

a, SLI of PFNd>Kir (n = 68) versus PFNd>Kir antenna glued (n = 109) flies in the flat chamber. b, SLI of Ctrl>Kir antenna glued (n = 106) versus PFNd>Kir antenna glued (n = 109) flies in the flat chamber. c, Left two columns: SLI of Ctrl>Kir (n = 74) versus PFNd>Kir (n = 68) flies in the flat chamber. Right two columns: SLI of Ctrl>Kir (n = 110) versus PFNd>Kir (n = 99) flies in the agarose chamber. Two-way ANOVA was used to calculate the interaction between the effect of silencing PFNd neurons and the chamber type. Šídák’s multiple comparisons test was used. d, Left two columns: SLI of Ctrl>GtACR1 (n = 41) versus PFNd>GtACR1 (n = 75) flies in the flat chamber. Right two columns: SLI of Ctrl>GtACR1 (n = 56) versus PFNd>GtACR1 (n = 68) flies in the agarose chamber. Two-way ANOVA was used to calculate the interaction between silencing PFNd neurons and chamber type on SLI. Šídák’s multiple comparisons test was used. e, Left two columns: SLI of Ctrl>Kir (n = 110) versus PFNd>Kir (n = 99) flies in the agarose chamber. Right two columns: Ctrl>Kir antenna glued (n = 65), and PFNd>Kir antenna glued (n = 73) flies in the agarose chamber. Two-way ANOVA was used to calculate the interaction between silencing PFNd neurons and antenna gluing on SLI. Šídák’s multiple comparisons test was used. f, Our model of how the flies learn a goal location in a featureless environment (left) and in an environment that is enriched with olfactory landmarks (right). The black arrow indicates the integrated path (IP) relative to the goal based on self-motion cues. The green area near the goal indicates the potential scent deposited area, which was assigned a positive value by MB. The red areas indicate the agarose strips, which were assigned a negative value by MB.

Do flies alter their strategies when tasked to learn in environments that contain more useful cues? We found that flies’ relative reliance on the olfactory vs. self-motion cues changed in our agarose chamber where the arena was enriched with agarose strips away from the goal. Whereas the olfactory learning circuit remained critical as silencing its components still caused a significant reduction in learning (Fig. 4g-l), the contribution of PFN neurons diminished in the agarose chamber, as silencing them caused less of an impact in the agarose chamber compared to the flat chamber (Fig. 5c, d). However, PFN neurons can “gain” back their critical role in the agarose chamber when we blocked flies’ olfactory input, as inhibiting them caused a more substantial impact in antennae-compromised compared to non-compromised flies (Fig. 5e, Extended Data Fig. 11c). These results suggest that the contribution of the self-motion cues-based learning strategy is context-dependent: when the environment is featureless, such strategy plays a more important role and works in parallel with a scent-marking-based strategy mediated by MB; but when the environment is enriched with salient external olfactory landmarks, self-motion cues become more disposable. Thus, flies are able to adopt different strategies for locating goals in visually challenging conditions, depending on the availability of quality non-visual cues.

Discussion

In this study, we examined the behavioral and neural strategies that flies use to return to a goal location without relying on prominent visual landmarks. Using a high-throughput setup we developed where flies can forage for an optogenetically delivered virtual reward at an unmarked location, our results suggest that when the foraging arena is essentially featureless, flies can learn to use scents from self-deposits along with self-motion information to locate the goal. When the arena is enriched with external salient olfactory landmarks situated away from the goal, however, flies switch strategies and principally learn to use odor landmarks that signal the presence and absence of reward to restrict their search area (Fig. 5f). These results highlight the flexibility and ability of flies to solve a spatial task in a visually challenging environment: when possible, they can transform the spatial task into primarily an odor association task.

Some key pieces of evidence supporting our claim came from our manipulations of the odor association center, the mushroom body (MB). Ablating the MB, as well as inhibiting it, either chronically or transiently, disrupted flies’ spatial learning performance. These results, combined with the finding that olfactory neurons also played a critical role, suggest that the MB aids learning by assigning value to odor landmarks. Specifically, we propose that in our featureless flat arena, the MB works by assigning a positive value (appetitiveness) to self-generated scents near or at the goal. Additionally, in our agarose arena, the MB assigns a negative value (aversiveness) to odor from agarose located away from the goal, allowing flies to restrict their search areas to regions with low or no such odor (Fig. 5f). Such negative value assignment to “reward anti-correlated cues” aligns with earlier findings that flies can learn to treat odors that are consistently experienced following rewards as aversive48. Could the MB work in some capacity other than its conventional association role in supporting learning? It is conceivable that the MB might facilitate using odor landmarks to reset or correct the path integrator, especially given that the output neurons of MB (MBON) are known to signal the central complex (CX)49,50, where many classes of spatially selective neurons, including PFNs, are housed. However, our results so far favor some amount of parallel nature of MB-based and PFN-based strategies, as olfactory input can still promote some learning without functional PFNs and vice versa.

One of the most unexpected findings of our work is that flies appeared to use scents from self-deposits to “create” landmarks – and then assigned them meaning – when locating a rewarded goal in a feature-impoverished environment. This result mirrors a recent finding showing that dessert ants can create their own visual landmarks when navigating in environments without obvious ones51. While we were not able to directly visualize the scents’ being concentrated at the goal location, our thesis is supported by several lines of evidence. First, we detected various fly-derived chemicals on the arena floors. Second, preventing flies from rubbing their bodies, especially their genitalia, reduced learning. Third, disabling olfactory neurons disrupted learning. Lastly, silencing the olfactory association center, MB, disrupted learning as well. Our findings raise two interesting questions. First, what is the exact identity of the substances being used? Some of the chemicals identified by GS-MS are likely candidates, although it is also possible that the relevant ones were present below the detection threshold. We cannot provide proof of the use for any of the chemicals for now, partly because the receptors for many of these chemicals are not known. It is worth noting that Drosophila males have been shown to mark locations where they encounter appetitive food odors with 9-tricosene to attract egg-laying females27. However, 9-tricosene was not the relevant scent used by our males, or at least not the sole scent, as the mutants for Or7a, the receptor for 9-tricosene, did not show reduced performance compared to controls (Extended Data Fig. 12). Second, how general might this strategy be? For example, will flies abandon this strategy or use a different scent depending on the nature of the reward and/or the foraging environment? Curiously, olfaction was found to be dispensable in a landmark study where the authors demonstrated that flies can use path integration when navigating towards a goal in darkness22. One important difference between the task described by Kim & Dickinson and ours is that our arena size is considerably smaller. It is possible that, given the potential low quantity and/or volatility of self-deposited scents, the strategy we described may be effective only in small and enclosed environments. As for whether the nature of the reward matters, we found that intact antennae were still required when we replaced optogenetic activation of 0273-Gal4-labeled neurons with activation of another group of neurons (the fructose sensing Gr43a neurons), which has also been shown to promote reward seeking21 (Extended Data Fig. 13). This suggests that the strategy we observed may generalize to tasks where the goal location is baited with a (virtual) sugar reward.

Download figureOpen in new tab
Extended Data Fig. 12
Or7a mutant flies did not show decreased spatial learning performance.

a, RI difference between experimental flies and their paired yoked controls of Ctrl and Or7a mutant flies in the flat chamber over time.

Download figureOpen in new tab
Extended Data Fig. 13
Optogenetic activation of the Gr43a-Gal4 labeled sweet-sensing neurons at the reward circle could also induce learning that depended on intact antennae.

a, RI difference over time between unmanipulated experimental and yoked control Gr43a-Gal4>CsChrimson flies (solid line) and between antenna-removed experimental and yoked control Gr43a-Gal4>CsChrimson flies (dashed line). Note that the decline of the RI difference over time might be due to the flies being starved 20 hours before the task and not receiving any food during the entire task, which might have led to fatigue.

Our work suggests that self-motion cues also play a role in aiding flies’ returns to the goal location when the environment lacks prominent visual cues. We showed that flies were able to collect many rewards without contacting the arena walls. More importantly, the proper function of neurons known to signal egocentric translational velocity (i.e., PFNs) was critical for full performance, as well as collecting many rewards without wall contacts. How exactly the flies use self-motion cues conveyed by PFNs to solve the task remains unclear for now. Intriguingly, disrupting the function of one target two synapses downstream of PFN neurons, the PFR neurons, which allow flies to map their egocentric movements onto the allocentric/world frame (by integrating translational velocity signals from PFNs and heading signals from EPG neurons)4, did not produce obvious defects in spatial learning. Similarly, disrupting the function of the EPG neurons did not significantly impact performance either. The lack of requirement for EPG and PFR neurons might be because unlike learning task driven by prominent visual cues52, our arenas lack any prominent external cues that can engage them reliably. Nonetheless, these findings raise two questions. First, since EPGs have been shown to provide critical heading input to PFNs4,5, it is curious what might be supplying PFNs with directional signals when we silenced EPGs. One possible source is the noduli4,5. Second, since PFRs were dispensable, too, what might the relevant downstream targets of PFNs be in allowing self-motion to be used to guide goal-directed movements? We don’t have answers for this either, but the recently identified PFL3 and PFL2 neurons that allow flies to steer their movements according to an internal goal heading conveyed in FC2 neurons, and hΔC/K neurons that signal goal direction gated by odor, might be worth testing34,36,53, as are other anatomical targets delineated in the connectome.

Methods
Fly genotypes

To perform the SLI and other behavioral analysis of sighted control flies and flies with manipulations in antennae (whole antennae glued third segment of antennae removed and arista removed), hind tarsi removal and gluing genitalia (Fig. 1d-g; 2a, b; 3a, e, f, h; 4b-d, g, j; Extended Data Fig. 1a, b, d, f; 4a, d; 5a-d, g-i; 9b; 10a, d, e; Table 1): UAS-CsChrimson/y; +/+; 0273-Gal4/+.

To perform the SLI and other behavioral analysis of blind flies (Fig. 1h; 4e, f; Extended Data Fig. 1e, 6a, b): norpA; +; UAS-CsChrimson/0273-Gal4.

To chronically silence target neurons with Kir, the control group flies (Fig. 2d, k; 3j; 4k; 5a, c, e; Extended Data Fig. 2a; 3b; 4e, f; 8a; 11b, c): UAS-CsChrimson/y; Empty-LexA/otd-flp; 0273-Gal4/LexAop-(FRT)-tdTomato-STOP-(FRT)-eGFP-Kir.

To chronically silence PFNd neurons (Fig. 2d; 5a-c, e; Extended Data Fig. 2a; 11 a-c): UAS-CsChrimson/y; 16D01-LexA/otd-flp; 0273-Gal4/LexAop-(FRT)-tdTomato-STOP-(FRT)-eGFP-Kir.

To chronically silence EPG neurons (Fig. 2k): UAS-CsChrimson/y; 60D05-LexA/otd-flp; 0273-Gal4/LexAop-(FRT)-tdTomato-STOP-(FRT)-eGFP-Kir.

To chronically silence PFR neurons (Extended Data Fig. 3b): UAS-CsChrimson/y; 37G12-LexA/otd-flp; 0273-Gal4/LexAop-(FRT)-tdTomato-STOP-(FRT)-eGFP-Kir.

To chronically silence MBKCs (Fig. 3j; 4k; Extended Data Fig. 4e, f, 8a): UAS-CsChrimson/y; 19B03-LexA/otd-flp; 0273-Gal4//LexAop-(FRT)-tdTomato-STOP-(FRT)-eGFP-Kir, and UAS-CsChrimson/y; 26E07-LexA/otd-flp; 0273-Gal4/LexAop-(FRT)-tdTomato-STOP-(FRT)-eGFP-Kir.

To transiently silence target neurons with GtACR1, the control group flies (Fig. 2e, l; 3k; 4l; 5d; Extended Data Fig. 2b; 3c; 4g, h; 8b): w; ctrl-lexA/lexAop-GtACR1; 0273-Gal4/UAS-CsChrimson.

To transiently silence PFNd neurons (Fig. 2e; 5d; Extended Data Fig. 2b): w; 16D01-lexA/lexAop-GtACR1; 0273-Gal4/UAS-CsChrimson.

To transiently silence EPG neurons (Fig. 2l): w; 60D05-lexA/lexAop-GtACR1; 0273-Gal4/UAS-CsChrimson.

To transiently silence PFR neurons (Extended Data Fig. 3c): w; 37G12-lexA/lexAop-GtACR1; 0273-Gal4/UAS-CsChrimson.

To transiently silence MBKCs (Fig. 3k; 4l; Extended Data Fig. 4g, h; 8b): w; 19B03-lexA/lexAop-GtACR1; 0273-Gal4/UAS-CsChrimson, and w; 26E07-lexA/lexAop-GtACR1; 0273-Gal4/UAS-CsChrimson.

To transiently activate target neurons, the control group flies (Fig. 2g, i, n; Extended Data Fig. 2c, d; 3e): w; UAS-CsC/empty-Gal4-AD; 0273-Gal4/empty-Gal4-DBD.

To transiently activate PFNd neurons (Fig. 2g; Extended Data Fig. 2c): w; UAS-CsChrimson/SS00078; 0273-Gal4/SS00078.

To transiently activate PFNv neurons (Fig. 2i; Extended Data Fig. 2d): w; UAS-CsChrimson/SS52628; 0273-Gal4/SS52628.

To transiently activate EPG neurons (Fig. 2n): w; UAS-CsChrimson/SS00090; 0273-Gal4/SS00090.

To transiently activate PFR neurons (Extended Data Fig. 3e): w; UAS-CsChrimson/SS54549; 0273-Gal4/SS54549.

To test the roles of Orco in learning (Fig. 3b; 4h; Extended Data Fig. 4b; 5e; 10f), we used w; UAS-CsChrimson/+; 0273-Gal4/Orco23130 as the control group, and w; UAS-CsChrimson/+; 0273-Gal4, Orco23129/Orco23130 as the experimental group.

To chronically silence Ir25a-expressing and Orco-experssing neurons simultaneously (Fig. 3c; 4i; Extended Data Fig. 4c; 5f; 10b, g), we used w; UAS-CsChrimson/Ir25a-QF; Orco-QF (BL-92400)/0273-Gal4 as control group #1, w; UAS-CsChrimson/+; 0273-Gal4, QUAS-Kir/+ as control group #2, and w; UAS-CsChrimson/Ir25a-QF; 0273-Gal4, QUAS-Kir/Orco-QF as the experimental group.

To chemically ablate MB (Extended Data Fig. 7): UAS-CsChrimson/+; 0273-Gal4/+.

To test the roles of Or7a in learning (Extended Data Fig. 12), the control group flies: UAS-CsChrimson/+; 0273-Gal4/+, and flies with Or7a mutant: Or7a/y; UAS-CsChrimson/+; 0273-Gal4/+.

To test the learning performance of starved flies with optogenetic activation of Gr43a neurons as reward (Extended Data Fig. 13): UAS-CsChrimson/y; Gr43a-Gal4/+ (II).

To image the expression pattern of driver lines that label PFNd neurons (Fig. 2c, f): w; R16D01-lexA/lexAop-GtACR1; 0273-Gal4, and w; +/SS00078; UAS-eGFP-Kir/SS00078.

To image the expression pattern of the driver line that labels PFNv neurons (Fig. 2h): w; +/SS52628; UAS-eGFP-Kir/SS52628.

To image the expression pattern of driver lines that label EPG neurons (Fig. 2j, m): w; R60D05-lexA/lexAop-GtACR1; 0273-Gal4, and w; +/SS00090; UAS-eGFP-Kir/SS00090.

To image the expression pattern of driver lines that label MBKCs (Fig. 3i): w; R19B03-lexA/lexAop-GtACR1; 0273-Gal4, and w; R26E07-lexA/lexAop-GtACR1; 0273-Gal4.

To image the expression pattern of driver lines that label PFR neurons (Extended Data Fig. 3a, d): w; R37G12-lexA/lexAop-GtACR1; 0273-Gal4, and w; +/SS54549; UAS-eGFP-Kir/SS54549.

Note that we used the same group of control flies in the following experiments since they were done at the same time periods:

Ctrl>Kir flies were the same for PFNd>Kir and MBKC-2>Kir in the flat chamber;

Ctrl>Kir flies were the same for EPG>Kir and PFR>Kir in the flat chamber;

Ctrl>GtACR1 flies were the same for MBKC-1>GtACR1 and MBKC-2>GtACR1 in both the flat and the agarose chambers;

Ctrl>CsChrimson flies were the same for PFNd>CsChrimson and EPG>CsChrimson.

Fly husbandry

Flies were raised at 25 °C on standard molasses food. We density-controlled the crosses and supplied them with yeast paste (6 g dry yeast in 10mL 0.5% propionic acid) to ensure the health of the progeny. Only 10- to 14-day old males were used for our spatial learning tasks. They were collected on the first day of eclosion into regular food vials for 6-10 days at the density of 12-14 flies/vial, transferred into food vials with 400 μM retinal and kept without light exposure for 2 days, and transferred again into fresh retinal food vials under circadian entrainment (12 hours light on/off) before being assayed. For Gr43a-Gal4>CsChrimson flies, they were starved for 20 hours before the spatial learning task.

Non-genetic manipulations on flies
Removing the 3rd segment of antenna, and the arista

The procedures were done using forceps one day before the assay to give the flies time to recover and adapt.

Gluing the whole antenna

This was done by applying a small piece of UV-cured glue (Bondic) to cover the entire antenna of the flies under a dissecting scope and exposing them to 5 seconds of UV light (Darkbeam UV Flashlight 365 nm). To allow the flies time to recover and adapt, these manipulations were performed one day before the assay.

Gluing the genitalia

This was done by applying a small piece of UV-cured glue (Bondic) to cover the whole genitalia of the flies under a dissecting scope and exposing them to 5 seconds of UV light (Darkbeam UV Flashlight 365 nm). To limit activation of 0273-GAL4-labeled neurons during these manipulations by the illuminator light (Nikon NI-150) of the dissecting scope, we set its intensity below 30% and restricted the total illumination time to under 3 minutes. Control flies, which were not glued, were illuminated under the dissecting scope, anesthetized, and exposed to UV for the same duration as the glued group. As the glue on the genitalia tended to fall off, we applied it 2 to 3 hours before the task and always inspected for its presence afterward to ensure it remained intact during the task.

Removing the hind tarsi

This was done using a pair of forceps. Since we used the same control flies as for the genitalia-glued group, we removed the hind tarsi of the flies 2 to 3 hours before the task.

MB ablation

MB in the fly brain were chemically ablated following the standard procedure54 with the modification that 0- to 1-hour old larvae were fed for 5 hours with yeast paste that contained 50 mg/ml hydroxyurea.

Odor sample collection and GC-MS

To collect substances deposited by the flies, we placed a small piece of transparent film (3.5 mm in diameter) at the center of each arena prior to the task and collected it immediately after training finished. Specifically, 18 pieces from arenas trained with experimental flies, 18 from arenas trained with yoked controls, and 18 from empty arenas (blank control) were collected, soaked in three separate vials with 100 µl of hexane each, and sent for gas chromatography-mass spectrometry (GC-MS) analysis at Alera Labs (https://aleralabs.com/). At Alera Labs, samples were evaporated and redissolved in 100 µL of hexane containing the internal standard (methyl nonadecanoate at 5 µg/mL). Then, 3 µL of each sample were analyzed using an Rxi-5MS column (30 m length, 0.25 mm ID, 0.25 um film thickness) with an inlet temperature of 280 °C and a detector temperature of 300 °C. Helium was used as the carrier gas with a split 10:1 flow rate. The temperature program was set to start at 120 °C, ramping at 6 °C/min to 300 °C, with a 5-minute hold. The mass spectrometer operated in electron ionization (EI) mode with an m/z scan range of 35-550. All assignments were based on the highest probability spectral matches.

Implementation of the high-throughput spatial learning task
Hardware

Arenas. We designed two types of chambers, each containing 40 individual arenas, for testing flies’ ability to locate the spatial goal. To increase the throughput of the task, we have created 6 setups, enabling us to simultaneously assay 240 flies in parallel. In the flat chambers, the arena is rectangularly shaped (dimensions: 16 x 10 x 3 mm) and featureless (Fig. 1a). In the agarose chamber, the arena has the same dimensions but includes two troughs at the ends (3 x 10 x 3 mm) that we filled with 1% agarose (Fig. 4a). Optogenetic stimulation. Light pulses were delivered by custom LED controller boards with 5-mm 527-nm 15°-viewing angle Cree LEDs (C503B-GAN-CB0F0791). Board schematic and layout are available at https://github.com/ulrichstern/SkinnerTrax. We used 25% light intensity for the 250-ms “reward” pulses for 0273-Gal4>CsChrimson flies, which corresponds to about 16.4 μW/mm2 at the arena floors, while for Gr43a-Gal4>CsChrimson flies (Extended Data Fig. 13), we used 125% light intensity, which corresponding to about 77.3 μW/mm2 at the arena floors. Cameras. Each apparatus uses two cameras (Microsoft LifeCam Cinema) with their internal IR-block filters removed and external IR-pass filters (LEE Filters 87) added. Infrared backlight. An 850-nm light pad was placed underneath the arenas and LED controller board to provide background lighting for tracking. The light pads were custom made by Junlong Display Factory; we asked them to replace the white LEDs in their Artograph A920 series light pads with 850-nm LEDs.

Software

SkinnerTrax37 was used to administer the learning task independently for each of the 40 flies per apparatus in parallel. SkinnerTrax’s experimental records, which served as input for follow-on analysis, included the flies’ positions, fitted ellipses for each frame, and the times when each fly was stimulated. The code for SkinnerTrax is available at https://github.com/ulrichstern/SkinnerTrax.

Handling of flies

Male flies, 10-14 days old and fed standard 400 μM retinal fly food for 4 days, were maintained under circadian control (12 h light on, 12 h light off) and placed in either flat or agarose chambers (one fly per arena) within the first 2.5 hours of light onset. The chambers were placed into the tracking system and shielded from ambient light with a cardboard box.

Analysis of the high-throughput spatial learning task

All the behavior analysis code used in this paper are available in GitHub at https://github.com/rcalfredson/nvsl-analysis

Exclusion of flies with poor tracking

To minimize the impact of tracking problems, our analysis code automatically excluded trajectories for which problems were detected. First, the percentage of “lost” frames – where the fly could not be detected after the initial onset of tracking – was calculated. The vast majority of lost frames occurred when flies were walking on the sidewalls, which appear darker in the frames, making it harder to track flies. Trajectories that contained more than 10% lost frames were excluded from analysis. Second, tracking may intermittently switch between the fly (the intended target) and fixed arena locations where tracking artifacts occur, especially if the fly gets lost. The result is “suspicious jumps” where a fly incorrectly appears to jump from its true location to the artifact and then back to about the original location when it is tracked again. If at least 3% of the jumps in a trajectory were determined to be suspicious, and there were at least three suspicious jumps, the trajectory was excluded from analysis.

Calculation of the heatmaps

The heatmaps shown in Fig. 1d and 4b were calculated directly by SkinnerTrax to allow for a quick assessment of the positional preferences of the flies during the training sessions. Warmer colors indicate more time spent at that position.

Calculation of the reward index (RI)

The reward index, which we first introduced in prior work39, is defined as follows:
The reward and control circles we used are depicted in Fig. 1e.

The time point 0 in the RI over time (and RI difference over time) plots during training was defined differently from the actual start time of the training session. For each training session, time 0 marks when the experimental fly first entered the reward circle, receiving a reward, rather than the start time of the session. This means we excluded the initial part of the session where the fly had no learning signal yet, and thus the time 0 in the plot can be considered the session’s beginning of learning for each fly. We used the term “sync bucket” to refer to the synchronization of temporal buckets (intervals) with the first reward of the session. For example, to calculate the RI for the fifth (last) 10-minute sync bucket, we counted all circle entries in the 10-minute interval from time point 40 to time point 50 minutes and then applied the reward index formula.

As we have previously noted39, the reward index was designed to be insensitive to flies’ speed. This was achieved in two ways. First and foremost, by comparing preference of entering one circle over another, it is not the absolute number of circle entries that matters (where a fast animal would have an advantage) but the preference index (where a slow animal that learns well can be as good as or better than a fast one). Second, to be able to calculate each preference value reliably, we excluded data points for buckets where the sum of the entries for the two circles was less than 10. This rule automatically excluded times when flies barely moved, and a fly that barely moved throughout the experiment would not contribute to any of the mean reward index scores.

Calculation of the spatial learning index (SLI)

To represent the spatial learning ability of a given group of flies during training, we first calculated the reward index difference between each experimental fly and its paired yoked control at each sync bucket. See main text for the benefits of using this difference. The SLI is simply this difference for the last sync bucket of the training session 3:

Calculation of light/reward preference

We performed open-loop light preference assays in the flat chambers to test flies’ innate preference for the optogenetically delivered rewards. The open-loop task comprised a 30-minute pre-training period, a 2-hour training session, and a 30-minute post-training session. During the training session, only the upper half of the chamber was illuminated in a repeating cycle of 4 minutes of light on (7% LED intensity, which corresponds to about 4.63 μW/mm2 at the arena floors) followed by 4 minutes of light off. We calculated the light preference as average over all light-on periods as follows:

Additional behavioral analyses
Calculation of the no wall contact index

See main text for the calculation of the no wall contact index. To ensure the index could be calculated reliably, we excluded pairs of flies unless the experimental fly and its paired yoked control each collected at least 10 rewards during the period used for the calculation.

Wall contact detection

Wall contact events were determined using a dual-boundary approach, in which two boundaries were defined for each wall: an event-start boundary 0.7 mm inward from the wall and an event-end boundary 1.0 mm inward from the wall. A wall contact event began when the point on the fly’s fitted ellipse closest to the wall crossed the event-start boundary walking toward the wall. The event continued until the point on the ellipse closest to the wall crossed the event-end boundary walking away from the wall. The boundary offsets were selected from four options (0.4/0.75 mm, 0.6/0.9 mm, 0.7/1.0 mm and 0.9/1.2 mm) based on which provided the best agreement between algorithmically detected and manually verified events.

Calculation of the probability of sharp turns toward the horizontal centerline at different distances

We aimed to identify sharp turns in the fly’s trajectory at virtual boundaries located symmetrically at distances 2, 3, 4, 5, and 6 mm from the horizontal centerline of the chamber (Fig. 3g, h, Extended Data Fig. 5, 8). Each distance was analyzed independently, and analysis was typically performed for the last sync bucket of training 3.

Detection of virtual boundary contact events

Boundary contact events began when the fly’s trajectory (which is based on fitted ellipse centers) crossed a virtual boundary while moving away from the centerline. The events ended when the trajectory crossed a horizontal line positioned 0.1 mm inward from the virtual boundary.

Detection of sharp turns

Sharp turns were defined as boundary contact events with a duration of 0.75 seconds or less and with a cumulative change in velocity angle (the angle of the velocity vector) in a single direction in excess of 90 degrees. When calculating the cumulative change in velocity angle, we excluded trajectory edges where the fly’s speed was below 2 mm/s as well as angle changes for the first frame of a wall contact event.

Probability calculation

The probability of sharp turns was calculated as the ratio of the number of sharp turns to the total number of boundary contact events.

Exclusion criteria and sample size standardization for plotting

To ensure only reliably calculated probabilities were used, at least 10 boundary contact events were required during the period used for the calculation. If a fly was excluded at one distance, it was excluded at all distances, resulting in the same sample size for all distances (e.g., Fig. 3h). Finally, except for the pre-training analysis in Fig. 3h, we included only flies for which an SLI had been calculated.

Calculation of the percentage of time spent on agarose (or corresponding) areas

The percentage of time flies spent on agarose was calculated based on the proportion of frames in which the ellipse center fell within the rectangles corresponding to the agarose areas (Extended Data Fig. 9a). For percentage calculations for the last sync bucket of training 3, we included only flies for which an SLI had been calculated.

Calculation of the distance distribution of the start of the first large turn

We aimed to determine the distribution of the distance from the chamber center where the flies initiated their first large turn after their departures from the reward circle (Extended Data Fig. 10c-g).

Detection of large turns

We used the fly’s heading angle instead of velocity angle to detect large turns since the former resulted in fewer false positives, and we skipped frames with speed below 2 mm/s to exclude trajectory segments for which the flies were resting. We defined large turns to start with an angle delta of at least 18° and to reach a cumulative angle delta of at least 90° in the same direction (left or right) as the turn-starting angle delta. If an angle delta of at least 18° in the opposite direction occurred before reaching 90°, we started a second angle delta sum to allow for large turns in either direction. Finally, we excluded turns where 1) wall contact or re-entry into the reward circle happened before reaching 90°, 2) the total distance traveled during the turn was less than 1 mm, or 3) more than 70% of the frames of the turn had a speed below 2 mm/s.

Calculation of the distance of the start of the first large turn histograms

Each fly’s distance data was binned into its own histogram. Histograms based on fewer than 20 large turns were excluded. Extended Data Fig. 10d-g shows mean histograms, averaging the bins across all flies within a group. Two-tailed Welch’s t-test with Bonferroni correction was used to compare groups for each bin. In addition, we calculated the mean distance for each fly and compared the means using Two-tailed Welch’s t-test.

Calculation of the average speed during learning

To calculate the average speed during learning (Extended Data Figs. 1a, b, 2, and 4), we used only the last sync bucket of training 3, excluding sidewall walking to improve the accuracy of the speed calculation. We included only flies for which an SLI had been calculated.

Author contributions

Y.C. and C.-H.Y. designed the project. Y.C. performed the experiments and analyzed the data. R.A. and U.S. wrote the code for analyzing the data. U.S. built the behavior-dependent stimulation system. Y.C., R.A., U.S., and C. -H.Y. interpreted the data. D.M. dissected fly brains for imaging. Y.C. wrote the initial draft of the paper, which was then edited by C.-H.Y., U.S., and R.A.

Competing interests

The authors declare no competing interests.

Supplementary Videos

Video S1. High-throughput spatial learning task with 0273Gal4>CsChrimson flies in the flat chamber

Left half: Example video showing 10 experimental flies and their paired yoked control flies undergoing training in our high-throughput spatial learning task in the flat chamber. Right half: The real-time positional heatmap of corresponding flies during training. The video is at 2X play back speed.

Video S2. High-throughput spatial learning task with 0273Gal4>CsChrimson flies in the agarose chamber

Left half: Example video showing 10 experimental flies and their paired yoked control flies undergoing training in our high-throughput spatial learning task in the agarose chamber. Right half: The real-time positional heatmap of corresponding flies during training. The video is at 2X play back speed.

Acknowledgements

We would like to thank the Bloomington Stock Center for providing fly strains, the Duke Physics Shop for fabricating the behavior apparati, and Alera Labs (https://aleralabs.com/) for GC-MS analysis. We would also like to thank Drs. Calakos, Nowicki, Volkan, and Dong, and members of the Yang Lab for helpful comments and suggestions. This work was supported by an invertebrate neuroscience research grant awarded to C.-H.Y.

References
↵Lee, S. M., Shin, J. & Lee, I. Significance of visual scene-based learning in the hippocampal systems across mammalian species. Hippocampus 33, 505–521 (2023).Google Scholar
↵Ofstad, T. A., Zuker, C. S. & Reiser, M. B. Visual place learning in Drosophila melanogaster. Nature 474, 204–207 (2011).CrossRefPubMedWeb of ScienceGoogle Scholar
↵Modi, M. N., Shuai, Y. & Turner, G. C. The Drosophila mushroom body: from architecture to algorithm in a learning circuit. Annual review of neuroscience 43, 465–484 (2020).CrossRefPubMedGoogle Scholar
↵Lyu, C., Abbott, L. & Maimon, G. Building an allocentric travelling direction signal via vector computation. Nature 601, 92–97 (2022).CrossRefPubMedGoogle Scholar
↵Lu, J. et al. Transforming representations of movement from body-to world-centric space. Nature 601, 98–104 (2022).Google Scholar
↵Müller, M. & Wehner, R. Path integration in desert ants, Cataglyphis fortis. Proceedings of the National Academy of Sciences 85, 5287–5290 (1988).Abstract/FREE Full TextGoogle Scholar
↵Heinze, S., Narendra, A. & Cheung, A. Principles of insect path integration. Current Biology 28, R1043–R1058 (2018).CrossRefGoogle Scholar
↵Wittlinger, M., Wehner, R. d. & Wolf, H. The ant odometer: stepping on stilts and stumps. science 312, 1965–1967 (2006).Abstract/FREE Full TextGoogle Scholar
↵Alyan, S. & McNaughton, B. Hippocampectomized rats are capable of homing by path integration. Behavioral neuroscience 113, 19 (1999).CrossRefPubMedWeb of ScienceGoogle Scholar
↵Alyan, S. & Jander, R. Short-range homing in the house mouse, Mus musculus: stages in the learning of directions. Animal Behaviour 48, 285–298 (1994).CrossRefWeb of ScienceGoogle Scholar
↵Aharon, G., Sadot, M. & Yovel, Y. Bats use path integration rather than acoustic flow to assess flight distance along flyways. Current Biology 27, 3650–3657. e3653 (2017).CrossRefPubMedGoogle Scholar
↵Séguinot, V., Cattet, J. & Benhamou, S. Path integration in dogs. Animal behaviour 55, 787–797 (1998).CrossRefPubMedWeb of ScienceGoogle Scholar
↵Patel, R. N., Kempenaers, J. & Heinze, S. Vector navigation in walking bumblebees. Current Biology 32, 2871–2883. e2874 (2022).Google Scholar
Srinivasan, M. V., Zhang, S. & Bidwell, N. Visually mediated odometry in honeybees. Journal of Experimental Biology 200, 2513–2522 (1997).Abstract/FREE Full TextGoogle Scholar
Srinivasan, M. V., Zhang, S., Lehrer, M. & Collett, T. Honeybee navigation en route to the goal: visual flight control and odometry. Journal of Experimental Biology 199, 237–244 (1996).Abstract/FREE Full TextGoogle Scholar
↵Frisch, K. v. The dance language and orientation of bees. (Harvard University Press, 1993).Google Scholar
↵El Jundi, B., et al. A snapshot-based mechanism for celestial orientation. Current biology 26, 1456–1462 (2016).CrossRefGoogle Scholar
el Jundi, B., Smolka, J., Baird, E., Byrne, M. J. & Dacke, M. Diurnal dung beetles use the intensity gradient and the polarization pattern of the sky for orientation. Journal of experimental biology 217, 2422–2429 (2014).Abstract/FREE Full TextGoogle Scholar
↵Yilmaz, A., Gagnon, Y., Byrne, M., Baird, E. & Dacke, M. Cold-induced anesthesia impairs path integration memory in dung beetles. Current Biology 32, 438–444. e433 (2022).CrossRefGoogle Scholar
↵Giraldo, Y. M. et al. Sun navigation requires compass neurons in Drosophila. Current Biology 28, 2845–2852. e2844 (2018).CrossRefPubMedGoogle Scholar
↵Corfas, R. A., Sharma, T. & Dickinson, M. H. Diverse food-sensing neurons trigger idiothetic local search in Drosophila. Current Biology 29, 1660–1668. e1664 (2019).CrossRefGoogle Scholar
↵Kim, I. S. & Dickinson, M. H. Idiothetic path integration in the fruit fly Drosophila melanogaster. Current Biology 27, 2227–2238. e2223 (2017).CrossRefPubMedGoogle Scholar
↵Behbahani, A. H., Palmer, E. H., Corfas, R. A. & Dickinson, M. H. Drosophila re-zero their path integrator at the center of a fictive food patch. Current Biology 31, 4534–4546. e4535 (2021).CrossRefGoogle Scholar
↵Hulse, B. K. & Jayaraman, V. Mechanisms underlying the neural computation of head direction. Annual review of neuroscience 43, 31–54 (2020).CrossRefPubMedGoogle Scholar
↵Marin, A. C., Schaefer, A. T. & Ackels, T. Spatial information from the odour environment in mammalian olfaction. Cell and Tissue Research 383, 473–483 (2021).CrossRefPubMedGoogle Scholar
Jacobs, L. F., Arter, J., Cook, A. & Sulloway, F. J. Olfactory orientation and navigation in humans. PLoS One 10, e0129387 (2015).CrossRefPubMedGoogle Scholar
↵Lin, C.-C., Prokop-Prigge, K. A., Preti, G. & Potter, C. J. Food odors trigger Drosophila males to deposit a pheromone that guides aggregation and female oviposition decisions. Elife 4, e08688 (2015).CrossRefPubMedGoogle Scholar
Zolin, A. et al. Context-dependent representations of movement in Drosophila dopaminergic reinforcement pathways. Nature neuroscience 24, 1555–1566 (2021).CrossRefPubMedGoogle Scholar
↵Steele, T. J., Lanz, A. J. & Nagel, K. I. Olfactory navigation in arthropods. Journal of Comparative Physiology A 209, 467–488 (2023).Google Scholar
↵Hardcastle, K., Ganguli, S. & Giocomo, L. M. Environmental boundaries as an error correction mechanism for grid cells. Neuron 86, 827–839 (2015).CrossRefPubMedGoogle Scholar
Etienne, A. S., Maurer, R., Boulens, V., Levy, A. & Rowe, T. Resetting the path integrator: a basic condition for route-based navigation. Journal of Experimental Biology 207, 1491–1508 (2004).Abstract/FREE Full TextGoogle Scholar
↵Fischler-Ruiz, W. et al. Olfactory landmarks and path integration converge to form a cognitive spatial map. Neuron 109, 4036–4049. e4035 (2021).Google Scholar
↵Green, J. et al. A neural circuit architecture for angular integration in Drosophila. Nature 546, 101–106 (2017).CrossRefPubMedGoogle Scholar
↵Mussells Pires, P., Zhang, L., Parache, V., Abbott, L. & Maimon, G. Converting an allocentric goal into an egocentric steering signal. Nature, 1–11 (2024).Google Scholar
↵Seelig, J. D. & Jayaraman, V. Neural dynamics for landmark orientation and angular path integration. Nature 521, 186–191 (2015).CrossRefPubMedGoogle Scholar
↵Westeinde, E. A. et al. Transforming a head direction signal into a goal-oriented steering command. Nature, 1–8 (2024).Google Scholar
↵Stern, U. & Yang, C.-H. SkinnerTrax: high-throughput behavior-dependent optogenetic stimulation of Drosophila. bioRxiv, 080614 (2017).Google Scholar
↵Jovanoski, K. D. et al. Dopaminergic systems create reward seeking despite adverse consequences. Nature 623, 356–365 (2023).Google Scholar
↵Stern, U. et al. Learning a spatial task by trial and error in Drosophila. Current Biology 29, 2517–2525. e2515 (2019).CrossRefGoogle Scholar
↵Govorunova, E. G., Sineshchekov, O. A., Janz, R., Liu, X. & Spudich, J. L. Natural light-gated anion channels: A family of microbial rhodopsins for advanced optogenetics. Science 349, 647–650 (2015).Abstract/FREE Full TextGoogle Scholar
↵Goldschmidt, D. et al. Exploration and exploitation are flexibly balanced during local search in flies. bioRxiv, 2024.2006. 2026.600764 (2024).Google Scholar
↵Vosshall, L. B. & Hansson, B. S. A unified nomenclature system for the insect olfactory coreceptor. Chemical senses 36, 497–498 (2011).CrossRefPubMedWeb of ScienceGoogle Scholar
↵Task, D. et al. Chemoreceptor co-expression in Drosophila melanogaster olfactory neurons. Elife 11, e72599 (2022).CrossRefGoogle Scholar
↵Howard, R. W. & Blomquist, G. J. Chemical ecology and biochemistry of insect hydrocarbons. Annual review of entomology 27, 149–172 (1982).CrossRefWeb of ScienceGoogle Scholar
↵Howard, R. W. & Blomquist, G. J. Ecological, behavioral, and biochemical aspects of insect hydrocarbons. Annu. Rev. Entomol. 50, 371–393 (2005).CrossRefPubMedWeb of ScienceGoogle Scholar
↵Aso, Y. et al. The neuronal architecture of the mushroom body provides a logic for associative learning. elife 3, e04577 (2014).CrossRefPubMedGoogle Scholar
↵de Belle, J. S. & Heisenberg, M. Associative odor learning in Drosophila abolished by chemical ablation of mushroom bodies. Science 263, 692–695 (1994).Abstract/FREE Full TextGoogle Scholar
↵Handler, A. et al. Distinct dopamine receptor pathways underlie the temporal sensitivity of associative learning. Cell 178, 60–75. e19 (2019).CrossRefPubMedGoogle Scholar
↵Hulse, B. K. et al. A connectome of the Drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection. Elife 10 (2021).Google Scholar
↵Aso, Y. et al. Mushroom body output neurons encode valence and guide memory-based action selection in Drosophila. elife 3, e04580 (2014).CrossRefPubMedGoogle Scholar
↵Freire, M., Bollig, A. & Knaden, M. Absence of visual cues motivates desert ants to build their own landmarks. Current Biology 33, 2802–2805. e2802 (2023).Google Scholar
↵Dan, C., Hulse, B. K., Kappagantula, R., Jayaraman, V. & Hermundstad, A. M. A neural circuit architecture for rapid learning in goal-directed navigation. Neuron (2024).Google Scholar
↵Matheson, A. M. et al. A neural circuit for wind-guided olfactory navigation. Nature Communications 13, 4613 (2022).Google Scholar
↵Prokop, A. & Technau, G. M. Normal function of the mushroom body defect gene of Drosophila is required for the regulation of the number and proliferation of neuroblasts. Developmental biology 161, 321–337 (1994).CrossRefPubMedWeb of ScienceGoogle Scholar
 Back to top
 Previous
Next 
Posted September 29, 2024.
Download PDF
Print/Save Options

Supplementary Material

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
Introduction
Results
Discussion
Methods
Author contributions
Competing interests
Supplementary Videos
Acknowledgements