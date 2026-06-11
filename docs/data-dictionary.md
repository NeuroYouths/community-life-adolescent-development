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
| NICAP55 SST | study-specific multicontrast (T1w/T2w) developmental template (normalization target) | `nicap55-template` → `standard-nicap55-sst`, `data/derivatives/template-nicap55/` |
| T1w/T2w myelin | **T1w/T2w ratio + T2 gray/white-matter boundary** surface contrast (HCP-style) — the second structural axis alongside DWI | `myelin-t1t2-mapping` → `data/derivatives/myelin-t1t2/` |
| DWI tractography | seed-based structural connectivity fingerprints | `seeded-diffusion-connectivity` → `data/derivatives/dwi-tractography/` |

**Comparison anchors:** Human Connectome Project (HCP / HCP-D; `standard-hcp`) for myelin mapping +
pulse-sequence lineage (EmoFilm is an HCP-pulse replica), and NICAP (the NICAP55 SST lineage). HCP-D is
NDA-gated → metadata-only, not CLAD data.

Full per-variable coding to be imported from the dictionary spreadsheet in the data pass.
