# Stern et al. (2019): trial-and-error learning of an unmarked rewarded location

[Published article](https://doi.org/10.1016/j.cub.2019.06.045) · [Full text (condensed methods)](cell-fulltext.md) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

Individual male flies learn, within tens of minutes, to re-enter a software-defined circle where each entry (from outside) triggers a 250 ms optogenetic pulse to 0273-GAL4 neurons, a driver whose activation is more attractive than sucrose or acetic acid and includes PAM dopamine neurons plus cholinergic neurons. Reward index rises relative to yoked controls (same genotype, same pulses, no contingency) and persists into a no-reward post-session. Blind (norpA) flies learn as well as sighted flies in the "regular" arena, which has agarose strips and a floor hole; learning falls in flat-floor arenas, more so for blind flies. Naïve flies do not prefer a location just used by experienced flies, arguing against scent marking in this arena (Chen 2024, the follow-up, reaches the opposite conclusion in a smaller featureless arena).

Circuit dissection: DR1 and D2R mutants, TH-RNAi in 0273 neurons, and removing CsChrimson from all DA/5-HT neurons reduce learning; removing it from the R58E02 PAM subset does not. Removing CsChrimson from cholinergic 0273 neurons reduces both learning and light seeking, suggesting a cholinergic drive-to-seek pathway and a dopaminergic association pathway. Hydroxyurea MB ablation and reward-locked GtACR1 inhibition of Kenyon cells reduce learning, more in blind flies; inhibition of R38G08 ring neurons reduces learning only in sighted flies. rut and dnc are dispensable.

## Why it matters for the synthesis

This is a destination-learning behavior with an explicit yoked control and a clear dissociation between MB (non-visual) and ring-neuron/CX (visual) contributions. It does not identify what is stored. The authors' speculation (locations as direction/distance relative to landmarks stored in CX/MB) remains untested, and they note that some individuals may use spatially agnostic motor strategies.

## Methods to remember

- SkinnerTrax: 16 cameras at 7.5 fps, whole-arena LED illumination, reward on circle entry only.
- Reward index = (rewarded-circle entries − control-circle entries)/total, in 10-min sync buckets from the first reward; buckets with < 10 entries excluded.
- GtACR1 experiments use green light that simultaneously activates CsChrimson; controls confirm 0273>GtACR1 flies avoid green light and 0273>CsChrimson flies are attracted.

## Caveats

- 0273-GAL4 is broad; the "reward" is a composite of cholinergic seeking and dopaminergic association, not a defined reinforcement signal.
- Arena features (agarose, hole) are uncontrolled cues; the flat-floor deficit shows they are used.
- Only males tested.

## Remaining questions

1. What is the CX contribution mechanistically: ring-neuron visual anchoring of the compass (Fisher 2019, Plitt 2025) or something else?
2. How does this reward-site learning relate to path-integration search (Kim 2017) and to the scent-marking strategy Chen 2024 finds in featureless chambers?
