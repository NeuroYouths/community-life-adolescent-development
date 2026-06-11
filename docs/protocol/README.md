# docs/protocol — QC'd against the canonical NIJ protocol (NeuroYouths Box)

Study (IRB v4 title): *"fMRI Study of Adverse Stressors Precluding Development of Cognitive-Emotional
Competence in Adolescence"* (NIJ 2016-R2-CX-0019). Multi-site: **Georgetown CFMI** (scanning) +
**University of Maryland School of Medicine** (recruitment/call center). High-risk oversample via DUSI
cutoff ≥5 (to ensure alcohol-misuse cases by Wave 3). QC sources: `ADS-protocol.pdf` (Siemens MAGNETOM
**TrioTim** sequence card, W1–3), `IRB-Protocol-v4.docx`, `ADS-Field-Manual.docx` (NeuroYouths Box).

## MRI acquisition
**Waves 1–3 (Siemens MAGNETOM TrioTim 3T):**
- **Structural** — MPRAGE T1w (1 mm iso); **multi-TI DIR** (`AMRI` dual/single-inversion, TR 2000/3000, ~32 TIs); **multi-echo GRE** (`AMRI_mgre`, TE≈4 ms) → **T2\*/QSM iron** mapping (striatal iron). Localizer.
- **Diffusion** — DWI/HARDI **80-dir**, b=1100 (`ep2d_diff`), 2.5 mm.
- **Functional** — resting-state (`ep2d`, TR 2.28 s); **Wheel of Fortune ×3** runs; **Go/No-Go**; **Emotional Counting Stroop** (alcohol-related words). 3×3×3 mm, TR 2.5 s, GRAPPA ×2.

**Wave-4 (different scanner — "not complete, different data"):** T1w MPRAGE, **T2w SPACE**, **T2w FGATIR/DIR**, DWI/HARDI, fieldmaps, **EmoFilm** BOLD (HCP-pulse replica), resting-state. The T1w/T2w pair gives the **T1w/T2w myelin ratio + T2 gray/white-matter boundary**.

**Normalization** — W1–3 → **ads56** SST (inherited); W4 → **CLAD Wave-4 SST** (own scanner). Comparison anchors (external): **HCP/HCP-D**, **NICAP** (3rd-party dataset; its NICAP55 template).

## Behavioral / cognitive battery
- **In-scanner (W1–3)**: Wheel of Fortune (reward/risk), Go/No-Go (inhibition), Emotional Counting Stroop (affective interference).
- **Off-scanner cognitive**: Temporal Discounting (delay discounting), **KBIT** (IQ: verbal/matrices/riddles); Emotional Face Recognition (NimStim) per the CMI paper.
- **Surveys (ACASI/CAPI)**: **DUSI** (substance + violence-proneness; child direct + parent indirect), **BIS/BAS**, **Scale of Physical Development** (puberty/PDS), **AUDIT** (W2/W3), parent **BRIEF**, demographic + responsibility inventories.

## Environmental / community-life assessment
Exposure to violence (school + neighborhood), neighborhood structure, family structure/climate,
and social-norm perceptions — the "Community Life" core driving the social-strain → violence cascade.

> **Open item (needs your call):** the W1–3 scanner card + field manual list **EmoCountStroop**, not EmoFilm,
> and EmoFilm appears only in the Wave-4 BIDS — so the evidence says **EmoFilm is a Wave-4 task**. This
> conflicts with the PR comment ("EmoFilm w1-3 not 4"). Confirm and I'll finalize the wave attribution.
> Exact instrument editions (neighborhood/family/violence-exposure scales) still to be pinned from the appendices.
