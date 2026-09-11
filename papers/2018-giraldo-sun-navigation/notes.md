# Giraldo, Leitch, Ros, Warren, Weir & Dickinson (2018): sun navigation requires compass neurons

[Published article](https://doi.org/10.1016/j.cub.2018.07.002) · [PMC author-manuscript HTML](pmc-fulltext.html) · [Figures](figures/) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

The flight counterpart of Green et al. (2019): tethered flying flies hold arbitrary, individual-specific headings relative to a small bright "sun" spot, retain that heading across gaps of up to six hours, and lose the ability when E-PG output is blocked with Kir2.1. Imaging shows the E-PG bump tracks the sun with an arbitrary offset that is preserved across flights and across a switch from sun to stripe. This is strong evidence that (a) a maintained bearing is an internal variable, not a stripe-fixation reflex, (b) it is stored across hours, and (c) the compass is necessary for expressing it.

It does not identify where the bearing is stored (not in E-PG offset: the bump–sun offset is stable while the chosen heading is arbitrary), how it is chosen, or how it is compared with heading. Those are the FC2/PFL3 questions addressed later by Green 2019, Mussells Pires 2024 and Westeinde 2024.

## Figure 1: arbitrary sun headings that persist

Tethered flight with a 2.4°-diameter green "sun" or a 15°-wide stripe in closed loop with wingbeat difference; 5 min (sun) or 1 min (stripe) flights. Flies distribute headings around the full circle for the sun but fixate the stripe frontally. Paired sun flights separated by 5 min, 1 h, 2 h or 6 h are correlated; mean absolute heading difference is below bootstrapped chance at every interval (p = 0.000, 0.011, 0.002, 0.029). Two models are compared: a time-compensated compass (heading shifts with sun ephemeris) and a fixed-menotaxis model (heading unchanged). The fixed model fits better at 6 h (p = 0.020); no evidence for time compensation at shorter intervals.

Inspection of Figure 1F shows the correlation is real but loose at long intervals: many points sit well off the identity line, and the plotted headings include both individual variability and a strong front-biased subpopulation. The claim is population-level persistence, not a demonstration that every fly returns to its exact bearing.

## Figure 2: E-PG bump tracks the sun with a stable offset

Two-photon imaging of E-PG axons in the bridge during flight. Bump position follows sun position with a per-fly offset; that offset is unchanged between the first and second sun flight (Figure 2J) and, strikingly, is the same for sun and stripe in most flies (Figure 2K, with a few outliers near ±180°). The offset is unrelated to the fly's chosen sun heading (Figure 2I). Headings during imaging are more front-biased than in the behavior rig, presumably because of the reduced 180° arena and the imaging preparation.

## Figure 3: compass neurons are required

Kir2.1 in three E-PG split-GAL4 lines (SS00096, SS00408, SS00131) collapses the heading distribution toward frontal sun fixation (variance significantly lower than bootstrapped controls, p = 0.000, 0.000, 0.011), while the stripe response is unaffected. This is interpreted as loss of arbitrary heading selection with retention of a direct visual fixation reflex; the same dissociation appears in Green 2019 (walking) and Turner-Evans 2020.

## Caveats for synthesis

- Persistence is inferred from paired flights, not continuous tracking; the memory could be regenerated from a stable internal state or from a preferred motor bias.
- The offset stability across sun and stripe presumes the fly treats both as the same landmark; a switch to a truly different scene (Kim 2019) can remap.
- Kir2.1 is chronic; developmental effects cannot be excluded.
- The 6-h result rejects one specific time-compensation model with equinox-like assumptions.

## Remaining questions

1. Where is the bearing stored over hours? Weisman 2025 extends persistence to days; Mussells Pires 2024 shows FC2 expresses a goal on minute timescales. Hours-long storage substrate remains open.
2. How does a fly choose its bearing initially? Dan 2024 (prestructured policy with a shiftable goal) offers a framework.
3. Does the sun/stripe offset conservation generalize to natural skies with polarization (Hardcastle 2021, Garner 2024)?
