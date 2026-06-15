# CLAD — Data Dictionary (OPEN)

Variable definitions for the study (the OPEN description; the underlying subject-level values are
CONTROLLED and live in the private backend). Canonical source: `ads-master-dictionary.xlsx`.

| Domain | Variables (abbrev.) | Instrument |
|--------|--------------------|-----------|
| Inhibitory control | CPT d′, response-bias β, Hit/FA RT SD; BIS | Continuous Performance Task; BIS/BAS |
| Risk / reward | WOF %high-risk, RT, cumulative winnings; TD AUC | Wheel of Fortune; Temporal Discounting |
| Emotion recognition | EFR accuracy/RT (neg: anger/fear/sad/disgust; pos: happy) | Emotional Face Recognition (NimStim) |
| Response inhibition | Go/NoGo accuracy, RT, commission errors | Go/NoGo (fMRI) |
| Reinforcement sensitivity | BAS-Drive, BAS-FunSeeking, BAS-RewardResponsivity | BIS/BAS |
| Outcomes | DUSI violence proneness (DUSI-VP), substance use, health risk | DUSI-R |
| Development | age, PDS (puberty), BMI, sex | anthropometrics; Pubertal Development Scale |
| Cognitive | composite IQ | KBIT |
| Context | SES (income + education z-composite) | caregiver interview |
| Imaging W1–3 (MRI Inventory) | T1w MPRAGE, DTI, BOLD: rest / EmoStroop / Go-NoGo / WOF×3 | Siemens TrioTim 3T |
| Imaging W4 (Visit-7) | + T2w SPACE, T2w FGATIR/DIR, EmoFilm BOLD, fmap | different scanner |

## Structural & template derivatives (the structure arm)
| Derivative | What | Method → output |
|-----------|------|-----------------|
| FreeSurfer recons | cortical surface reconstruction + morphometry (thickness, area, curvature) | `freesurfer-recon` → `data/derivatives/freesurfer/` |
| fMRIPrep | standardized BOLD/anat preprocessing, normalized to the SST | `fmriprep` → `data/derivatives/fmriprep/` |
| **ads56 SST** (W1–3) | ADS Wave-1–3 study-specific multicontrast (T1w/T2w/FA) developmental template; **inherited** from ADS (`ads-glimmer:standard-ads56-sst`) | `ads-glimmer:method-ads-sst-mvtc2` |
| **Wave-4 SST** (CLAD-owned) | study-specific template built from **Wave-4 data** (different scanner) — the W4 normalization target | `clad-wave4-sst` → `standard-clad-wave4-sst`, `data/derivatives/template-nicap55/` |
| T1w/T2w myelin | **T1w/T2w ratio + T2 gray/white-matter boundary** surface contrast (HCP-style) — the second structural axis alongside DWI | `clad-myelin-t1t2` → `data/derivatives/myelin-t1t2/` |
| DWI tractography | seed-based structural connectivity fingerprints | `clad-dwi-w4` → `data/derivatives/dwi-tractography/` |

**Comparison anchors (external):** **HCP / HCP-D** (`standard-hcp`) for myelin mapping + pulse-sequence
lineage (EmoFilm is an HCP-pulse replica), and **NICAP** — a separate 3rd-party validation dataset
(`standard-nicap`) whose **NICAP55** template (`standard-nicap55`) is a comparison template (NOT the ADS
SST). HCP-D + NICAP are external → metadata-only, not CLAD data.

Full per-variable coding to be imported from the dictionary spreadsheet in the data pass.


## FreeSurfer recon versions (edited / non-edited · modern / legacy)

Distinguish the recon generations — analyses must state which they use:

- **(A) Legacy FS5.3 / FSFAST-era + ANTs (Wave-1, 2016).** The original cortical-thickness / `ads56`
  template line (`recon-all -3T -qcache`, GNU-parallel batch, 22 Jul 2016; `Parcellations/FreeSurfer5.3/`).
  *fsfast* functional stream, not fMRIPrep.
- **(B) Modern FS6.0.0 `recon-all` — the canonical W1–3 store (auto + a small EDITED subset).** Bulk recons
  are **unedited auto FS6**; a hand-edited ground-truth subset exists (e.g. 149959-wave-001, the IRR
  reliability set, the Dissert-ToGo striatal-longitudinal dirs). Manual edits are tracked in
  `ADS FreeSurfer QC.xlsx` (`NumBrainMaskEdits` + `NumWhiteMaskDel` + `NumWhiteMaskFill`); a **pre-edit**
  stats snapshot is kept under `data/MRI/freesurfer/stats/**preedit/**`. Per-session edit map:
  `w13-recons/edit-status.txt` (`<id>-wave-NNN  yes|no`).
- **(C) Modern FastSurfer / FS7.4.1 — the re-derive set (auto only, W1–3).** Box annex
  `ads-glimmer-annex/w13-fastsurfer/`; benchmarked vs (B) by `compare_fs6_vs_fastsurfer.py`.

**Wave-4 recons are NOT edited — in fact W4 was never reconned in the legacy stores.** Only W1–3 have
recons (and within those only the small hand-picked subset above is edited); the recon stores
(`edit-status.txt`, `w13-recons/`, `w13-fastsurfer`) stop at wave-003/003a. W4 is treated as raw BIDS input
flagged RE-DERIVE. ("fsfast vs not": the *structural* recon is `recon-all`; the W1–3 *functional* analysis was
FSFAST — a separate FreeSurfer stream — whereas the modern re-derive is fMRIPrep.)
