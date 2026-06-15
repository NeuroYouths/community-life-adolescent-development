# docs/protocol — QC'd against the canonical NIJ protocol (NeuroYouths Box)

Study (IRB v4 title): *"fMRI Study of Adverse Stressors Precluding Development of Cognitive-Emotional
Competence in Adolescence"* (NIJ 2016-R2-CX-0019). Multi-site: **Georgetown CFMI** (scanning) +
**University of Maryland School of Medicine** (recruitment/call center); co-mentors Diana Fishbein and
Emma Rose at **Penn State** (P-TRAN) and **UNC**. High-risk oversample via DUSI
cutoff ≥5 (to ensure alcohol-misuse cases by Wave 3). QC sources: `ADS-protocol.pdf` (Siemens MAGNETOM
**TrioTim** sequence card, W1–3), `IRB-Protocol-v4.docx`, `ADS-Field-Manual.docx` (NeuroYouths Box).

## MRI acquisition
Per the **ADS-MASTER-SHEET "MRI Inventory"** (the actually-acquired series, N=147), **W1, W2, and W3 each
acquired the same set**:
**Waves 1–3 (Siemens MAGNETOM TrioTim 3T):**
- **Structural** — **MPRAGE T1w only** (no T2w, no DIR, no iron/QSM in the inventory). Localizer.
- **Diffusion** — **DTI** (the scanner card lists `ep2d_diff` 80-dir, b=1100, 2.5 mm — confirm against headers).
- **Functional** — resting-state; **Wheel of Fortune ×3**; **Go/No-Go**; **Emotional Counting Stroop** (alcohol-related words). 3×3×3 mm, TR 2.5 s, GRAPPA ×2.
- *(The scanner card also shows `AMRI` dual-inversion + multi-echo GRE sequences, but these are **not in the acquired-series inventory** for W1-3 — treat as not-acquired pending confirmation.)*

**Wave-4 (Visit-7, different scanner — adds what W1–3 lacked):** T1w MPRAGE + **T2w SPACE** + **T2w FGATIR/DIR** + DWI/HARDI + fieldmaps + **EmoFilm** BOLD + resting-state. The T1w+T2w pair (W4 only) enables the **T1w/T2w myelin ratio + T2 gray/white-matter boundary**; **DIR is W4-only**.

**Wave-4 (different scanner — "not complete, different data"):** T1w MPRAGE, **T2w SPACE**, **T2w FGATIR/DIR**, DWI/HARDI, fieldmaps, **EmoFilm** BOLD (HCP-pulse replica), resting-state. The T1w/T2w pair gives the **T1w/T2w myelin ratio + T2 gray/white-matter boundary**.

**Normalization** — W1–3 → **ads56** SST (inherited); W4 → **CLAD Wave-4 SST** (own scanner). Comparison anchors (external): **HCP/HCP-D**, **NICAP** (3rd-party dataset; its NICAP55 template).

## Behavioral / cognitive battery
Confirmed against **`ADS-MASTER-SHEET.xlsx`** ("Data Consolidation Status" task×wave matrix, W1–3):
- **In-scanner (W1)**: Wheel of Fortune (×3 runs, reward/risk), Go/No-Go (GNG, inhibition), Emotional Counting Stroop (EmoStroop, affective interference) + resting-state.
- **Off-scanner cognitive (W1–3)**: **ERT** (Emotion Recognition Task, NimStim — the CMI "EFR"), Temporal Discounting (TD), **KBIT** (IQ), and an **executive/memory battery — RAVLT** (verbal memory), **Trail Making** (set-shifting), **Spatial Working Memory (SWM)** + **Stockings of Cambridge (SoC)** (CANTAB).
- **Child surveys (ACASI/CAPI)**: **DUSI** (scored all 3 waves; substance + violence-proneness; high-risk screener cutoff ≥5), **BIS/BAS**, **Scale of Physical Development** (puberty), **TAD** (tobacco/alcohol/drug, W2), AUDIT, Sleep, Moderators, Responsibility, MAUDIT, Handedness.
- **Parent surveys**: **BRIEF**, DUSI (W1), **Family History** (W1), Demographics, Responsibility.
- Demographics show **V1–V6** visits across the longitudinal design; EmoFilm + the Wave-4 acquisitions are the NIJ Visit-7 add-on (different scanner).

## Environmental / community-life assessment
Exposure to violence (school + neighborhood), neighborhood structure, family structure/climate,
and social-norm perceptions — the "Community Life" core driving the social-strain → violence cascade.

> **Resolved (owner-confirmed + protocol printout):** **EmoCountStroop is the Wave-1–3 in-scanner affective task; EmoFilm is the Wave-4 task** — corroborated by the W1–3 scanner card/field manual, the Siemens TrioTim protocol printout, and the Wave-4 BIDS.
> Exact instrument editions (neighborhood/family/violence-exposure scales) still to be pinned from the appendices.
