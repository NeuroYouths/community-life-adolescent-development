# CLAD — Research Questions (the spine)

Canonical scientific index for the study. Each research question maps to an analysis
(`code/analyses/<x>/`), its outputs (`data/derivatives/<x>/`), and a `graph/` publication node.
Cohort: **N=141**, waves 1–4, ages ~11→21 (NIJ 2016-R2-CX-0019; ADS/CLAD).

---

## Flagship program hypothesis — cortico-striatal convergence
`concept-corticostriatal-convergence`

The **two strongest CMI latent factors** — **inhibitory/impulse control** (CPT + the Go/NoGo fMRI task;
the single strongest age predictor) and **emotional face recognition (EFR)** — each index an individual
**cortico-striatal phenotype** that **converges across modalities (behavior → function → structure)
onto distinct, identifiable striatal parcels** within its cortico-striatal loop:

- **Impulse-control axis** → *associative / dorsal-caudate* parcels coupled to prefrontal executive
  cortex (DLPFC / IFG / preSMA). Individual inhibitory-control deviation tracks **Go/NoGo frontostriatal
  activation + functional connectivity** AND **frontostriatal white-matter (DWI/HARDI)** structure.
- **Emotion axis** → *limbic / ventral-striatal* parcels coupled to vmPFC / OFC / amygdala. EFR-latent
  deviation tracks **EmoFilm intersubject synchrony (ISC)** AND emotion-network **DWI** structure.

**Structure arm — two converging structural measures.** Beyond DWI white-matter, the same emotion/control
networks should show structural differences in **T1w/T2w myelin contrast and the T2 gray/white-matter
boundary** (HCP-style myelin mapping over the FreeSurfer recons, normalized to the NICAP55 study-specific
template). DWI tractography + T1w/T2w myelin are the two structural readouts; the **Human Connectome
Project (HCP / HCP-D)** and **NICAP** are the comparison anchors. (Sub-concept `concept-structural-myelin-convergence`.)

Both axes are recovered by **multimodal striatal parcellation** (functional group-ICA *fused with*
seed-based diffusion connectivity); individual latent-factor deviation predicts the matching parcel's
connectivity; and these predict **vulnerability outcomes** — a NEW forward hypothesis (status: under-investigation; NOT a dissertation finding — the 2017 monograph Ch4 connectivity is age-covariant + inhibitory-control mediation only)
that baseline **medial-caudate↔prefrontal (DLPFC/SPL, mPFC)** connectivity predicts substance-use
initiation 18 months later and inversely tracks violence proneness.

`decomposes-into` → the impulse-control sub-concepts (`concept-impulse-control-frontostriatal`,
`concept-gonogo-inhibition`), the emotion sub-concepts (`concept-efr-individual-differences`,
`concept-emofilm-synchrony`), the structure sub-concept (`concept-structural-myelin-convergence`), plus
`concept-neurocognitive-maturity` and `concept-striatal-development`. `tested-by-experiment` → ads-cpt,
ads-gonogo, ads-efr, ads-emofilm, ads-dwi-hardi, ads-anat-mprage, ads-anat-t2. Planned output:
`pub-corticostriatal-convergence`.

> **Project context.** CLAD is a **subproject of ADS** (same cohort) — `program-clad` `cross-project`→
> `ads-glimmer:program-ads`. Nodes shared with / inherited from the parent ADS graph carry a
> `cross-project` edge to the ADS-canonical id; see [`migration-ads-clad.md`](migration-ads-clad.md).

---

## Component research questions

### RQ1 — Neurocognitive maturity (CMI) · `concept-neurocognitive-maturity`
Latent factors of inhibitory control, risk/reward, and emotional face recognition predict cognitive
age; the residual (Cognitive Maturity Index, CMI) indexes maturational imbalance and predicts
vulnerability. **Output: `eldamaty2020b` — PUBLISHED** (Frontiers in Psychology 2022,
[doi:10.3389/fpsyg.2022.1017317](https://doi.org/10.3389/fpsyg.2022.1017317), PMID 36571021).
Analysis: `code/analyses/cmi/` → `data/derivatives/cmi/`.

### RQ2 — Social-strain → violence cascade · `concept-violence-cascade`
SEM / latent-growth modeling: adolescent social strain → altered social norms → violence/vulnerability
in emerging adulthood. **Output: `eldamaty2020a` — draft** (dissertation core).
Analysis: `code/analyses/violence-cascade/` → `data/derivatives/violence-cascade/`.

### RQ3 — Multimodal striatal parcellation · `concept-striatal-development`
Masked group-ICA functional parcellation of the striatum + split-half reproducibility, **fused with
seed-based diffusion connectivity**; recovers BOTH limbic (emotion) and associative (control) parcels;
relate medial-caudate↔prefrontal connectivity to outcomes. **Note: the parcellation was performed on
Wave-1 resting-state** (parent-canonical in ADS; 2017 dissertation); **Wave-4 was incomplete and on a different scanner**, so the CLAD
question is *validating and transferring* the Wave-1 parcels to W4 (see RQ7). **Output: `eldamaty2020c` /
OHBM·CCN·FLUX — draft.** Analysis: `code/analyses/striatal-parcellation-multimodal/` → `data/derivatives/striatal-multimodal-parcels/`.

### RQ4 — EFR → EmoFilm synchrony (emotion-axis bridge) · `concept-emofilm-synchrony`
Individual EFR-latent deviation from the population predicts **intersubject synchrony (ISC)** during
naturalistic EmoFilm viewing. Analysis: `code/analyses/efr-emofilm-synchrony/` →
`data/derivatives/emofilm-isc/`.

### RQ5 — Impulse control → Go/NoGo frontostriatal (control-axis bridge) · `concept-impulse-control-frontostriatal`, `concept-gonogo-inhibition`
Individual inhibitory-control latent deviation predicts **Go/NoGo frontostriatal** (caudate↔DLPFC/IFG)
activation and functional/structural connectivity. Analysis: `code/analyses/gonogo-frontostriatal/` →
`data/derivatives/gonogo-frontostriatal/`.

### Secondary — EmoFilm → Wave-4 violence outcome · `concept-emofilm-violence`
Prospective prediction of Wave-4 violence/substance outcomes (DUSI-VP) from W4 EmoFilm emotion-network
response (parent-canonical `concept-emofilm-violence-outcome` in ads-glimmer-graph).
Analysis/output: `code/analyses/emofilm-violence/` → `data/derivatives/emofilm-violence/`.

### RQ6 — Validate W1–3 analytic choices · `concept-w13-analytic-validation` *(methodological)*
Validate the W1–3 denoising / ICA model-order / parcellation / template choices and their robustness
(multiverse) before forward application to Wave-4.

### RQ7 — W1–3 vs Wave-4 scanner harmonization · `concept-scanner-harmonization` *(methodological)*
Wave-4 used a **different, incomplete scanner**. Quantify and harmonize W1–3-vs-W4 scanner/sequence
differences (own Wave-4 SST + cross-scanner QC) before pooling or transferring W1–3 models to W4.

---

## Claims ↔ methods ↔ citation (the evidence links)
Each dissertation/CMI claim, the method that produced it, and the publication node it lives in:

| Claim (with statistic) | Method node | Publication |
|---|---|---|
| Latent factors predict age (ridge **R²=0.51, MAE ±10.11 mo**; raw-metric R²=0.16) | `cfa-sem` + `lasso-age-prediction` | `pub-eldamaty-2022-cmi` (Frontiers 2022, doi:10.3389/fpsyg.2022.1017317) |
| **ICLF ↑ with age β=0.72** (p<.001); CPT d′=0.65, Hit-RT-SD=−0.91 | `cfa-sem` (CPT indicators) | `pub-eldamaty-2022-cmi` |
| **ICLF → −RRLF (−0.22, p<.031)**; ICLF → +ENLF (0.55) — Maturational-Imbalance | `cfa-sem` (SEM) | `pub-eldamaty-2022-cmi` |
| **CMI → BAS-D → DUSI-VP** mediation (indirect −0.073 p=.032; direct −0.597) | `cfa-sem` (mediation) | `pub-eldamaty-2022-cmi` |
| *[HYPOTHESIS — not in dissertation]* baseline **medial-caudate↔DLPFC/SPL** higher in future substance users; **↔mPFC** protective vs violence | `clad-masked-ica-w4`; `conn` (new-program rsfMRI) | `pub-corticostriatal-convergence` (hypothesis) |
| Striatal parcels reproducible (split-half) at orders 3/5/9; **9 selected** for the dissertation — **Wave-1** | `ads-glimmer:method-striatum-group-ica` + `split-half-reproducibility` | `pub-eldamaty-striatal-parcellation` |

## Key dissertation findings (parsed from `eldamaty2020b` + the rsfMRI drafts)
Anchors the spine; full provenance in the `graph/` publication + finding nodes.

- **Age prediction**: latent-factor **ridge** model predicts age R²=0.51, MAE ±10.11 months — vs R²=0.16
  training on raw task metrics.
- **Inhibitory Control Latent Factor (ICLF)** ↑ with age (β=0.72, p<.001) and SES (β=0.27, p<.001).
  Loadings: CPT d′=0.65, Hit-RT-SD=−0.91, response-bias β=−0.50, BIS=0.19.
- **Risk/Reward (RRLF)** ↓ with age (−0.22, p=.019). Loadings: WOF %high-risk=0.70, cumulative
  winnings=−0.90, temporal discounting=−0.13.
- **Emotion (EFR)**: negative-emotion factor (ENLF) ↑ with age (β=0.35, p=.015) and SES; positive-emotion
  (EPLF) ↓ with pubertal development (β=−0.70, p<.001).
- **SEM interactions**: ICLF → −RRLF (−0.22, p<.031; inhibitory control tempers risk → supports
  Maturational-Imbalance model) and ICLF → +ENLF (0.55, p=.037).
- **CMI ↔ outcomes**: CMI correlates with DUSI violence proneness (R=−0.28), substance use (−0.20),
  health risk (−0.16), IQ (+0.20). **Mediation** CMI → BAS-D → DUSI-VP: indirect −0.073 (p=.032),
  direct −0.597 (p<.001), total −0.449. Advanced-puberty **males** show lower CMI (sex×PDS, p<.001).
- **Striatal rsfMRI**: masked group-ICA → reproducible striatal parcels at orders **3, 5, and 9** (split-half); the **9-parcel** solution was selected for the dissertation (most interpretable). *(Forward hypothesis, NOT a dissertation finding:* baseline medial-caudate↔DLPFC/SPL higher in future substance users; ↔mPFC protective vs violence — new-program rsfMRI.)

## Constructs & instruments
CPT (inhibitory control), Wheel of Fortune + Temporal Discounting (risk/reward), Emotional Face
Recognition / NimStim (EFR), Go/NoGo (response inhibition, fMRI), BIS/BAS (reinforcement sensitivity),
DUSI-R (violence proneness + substance use), PDS (puberty), KBIT (IQ), SES. Imaging: resting-state +
EmoFilm + Go/NoGo BOLD, T1w/T2w, DWI/HARDI, fieldmaps. See [`data-dictionary.md`](data-dictionary.md).
