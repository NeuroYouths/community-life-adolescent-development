# Protocol — study methods (QC'd against the NIJ protocol + Siemens printout)

Agent-readable methods section for the ADS/CLAD study. Acquisition parameters are CONFIRMED against the
Siemens MAGNETOM **TrioTim** B17 protocol printout (the internal "LongAlc" card, W1–3) and the Wave-4 NIJ
MR protocol; battery against `ADS-MASTER-SHEET.xlsx` ("Data Consolidation Status") + the Instrument Matrix.
Sources (NeuroYouths Box): `ADS-protocol.pdf` (TrioTim card), `IRB-Protocol-v4.docx`, `ADS-Field-Manual.docx`,
`Siemens_Magnetom-3T-Protocol.pdf`, `nij-2016-r2-cx-0019_protocol.pdf`.

## Study & design
- **Title** (IRB v4): *"fMRI Study of Adverse Stressors Precluding Development of Cognitive-Emotional
  Competence in Adolescence."* The Wave-4 recontact is **NIJ 2016-R2-CX-0019**; the original longitudinal
  study (W1–3) was **NIAAA/NIDA**-funded (Georgetown IRB 2011-322).
- **Sites:** scanning at **Georgetown CFMI** (TrioTim for W1–3; Prisma for W4); recruitment/call-center via
  **University of Maryland** — where co-investigators **Diana Fishbein** and **Emma Rose** were based during
  the study (now **UNC Chapel Hill** and **Penn State**, respectively).
- **Cohort:** N=141 enrolled (ages 11–13), 4 waves at ~18-month intervals; **high-risk oversample** via DUSI
  cutoff ≥5 (to ensure alcohol-misuse cases by Wave 3). Per-wave imaging N + the BIDS-vs-manifest
  reconciliation: see [`../DATA-MANIFEST.md`](../DATA-MANIFEST.md).
- **Strategy/goals:** index neurocognitive maturation (the CMI; RQ1) and a social-strain → altered-norms →
  violence cascade (RQ2); the Wave-4/CLAD recontact adds multimodal imaging (T2w myelin, DIR, multi-shell
  HARDI, EmoFilm) to test cortico-striatal convergence (RQ3).

## MRI acquisition

### Waves 1–3 — Siemens MAGNETOM TrioTim 3T (single-band; one protocol card, same across W1/W2/W3)
- **Structural — MPRAGE T1w only:** 1.0 mm iso, TR 1900 / TE 2.52 / TI 900 ms, flip 9°, 176 slices, GRAPPA 2
  (TA 4:18). **No T2w, no DIR, no MP2RAGE.**
- **Diffusion — HARDI (`ep2d_diff`):** 2.5 mm iso, TR 7500 / TE 87, **b = 1100 s/mm², 80 directions,
  single-shell**, GRAPPA 2 (TA 10:23).
- **Functional (`ep2d_pace`; fat-sat, BW 2604 Hz/px, EPI factor 64, GRAPPA 2):**
  - resting-state — 3.0×3.0×2.5 mm, TR 2280 / TE 30, 43 sl, 150 vol (TA 5:49)
  - **EmoCountStroop** (affective interference; alcohol-related words) — 3.0 mm iso, TR 2500 / TE 30, 47 sl,
    110 vol, **block** design (TA 4:43)
  - **Wheel of Fortune ×3** (reward/risk) — 3.0 mm iso, TR 2500, 168 vol/run (TA 7:08/run)
  - **Go/No-Go** (inhibition) — 3.0 mm iso, TR 2500, 121 vol (TA 5:10)
- **Iron / microstructure substudy:** the card also ran **AMRI dual-inversion EPI + multi-echo GRE**
  (`AMRI_mgre`, TE 4 ms + 7 echoes) — the **brain-iron substudy (Erika Raven)**, **acquired but never pulled**
  (out of scope). This is *not* a DIR or MP2RAGE structural sequence.

### Wave-4 (Visit-7) — Siemens Prisma 3T (multiband; different scanner, incomplete cohort)
Adds what W1–3 lacked: **T1w MPRAGE + T2w SPACE + T2w FGATIR/DIR + multi-shell HARDI + fieldmaps + EmoFilm
BOLD (HCP-pulse replica) + resting-state** (multiband SMS = 6, 2.2 mm, TR 727 ms). The T1w+T2w pair enables
the **T1w/T2w myelin ratio + T2 gray/white-matter boundary**. **DIR, MP2RAGE, T2w, and EmoFilm are Wave-4
only**; the W4 diffusion is **multi-shell** (vs the W1–3 single-shell 80-dir).

## Spatial normalization — study-specific templates (SSTs)
The study's *own* templates (antsMultivariateTemplateConstruction2), distinct from the external reference
atlases below:
- **`ads56`** — the **W1–3** SST; inherited by CLAD as the parent-canonical W1–3 normalization space.
- **CLAD Wave-4 SST** — built from **W4** data on the Prisma (own scanner/params), for the W4 multimodal work.

## Reference & comparison atlases (external)
- **Tian-2020** (Melbourne Subcortex Atlas) — HCP 1000-subject functional-connectivity-gradient hierarchical
  subcortex parcellation; the striatal-parcellation **gradient gold-standard** (the mICA parcels' closest match).
- **HCP / HCP-D** — comparison cohort + the HCP myelin/surface pipeline reference.
- **NICAP** (3rd-party developmental dataset) + its **NICAP55** template — developmental-normalization anchor.
- **Tziortzi** (probabilistic tractography striatal atlas), **Choi-2012** (cortical-prior striatal networks),
  **Schaefer** (cortical), **Glasser HCP-MMP** (cortical) — parcellation comparison/benchmark references.

## Behavioral / cognitive battery
Instruments + actual materials are in ads-glimmer `materials/instruments/`; the per-instrument nodes carry
admin/waves/timing/reference.
- **In-scanner (W1–3):** Wheel of Fortune (reward/risk), Go/No-Go (inhibition), Emotional Counting Stroop
  (affective interference), resting-state. *(Wave-4 adds EmoFilm.)*
- **Off-scanner cognitive (W1–3):** **ERT** (NimStim emotion recognition = the CMI "EFR"; consolidated W1–2),
  Temporal Discounting, **KBIT** (IQ), **RAVLT** (verbal memory), **Trail Making** (set-shifting), **Spatial
  Working Memory** + **Stockings of Cambridge** (CANTAB).
- **Child surveys (ACASI/CAPI):** **DUSI** (all 3 waves; substance + violence-proneness; high-risk cutoff ≥5),
  BIS/BAS, Scale of Physical Development (puberty), M-AUDIT, ETI, Gambling, ADHD, Sleep, Moderators, Edinburgh
  Handedness.
- **Parent surveys:** BRIEF, DUSI (parent), Family History, Demographics, Income, Child Responsibility, Perinatal.

## Environmental / community-life assessment
Exposure to violence (school + neighborhood), neighborhood structure, family structure/climate, and
social-norm perceptions — the "Community Life" core driving the social-strain → altered-norms → violence
cascade (RQ2). Exact instrument editions (neighborhood/family/violence-exposure scales) to be pinned from the
protocol appendices.
