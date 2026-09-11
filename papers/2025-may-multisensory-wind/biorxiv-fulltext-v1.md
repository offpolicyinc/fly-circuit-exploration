# May et al. — "A compact multisensory representation of self-motion is sufficient for computing an external world variable" — bioRxiv 10.1101/2025.05.09.653128v1

Captured 2026-09-10 via in-app browser get_page_text from https://www.biorxiv.org/content/10.1101/2025.05.09.653128v1.full. Figures not saved.


Abstract

External forces shape navigation, but cannot be directly measured by an animal in motion. How the brain integrates multi-modal cues to estimate external forces remains unclear. Here we investigated the representation of multi-modal self-motion cues across columnar inputs to the fly navigation center, known as PFNs. We find that one type integrates optic flow and airflow direction signals with distinct dynamics. We reveal airspeed encoding by a different type. Based on these data, we construct and validate models of how multi-sensory dynamics are encoded across PFNs, allowing us to simulate neural responses during rapid flight maneuvers. Applying a nonlinear observability analysis to these responses, we show that PFN representations during active maneuvers are sufficient to decode the direction of an external force (wind) during free flight. Our work provides evidence that active sensation, combined with multisensory encoding, can allow a compact nervous system to infer a property of the external world that cannot be directly measured by a single sensory system.

Introduction

External forces such as gravity and wind impact the kinds of movements animals can make, and serve as important orientation cues; for example, flying insects use wind direction to navigate towards odor sources both while walking and in flight (1–5). Inferring the direction of such a force is challenging because an animal’s mechanosensors do not distinguish deflections induced by internally generated movement from those by external forces (6, 7). By combining active maneuvers with multisensory feedback, recent theoretical studies have argued that an animal should be able to infer the direction of wind while in flight (8–11). However, it is not known whether the influences of the external force on neural representations of self-motion are sufficient for such calculations.

When an animal moves through the world, it produces both characteristic patterns of visual feedback, known as optic flow (12, 13), and patterns of mechanosensory feedback, in the form of vestibular sensation (14). Optic flow provides high directional accuracy but is relatively slow, can be evoked artificially by environmental movement, and cannot provide accurate speed information without an estimate of distance (8, 15, 16). In contrast, vestibular feedback is fast, but only transiently encodes movement speed, acceleration, and direction (17). While both cues can redundantly signal self-motion in some cases, neither cue alone is sufficient to accurately estimate self-motion under natural conditions (16). Consistent with their prominent role in self-motion estimation, neurons that integrate vestibular and visual self-motion cues have been described in many regions of the vertebrate brain, including the vestibular brainstem (16, 17), cerebellum (18–20), and temporal and parietal cortices (21–23). How these multimodal representations are translated into internal estimates of navigational variables remains challenging to address in vertebrate brains.

In insects, columnar neurons that input to the brain’s navigation center (Central Complex, CX) called PFNs have been shown to encode both optic flow (24–26) and airflow (27, 28), visual and mechanosensory cues that both signal self-motion (8, 29, 30). Intriguingly, both cues appear to be represented in a similar “vector” format: arrays of PFN neurons in the left and right hemisphere encode a bump of Ca2+ activity that tracks the animal’s allocentric heading, while the relative amplitude of left and right bumps encodes the egocentric direction of flow along basis vectors pointing to the left and right of the fly at ±45° (Fig. 1A). Through summation of specific pairs of PFN types, recent studies have shown that the CX can perform vector addition to compute the fly’s travelling direction (24, 31), or the allocentric direction of the wind while walking (28). However, how visual and mechanosensory cues are represented and integrated during dynamic input is not known.

Download figureOpen in new tab
Fig. 1.
PFNs encode variables critical for wind direction estimation in flight.

A. Vector representations by calcium activity across populations of columnar neurons (PFNs). Bump position represents allocentric heading angle while the relative amplitude of left and right bumps represents egocentric direction of optic flow or airflow(24, 31, 33).

B. The wind triangle for flying flies. Ambient wind produces offset airflow and optic flow vectors for a flying fly. Ambient wind direction (ζ) in allocentric coordinates and wind speed (w) determine the egocentric airflow direction (γ) and airspeed (a), and egocentric travel direction (ψ) and groundspeed (g). The optic flow vector points in the opposite direction from the travel direction, and its magnitude (o) is equal to g divided by altitude.

One computation that may take advantage of this multisensory representation is resolving the direction of ambient wind during flight. During flight, wind direction, groundspeed, airflow, and heading are related through the so-called wind triangle (Fig. 1B). If sufficient angles or lengths of this triangle are known, the ambient wind direction can be decoded accurately (8, 11). However, true groundspeed cannot be directly determined by a flying organism without a measure of altitude or the distance of visual objects. Nevertheless, behavioral studies in flying flies argue that flies can indeed perform this estimation task (32). Optogenetic activation of olfactory receptor neurons in flight causes flies to decelerate and often turn in a random direction, followed by a rapid and ballistic orientation upwind. Because of the speed of the upwind turn, it must be based on an internal direction estimate, rather than driven by sensory feedback. The observed preceding movements suggests that these maneuvers may be used to measure wind direction, perhaps by dynamically updating the multisensory representation in PFNs.

To test the feasibility of this hypothesis, we used 2-photon imaging to measure the dynamic integration of optic flow and airflow cues across PFNs. We show that one PFN type, called PFNd, linearly sums a transient airflow direction signal with a slower optic flow direction signal, while a second PFN type, called PFNp_c, encodes both airflow direction and speed. We identify a range of different encodings of airflow variables across other PFN types, and show that PFNs remain active during tethered flight, but do not encode turning maneuvers in this setting. Based on our imaging data, we construct dynamic encoding models for PFNs, and use these to simulate neural responses to real flight trajectories. We then use a nonlinear empirical observability analysis to evaluate whether this representation is sufficient to allow a fly to decode wind direction. We find that a range of flight maneuvers allow the multimodal representation in PFNs to accurately estimate wind direction. We observe a good match between the types of turns observed in freely flying flies and those that our analysis shows are required for accurate wind estimation using PFNs. By removing various elements of our model, we estimate the contribution of different PFN types, and different modalities, to this decoding problem. Together our data and analysis show how active movements can be combined with multisensory encoding to infer the presence and direction of an external force, and provide testable hypotheses about the role of different neuron types in this computation.

Results
Linear summation of airflow and optic flow direction signals in PFNd

To examine the dynamic integration of optic flow and airflow cues in PFNs, we presented translational optic flow, airflow, and coherent or divergent combinations of these stimuli to tethered, non-flying flies (Fig. 2A). PFNs (Fig. 2B) make outputs in the Fan-shaped Body (FB) and receive inputs in both the Protocerebral Bridge (PB), and the Noduli (NO). We imaged primarily from the PB (Fig. 2B, lower), in which a bump of activity can be observed in each hemisphere (24, 31). In PFNd neurons, these bumps have been shown to track heading when flies walk or fly in closed-loop with a visual landmark cue, using signals inherited from EPG compass neurons (24, 31, 33). PFNd neurons have previously been shown to encode both optic flow direction and airflow direction through the relative amplitude of activity in each hemisphere (24, 27), although the integration of these stimuli has not previously been investigated.

Download figureOpen in new tab
Fig. 2.
PFNd neurons integrate optic flow and airflow direction with distinct timecourses.

A. (above) Paradigm for two-photon imaging of responses to directional airflow and optic flow in tethered, non-flying flies. (below) Stimuli of each modality were presented from five directions alone, coherently, or from diverging directions.

B. PFNd anatomy. (above) Anatomy of PFN neurons: these receive input in the protocerebral bridge (PB) and noduli (NO) and output in the fan-shaped body (FB). Bump-shaped calcium activity can be imaged in the PB or FB (green and blue gradients). Imaging was performed from the PB as indicated by the black box. (below) Single volumetric (mean z-projection) frame of imaging from the PB in PFNd showing bump structures in left and right hemispheres. ROIs of the left and right PB halves indicated in yellow.

C. Example single-trial calcium activity in PFNd PB hemispheres in response to select stimuli. All data from the same fly.

D. Calcium activity dynamics in PFNd PB halves to contralateral (negative directions) and ipsilateral (positive directions) stimuli. Gray areas indicate 10-s stimulus period. Colored traces represent mean response ±SEM across flies (N=10 flies, n = 2-4 trials per fly).

E. Mean calcium response in PFNd PB halves as a function of stimulus direction for airflow only (left: 1st second of response), optic flow only (middle: last 3 s of response), and coherent multimodal stimuli (right: full 10-s stimulus period). Positive values represent ipsilateral stimuli and negative values represent contralateral stimuli as in D. Traces represent mean ±SEM. Same data as in D.

F. Comparison of the sum of responses to individual stimuli from the same direction (black traces, left panels) to responses to coherent stimuli (purple traces, right panels). Traces represent mean ±SEM across flies (N=10 flies, n= 2-4 trials), same data as D.

G. The sum of the 10-second mean responses to individual stimuli (x-axis) versus the mean activity during the 10-second coherent stimulus (y-axis). Each dot is one timepoint of the mean across flies for each stimulus direction. Regression line in purple. N=10 flies, same data as D.

H. Comparison of the sum of responses to individual stimuli from different directions (black traces, left panels, OF direction indicated and AF direction = 0°) to responses to divergent stimuli (purple traces, right panels). Traces represent mean ±SEM across flies (N=10 flies, n= 2-4 trials), same data as D.

I. The sum of the 10-s responses to divergent individual stimuli (x-axis) versus the mean activity during the 10-second divergent stimulus (y-axis). Each dot is one timepoint of the mean across flies for each stimulus direction. Regression line in yellow. n=10 flies, same data as D.

We observed that in non-flying flies, both optic flow and airflow modulated PFNd signal amplitude, but with distinct time courses (Fig. 2C-E). Airflow drove a rapid increase in signal amplitude in the ipsilateral hemisphere that decayed to a lower steady state within a few seconds. Optic flow also drove an increase in amplitude in the ipsilateral hemisphere, but this response was slower and more sustained. When airflow and optic flow were presented from the same direction, we observed a large response with a roughly square amplitude profile, suggesting that airflow and optic flow responses sum. When airflow was presented from the front with optic flow from different directions, we observed the characteristic transient response to frontal airflow, with an additional sustained component during ipsilateral optic flow delivery, also consistent with summation (Supp Fig. 1A). In addition to its effects on signal amplitude, airflow also influenced bump position in a subset of flies (Supp Fig. 1B, C). We did not observe this effect with optic flow (Supp Fig. 1B, C). This movement might reflect the bump activity of EPGs which have been shown to shift with wind direction in non-behaving flies (34).

Download figureOpen in new tab
Fig. S1 related to Fig. 2.
Additional data on PFNd responses.

A. Calcium activity dynamics in PFNd PB halves to divergent multisensory stimuli. Airflow is from 0° for all stimuli; translational optic flow is from the directions indicated. The response to coherent airflow and optic flow from 0° is reproduced from Fig. 2D. Gray areas indicate stimulus period. Colored traces represent mean across flies ±SEM (N=10 flies, 2-4 trials per fly, same data as in Fig. 2D).

B. Bump phase across PB columns over time, normalized to phase immediately before stimulus onset for all data. Negative directions indicate stimuli coming from fly’s egocentric left. Data are means of means across flies and trials; light traces are circular means across trials per fly; bold traces and color shading represent circular mean across flies ± circular standard deviation. n=10 flies, 2-4 trials per fly, same data as in Fig. 2D.

C. Mean change in bump phase across PB columns relative to phase immediately before stimulus onset for all data. Negative directions indicate stimuli coming from fly’s egocentric left. Light traces are circular means across trials per fly; bold traces are circular means; shading is ±circular standard deviation. n=10 flies, 2-4 trials per fly, same data as in B.

D. Mean activity during the 10-second coherent stimulus (y-axis) versus a weighted sum (see Methods) of the 10-s responses to individual stimuli (x-axis); same data as in Fig. 2G.

E. Mean activity during the 10-second divergent stimulus (y-axis) versus a weighted sum (see Methods) of the 10-s responses to individual stimuli (x-axis); same data as in Fig. 2I.

F. PFNd calcium activity in response to three stimulus speeds delivered from 0°. Traces represent mean ±SEM across flies for each PB half (N= 6 flies, 2-4 trials per fly). Gray areas indicate 10 s stimulus period.

G. Speed tuning curves for PFNd (1st second of the calcium response), same data as in F Shading is ±SEM across flies.

To test the hypothesis of linear summation across modalities, we plotted mean responses to coherent stimuli (Fig. 2F, G) or to divergent stimuli (Fig. 2H, I) as a function of the sum of the mean individual modality responses. We found that these data were well-fit by a line (R2=0.77), consistent with linear summation. The slope of the relationship is significantly less than 1 (p<1.6e-105), indicating that there is a component of the summation that our model does not capture— most likely an additional slow decay (see supplement to Figure 6). Divergent stimuli also produced responses similar to the sum of the single-modality responses (R2=0.79), though the initial airflow-induced transient was stronger than expected, suggesting a larger weight on airflow input (Supp Fig. 1D, E). We observed weak to no tuning for either airflow or optic flow speed in PFNd neurons (Supp. Fig. 1F, G). We conclude that PFNd encodes a multisensory representation of self-motion direction by linearly integrating airflow and optic flow signals tuned to the same direction (∼45° ipsilateral).

Download figureOpen in new tab
Fig. 3.
PFNp_c neurons encode airspeed and airflow direction.

A. PFNp_c neuropil anatomy. Box around protocerebral bridge indicates imaging region with ROIs indicated in yellow.

B. Example single-trial PFNp_c columnar calcium activity patterns in the PB to select stimuli. All data from the same fly.

C. PFNp_c calcium activity in response to three stimulus speeds delivered from 0° (frontal). Traces represent mean ±SEM across flies for each PB half (N= 9 flies, 2-4 trials per fly). Gray areas indicate 10-s stimulus period.

D. Airspeed tuning curves of the mean response transient (1st-second) amplitude for PFNp_c (light gray) versus PFNd (dark gray, same data as Supp. Fig. 1G). Lines represent mean ±SEM across flies. N=6 PFNd flies and 9 PFNp_c flies, 2-4 trials per fly, PFNp_c sdata same as in C.

E. PFNp_c calcium activity in response to five stimulus directions. Coloring and shading as in C. N=7 flies, 2-4 trials per fly.

F. Mean response transient (1st second) amplitude of PFNp_c (light gray) versus PFNd (dark gray, same as Fig. 2E) as a function of airflow direction. Lines represent mean ±SEM across flies (N = 10 PFNd flies and 7 PFNp_c flies, n = 2-4 trials per fly).

G. Bump structure in PFNp_c (light gray) versus PFNd (dark gray) as a mean fluorescent activity across columns in the first stimulus frame of every airflow trial, with fluorescent maxima aligned to column 5; column 1 is plotted twice (once on either side). Data are means across all trials ±SEM (N=10 PFNd flies and 7 PFNp_c flies, 2-4 trials per fly).

H. Synaptic weights of heading-encoding neurons in the PB (EPG and Δ7) onto four PFN types. Relative line thickness and numbers indicate mean per-PFN-neuron weight calculated from hemibrain connectome (see Methods).

Download figureOpen in new tab
Fig. 4.
Broad encoding of airflow variables across the columnar input pathway to the FB.

A. PFNa calcium activity in response to five directions of stimulus presentation; positive directions indicate stimuli ipsilateral to each PB half; negative directions indicate contralateral presentation. Traces represent mean ±SEM across flies for each PB half (N=9 flies, 3-4 trials per fly).

B. Direction tuning curves for PFNa (colored traces, shading is ±SEM) for airflow (left), optic flow (middle), and the coherent stimuli (right). Data are means of the response during the entire 10-s stimulus period.

C. Speed tuning curves for PFNa vs. PFNp_c (shading is ±SEM) for airflow (left), optic flow (middle), and coherent stimuli (right).PFNa data are means of the response during the entire stimulus period; PFNp_c data are means of the response transients (1st second of the stimulus).

D. LCNOpm neuropil anatomy. Box around noduli indicates imaging region. Inset: single volumetric (mean z-projection) frame of imaging from noduli in LCNOpm. Left and right noduli ROIs indicated in yellow.

E. Mean calcium activity in left and right noduli, combined across noduli, to three stimulus speeds delivered from 0° (N=8 flies, 2-4 trials per fly). Traces represent mean ±SEM across flies.

F. Mean calcium activity in left and right LCNOpm noduli to five directions of stimulus presentation at middle speed (45 cm/s airflow, N=4 flies, 2-4 trials per fly). Traces represent mean ±SEM across flies.

G. LCNOp neuropil anatomy. Box around noduli indicates imaging region.

H. Mean calcium activity in left and right noduli to three stimulus speeds delivered from 0° (N=8 flies, 2-4 trials per fly). Traces represent mean ±SEM across flies.

I. Mean calcium activity in left and right LCNOp noduli to five directions of stimulus presentation at middle speed (45 cm/s airflow, N=8 flies, 2-4 trials per fly). Traces represent mean ±SEM across flies.

Download figureOpen in new tab
Fig. 5.
PFNs remain active during flight but do not encode flight maneuvers in tethered flies.

A. Paradigm for recording flight behavior during 2-photon imaging. Microphones positioned behind each wing measure left and right wingbeat amplitude and frequency.

B. Representative calcium activity in PB columns of PFNd (upper), PFNp_c (middle), and PFNa (lower). For each calcium data plot, the recorded flight state (see Methods) for the trial is plotted below.

C. Mean calcium activity around the onset of flight for each PFN type. All flight bouts of 4 or more seconds long were included. Black vertical lines at time 0 indicate the start of the flight bout. Traces are means across all bouts, shading indicates ±SEM (n=41 bouts across 33 trials in 7 PFNd flies, n=28 bouts across 22 trials in 8 PFNp_c flies, n=17 bouts across 14 trials in 6 PFNa flies).

D. Mean calcium activity around left or right turns for each PFN type (see Methods). n=31 left and 16 right turns across 16 trials in 7 flies for PFNd; n=14 left and 3 right turns across 8 trials in 5 flies for PFNp_c; n=22 left and 9 right turns across 13 trials in 6 flies for PFNa. Data drawn from same set as C.

Download figureOpen in new tab
Fig. 6.
A dynamic multisensory encoding model for PFNs.

A. (left) Example of a real active flight maneuver (32) that generates dynamically varying egocentric optic flow and airflow experience. (right) Dynamic vector coding model of PFN responses in which dynamic sensory experience is encoded by time-varying amplitudes of left and right PFN signals while bump position tracks heading as modeled previously (24, 28, 31).

B. Direction tuning for optic flow or airflow was fit to a cosine function for unimodal response data for each genotype. Left and middle panels show tuning curves for PFNd (reproduced from Fig. 2E) in colored traces with overlaid fits in black dashed lines. Right panel shows direction tuning curves in PFNp_c with modulation by airspeed in grey dashed lines.

C. Response dynamics for each modality were fit with an exponential decay (for airflow) or rise (for optic flow). Left panels show mean PFNd response to ipsilateral 45° airflow (upper) or optic flow (lower, reproduced from Fig. 2D). Right panels show modeled response dynamics (see Methods).

D. Real (top, colored traces, reproduced from Fig. 2D) and modeled (black) responses fit to single-modality stimuli from five directions in PFNd. MSE between model and data shown below each pair of traces.

E. Real (top, colored traces, reproduced from Fig. 3C) and modeled (black) responses fit to single - modality stimuli at three speeds in PFNp_c. MSE shown below each pair of traces.

F. Real (top, colored traces, reproduced from Fig. 2D) and predicted model (black) responses to coherent multimodal stimuli in PFNd. MSE between model and data shown below each pair of traces.

G. Real (top, colored traces, reproduced from Fig. 2D) and predicted model (black) responses to divergent multimodal stimuli in PFNd. MSE between model and data shown below each pair of traces.

H. Real (top, colored traces) and predicted model (black) responses to multimodal “slip” stimuli. In the left panel, the coherent stimuli are presented statically from 0° during the entire 20-sec stimulus period. In the middle panel, the coherent stimuli are presented from 0° for 10 sec, and then slipped sideways to present from contralateral 45° for 10 sec. In the right panel, the coherent stimuli are presented from 0° for 10 sec, and then slipped to ipsilateral 45° for 10 sec. MSE between model and data shown below each pair of traces.

I. Box plots of MSE for PFNd mean response to each modality (dots) per fly, relative to model output. MSEs for predicted responses to multimodal stimuli (coherent, divergent, and slip) are not significantly different (p = 0.0639, one-way ANOVA; ns by Tukey’s multiple comparisons test) from MSEs for stimuli used to fit the model (OF, AF). (Data has n=10 flies, as in Figure 2D).

Airflow speed and direction encoding in PFNp_c

We next examined sensory encoding in PFNp_c neurons (Fig. 3A), a cell type previously shown to encode airflow direction (27). We observed that PFNp_c neurons responded strongly and transiently to airflow, with strongly increasing responses as a function of airspeed (Fig. 3B, C). PFNp_c responses to airflow were more transient than those of PFNd, with activity falling below baseline within 5-8 seconds of stimulus onset, and a robust offset response often following the end of the airflow stimulus (Fig. 3C). Speed tuning in PFNp_c was more robust than in PFNd (Fig. 3D), while optic flow responses were essentially absent (Fig. 3B, C, E).

In addition to airspeed tuning, PFNp_c neurons also showed airflow direction tuning (Fig. 3E). Direction tuning magnitude was comparable to PFNd (Fig. 3F), but with a positive offset, with even the least-preferred direction (45° contralateral) producing a significant transient response. Bump structure was much less obvious in PFNp_c (Fig. 3B, G) and we did not observe any consistent bump movement with airflow (Supp. Fig. 2A). This might reflect weaker input from the EPG compass system to PFNp_c compared to PFNd (Fig. 3H).

Download figureOpen in new tab
Fig. S2 related to Fig. 3.
PFNp_c does not exhibit bump movement to any stimulus.

A. Mean PFNp_c bump phase across PB columns over time, normalized to phase immediately before stimulus onset for all data. Negative directions indicate stimuli coming from fly’s egocentric left. Traces are circular means; shading is ±circular standard deviation. N=7 flies, 2-4 trials per fly, same dataset as Figure 3E

Other PFN types likely encode diverse representations of airflow speed and direction

The fly brain contains eight additional types of PFNs (33). Of these, PFNv was previously shown to encode optic flow (24) but not airflow (27) direction and we did not examine it further here. One other type, PFNa, can be precisely targeted using genetic driver lines and was previously shown to strongly encode airflow direction (27, 28). Imaging from PFNa revealed a bimodal tuning curve with a small transient peak at 45° ipsilateral and a larger, more persistent response at 90° contralateral (Fig. 4A, B). These results are consistent with a recent study showing that hyperpolarization of PFNa drives large calcium responses mediated by T-type Ca2+ channels (28). We observed no response to optic flow and little tuning for airflow speed in PFNa (Fig. 4B, C). We did observe strong PFNa bump structure (Supp. Fig. 3A), as expected from its compass inputs (Fig. 3H).

Download figureOpen in new tab
Fig. S3 related to Fig. 4.
Additional data on airflow tuning in PFNa and LNO neurons

A. (left) Example single trial calcium activity in PFNa to 45 cm/s airflow from 90° to the fly’s right. (right) Mean bump structure in PFNa (light gray), PFNp_c (dark gray) and PFNd (black). Column 1 is plotted twice (once on either side). Data are means across all trials ±SEM.

B. Speed tuning curves (mean ±SEM of the LCNOpm response during the 10-s stimulus period). Same data as Figure 4E.

C. Direction tuning curves (mean ±SEM of the LCNOpm response during the 10-s stimulus period). Same data as Figure 4F.

D. Mean pixel intensity values of LCNOpm in the NO regions (following mean-z-projection and motion correction; see Methods) minus the mean motion-corrected pixel intensity value of a non-fluorescent background region. Note the nearness of the raw pixel values to zero intensity during the stimulus. Stimulus occurred from 10-20 s.

E. Speed tuning curves (mean ±SEM of the LCNOp calcium response during the 10-s stimulus period). Same data as Figure 4H.

F. Direction tuning curves (mean ±SEM of the LCNOp calcium response during the 10-s stimulus period). Same data as Figure 4I.

The remaining six types of PFNs cannot currently be accessed with specific genetic lines (35). To obtain insight into what these neurons might encode, we imaged from their upstream partners in the NO, called LCNOpm and LCNOp (Fig. 4D-I). Like other LAL-NO neurons, these are predicted to be glutamatergic and inhibitory (24, 27, 31, 36); we thus expect them to have inverted tuning to their downstream PFN partners, whose sensory tuning would arise through disinhibition.

LCNOpm provides input to the six PFN types in addition to PFNp_c, while LCNOp provides input to four types, a subset of those that receive input from LCNOpm (excluding PFNp_c, Fig. 4D, G) (33, 37). Imaging from a specific LCNOpm line (Fig. 4D-F; Supp. Fig. 3B-D) revealed inhibition in response to airflow, similar to observations in the neuron LNOa that provides input to PFNa (27). The duration of inhibition grew between slow and medium airspeeds, but saturated at the highest airspeed, perhaps reflecting a floor effect from our imaging (Supp. Fig. 3D). These neurons were most strongly inhibited by airflow coming from directly in front of the fly. They were also transiently activated by ipsilateral airflow (Fig. 4F; Supp. Fig. 3C). LCNOp was weakly inhibited by airflow and showed prominent offset responses to airflow that grew with airflow speed (Fig. 4H, I). We observed no significant responses to optic flow in either LCNOpm or LCNOp (Fig. 4E, F, H, I; Supp. Fig. 3B, C, E, F). Our imaging from these two LNO neurons suggests that the additional PFN types we are unable to record likely also encode combinations of airspeed and airflow direction.

PFNs are active during tethered flight but do not encode turning maneuvers

In addition to airflow and optic flow, PFNs might encode self-motion through efference copy or proprioception during flight. Indeed, imaging results from walking flies suggest that they may receive proprioceptive input about self-motion (31). To examine encoding of flight maneuvers we imaged from tethered flying flies, and measured wing flapping behavior using two microphones positioned behind each wing (Fig. 5A). We observed that PFNd and PFNp_c showed increased activity during flight behavior, while PFNa activity remained robust but did not increase (Fig. 5B, C). Experience of frontal airflow minimally inhibited PFNd and PFNp_c activity during flight (Supp. Fig. 4A, B). We then asked whether flight turn information (perhaps through an efference copy) might also be represented in PFNs. To address this question, we detected fictive flight turns as differences between the two microphone signals that crossed a threshold (see Methods). We then plotted PFN activity associated with either left or right turns (Fig. 5D). We observed no significant signals related to fictive turns, arguing that efference copy of these maneuvers is not encoded by these PFNs, at least in tethered flight. We conclude that PFNs are active during flight, and likely encode primarily optic flow and airflow, as characterized here, and heading, as characterized previously (24, 31), although it remains possible that input from sensors active during real flight turns, such as halteres, could be encoded by these neurons (38).

Download figureOpen in new tab
Fig. S4 related to Fig. 5.
Airflow inhibits PFNd activity during flight.

A. Four closed-loop sensory conditions activated during flight: top left, no airflow or optic flow, only sun dot in closed loop; top right, sun dot in closed loop and airflow from 0° (front of the fly) only when fly is flying; bottom left, sun dot in closed loop and forward optic flow experience in closed loop with turning behavior and flight; bottom right, sun dot in closed loop with airflow from 0° and forward optic flow in closed loop with behavior.

B. Mean calcium activity in the PB in each of the three PFN types across the four conditions in A. Flight bout begins at time = 0 s (black vertical line). All flight bouts longer than 4 s were included. Traces are means across bouts ±SEM (n=37-64 bouts across 29-50 trials in 7-9 PFNd flies, n=23-38 bouts across 20-33 trials in 8-9 PFNp_c flies, n=17-54 bouts across 14-39 trials in 5-6 PFNa flies).

Generating and validating dynamic encoding models for PFNs

We hypothesize that the population of PFNs provides a compact multisensory representation of the fly’s movement through space that can be used to compute external variables such as the direction of ambient wind. To test this hypothesis, we next sought to develop a dynamic encoding model that would allow us to estimate PFN responses during real flight maneuvers, which are challenging to accurately replicate in head-fixed tethered flight because of their speed (39–42).

Previous studies (24, 31) have modeled the steady-state responses of PFNs as vectors, in which bump position represents a vector angle, and bump amplitude represents a vector length (Fig. 6A). Here we extended this framework to dynamically varying multisensory input, allowing us to simulate PFN representations to dynamic flight maneuvers. We focused our models on the three neuron types characterized here – PFNd, PFNp_c, and PFNa – and on PFNv, which has been well-characterized in other studies (24, 27, 31).

As in previous studies (24, 28, 31), we modeled PFN bump structure in half of the PB as a sinusoidal function in phase with heading (Fig. 6A, B). The amplitude of the bump in each hemisphere was modulated by the egocentric direction and magnitude of sensory input (optic flow and airflow, Fig. 6A). Direction tuning was specified by a cosine function peaking at ∼45° ipsilateral and fit to steady-state responses to optic flow and to transient responses to airflow (Fig. 6B). Speed tuning in PFNp_c was implemented by scaling this cosine by an exponential function of airspeed, and fitting to airflow response transients that varied in both speed and direction (PFNp_c, Fig. 6B; Supp. Fig. 5A, B). To extend this modeling framework to dynamic inputs, we fit exponential rises (for optic flow) or decays (for airflow) to the dynamic responses we observed in our imaging (Fig. 6C-E). We fit the same model framework to data for PFNd, PFNp_c, and PFNa (Supp. Fig. 5A-F), with modifications to capture bimodal tuning in PFNa (Supp. Fig. 5C, E; see Methods). The resulting models accurately capture the mean responses to single-modality stimulus presentation (Fig. 6D, E, I; Supp. Fig. 5A-C, G).

Download figureOpen in new tab
Fig. S5 related to Fig. 6.
Mean squared error for PFNp_c and PFNa timecourses, and for PFN tuning curves.

A. Real (top, colored traces, reproduced from Fig. 3E) and modeled (black) responses of PFNp_c to 5 directions of stimulus presentation. MSE between model and data shown below each pair of traces.

B. Real (top, colored traces, N = 8 flies, 2-4 trials per fly) and modeled (black) responses of PFNp_c to 5 directions of stimulus presentation at two speeds (20 cm/s and 60 cm/s). Colored traces are mean ±SEM, and black traces are the model outputs for each stimulus condition. MSE between model and data shown below each pair of traces.

C. Real (top, colored traces, reproduced from Fig. 4A) and modeled (black) responses of PFNa to 5 directions of stimulus presentation. MSE between model and data shown below each pair of traces.

D. PFNd direction tuning curves for individual flies during the first second of the stimulus period (colored traces) with model tuning curve overlaid in black.

E. Same as D, for PFNa airflow direction tuning.

F. Same as D, for PFNp_c airflow direction and airspeed tuning.

G. Box plots of MSE for PFNp_c mean response to each modality (dots) per fly, relative to model output. MSEs for predicted responses to multimodal stimuli (coherent, divergent, and slip) are not significantly different (p = 0.2505, one-way ANOVA; ns by Tukey’s multiple comparisons test) from MSEs for stimuli used to fit the model (OF, AF). (Data has n=7 flies, as in Figure 3E).

H. MSE of equal-weight sum of single-modality responses plus a fitted additional decay function (see Methods) vs. coherent data from slip experiment (same data as Figure 6H).

We next asked whether models fit to single-modality data could be used to accurately predict responses to multimodal input. Based on our observations in PFNd, we modeled responses to multimodal stimuli as a sum of the responses to optic flow and airflow alone (see Methods). We generated predicted responses for convergent stimuli (Fig. 6F), divergent stimuli (Fig. 6G), and for a series of “slip” experiments in which airflow and optic flow were dynamically and coherently shifted by 45° midway through stimulus presentation (Fig. 6H). Overall, we found that our linear model provided a good fit to multisensory responses, although real responses to convergent and divergent stimuli were somewhat more transient than the linear predictions, suggesting a greater weighting on airflow input or an additional decay (Fig. 6F-H). For slip stimuli, real responses were again more transient than prediction, particularly towards end of each stimulus, suggesting that the real neurons show an additional slow decay not captured by our model (Supp. Fig. 5H). To quantify goodness of fit, we computed the mean squared error (MSE) between the mean of individual fly data and the model response. Multimodal data showed no significant difference in mean MSE compared to the single modality data on which the model was fit (Fig. 6I; Supp. Fig. 5G).

Wind direction is observable from PFN activity during saccadic flight turns

Armed with our dynamic encoding model, we set out to ask whether the representation of self-motion in PFNs is sufficient to decode ambient wind direction in flight, as has previously been shown for raw sensor measurements (10, 11). We first simulated responses of the PFNs to the reconstructed sensory experience of real flight trajectories recorded in a wind tunnel (32). In these recordings, freely flying flies expressing CsChrimson in orco+ olfactory receptor neurons were subjected to a flash of red light, providing a fictive odor stimulus. As reported previously, fictive odor stimulation often led to two turns: a random-direction “anemometric” turn and deceleration in the first 50-100 ms that we hypothesize allows the fly to estimate wind direction, followed by an upwind “anemotactic” turn ∼100-150 ms later (Fig. 7A). Using our dynamic encoding model, we simulated the responses of four PFN types to real flight trajectories, providing a rich but compact neural representation of self-motion in wind (Fig. 7B, C). Note that for these simulations, we assumed that the fly’s heading was aligned with the direction of its movement (see Methods).

Download figureOpen in new tab
Fig. 7.
Wind direction during flight is observable from PFN representations.

A. Real horizontal trajectory of a freely flying fly in a laminar wind tunnel in response to fictive optogenetic odor (gold). Data from (32). The fly is initially oriented crosswind, then decelerates and makes a turn away from upwind in response to the fictive odor (anemometric turn, burgundy), and finally turns upwind shortly after (anemotactic turn, pink). Sample rate is 100 Hz.

B. Predicted heading, egocentric airflow, and egocentric optic flow experience during the trajectory in A (see Methods).

C. Predicted activity in four PFN types using the models fit in Fig. 6 and the inputs shown in B.

D. Heatmap of wind direction estimate error (square root of variance) as a function of initial heading direction and turn amplitude. Error computed from observability analysis of simulated 100-ms saccadic flight trajectories with 2.5 m/s2 forward deceleration (see Methods). White data points show headings and turn magnitudes of real flight trajectories from (32). Black outlined regions indicate parameters held constant for G-J.

E. Same as D but for simulated saccadic flight trajectories of turn amplitude 20°, varying across forward deceleration magnitudes.

F. Heatmap of wind direction estimate error as a function of forward deceleration and turn amplitude, all with initial heading at 90° and wind from 0°.

G. Effects of sensor dropout on wind direction estimate error for 60°-turn saccades with 2.5 m/s2 deceleration across various initial headings. Left: results using raw sensors, all PFNs (as in D,E,F), or removing single PFN types. Middle: effects of removing pairs of PFN types. Right: effects of removing any three PFNs, leaving one as the sole sensor set.

H. Same as J, but reporting observability from 60°-turn trajectories with initial heading 90°, varying across forward deceleration magnitude.

I. Effects of dropping heading, AF, or OF information on wind direction estimate error, varying across initial headings.

J. Same as L, but reporting observability from 60°-turn trajectories with initial heading 90°, varying across forward deceleration magnitude.

We next applied a nonlinear empirical observability analysis (10) to ask whether ambient wind direction can be decoded in principle from these PFN representations. Derived from Fisher information (43), observability can be used to determine what unknown information can be estimated from a set of sensory measurements (8, 44–46), including those that vary over time (10) (see Methods). Our observability analysis pipeline consisted of three steps. First, we simulated sensory variables available to a fly during 100-ms saccade-like turn trajectories with both deceleration and a sharp change in heading (Supp. Fig. 6A-C) using model predictive control (32, 47–49). These trajectories were defined by flight speed, flight direction, angular velocity, ambient wind direction, ambient wind speed, and altitude. From these, we produced time courses of the fly’s (global-coordinate) heading, egocentric airflow direction and speed, and egocentric optic flow direction and speed, and fed these five sensory experience variables into our PFN activity models. We note that optic flow speed is not encoded by PFNs in our data and so effectively disappears at this stage. We then use observability to compute a metric for the minimum possible reconstruction error variance for the wind direction, given a set of PFN neural responses as measurements (see Methods for specific details). A small error variance indicates that wind direction can be accurately decoded (more observable), whereas a large error variance means it cannot (less observable).

Download figureOpen in new tab
Fig. S6 related to Fig. 7.
Simulated anemometric turn parameters, and observability analysis using “raw” variable sensors.

A. Example simulated saccade-like trajectory with sequential deceleration and acceleration. The arrows represent position and heading (the pointed direction) at periodic timepoints in the trajectory.

B. Heading and travel (course) direction over time for the simulated trajectory in A.

C. Forward velocity for the simulated trajectory in A. In gray is the simulated fly’s intended velocity; in blue is the resulting velocity from model predictive control.

D. Wind direction estimate error using five raw variables (heading, optic flow direction, airflow direction, optic flow speed and airflow speed) during trajectories varying across intended turn amplitude and initial heading. Note that the wind direction estimation error is low for the trajectories with an intended turn angle of 0° because the direction of travel (course) was shifted away from heading due to the relaxed control parameters in the model predictive controller. All trajectories’ intended deceleration magnitude = 2.5 m/s2.

E. Same as D, but trajectories vary across intended forward deceleration magnitude and initial heading, all with an intended turn amplitude = 20°.

F. Same as D, but trajectories vary across turn amplitude and forward deceleration magnitude. All trajectories’ initial heading = 90°.

G. G-G’’: Example saccade-like trajectory, heading and course direction, and forward velocity over time with no intended deceleration component.

H. H-H’’: Example of a nominally straight-flight trajectory, heading and course direction, and forward velocity over time with no intended turn component.

I. Wind direction estimate error using PFN activity during trajectories with no intended deceleration, as in G-G’’.

J. As in I, but wind direction observability was calculated using the five raw variables (heading, optic flow direction, airflow direction, optic flow speed and airflow speed).

K. Wind direction estimate error using PFN activity for trajectories with no intended turn, as in H-H’’.

L. As in K, but wind direction observability was calculated using the five raw variables.

M. Example trajectory with no intended deceleration and no intended turn, but with more aggressive control values set such that wind cannot displace the simulated fly, leading to a better match between the intended and resulting trajectory.

N. Heading and course direction over time for the simulated trajectory in M.

O. Forward velocity for the simulated trajectory in M. The gray line is the simulated fly’s intended velocity; it completely overlaps the dashed blue line of the resulting velocity due to the higher control settings.

P. Wind direction estimate error using five raw variables and heightened control settings, from trajectories varying across intended turn amplitude and intended forward deceleration magnitude. All trajectories’ initial heading = 90°.

Q. Effect on wind direction observability with more aggressive control parameters such that the simulated travel direction is unaffected by wind (see Methods). All simulated trajectories varied across a range of initial headings, maintained constant forward velocity, and were of the indicated turn amplitude (60° or straight = 0°). Observability analysis uses the specified sensor set (raw variables or all PFNs).

R. Same as Q (90° initial heading and 0 or 60° intended turn angle), but with varying deceleration magnitude profiles.

Our analysis revealed that wind direction observability depends strongly on parameters of flight trajectories including initial heading, turn amplitude, and deceleration (Fig. 7D-F). We found that wind direction was observable (reconstruction error < ±45°) for most saccadic turns except for small turns (<∼30°) with decelerations that maintained forward motion (<∼6 m/s2) (Fig. 7D, E). Real measured active flight maneuvers (10) (white dots in Fig. 7D) fell well within the observable range, supporting the idea that active movements, combined with biological encoding of sensory feedback, are sufficient to decode the ambient wind direction under natural conditions. The pattern of observability dependence on active maneuvers was similar to what we found using raw sensors (Supp Fig. 6D-F), although the minimum error variance was larger using PFN representations. This suggests that, despite the biological noise and encoding dynamics, as well as the omission of optic flow information, the PFN representations are sufficient for a fly to reconstruct its sensory world.

Is a saccadic turn necessary for wind estimation? To address this question, we performed the same analysis on simulated flight maneuvers that lacked either the deceleration/acceleration component (Supp. Fig. 6G-I) or the turn component (Supp. Fig. 6J-L). We found that the turn component was valuable to the wind direction observability for trajectories with deceleration magnitudes that maintained forward motion; however, deceleration that led to backwards motion led to observable wind direction without a need for turning (Supp. Fig. 6H). We also found that the linear deceleration component contributed slightly to observability particularly for turn amplitudes <30° (Fig. 7F). The respective importance of these two components were also evident when raw sensory experience variables were used as sensors instead of the PFN representations (Supp. Fig. 6I, L). Thus, both deceleration and turning can contribute to the observability of ambient wind direction with biological sensory encoding. We note that, using raw sensors, wind direction is observable even with no active turn and no active deceleration (Supp Fig. 6F). This arises because the fly has imperfect control of its trajectory (see Methods), allowing the wind to influence travel direction. If we set the control variables “high” such that wind had essentially no effect on the trajectory, we find that active flight maneuvers are required to decode wind direction using either raw or PFN sensor sets (Supp. Fig. 6M-R). Because PFNs have more noise, and do not encode optic flow speed, larger active maneuvers are generally required for accurate wind decoding using PFN sensors.

Finally, we asked how different PFN types contribute to the observability of wind direction. We ran observability tests specifically for a saccade with turn amplitude of 60° because this is a smaller turn that produces good observability across all tested initial headings (Fig. 7D, horizontal box). We then asked how observability for this turn amplitude across initial headings (Fig. 7G) or across linear deceleration magnitudes (Fig. 7H) changes if one or more PFNs are removed from the array. We find that removing a single PFN type produces little change in the estimate error (Fig. 7G and H, left), likely because most information is redundantly represented across multiple PFN types. The exception is PFNp_c, which is the only PFN type that encodes airspeed in our model. Removing this PFN type from our model produced a more pronounced increase in estimation error compared to the other types.

Similarly, removing multiple PFN types had stronger effects (Fig. 7G and H, middle and right). In particular, removing both PFNd and PFNv, which are the only two PFNs that encode optic flow, produced a large increase in reconstruction error. These observations led us to ask what happens if other key parameters are removed from the representation. We ran a set of simulations in which bump position did not track heading – similar to what we expect if EPG neurons are silenced – in addition to a set of simulations in which all optic flow, or all airflow information is removed (Fig. 7I, J). We found that the loss of any of these inputs drastically increased the minimum possible error, well beyond any threshold for estimating the wind direction (> ±180°). Together, our results argue that the dynamics and integration of airflow and optic flow self-motion information in PFNs are sufficient to estimate wind direction in flight.

Discussion
A multisensory representation of self-motion in the columnar input pathway to the insect navigation center

To navigate through space, the brains of both vertebrates and invertebrates construct internal representations that allow them to generalize across sensory inputs and make spatial inferences (20, 50, 51). For example, the compass system of flies integrates both visual (52–54) and mechanosensory (34) cues about heading to produce an “abstract” representation of heading direction. This representation allows the fly to associate a particular direction with punishment (55) or a wind direction with visual landmarks (56). Similarly, place cells of the rodent hippocampus generate an abstract representation of space thought to allow the animal to navigate towards remembered locations based on distal cues (57–59). Abstract representations also emerge in artificial neural networks trained to perform spatial tasks (60, 61). What kinds of abstract internal representations each nervous system builds, and what computational function these representations serve are currently topics of intense research interest.

In vertebrates, several regions of the brain have been shown to integrate multisensory cues that signal self-motion. For example, neurons in cortical areas MSTd, VIP, and 7a integrate both optic flow and vestibular cues that signal translational self-motion (22, 62, 63). Single neurons can be tuned either to the same direction (congruent cells) or to opposing directions (opposite cells) (22). Population activity provides a good fit to the animal’s reported direction of self-motion (22). Multisensory input from these areas, especially 7a, are thought to provide indirect input to spatially tuned neurons in the retrosplenial cortex and medial entorhinal cortex (64, 65), which support allocentric computations of location in space (66), in part by integrating self-motion information (22, 67), but the precise pathways involved in this transformation are not known.

Here we show that the LNO-PFN pathway that provides input to the insect navigation center builds a compact multisensory representation of self-motion. In insects, optic flow is computed by T4/T5 neurons of the optic lobe (68, 69) and integrated by lobula plate tangential neurons (70) to produce representations of typical flight maneuvers (12). Mechanosensory neurons in the antenna, known as JONs, respond to antennal movement produced by both self-motion and ambient wind (71–74), and may function as a kind of vestibular system in some insect species (30). Airflow direction can be decoded from differential displacements of the two antennae (34, 71), and is likely carried to PFNs by a pathway involving the AMMC, WED, and LAL (27, 34). Strikingly, multisensory PFNs (PFNd) are tuned to optic flow and airflow signals from the same direction, 45° ipsilateral to the protocerebral bridge innervation of each neuron. Moreover, we find that the visual and mechanosensory responses of these neurons exhibit distinct time courses, consistent with the known sensitivity of each sensory system. Visual responses are slow and sustained, reflecting the slow but accurate nature of visual self-motion direction signals, while mechanosensory responses are fast and more transient, reflecting the more transient nature of mechanosensory cues about self-motion. We found that PFNd linearly combines multisensory direction information, regardless of the degree of coherence of the two stimuli. This suggests a role for PFNd activity in reflecting self-motion direction, even in the absence of one of the modalities, e.g. if the antennae were damaged or if the fly were flying in darkness.

To determine its location, an animal must keep track of movement speed as well as direction. Previous studies of speed coding in PFNs have yielded conflicting results. PFNd and v neurons did not show tuning for optic flow speed (24) but did show velocity tuning for walking (31). Here we measured optic flow and airflow speed tuning across multiple PFN and LNO types. We did not observe any tuning for optic flow speed, but did observe robust tuning for airflow speed in both PFNp_c and two LNO types: LCNOpm and LCNOp. Together these data suggest that mechanosensory cues (airflow and proprioception), rather than optic flow, might be used to estimate speed in the fly navigation center. Curiously, all of the speed-tuned responses we observed were transient, responding either to the onset or offset of airflow, or both. This suggests that these responses may encode airflow (or self-motion) acceleration. Acceleration-tuned neurons have been observed at many layers of the vertebrate vestibular system (75).

A limitation of our study is that there are currently six PFN types that cannot presently be individually targeted with genetic reagents. Imaging from the upstream partners of these neurons, called LNOs, revealed airflow speed and direction tuning, but no optic flow responses. It is therefore likely that some of these “dark PFNs” may encode other functions of airflow (or mechanosensory self-motion feedback). For example, they might encode these variables over different dynamic ranges or integrate them over different timescales. In addition, many of these PFNs may encode proprioceptive cues about self-motion. Although we did not observe encoding of turning maneuvers in tethered flight, natural flight strongly activates the halteres (76), which are known to provide input to the navigation center in other fly species (38). Activity related to walking has also been recorded in some PFNs (31). Future studies examining the integration of airflow and optic flow with proprioceptive information from the legs and halteres will allow us to understand how PFNs as a population encode self-motion.

PFN representations are sufficient to compute wind direction when combined with active sensing

What is the function of the multisensory representation in PFNs? One established function of optic flow-tuned neurons is to enable a transformation from egocentric to allocentric coordinates (24, 31). Airflow tuned PFNs (PFNa) have also been proposed to compute allocentric wind direction through a similar vector summation algorithm (28). However, these computations do not explicitly require multisensory integration. Here we propose a third possible function for the PFN representation: allowing the computation of ambient wind direction while in flight. Wind direction is an essential cue for flying flies (1, 32), similar to flow direction for fish (77, 78). Catching the wind can power dispersal over longer distances, while upwind and crosswind orientation facilitate different stages of olfactory navigation (79). In flight, self-generated movement and ambient wind sum together producing ambiguous visual and mechanosensory sensory feedback. However, olfactory navigation experiments argue that flies can estimate the wind direction in free flight, perhaps through rapid saccadic “anemometric” turns or decelerations (32). Mathematically, a flying fly can compute the ambient wind direction if it has access to sufficient angles or lengths of the wind triangle (8, 11). Here we showed that PFNs encode one angle and one length of this triangle: airflow and optic flow direction relative to the fly, and airflow speed (Figure 8). Notably, we observed little encoding of optic flow speed for our stimuli. This might reflect the fact that groundspeed is challenging to estimate accurately from optic flow speed (80, 81). A previous study in flies also observed little encoding of optic flow speed using starfield stimuli similar to ours (24), while a study in bees found optic flow speed encoding using grating stimuli in TN neurons (26), homologous to LNO neurons in fly. These differences might reflect differences between species, stimuli, or neurons targeted.

Download figureOpen in new tab
Fig. 8.
PFN encoding of self-motion variables during active flight maneuvers supports accurate estimation of wind direction.

At the first timepoint (‘t=1’), a fly is flying crosswind with a groundspeed g larger than windspeed w. Heading φ, airspeed a, airflow direction γ, and optic flow direction ψ are known, while g (and optic flow speed o) are unknown. Computing wind direction ζ therefore has many possible solutions (dashed lines with question marks denote possible wind vectors that satisfy the relationship between the known variables). By changing course direction with a turn and/or decelerating to obtain a second measurement of the known variables (‘t=2’), the PFN encoding is sufficient to resolve the correct ζ.

To test the sufficiency of PFN representations for decoding wind direction, we generated dynamic encoding models for four PFN types. Previous studies have developed a vector encoding model for PFN steady-state responses. Here we extended that approach to allow for encoding of dynamically changing multisensory input. To validate our model, we used it to predict responses to multisensory input that were not used to fit the model. Overall, we found that our model predicted responses to these stimuli well, although a slow decay was present in the real data that was not well-captured by our model. We then combined the output of our dynamic encoding model with a nonlinear observability analysis to determine whether this representation is sufficient to compute ambient wind direction. Although the PFN representation is inferior to raw sensor measurements, we found that it was sufficient to decode wind direction to within ±45° (i.e. quadrant accuracy), when combined with natural “anemometric” flight maneuvers. An advantage of this approach is that it lets us estimate the contribution of each PFN type to the wind direction estimate. Surprisingly, we found that few single PFN types had a strong impact on the observability of wind direction. This is because most of the variables needed to decode wind direction are redundantly represented across multiple PFN types. Our models make specific predictions about behavioral deficits that should arise when particular neuron types are silenced. Future experiments in which different PFN types are silenced during flight should allow us to directly test these predictions.

Although our computational analysis shows that PFNs could be used to compute ambient wind direction, it does not explain how this computation occurs. Our observability analysis suggests that estimation error depends heavily on initial heading relative to ambient wind direction. One possible reason for this is that crossing upwind or downwind significantly increases observability of wind direction; therefore, turns that begin near enough to these directions to align with upwind or downwind in the course of the turn will have lower estimate error. It is likely that the computation of ambient wind direction takes place within the numerous local neurons type of the fan-shaped body, known as hΔ and vΔ neurons(33, 37), and might involve a linear approximation of non-linear computations. Future studies of these neurons should allow us to determine whether and how PFNs are used to estimate this external force.

Materials and Methods
Fly husbandry

All flies (Drosophila melanogaster) were reared and maintained on standard cornmeal-agar media at 25°C, on a 12-hour light cycle (9 AM lights on or 1 PM lights on for experimental flies imaged in the afternoon). Experimental flies were mated adult females 6-12 days post-eclosion at the time of imaging; these were sorted into culture vials using CO2 anesthesia at least five days prior to imaging.

Fly stocks

Genotypes used in each figure were as follows:

View inlineView popup
 
Imaging Preparation

Flies were briefly cold-anesthetized before mounting on a custom-made imaging chamber. For open-loop experiments, the chamber was a thin steel foil molded into a dish and affixed to a 3D-printed frame (Clear Resin) with a hexagonal hole for the fly’s head and thorax. For all flight experiments, a separate chamber was 3D-printed with opaque Gray Resin V4 (FormLabs) on a Form3+ 3D printer. While the fly was anesthetized, the two most distal segments of all six legs were removed and the fly was glued to the chamber using UV-cured glue applied around the head and to two points on the thorax. The head and thorax were angled such that the posterior head cuticle was easily accessible through the chamber window. The proboscis was then gently extended using forceps and fixed at the base using the UV glue, so that the labella were free to open and the fly could be fed and watered while mounted. The fly was allowed to recover for at least 30 minutes before the cuticle was dissected away from the head to expose the posterior side of the brain in a bath of artificial hemolymph (AHL: 103 mM NaCl, 3 mM KCl, 5 mM TES, 8 mM trehalose dihydrate, 10 mM glucose, 26 mM NaHCO3, 1 mM NaH2PO4H2O, 1.5 mM CaCl22H2O, and 4 mM MgCl26H2O, pH 7.1-7.4, osmolarity 270-274 mOsm), bubbled with carbogen (5% CO2, 95% O2).

Calcium Imaging

To image, each paired structure (protocerebral bridge halves or noduli) was centered in the field of view. The imaging area for the protocerebral bridge ranged from 137.73 x 68.86 μm to 164.10 x 123.07 μm, and the imaging area for the noduli ranged from 74.11 x 49.41 μm to 84.67 x 56.45 μm. Volumes were taken in depth to record the full structures, at a range of 20-32 μm thick and at a rate of 2.6-4.3 volumes per second. Genetically expressed fluorophores (GCaMP7f (82) and tdTomato ) were simultaneously excited with a pulsed 2-photon laser (Spectra-Physics MaiTai HP) with wavelength 920 nm. Emitted photons were separated by wavelength using a dichroic mirror and bandpass filters (Semrock, FF01-525/50-32 for green and FF01-607/70-32 for red) and collected by GaAsP PMTs. For all open-loop experiments, we used a 20x Olympus water-immersion objective (XLUMPLFLN) with working distance 2.0 mm. For all simultaneous behavior and imaging experiments (Fig. 4 and Fig. S4), we used a 40x Nikon water-immersion objective (CFI APO NIR) with working distance 3.5 mm. Intensity at the sample was 20-55 mW using the 20x objective, and 10-35 mW using the 40x objective.

Sensory Stimuli

To present airflow to the fly, we used a rotary union apparatus (83) to deliver charcoal-filtered air at a flow rate of 0.2, 0.45 or 0.6 L/min, corresponding to 20, 45, and 60 cm/s. Flow rate was set by a mass flow controller (Aalborg, GFC17 0-2 L/min). Airspeeds were confirmed using a filament anemometer from Dantec Dynamics (model: 9055P0161).

Translational optic flow stimuli were generated using custom Python code and projected onto a 2.75-mm-thick flat, plastic screen 6.5 cm in front of the fly using a DLP 4500EVM and a single flat mirror (3 mm thick) angled 45° relative to the screen. The stimulus filled approximately 90 azimuthal degrees and 60 vertical degrees of the fly’s frontal visual field. The projector framerate was consistently 178-180 Hz, measured by photodiode (ThorLabs, PBM42), and the visual experience was updated at a rate of 50 Hz. To reduce imaging confounds from the blue visual stimulus, we installed a narrow bandpass filter permitting only blue light (Semrock BrightLine FF01-470/28-25) and a neutral density absorptive filter (Thorlabs, NE04B) into the path of the light coming from the projector.

Using the Panda3D package (84), blue virtual spheres subtending up to 23° (at the sphere’s closest virtual distance to the fly) of the fly’s visual field randomly populated a black virtual space around the fly. During the optic flow stimulus, the fly’s virtual position in the space was moved in the direction specified without changing its heading direction. While spheres were generated in a large virtual space, for the duration of each trial only those spheres between 5 and 60 units virtual distance in depth from the fly at each timepoint were displayed. To match the optic flow rates to the airflow speeds, we calculate that one virtual distance unit equals 3 cm in real space.

For slip experiments, the optic flow direction was simultaneously slipped at the same speed as the airflow. However, the optic flow stimulus code for the slip data did not utilize a 3D virtual space populated with spheres; instead, it merely produced a dot expansion stimulus from an origin point on-screen. When slipped, this generated a change in yaw in addition to a change in translational travel direction, as it slipped the origin of expansion to the right or left. This artifact was corrected in the 3D virtual space code used in all other experiments reported in this manuscript. In the same experiments, the airflow stimuli were “slipped” 45° to the fly’s right or left at a rate of approximately 93.75°/s, starting at the beginning of the 11th second of the 20-second stimulus.

For simultaneous recording of behavior and calcium activity, the optic flow stimulus populated only the lower half/third of the region of the fly’s field of view subtended by the visual stimulus screen, producing a horizon-like visual effect. The upper half of the visual stimulus screen contained a “sun dot”, a larger sphere (subtending approximately 10° of the fly’s field of view) that moved laterally with changes in heading but was always the same size on the screen as it maintained a constant 40-unit virtual distance from the fly.

Flight Behavior Recording

For simultaneous recording of flight behavior and neuronal calcium, the custom imaging chamber was modified to permit the fly’s wings to flap in flight and to mount two lavalier microphones (Audio-Technica, CAT#AT899) posterior to and on either side of the fly.

After mounting and after cuticle dissection to expose the brain, the flies were fed a small amount of sucrose diluted in water, via a Kimwipe soaked in the solution touched to their proboscis, to supply them with energy. Flies that did not drink the solution or were otherwise lethargic were not imaged.

Once the flies were mounted beneath the 2-p objective, the microphones were placed in their holders below and behind the fly, their distances relative to the fly were balanced, and the threshold signal for flight behavior detection was adjusted during the first 2-10 trials during which flight behavior (wing flapping) was encouraged. Flight was elicited by briefly puffing air from behind the fly through a tube fed through the light-protective box around the imaging setup, such that the flies could be encouraged to fly/flap wings while imaging was ongoing. During these initial habituation/testing trials we delivered both frontal airflow and closed-loop optic flow feedback to the fly when it started flying (Supp. Fig. 4A). Flies that did not fly in these first trials were not further imaged, and their data were not included in final analysis.

Behavior and imaging data were recorded in 30-s trials, with one of four randomized sensory feedback conditions triggered by wing flapping as recorded by the microphones (Supp. Fig. 4A). Sensory feedback started when wing flapping was detected and ended when wing flapping ceased. The four conditions included: airflow from the front of the fly (0°), closed-loop optic flow, both frontal airflow and closed-loop optic flow, and neither sensory experience. For all four conditions, a sun dot was presented 5 virtual units to the left or right of center at the beginning of the trial and moved with the fly’s changes in heading (see details in Sensory Stimuli methods).

Imaging Data Analysis

Imaging volumes were first processed by computing the mean z projection to generate single frames of data through time. A NoRMCorre rigid motion correction (85) was then performed on the red (tdTomato) channel and the same shifts were applied to the green (GCaMP) channel.

Following motion correction, ROIs were drawn by hand in ImageJ/FIJI using the tdTomato/red signal channel. For the protocerebral bridge, one region was drawn around each PB half, then each half was subdivided by hand into eight columnar regions of similar area. For nodulus recordings, one ROI was drawn around each nodulus (left and right). Each two-dimensional ROI was then converted to a mean pixel intensity value at every timepoint, and the intensity time series of a background region was subtracted from the time series for each ROI to correct both for motion in the z-axis and for signal bleed-through from the visual stimulus.

Depending on the analysis, two separate baselines were used to calculate ΔF/F in each columnar ROI. One baseline, F0, was computed as the mean activity in the ROI within the two seconds leading up to the onset of an open-loop stimulus. This was used to measure the change in signal amplitude across the PB hemisphere due to the stimulus. ΔF/F0 was then computed as the difference in fluorescence at every timepoint from F0, divided by F0.

The other baseline, F5, was used to visualize bump position within columns over time. F5 was calculated as the mean of the lowest five percent of the column ROIs’ intensity values over the course of an entire experiment. As with ΔF/F0, ΔF/F5 was computed as the difference in fluorescence at every timepoint from F5, divided by F5. These values were then convolved with a 5x7 (time x column) gaussian filter with circular padding (imgaussfilt, MATLAB). To compute protocerebral bridge bump position at every timepoint, ΔF/F5 for all column ROIs at every timepoint were fit to a sinusoid and the phase was recorded as the columnar position of the sinusoid’s maximum.

To compute bump structure in Fig. 3G and Supp. Fig. 4A, we took the mean fluorescent activity (ΔF/F5) across the columns in the first stimulus frame of every trial, with fluorescent maxima aligned to column 5.

Connectome Data

Connectome data in Fig. 3I was obtained from the hemibrain connectome (v1.2.1, http://neuprint.janelia.org/, (37)). Synaptic weights were calculated by summing the total number of synapses between all neurons the two cell types (for all connections >3 synapses), then dividing by the number of neurons in the PFN population, for a per-PFN-neuron synaptic weight.

Behavioral Data Analysis

To detect flight behavior and flight turns from microphone data, we recorded audio at a rate of 1000 Hz and normalized this signal to have zero mean every 10 samples. Flight state was detected online if the sum of the absolute value of normalized signal of the past 30 microphone samples was above threshold for the fly for either microphone. Turns were detected by comparing the envelopes of the signal from the right and left microphones every 10 samples.

Flight behavior was analyzed post-hoc by filtering the normalized microphone data using a bandpass butterworth filter passing harmonics of wing flapping in the frequency range 320-500 Hz, filtering out signal in the band 80-180 Hz (range of noise at and below the frequency of wing flapping) A full spectrogram of the unfiltered microphone data from initial trials was used to identify the 320-500 Hz band as clean harmonic frequency bands for wing flapping. Flight bouts were extracted using the flight state computed online during experiment, and then matched to both the filtered microphone data and neuronal data frames. Turn bouts shown in Figure 5D were extracted post-hoc by setting threshold of virtual angular velocity (100°/s) computed during behavior for the closed-loop experience (see above) and selecting the data from -2:4 s around the instant the threshold was exceeded.

Modeling
Dynamic encoding model for PFNs

Our dynamic encoding models extend previously established vector models of PFN bump activity (24, 31) to capture the temporal dynamics, speed tuning, and multisensory integration we describe in this manuscript. Bump position in PFNd, PFNa, and PFNv was modeled as a sinusoid that moves in the opposite circular direction to the animal’s heading, as shown and modeled previously (). The amplitude of left and right bumps was then modulated by egocentric airflow and optic flow experience according to the equations described below. Models for each modality were fit separately to unimodal data, then combined and tested against multi-modal data.

To model egocentric encoding of optic flow direction, we fit a cosine direction tuning curve to the the steady-state amplitude of the responses to the five directions of optic flow:
where 𝐴 is the maximal response , 𝜃$is the preferred stimulus direction, and 𝑏 is an offset. All fitting was performed using MATLAB’s built-in nonlinear iterative least-squares regression function (nlinfit, MATLAB 2020b).

To model egocentric encoding of airflow direction, we fit Eq. 1 to the average amplitude of the airflow response transients across airflow directions in each PFN type. For PFNa, we augmented this direction tuning curve to have two peaks (as we see in our data and as reported in(28)) with a square of cosine term, and with a sum of cosines to produce different peak amplitudes:
To model airspeed tuning in PFNp_c, we multiplied the direction tuning curve by a saturating exponential function that depended on airspeed and fit this function to the mean amplitude of the airflow response transient to each airflow speed and direction (Supp. Fig. 5A,B).
where 𝑠 is airspeed in m/s and 𝑔 is a gain term.

The temporal dynamics of airflow and optic flow responses were described by a single exponential rise (for optic flow) or fall (for airflow). With fixed parameters for direction- and speed-tuning (𝑦/)), we fit the remaining parameters to the mean response over time to the stimulus from all directions at all speeds.
To generate responses to dynamic flight trajectory inputs, we formulated these models as difference equations for each PFN type with the basic form:
For all simulations, the initial conditions of the PFN responses were assumed to be the steady-state response to the sensory inputs at the first time-step of the simulation.

To capture the multisensory integration strategy in PFNd, we implemented an equal-weight summation of the responses to single-modality stimuli over time. To test the model’s performance, we compared it to actual multisensory responses, which were not used for fitting, by calculating the mean squared error (MSE) between the mean of the multisensory data and the model output over time.

We examined the effect of unequal weighting of the airflow and optic flow response in Supp. Fig. 1 using MATLAB’s fitlm function and fitting a two-term linear function to the coherent and divergent PFNd response data:
where α is the airflow response weight and β is the optic flow response weight. To compute the additional decay component in Supp. Fig. 5H, we subtracted the equal-weight summation model of coherent activity from the 20-s static coherent response recorded in the stimulus-direction-slip experiment, then fit the parameters of a decay function to the result using MATLAB’s nlinfit:
where A is the amplitude, g is a gain term and β is the offset term.

All modeling code was implemented first in MATLAB, then translated into Python for integration with code for model predictive control (47) and observability.

Wind Direction Observability Analysis

To gauge the capability of the PFN system to estimate the wind direction, we applied an observability analysis. Observability is a concept that describes how difficult a given variable is to estimate, given a set of sensors, or measurements, over time. As applied to our problem, we asked if the ambient wind direction could be inferred from the PFN encodings of heading angle, optic flow direction, and apparent airflow speed and direction.

We employed an established dynamical model of fly flight in the presence of ambient wind that defines the geometric relationship between the state vector 𝐱, which includes the ambient wind vector and a fly’s self-motion variables (heading, ground speed, etc.), and the corresponding sensor measurement vector 𝐲, which includes heading, optic flow, and apparent airflow (10, 11). We then appended our fit PFN encoding models to the sensor dynamics in this model such that a new measurement vector 𝐲!"#was defined as a function of the original measurements 𝐲<=> = 𝑓<=>(𝐲), where 𝑓<=> defined our fit PFN encoding models. This allowed us to analyze an arbitrary flight trajectory and simulate the corresponding PFN responses over time. We used model predictive control (MPC) to precisely drive our model along desired trajectories (9, 47).

To evaluate the observability of wind direction, we constructed the observability matrix (𝒪) and Fisher information matrix (ℱ) in sliding windows along each flight trajectory as in the pybounds python package(10). In brief, we empirically computed 𝒪 in each sliding window using our simulation model by applying a small positive and negative perturbation 𝜀 to each initial state variable  and simulating the corresponding change in the measurements 𝛥𝐲 = 𝐲8 − 𝒚+ over time:
where 𝑛 is the number of states, and 𝑤 is size of the sliding time-window, and 𝜀 = 10+B (9). In plain language, 𝒪 encodes the sensitivity of the model measurements to small change in the initial state and can tell us if each state can be reconstructed from the given measurements.

To compute a quantitative metric for observability, we constructed the Fisher information matrix (ℱ). In general terms, ℱ provides information about how much a set of random variables 𝑌 provides about a set of parameters 𝑋. As applied to our dynamical model, 𝑌 is defined by our measurements and 𝑋 is defined by our states. While ℱ is typically estimated directly from data (86), we construct it from 𝒪 while also considering the presumed noise covariance of measurements. ℱ can then be used to compute a quantitative metric for observability given. ℱ is defined as
where ℛ sets the measurement noise covariance matrix (9, 43).

We set ℛ = 0.1𝐈D×D where 𝐈D×D is the identity matrix of size 𝑘 equal to the number of rows in 𝒪. The Cramér–Rao bound states that the inverse of ℱ is a lower bound on an unbiased estimator’s error variance (87, 88). In simple terms, the inverse ℱ+9 provides information about how well a given state could be used in units of variance, e.g. radians squared for the wind direction state. Thus ℱ+9 yields a quantitative metric for observability, where small values correspond to high observability (low error variance) and large values correspond to low observability (high error variance). In practice, ℱ was often uninvertible, thus we employed a regularized Chernov inverse
where we set 𝜆 = 10+I. The diagonal elements of ℱ+9 correspond to the minimum error variance for each state variable, respectively. We report the observability of the wind direction throughout as the square root of the minimum error variance for the wind direction state variable pulled from ℱ+9.

Trajectory simulations

In Fig. 7D, all 100-ms simulated trajectories were saccade-like, characterized by a sigmoidal change in heading angle (all in the same direction, towards the fly’s left) and an inverted parabolic change in linear velocity (2.5 m/s2 deceleration into the peak of the turn, and equivalent acceleration after the turn) (Supp. Fig. 6A-C). In Fig. 7E, all trajectories shared the same turn amplitude (20°) but varied across deceleration magnitude. In Fig. 7F, all turns were executed with an initial heading of 90° clockwise rotation away from upwind.

Nearly all trajectories in the paper were simulated using model predictive control input penalties of 0.05 on forward velocity and 0.1 on lateral velocity, producing offsets for trajectory parameters due to wind (e.g., Supp. Fig. 6C-C’). In the Fig. 7G-H and Supp. Fig. 6D’’’-E’’’ “High Control” plots, control penalties were each lowered to 1×10-7. By decreasing the penalty, we increased the simulated fly’s control of its travel, reducing the effect of wind.

In Fig. 7I-J, information (both bump position and half-PB calcium amplitude) from the indicated PFN types were removed from the sensor set used in generating the observability matrix. In Fig. 7K-L, all indicated modality information in all the PFN types was removed from the PFN activity models such that their bump position and calcium intensity outputs would not reflect any of that modality’s inputs.

Funding

Leon Levy Scholarship in Neuroscience (C.E.M.)

National Science Foundation Postdoctoral Fellowship in Biology (B.C.)

National Institutes of Health grant R01NS136988 (F.v.B.)

National Institutes of Health grant R01DC107979 (K.I.N.) National Institutes of Health grant R01NS127129 (K.I.N.)

Author Contributions

Conceptualization: C.E.M., B.C., F.v.B., K.I.N.

Methodology: C.E.M., B.C., F.v.B., K.I.N.

Investigation: C.E.M. Visualization: C.E.M. Supervision: F.v.B., K.I.N.

Writing— original draft: C.E.M., K.I.N.

Writing—review and editing: C.E.M., B.C., F.v.B., K.I.N.

Competing Interests

All authors declare they have no competing interests.

Data and materials availability

All data collected in this manuscript will be made publicly available on Zenodo upon publication. All code (encoding model and observability) as well as CAD files for fly holders is available at Github at https://github.com/nagellab/Mayetal2025.

Acknowledgements

The authors thank David Schoppik, David Schneider, and Dora Angelaki for input on the project.

FUNDER INFORMATION DECLARED
National Institutes of Health, https://ror.org/01cwqze88, R01NS127129, R01DC107979, R01NS136988
National Science Foundation, https://ror.org/021nxhr62, NSF 22-623
References
1.↵ J. S. Kennedy, D. Marsh, Pheromone-regulated anemotaxis in flying moths. Science (1979) 184, 999–1001 (1974).Abstract/FREE Full TextGoogle Scholar
2. W. J. Bell, E. Kramer, Search and anemotactic orientation of cockroaches. J. Insect Physiol. 25, 631–640 (1979).CrossRefWeb of ScienceGoogle Scholar
3. H. Wolf, R. Wehner, Pinpointing food sources: olfactory and anemotactic orientation in desert ants, Cataglyphis fortis. J. Exp. Biol. 203, 857–868 (2000).AbstractGoogle Scholar
4. F. Van Breugel, M. H. Dickinson, Plume-tracking behavior of flying Drosophila emerges from a set of distinct sensory-motor reflexes. Curr. Biol. 24, 274–286 (2014).CrossRefPubMedGoogle Scholar
5.↵ E. Álvarez-Salvado, A. M. Licata, E. G. Connor, M. K. McHugh, B. M. N. King, N. Stavropoulos, J. D. Victor, J. P. Crimaldi, K. I. Nagel, Elementary sensory-motor transformations underlying olfactory navigation in walking fruit-flies. Elife 7 (2018).Google Scholar
6.↵ E. von Holst, H. Mittelstaedt, Das Reafferenzprinzip - Wechselwirkungen zwischen Zentralnervensystem und Peripherie. Naturwissenschaften 37, 464–476 (1950).CrossRefGoogle Scholar
7.↵ K. E. Cullen, L. B. Minor, Semicircular canal afferents similarly encode active and passive head-on-body rotations: implications for the role of vestibular efference. J. Neurosci. 22, RC226 (2002).FREE Full TextGoogle Scholar
8.↵ F. Van Breugel, A nonlinear observability analysis of ambient wind estimation with uncalibrated sensors, inspired by insect neural encoding. Proc. IEEE Conf. Decis. Control 2021-December, 1399–1406 (2021).Google Scholar
9.↵ B. Cellini, B. Boyacioǧlu, F. Van Breugel, Empirical individual state observability. Institute of Electrical and Electronics Engineers Inc. [Preprint] (2023). doi:10.1109/cdc49753.2023.10383812.CrossRefGoogle Scholar
10.↵ B. Cellini, B. Boyacioǧlu, S. David Stupski, F. Van Breugel, Discovering and exploiting active sensing motifs for estimation with empirical observability. bioRxiv, 2024.11.04.621976 (2024).Google Scholar
11.↵ F. Van Breugel, R. Jewell, J. Houle, Active anemosensing hypothesis: how flying insects could estimate ambient wind direction through sensory integration and active movement. J R Soc Interface 19 (2022).Google Scholar
12.↵ H. G. Krapp, R. Hengstenberg, Estimation of self-motion by optic flow processing in single visual interneurons. Nature 384, 463–466 (1996).CrossRefPubMedWeb of ScienceGoogle Scholar
13.↵ M. Lappe, F. Bremmer, A. V. Van Den Berg, Perception of self-motion from visual flow. Trends Cogn Sci 3, 329–336 (1999).CrossRefPubMedWeb of ScienceGoogle Scholar
14.↵ F. Hlavačka, T. Mergner, G. Schweigart, Interaction of vestibular and proprioceptive inputs for human self-motion perception. Neurosci Lett 138, 161–164 (1992).CrossRefPubMedWeb of ScienceGoogle Scholar
15.↵ J. Dichgans, T. Brandt, Visual-Vestibular Interaction: Effects on Self-Motion Perception and Postural Control. Perception, 755–804 (1978).Google Scholar
16.↵ J. P. Noel, D. E. Angelaki, Cognitive, Systems, and Computational Neurosciences of the Self in Motion. Annu Rev Psychol 73, 103–129 (2022).CrossRefPubMedGoogle Scholar
17.↵ K. E. Cullen, Vestibular processing during natural self-motion: implications for perception and action. Nat. Rev. Neurosci. 20, 346–363 (2019).CrossRefPubMedGoogle Scholar
18.↵ N. H. Barmack, H. Shojaku, Vestibular and visual climbing fiber signals evoked in the uvula-nodulus of the rabbit cerebellum by natural stimulation. doi:10.1152/jn.1995.74.6.2573 74, 2573–2589 (1995).CrossRefPubMedWeb of ScienceGoogle Scholar
19. K. Maekawa, J. I. Simpson, Climbing fiber responses evoked in vestibulocerebellum of rabbit from visual system. J Neurophysiol 36, 649–666 (1973).CrossRefPubMedWeb of ScienceGoogle Scholar
20.↵ K. E. Cullen, Internal models of self-motion: neural computations by the vestibular cerebellum. Trends Neurosci 46, 986–1002 (2023).CrossRefPubMedGoogle Scholar
21.↵ A. Chen, G. C. DeAngelis, D. E. Angelaki, Representation of Vestibular and Visual Cues to Self-Motion in Ventral Intraparietal Cortex. Journal of Neuroscience 31, 12036–12052 (2011).Abstract/FREE Full TextGoogle Scholar
22.↵ Y. Gu, D. E. Angelaki, G. C. DeAngelis, Neural correlates of multisensory cue integration in macaque MSTd. Nat Neurosci 11, 1201–1210 (2008).CrossRefPubMedWeb of ScienceGoogle Scholar
23.↵ C. R. Fetsch, A. Pouget, G. C. Deangelis, D. E. Angelaki, Neural correlates of reliability-based cue weighting during multisensory integration. Nat Neurosci 15, 146–154 (2012).CrossRefPubMedGoogle Scholar
24.↵ C. Lyu, L. F. Abbott, G. Maimon, Building an allocentric travelling direction signal via vector computation. Nature 601, 92–97 (2022).CrossRefPubMedGoogle Scholar
25. P. T. Weir, M. H. Dickinson, Functional divisions for visual processing in the central brain of flying Drosophila. Proc Natl Acad Sci U S A 112, E5523–E5532 (2015).Abstract/FREE Full TextGoogle Scholar
26.↵ T. Stone, B. Webb, A. Adden, N. Ben Weddig, A. Honkanen, R. Templin, W. Wcislo, L. Scimeca, E. Warrant, S. Heinze, An Anatomically Constrained Model for Path Integration in the Bee Brain. Current Biology 27, 3069–3085.e11 (2017).CrossRefPubMedGoogle Scholar
27.↵ T. A. Currier, A. M. M. Matheson, K. I. Nagel, Encoding and control of orientation to airflow by a set of Drosophila fan-shaped body neurons. Elife 9, 1–29 (2020).CrossRefPubMedGoogle Scholar
28.↵ I. G. Ishida, S. Sethi, T. L. Mohren, L. F. Abbott, G. Maimon, Neuronal calcium spikes enable vector inversion in the Drosophila brain. bioRxiv, doi: 10.1101/2023.11.24.568537 (2023).Abstract/FREE Full TextGoogle Scholar
29.↵ L. Polat, T. Harpaz, A. Zaidel, Rats rely on airflow cues for self-motion perception. Current Biology 34, 4248–4260.e5 (2024).CrossRefPubMedGoogle Scholar
30.↵ S. P. Sane, A. Dieudonné, M. A. Willis, T. L. Daniel, Antennal mechanosensors mediate flight control in moths. Science 1979 315, 863–866 (2007).Abstract/FREE Full TextGoogle Scholar
31.↵ J. Lu, A. H. Behbahani, L. Hamburg, E. A. Westeinde, P. M. Dawson, C. Lyu, G. Maimon, M. H. Dickinson, S. Druckmann, R. I. Wilson, Transforming representations of movement from body-to world-centric space. Nature 601, 98–104 (2022).CrossRefPubMedGoogle Scholar
32.↵ S. D. Stupski, F. van Breugel, Wind gates olfaction-driven search states in free flight. Current Biology 34, 4397–4411.e6 (2024).CrossRefPubMedGoogle Scholar
33.↵ B. K. Hulse, H. Haberkern, R. Franconville, D. B. Turner-Evans, S. Y. Takemura, T. Wolff, M. Noorman, M. Dreher, C. Dan, R. Parekh, A. M. Hermundstad, G. M. Rubin, V. Jayaraman, A connectome of the Drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection. Elife 10, e66039 (2021).CrossRefPubMedGoogle Scholar
34.↵ T. S. Okubo, P. Patella, I. D’Alessandro, R. I. Wilson, A neural network for wind-guided compass navigation. Neuron 107, 924–940 (2020).CrossRefPubMedGoogle Scholar
35.↵ T. Wolff, M. Eddison, N. Chen, A. Nern, P. Sundaramurthi, D. Sitaraman, G. M. Rubin, Cell type-specific driver lines targeting the Drosophila central complex and their use to investigate neuropeptide expression and sleep regulation. bioRxiv, 2024.10.21.619448 (2024).Google Scholar
36.↵ N. Eckstein, A. S. Bates, A. Champion, M. Du, Y. Yin, P. Schlegel, A. K. Y. Lu, T. Rymer, S. Finley-May, T. Paterson, R. Parekh, S. Dorkenwald, A. Matsliah, S. C. Yu, C. McKellar, A. Sterling, K. Eichler, M. Costa, S. Seung, M. Murthy, V. Hartenstein, G. S. X. E. Jefferis, J. Funke, Neurotransmitter classification from electron microscopy images at synaptic sites in Drosophila melanogaster. Cell 187, 2574–2594.e23 (2024).CrossRefPubMedGoogle Scholar
37.↵ L. K. Scheffer, C. S. Xu, M. Januszewski, Z. Lu, S. Y. Takemura, K. J. Hayworth, G. B. Huang, K. Shinomiya, J. Maitin-Shepard, S. Berg, J. Clements, P. M. Hubbard, W. T. Katz, L. Umayam, T. Zhao, D. Ackerman, T. Blakely, J. Bogovic, T. Dolafi, D. Kainmueller, T. Kawase, K. A. Khairy, L. Leavitt, P. H. Li, L. Lindsey, N. Neubarth, D. J. Olbris, H. Otsuna, E. T. Trautman, M. Ito, A. S. Bates, J. Goldammer, T. Wolff, R. Svirskas, P. Schlegel, E. R. Neace, C. J. Knecht, C. X. Alvarado, D. A. Bailey, S. Ballinger, J. A. Borycz, B. S. Canino, N. Cheatham, M. Cook, M. Dreher, O. Duclos, B. Eubanks, K. Fairbanks, S. Finley, N. Forknall, A. Francis, G. P. Hopkins, E. M. Joyce, S. Kim, N. A. Kirk, J. Kovalyak, S. A. Lauchie, A. Lohff, C. Maldonado, E. A. Manley, S. McLin, C. Mooney, M. Ndama, O. Ogundeyi, N. Okeoma, C. Ordish, N. Padilla, C. Patrick, T. Paterson, E. E. Phillips, E. M. Phillips, N. Rampally, C. Ribeiro, M. K. Robertson, J. T. Rymer, S. M. Ryan, M. Sammons, A. K. Scott, A. L. Scott, A. Shinomiya, C. Smith, K. Smith, N. L. Smith, M. A. Sobeski, A. Suleiman, J. Swift, S. Takemura, I. Talebi, D. Tarnogorska, E. Tenshaw, T. Tokhi, J. J. Walsh, T. Yang, J. A. Horne, F. Li, R. Parekh, P. K. Rivlin, V. Jayaraman, M. Costa, G. S. X. E. Jefferis, K. Ito, S. Saalfeld, R. George, I. A. Meinertzhagen, G. M. Rubin, H. F. Hess, V. Jain, S. M. Plaza, A connectome and analysis of the adult Drosophila central brain. Elife 9, e57443 (2020).CrossRefPubMedGoogle Scholar
38.↵ N. D. Kathman, J. L. Fox, Representation of Haltere Oscillations and Integration with Visual Inputs in the Fly Central Complex. Journal of Neuroscience 39, 4100–4112 (2019).Abstract/FREE Full TextGoogle Scholar
39.↵ F. T. Muijres, M. J. Elzinga, N. A. Iwasaki, M. H. Dickinson, Body saccades of Drosophila consist of stereotyped banked turns. Journal of Experimental Biology 218, 864–875 (2015).Abstract/FREE Full TextGoogle Scholar
40. B. Cellini, J. M. Mongeau, Hybrid visual control in fly flight: insights into gaze shift via saccades. Curr Opin Insect Sci 42, 23–31 (2020).CrossRefPubMedGoogle Scholar
41. B. Schnell, I. G. Ros, M. H. Dickinson, A Descending Neuron Correlated with the Rapid Steering Maneuvers of Flying Drosophila. Current Biology 27, 1200–1205 (2017).CrossRefPubMedGoogle Scholar
42.↵ I. G. Ros, J. J. Omoto, M. H. Dickinson, Descending control and regulation of spontaneous flight turns in Drosophila. Curr. Biol. 34, 531–540.e5 (2024).CrossRefPubMedGoogle Scholar
43.↵ B. Boyacioǧlu, F. Van Breugel, DUALITY OF STOCHASTIC OBSERVABILITY AND CONSTRUCTABILITY AND LINKS TO FISHER INFORMATION A PREPRINT. (2025).Google Scholar
44.↵ A. K. Singh, J. Hahn, On the use of empirical gramians for controllability and observability analysis. Proceedings of the American Control Conference 1, 140–141 (2005).CrossRefGoogle Scholar
45. C. Jauffret, Observability and Fisher information matrix in nonlinear regression. IEEE Trans Aerosp Electron Syst 43, 756–759 (2007).CrossRefGoogle Scholar
46.↵ A. J. Krener, K. Ide, Measures of unobservability. Proceedings of the IEEE Conference on Decision and Control, 6401–6406 (2009).Google Scholar
47.↵ F. Fiedler, B. Karg, L. Lüken, D. Brandner, M. Heinlein, F. Brabender, S. Lucia, do-mpc: Towards FAIR nonlinear and robust model predictive control. Control Eng Pract 140 (2023).Google Scholar
48. C. Schilstra, J. H. Van Hateren, Blowfly flight and optic flow. I. Thorax kinematics and flight dynamics. Journal of Experimental Biology 202, 1481–1490 (1999).Abstract/FREE Full TextGoogle Scholar
49.↵ L. F. Tammero, M. H. Dickinson, The influence of visual landscape on the free flight behavior of the fruit fly Drosophila melanogaster. Journal of Experimental Biology 205, 327–343 (2002).Abstract/FREE Full TextGoogle Scholar
50.↵ J. Laurens, H. Meng, D. E. Angelaki, Computation of linear acceleration through an internal model in the macaque cerebellum. Nat Neurosci 16, 1701–1708 (2013).CrossRefPubMedGoogle Scholar
51.↵ M. Collett, How navigational guidance systems are combined in a desert ant. Current Biology 22, 927–932 (2012).CrossRefPubMedGoogle Scholar
52.↵ S. S. Kim, A. M. Hermundstad, S. Romani, L. F. Abbott, V. Jayaraman, Generation of stable heading representations in diverse visual scenes. Nature 576, 126–131 (2019).CrossRefPubMedGoogle Scholar
53. Y. E. Fisher, J. Lu, I. D’Alessandro, R. I. Wilson, Sensorimotor experience remaps visual input to a heading-direction network. Nature 2019 576:7785 576, 121–125 (2019).CrossRefPubMedGoogle Scholar
54.↵ Y. Sun, A. Nern, R. Franconville, H. Dana, E. R. Schreiter, L. L. Looger, K. Svoboda, D. S. Kim, A. M. Hermundstad, V. Jayaraman, Neural signatures of dynamic stimulus selection in Drosophila. Nature Neuroscience 2017 20:8 20, 1104–1113 (2017).CrossRefPubMedGoogle Scholar
55.↵ C. Dan, B. K. Hulse, R. Kappagantula, V. Jayaraman, A. M. Hermundstad, A neural circuit architecture for rapid learning in goal-directed navigation. Neuron 112, 2581–2599.e23 (2024).CrossRefPubMedGoogle Scholar
56.↵ P. Mussells Pires, L. Zhang, V. Parache, L. F. Abbott, G. Maimon, Converting an allocentric goal into an egocentric steering signal. Nature 626, 808–818 (2024).CrossRefPubMedGoogle Scholar
57.↵ J. Ormond, J. O’Keefe, Hippocampal place cells have goal-oriented vector fields during navigation. Nature 2022 607:7920 607, 741–746 (2022).CrossRefPubMedGoogle Scholar
58. R. G. M. Morris, P. Garrud, J. N. P. Rawlins, J. O’Keefe, Place navigation impaired in rats with hippocampal lesions. Nature 297, 681–683 (1982).CrossRefPubMedWeb of ScienceGoogle Scholar
59.↵ J. O’Keefe, J. Dostrovsky, The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. Brain Res 34, 171–175 (1971).CrossRefPubMedWeb of ScienceGoogle Scholar
60.↵ S. H. Singh, F. van Breugel, R. P. N. Rao, B. W. Brunton, Emergent behaviour and neural dynamics in artificial agents tracking odour plumes. Nature Machine Intelligence 2023 5:1 5, 58–70 (2023).CrossRefPubMedGoogle Scholar
61.↵ S. Vijayabaskaran, S. Cheng, Navigation task and action space drive the emergence of egocentric and allocentric spatial representations. PLoS Comput Biol 18, e1010320 (2022).CrossRefPubMedGoogle Scholar
62.↵ R. A. Andersen, Multimodal integration for the representation of space in the posterior parietal cortex. Philos Trans R Soc Lond B Biol Sci 352, 1421–1428 (1997).CrossRefPubMedWeb of ScienceGoogle Scholar
63.↵ E. Avila, K. J. Lakshminarasimhan, G. C. Deangelis, D. E. Angelaki, Visual and Vestibular Selectivity for Self-Motion in Macaque Posterior Parietal Area 7a. Cereb Cortex 29, 3932–3947 (2019).CrossRefPubMedGoogle Scholar
64.↵ E. T. Rolls, Spatial coordinate transforms linking the allocentric hippocampal and egocentric parietal primate brain systems for memory, action in space, and navigation. Hippocampus 30, 332–353 (2020).CrossRefPubMedGoogle Scholar
65.↵ Y. Kobayashi, D. G. Amaral, Macaque monkey retrosplenial cortex: II. Cortical afferents. Journal of Comparative Neurology 466, 48–79 (2003).CrossRefPubMedWeb of ScienceGoogle Scholar
66.↵ T. Hafting, M. Fyhn, S. Molden, M. B. Moser, E. I. Moser, Microstructure of a spatial map in the entorhinal cortex. Nature 2005 436:7052 436, 801–806 (2005).CrossRefPubMedWeb of ScienceGoogle Scholar
67.↵ M. S. Madhav, R. P. Jayakumar, B. Y. Li, S. G. Lashkari, K. Wright, F. Savelli, J. J. Knierim, N. J. Cowan, Control and recalibration of path integration in place cells using optic flow. Nature Neuroscience 2024 27:8 27, 1599–1608 (2024).CrossRefPubMedGoogle Scholar
68.↵ M. S. Maisak, J. Haag, G. Ammer, E. Serbe, M. Meier, A. Leonhardt, T. Schilling, A. Bahl, G. M. Rubin, A. Nern, B. J. Dickson, D. F. Reiff, E. Hopp, A. Borst, A directional tuning map of Drosophila elementary motion detectors. Nature 500, 212–216 (2013).CrossRefPubMedWeb of ScienceGoogle Scholar
69.↵ B. Schnell, S. V. Raghu, A. Nern, A. Borst, Columnar cells necessary for motion responses of wide-field visual interneurons in Drosophila. J Comp Physiol A Neuroethol Sens Neural Behav Physiol 198, 389–395 (2012).CrossRefPubMedGoogle Scholar
70.↵ K. Shinomiya, A. Nern, I. A. Meinertzhagen, S. M. Plaza, M. B. Reiser, Neuronal circuits integrating visual motion information in Drosophila melanogaster. Curr Biol 32, 3529–3544.e2 (2022).CrossRefPubMedGoogle Scholar
71.↵ M. P. Suver, A. M. M. Matheson, S. Sarkar, M. Damiata, D. Schoppik, K. I. Nagel, Encoding of Wind Direction by Central Neurons in Drosophila. Neuron 102, 828–842.e7 (2019).CrossRefPubMedGoogle Scholar
72. M. P. Suver, A. M. Medina, K. I. Nagel, Active antennal movements in Drosophila can tune wind encoding. Current Biology 33, 780–789.e4 (2023).CrossRefPubMedGoogle Scholar
73. A. Kamikouchi, H. K. Inagaki, T. Effertz, O. Hendrich, A. Fiala, M. C. Göpfert, K. Ito, The neural basis of Drosophila gravity-sensing and hearing. Nature 2009 458:7235 458, 165–171 (2009).CrossRefPubMedWeb of ScienceGoogle Scholar
74.↵ S. Yorozu, A. Wong, B. J. Fischer, H. Dankert, M. J. Kernan, A. Kamikouchi, K. Ito, D. J. Anderson, Distinct sensory representations of wind and near-field sound in the Drosophila brain. Nature 458, 201–205 (2009).CrossRefPubMedWeb of ScienceGoogle Scholar
75.↵ K. E. Cullen, J. S. Taube, Our sense of direction: progress, controversies and challenges. Nature Neuroscience 2017 20:11 20, 1465–1473 (2017).CrossRefPubMedGoogle Scholar
76.↵ J. L. Fox, A. L. Fairhall, T. L. Daniel, Encoding properties of haltere neurons enable motion feature detection in a biological gyroscope. Proc Natl Acad Sci U S A 107, 3840–3845 (2010).Abstract/FREE Full TextGoogle Scholar
77.↵ P. Oteiza, I. Odstrcil, G. Lauder, R. Portugues, F. Engert, A novel mechanism for mechanosensory-based rheotaxis in larval zebrafish. Nature 547, 445–448 (2017).CrossRefPubMedGoogle Scholar
78.↵ G. Valera, D. A. Markov, K. Bijari, O. Randlett, A. Asgharsharghi, J. P. Baudoin, G. A. Ascoli, R. Portugues, H. López-Schier, A neuronal blueprint for directional mechanosensation in larval zebrafish. Current Biology 31, 1463–1475.e6 (2021).CrossRefPubMedGoogle Scholar
79.↵ K. J. Leitch, F. V. Ponce, W. B. Dickson, F. Van Breugel, M. H. Dickinson, The long-distance flight behavior of Drosophila supports an agent-based model for wind-assisted dispersal in insects. Proc. Natl Acad. Sci. USA 118, e2013342118 (2021).Abstract/FREE Full TextGoogle Scholar
80.↵ F. Van Breugel, K. Morgansen, M. H. Dickinson, Monocular distance estimation from optic flow during active landing maneuvers. Bioinspir. Biomim. 9 (2014).Google Scholar
81.↵ B. Lingenfelter, A. Nag, F. Van Breugel, Insect inspired vision-based velocity estimation through spatial pooling of optic flow during linear motion. Bioinspir. Biomim. 16, 66004 (2021).CrossRefGoogle Scholar
82.↵ H. Dana, Y. Sun, B. Mohar, B. K. Hulse, A. M. Kerlin, J. P. Hasseman, G. Tsegaye, A. Tsang, A. Wong, R. Patel, J. J. Macklin, Y. Chen, A. Konnerth, V. Jayaraman, L. L. Looger, E. R. Schreiter, K. Svoboda, D. S. Kim, High-performance calcium sensors for imaging activity in neuronal populations and microcompartments. Nature Methods 2019 16:7 16, 649–657 (2019).CrossRefPubMedGoogle Scholar
83.↵83. N. D. Kathman, A. J. Lanz, J. D. Freed, K. I. Nagel, Neural dynamics for working memory and evidence integration during olfactory navigation in Drosophila. bioRxiv, 2024.10.05.616803 (2024).Google Scholar
84.↵ M. Goslin, M. R. Mine, The Panda3D graphics engine. Computer (Long Beach Calif) 37, 112– 114 (2004).Google Scholar
85.↵ E. A. Pnevmatikakis, A. Giovannucci, NoRMCorre: an online algorithm for piecewise rigid motion correction of calcium imaging data. J. Neurosci. Methods 291, 83–94 (2017).CrossRefPubMedGoogle Scholar
86.↵ I. Kanitscheider, R. Coen-Cagli, A. Kohn, A. Pouget, Measuring Fisher Information Accurately in Correlated Neural Populations. PLoS Comput Biol 11 (2015).Google Scholar
87.↵ C. R. Rao, Information and the Accuracy Attainable in the Estimation of Statistical Parameters. 235–247 (1946).Google Scholar
88.↵ H. Cramér, Mathematical Methods of Statistics (PMS-9). Mathematical Methods of Statistics (PMS-9), doi: 10.1515/9781400883868/HTML (1946).CrossRefGoogle Scholar
 Back to top
 Previous
Next 
Posted May 09, 2025.
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

2

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
Materials and Methods
Funding
Author Contributions
Competing Interests
Data and materials availability
Acknowledgements