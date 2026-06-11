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
connectivity; and these predict **vulnerability outcomes** — consistent with the dissertation finding
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
relate medial-caudate↔prefrontal connectivity to outcomes. **Output: `eldamaty2020c` / OHBM·CCN·FLUX — draft.**
Analysis: `code/analyses/striatal-parcellation-multimodal/` → `data/derivatives/striatal-multimodal-parcels/`.

### RQ4 — EFR → EmoFilm synchrony (emotion-axis bridge) · `concept-emofilm-synchrony`
Individual EFR-latent deviation from the population predicts **intersubject synchrony (ISC)** during
naturalistic EmoFilm viewing. Analysis: `code/analyses/efr-emofilm-synchrony/` →
`data/derivatives/emofilm-isc/`.

### RQ5 — Impulse control → Go/NoGo frontostriatal (control-axis bridge) · `concept-impulse-control-frontostriatal`, `concept-gonogo-inhibition`
Individual inhibitory-control latent deviation predicts **Go/NoGo frontostriatal** (caudate↔DLPFC/IFG)
activation and functional/structural connectivity. Analysis: `code/analyses/gonogo-frontostriatal/` →
`data/derivatives/gonogo-frontostriatal/`.

### Secondary — EmoFilm → Wave-4 violence outcome · `concept-emofilm-violence`
Prospective prediction of Wave-4 violence/substance outcomes from EmoFilm emotion-network response
(cross-links to `concept-emofilm-violence-outcome` in ads-glimmer-graph).
Analysis/output: `code/analyses/emofilm-violence/` → `data/derivatives/emofilm-violence/`.

---

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
- **Striatal rsfMRI**: masked group-ICA → reproducible striatal parcels (primary k≈5, fine to ~8–10
  via split-half); baseline **medial-caudate↔DLPFC/SPL** connectivity higher in future substance users;
  **medial-caudate↔mPFC** connectivity protective, inversely related to violence proneness.

## Constructs & instruments
CPT (inhibitory control), Wheel of Fortune + Temporal Discounting (risk/reward), Emotional Face
Recognition / NimStim (EFR), Go/NoGo (response inhibition, fMRI), BIS/BAS (reinforcement sensitivity),
DUSI-R (violence proneness + substance use), PDS (puberty), KBIT (IQ), SES. Imaging: resting-state +
EmoFilm + Go/NoGo BOLD, T1w/T2w, DWI/HARDI, fieldmaps. See [`data-dictionary.md`](data-dictionary.md).
