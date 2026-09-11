# PFL outputs toward descending neurons (MaleCNS v1.0, full graph)

Script: [scripts/pfl_descending_trace.py](../scripts/pfl_descending_trace.py) (requires `pyarrow`; run with `.venv/bin/python`). Tables: `data/derived/pfl_outputs_hop1.csv` (every postsynaptic body of PFL1/2/3, with L/R split and the PFL share of that body's total input), `pfl_outputs_hop2_to_dn.csv` (first-hop targets that synapse onto descending neurons), `pfl_trace_summary.json`. Raw graph streamed twice; date 2026-09-10.

## Caveat first

64 % of PFL3 output weight and 78 % of PFL2 output weight go to bodies with no type annotation (35 k and 14 k such bodies). These are mostly small segments in the confidence-0.5 export, not curated neurons; some lack annotation rows entirely. Everything below concerns typed targets only, so shares "of PFL output" are not quoted; shares of the target's total input are.

## First hop

**PFL3 (24 cells).** Largest typed targets: LAL121 (2 cells, glutamatergic, 2,671 synapses, 37 % of each cell's total input), AOTU042 and AOTU019 (GABAergic, 5 % and 3 %), VES054 (cholinergic, 21 %), LAL126, LAL083, LAL040, LAL141, CRE041, PFL3 itself (853), LAL076, FB5A, then the descending neurons DNb01 (753, 5 % of input) and DNa02 (736, 1.5 % of input). PFL3→DNa03 is 468 (1.4 %).

**PFL3 output is strictly contralateral at cell level.** Left PFL3 → right DNa02 (380 vs 0), right PFL3 → left DNa02 (356 vs 0); the same holds for LAL121, LAL126, LAL083, AOTU019, DNb01, LAL076 and LAL122. This is the anatomical basis of the "left PFL3 drives right turns" sign convention used by Westeinde 2024 and Mussells Pires 2024, now seen for every major PFL3 target.

**PFL2 (12 cells).** Largest typed targets: DNa03 (1,571 synapses, 4.5 % of each DNa03's input), LAL076 (glutamatergic, 22 %), LAL073, FB5A, PFL2 itself, LAL090, LoVC11 and LoVC9 (GABAergic visual centrifugal cells), LAL127, LAL120_b, LAL014. Unlike PFL3, PFL2 input to each target is bilateral (e.g. DNa03 L: 386 from left PFL2, 444 from right), consistent with PFL2 carrying a non-lateralised error-magnitude signal (Westeinde 2024).

**PFL1 (14 cells)** targets LAL047, LAL048, LAL087, LAL086 (42–59 % of their input, GABA/glutamate), WED082, FB2B, AOTU037; no direct descending targets of note.

**Absent links.** LAL013 receives ≤ 5 synapses from all PFLs combined, and DNa11 receives 7. Feng 2024's top steering layer (DNa03/LAL013) and saccade layer (DNa11) are therefore not direct PFL targets; PFL2 reaches DNa03 directly and PFL3 reaches DNa03 weakly, but LAL013 and DNa11 must be reached through intermediates.

## Second hop (first-hop targets → descending neurons)

Strongest routes with ≥ 50 PFL synapses into the intermediate: LAL126 → DNg04 (1,212), DNae001 (765), DNa02 (634), DNa16 (626), DNa15 (526); LAL083 → DNa15 (905), DNa02 (669), DNg04 (667), DNa13 (652); LAL014, LAL121, LAL122 → DNa03 (878, 751, 727); AOTU019 → DNa15 (792), DNa13 (720), DNa02 (586), DNg04 (547); PS010 → DNb09 (640); VES041 → DNa03 (611); DNa03 → DNa13 (577) and DNa02 (552). Routes into DNa11 are many but individually tiny (≤ 2 synapses each from PFL-recipient cells).

So the PFL3 signal reaches DNa02 both directly and through LAL126, LAL083 and AOTU019, and reaches DNa03 through LAL121, LAL014 and LAL122; PFL2 reaches DNa03 directly. DNa02 and DNa03 also talk to each other and to DNa13.

## What this changes in the circuit picture

- The PFL3 → DNa02 edge that the steering papers rely on is real but small on DNa02's side (1.5 % of its input); the larger PFL3 output goes to LAL interneurons, several inhibitory, that themselves target DNa02/DNa03/DNa15/DNg04. Steering commands are therefore likely shaped in the LAL before reaching descending neurons, as Rayshubskiy 2020 and Feng 2024 proposed.
- LAL013's winner-take-all loop with DNa03 (Feng 2024) sits downstream of PFL2→DNa03, not of PFL3; how PFL3's lateralised signal enters that loop is an open question (candidates: LAL121, LAL014, LAL122).
- Direct PFL→DN edges cannot by themselves specify turn direction; sign depends on transmitter (LAL121 and LAL076 are predicted glutamatergic, AOTU019/042 GABAergic) and on the VNC targets of each DN, which this brain-only graph does not contain.
