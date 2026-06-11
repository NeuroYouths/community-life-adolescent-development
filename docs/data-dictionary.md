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
| Imaging (acquired) | T1w MPRAGE, T2w, BOLD (rest/EmoFilm/GoNoGo), DWI/HARDI, fmap | Siemens 3T |

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
