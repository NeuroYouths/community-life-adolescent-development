# CLAD — Data Manifest Audit

Reconciled inventory of all CLAD/Wave-4 data across storage locations, keyed by
**data class × wave × modality**, with tier, recovery status, and canonical-input-vs-rederive call.
Audit date: 2026-06-10. **No PHI is committed to this repo** — this manifest documents *where bytes
live*; controlled/PHI tiers resolve to a private backend (see [`data-governance.md`](data-governance.md)).

Status legend: ✅ local & reachable · 🟡 cloud-reachable (Box/GCS, needs creds) · 🔴 offline/gated
(voxel-forge-duo / CFMI / physical). Tier: OPEN · CONTROLLED · PHI.

## Cohort
N=141 enrolled (2011); waves 1–4 at ~18-month intervals; Wave-4 / Visit-7 = the NIJ
2016-R2-CX-0019 recontact (the CLAD-specific collection). Wave-4 local BIDS currently 61 subjects;
Waves 1–3 BIDS 142 subjects.

## Imaging (BIDS)
| Class · wave · modality | Where | Count / size | Tier | Status | Input vs re-derive |
|---|---|---|---|---|---|
| Wave-4 BIDS (all modalities) | `~/ads-glimmer/data/legacy-bids-w4/` | 61 subj / ~104 niftis / 3.4 GB | OPEN (de-id; deface pending) | ✅ | **INPUT — freeze** |
| Waves 1–3 BIDS | `~/ads-glimmer/data/legacy-bids-w13/` | 142 subj / ~153 niftis / 78 GB | OPEN (de-id) | ✅ | **INPUT — freeze** |
| W4 T1w MPRAGE | legacy-bids-w4 `anat/`; Box `ADS-MPRAGE-forGoldie` | ~61 local / 1,078 DICOM zips | OPEN/CONTROLLED | ✅ / 🟡 | INPUT |
| W4 T2w (FLAIR/DIR) | legacy-bids-w4 `anat/` | ~61 | OPEN | ✅ | INPUT |
| W4 BOLD resting-state | legacy-bids-w4 `func/` | ~61 runs | OPEN | ✅ | INPUT |
| W4 BOLD EmoFilm | legacy-bids-w4 `func/`; E-Prime logs in Box | ~61 BOLD / 266 E-Prime files (58 subj) | OPEN/CONTROLLED | ✅ / 🟡 | INPUT |
| W4 BOLD Go/NoGo | per-subject DICOM (Box); local subset | task in battery | OPEN/CONTROLLED | 🟡 | INPUT |
| W4 DWI/HARDI | legacy-bids-w4 `dwi/` | ~61 | OPEN | ✅ | **INPUT (flagship structural axis)** |
| W4 fieldmaps | legacy-bids-w4 `fmap/` | ~61 pairs | OPEN | ✅ | INPUT |
| Raw DICOM (all waves) | voxel-forge-duo `/Volumes/hi/mri.raw/`; CFMI node020; Box zips | ~1.68M files / ~180 GB | PHI | 🔴 / 🟡 | INPUT (de-id on convert) |

## Derivatives
| Class | Where | Tier | Status | Input vs re-derive |
|---|---|---|---|---|
| FreeSurfer recons (W1, legacy) | voxel-forge-duo `/Volumes/hi/...freesurfer/` | OPEN | 🔴 | **RE-DERIVE** (FastSurfer/fMRIPrep) |
| SPM12 preproc (legacy) | voxel-forge-duo `/Volumes/hi/spm12-*` | OPEN | 🔴 | RE-DERIVE (→ fMRIPrep) |
| CONN connectomes (legacy) | voxel-forge-duo `/Volumes/hi/CONNv19b` | OPEN | 🔴 | RE-DERIVE |
| Striatal masked-ICA outputs + reproducibility grids | voxel-forge-duo `/Volumes/Dissert-ToGo/.../striatal-longitudinal-parcellation/` | OPEN | 🔴 | RE-DERIVE from code (canonical pipeline frozen) |
| ICA effect-sizes / PLSR | voxel-forge-duo `/Volumes/neuroyouths/data/` | OPEN | 🔴 | RE-DERIVE |
| WoF-gPPI (legacy) | voxel-forge-duo `/Volumes/hi/wof-gppi/` | OPEN | 🔴 | RE-DERIVE |

## Templates & atlases
| Class | Where | Tier | Status | Note |
|---|---|---|---|---|
| NICAP55 study-specific template (T1w/T2w/template0) | `/Volumes/spare/nicap55_*.nii.gz` | OPEN | ✅ (when mounted) | **CANONICAL INPUT** — developmental normalization |
| Schaefer parcellations (100–1000, 7/17 net) | `~/neuroscience/ADS/Parcellations/` | OPEN | ✅ | reference atlas |
| Striatal atlases (Keuken 7T, Tian, Choi) | `~/neuroscience/ADS/Parcellations/` (Tian unconfirmed) | OPEN | ✅ / 🔴 | reference |
| ads56 mean template (pre-NICAP) | `~/neuroscience/ADS/ads56.nii.gz` | OPEN | ✅ | archive (superseded) |

## Behavioral / tabular
| Class | Where | Tier | Status | Note |
|---|---|---|---|---|
| Master covariates | `~/neuroscience/ADS/ads-master-covariates.xlsx` | CONTROLLED | ✅ | INPUT (private backend) |
| Data dictionary | `~/neuroscience/ADS/ads-master-dictionary.xlsx` | OPEN | ✅ | reference |
| Go/NoGo (W2, W3) | `~/neuroscience/ADS/w{2,3}-gonogo.csv` | CONTROLLED | ✅ | INPUT |
| BIS/BAS (W3) | `~/neuroscience/ADS/w3-bisbas-r.xlsx` | CONTROLLED | ✅ | INPUT |
| Stroop | `~/neuroscience/ADS/Stroop Data.xlsx` | CONTROLLED | ✅ | INPUT |
| EmoFilm E-Prime logs | Box `NIJ-ADS_Wave4_Visit7` (266 files / 58 subj) | CONTROLLED | 🟡 | INPUT |
| EmoFilm timing / paradigm | `~/neuroscience/ADS/emofilm-timing` | OPEN | ✅ | reference |
| DUSI (W1, W2) | `/Volumes/recon/tables/QC/DUSI-w*.xlsx` | CONTROLLED | ✅ | INPUT |

## Protocols / grant / IRB
| Class | Where | Tier | Status |
|---|---|---|---|
| NIJ protocol (2016-R2-CX-0019) | `~/neuroscience/ADS/NIJ_protocol_12-20-19.pdf` | OPEN | ✅ |
| NIJ program narratives + budgets | voxel-forge-duo `/Volumes/neuroyouths/2016-R2-CX-0019/` | OPEN | 🔴 |
| IRB approval letter | `~/neuroscience/ADS/2018.06.20.IRB.Letter.2016-R2-CX-0019.pdf` | OPEN | ✅ |
| W4 budget | `~/neuroscience/ADS/NIJ-ADS Wave 4_ Budget*.xlsx` | OPEN | ✅ |

## Dissertation artifacts
| Class | Where | Status |
|---|---|---|
| Defense slides (17 May 2017) | `~/ads-glimmer-staging/neuroyouths-recovery/dissertation/17May_Slides.pptx` (63 MB) | ✅ (annex in data pass) |
| Signed committee form / proposal / reviewer forms | same dir | ✅ |
| Striatum FC poster + rsfMRI methods/results drafts | `~/ads-glimmer-staging/neuroyouths-recovery/{poster,drafts/rsfMRI}/` | ✅ |
| Dissertation monograph PDF | `/Volumes/spare/phd-dissertation/` (unmounted) or ProQuest/Georgetown | 🔴 GAP |

## GAPS (explicit)
- **Dissertation monograph PDF** not local (recover from `/Volumes/spare` when mounted, or ProQuest/Georgetown repository).
- **eldamaty2020c** repo location unconfirmed (private hebbianloop, or folded into ads-glimmer methods).
- **eldamaty2020a** is an unpublished draft — publication status to confirm.
- Offline recovery (voxel-forge-duo / CFMI) for raw DICOM, striatal-ICA outputs, legacy derivatives needs SSH/VPN authorization.
- **Defacing** of de-identified anatomicals required before any imaging byte is annexed/published.
- Tian subcortical atlas NIfTI location to confirm.

## Recovery order (later passes)
1. Freeze canonical inputs: legacy-bids-w4 + legacy-bids-w13 + NICAP55 template + behavioral covariates.
2. Wire encrypted annex (Hetzner) + private controlled backend (revive `clad-master`); migrate bytes (defaced).
3. Re-derive: fMRIPrep → striatal multimodal parcellation → connectivity → analyses.
4. Offline/gated recovery (voxel-forge-duo, CFMI bids-oa) only if raw reprocessing is needed.
