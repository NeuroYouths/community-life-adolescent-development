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
| NIJ protocol (2016-R2-CX-0019) | `nij-2016-r2-cx-0019_protocol.pdf` (Box; in-repo at `materials/wave4-mri/`) — NOTE the local `NIJ_protocol_12-20-19.pdf` is the Siemens **scanner manual**, not the study protocol | OPEN | ✅ |
| NIJ program narratives + budgets | voxel-forge-duo `/Volumes/neuroyouths/2016-R2-CX-0019/` | OPEN | 🔴 |
| IRB approval letter | `~/neuroscience/ADS/2018.06.20.IRB.Letter.2016-R2-CX-0019.pdf` | OPEN | ✅ |
| W4 budget | `~/neuroscience/ADS/NIJ-ADS Wave 4_ Budget*.xlsx` | OPEN | ✅ |

## Dissertation artifacts
| Class | Where | Status |
|---|---|---|
| Defense slides (17 May 2017) | `~/ads-glimmer-staging/neuroyouths-recovery/dissertation/17May_Slides.pptx` (63 MB) | ✅ (annex in data pass) |
| Signed committee form / proposal / reviewer forms | same dir | ✅ |
| Striatum FC poster + rsfMRI methods/results drafts | `~/ads-glimmer-staging/neuroyouths-recovery/{poster,drafts/rsfMRI}/` | ✅ |
| Dissertation monograph PDF | `dissertation/monograph/El_Damaty__Dissertation_2020.pdf` (154 pp, recovered from Box) | ✅ |

## GAPS (explicit)
- **eldamaty2020c** repo location unconfirmed (private hebbianloop, or folded into ads-glimmer methods).
- **eldamaty2020a** is an unpublished draft — publication status to confirm.
- Offline recovery (voxel-forge-duo / CFMI) for raw DICOM, striatal-ICA outputs, legacy derivatives needs SSH/VPN authorization.
- **Defacing** of de-identified anatomicals required before any imaging byte is annexed/published.
- Tian subcortical atlas NIfTI location to confirm.

## ADS-MASTER ground truth (Box: Projects/ADS) — keep this current
Authoritative sources confirmed in the NeuroYouths Box `ADS-MASTER` + `datafiles` + `bashscripts` folders:
- **`ADS-MR-INVENTORY.xlsx`** (WAVE 1/2/3 × series): W1–3 acquired = **MPRAGE, DWI/DTI, Rest, EmoStroop, Go/NoGo, WOF×3** (no T2w/DIR). **`mr-data-manifest_withkey.txt`** = per-task run/volume counts (EmoStroop 110, Go/NoGo 121, …).
- **`datafiles/`** (the data to mirror into ads-glimmer): `mri-data` (8,170), `Neuropsych` (2,624), `rois` (840), `Stimulus-Computer` (3,530), `Genetics`, `Behavioral&Demographic`, `tables`; + `ads.dd.matched.xlsx` (matched data dictionary), `Ever_User_*.xlsx` (substance-use vector), `w{1,2}-{ES,GNG,WOF}-*.txt` task exports.
- **`bashscripts/`** = the **actual W1–3 pipeline** (ground truth over the modernization plan): `recon-all`, **FSFAST** (`FSFAST-setup/preproc/2ndlvl` — FreeSurfer functional, *not* fMRIPrep), `fsqc`, `get-fs-stats`, `importSubs`, `extractomatic`, `cfmi-sync` (+ `bin/`, `dev/`, `lists/`).
- **Iron (T2\*/QSM, multi-echo GRE)**: **acquired in W1–3 but NOT pulled** — a separate brain-iron sub-study (Erika Raven). Recoverable if the iron axis is pursued; currently out of scope.

**ads-glimmer (github/main) status:** the imaging data is already represented (16 dataset nodes incl. all func tasks + structural + DIR/MP2RAGE + SST-n56; 38 method nodes). **Gaps to import:** the non-imaging data classes above (Genetics/Neuropsych/rois/pls-r/Stimulus/tables/dictionaries), the iron-not-pulled note, v0.4 program/subproject, and the people (Fishbein/Rose/Raven + Penn State/UNC). Tracked for the ADS v0.4 + data-completion PR.

## Pipeline & manifest provenance (how the inventory + derivatives were produced)

**How `mr-data-manifest_withkey.txt` was built** — a two-stage pipeline, NOT a single DICOM→table script:
1. **DICOM-header extraction → MR inventory.** `resources/bash/extract-ADS-dicoms.sh` reads an
   `ads-extraction-table.txt` (MLID/MRID/WAVE/dates) and calls `fetch-dicom` (`~/neuroscience/ADS/fetch-dicom`),
   which walks the Siemens `.STU/.SER/.IMA` tree and runs AFNI `dicom_hdr` to pull PatientName, **Series
   Description → TASK**, scan date/time → **SESSION (wave)**, and the acquisition parameters (TR/TE/TI/flip/…).
   Output = `ads-mr-inventory.txt` → **`ADS-MR-INVENTORY.xlsx`** (per-subject × series presence matrix).
2. **Manifest assembly with the ID key.** `build_data-manifest.sh` / `create_data-manifest.sh`
   (`ads-glimmer/code/legacy-ants/`) crosswalk numeric BIDS-IDs → ADS-IDs via an external
   **`participants-key.tsv`** (the "withkey"), enumerate `sub-/ses-/run-/task` from filenames, and count runs
   per subject×session×task. `SCANLENGTH` = volume count (DIM4 via FSL `fslinfo`); the live file is the
   NUMVOLS-trimmed variant of this family (the 24-column superset is `check_manifest()` in `legacy-ants/main.sh`,
   which reads BIDS `.json` sidecars with `jq` + `fslinfo`/`3dinfo`).
   **Spot-check:** the manifest was reconciled **manually** against `ADS-MR-INVENTORY.xlsx` + offline
   (voxel-forge-duo / CFMI) data (this manifest's 2026-06-10 audit) — there is no automated assertion script.

**W1–3 pipeline = the legacy ground truth** (Box `ADS/bashscripts/`), distinct from the modernization plan:
- **Functional = FSFAST** (`FSFAST-setup/preproc/1stlvl/2ndlvl/merge`), FreeSurfer's own functional stream —
  **not fMRIPrep**. *This is why fMRIPrep "is missing": W1–3 never used it.* **fMRIPrep is the re-derive
  target** (orchestrated in `legacy-ants/main.sh` via `fmriprep-docker` + `fmriprep_filter.json`; modern
  consumer `nipype/fmriprep_confounds.py`) — no standalone `run_fmriprep.sh` because it ran inside `main.sh`.
- **Structural = `recon-all` (FreeSurfer 6.0.0)** + ANTs N4/Rician denoise; QC via `fsqc.sh`/`setupFSQC.sh`.
- **Masked-ICA (mICA)** is present, just not named "mica": `analysis/calc_stableICs_munkres.py` (split-half IC
  matching), `make_Parcels.py` (winner-take-all striatal parcels), `calc_critPearson.py` (reproducibility
  threshold), `calc_reproducibility.m` (vendored). Outputs at voxel-forge-duo `Dissert-ToGo/…`.
- **PLS-R is an ANALYSIS METHOD, not a data class** — `analysis/qc_editing_relationships.py` (PLSR + VIP
  brain-behavior; QC↔manual-rating) and the CONN PLS-R batches. The Box `datafiles/pls-r` folder holds its
  *outputs*, not raw data.

## Recovery order (later passes)
1. Freeze canonical inputs: legacy-bids-w4 + legacy-bids-w13 + NICAP55 template + behavioral covariates.
2. Wire encrypted annex (Hetzner) + private controlled backend (revive `clad-master`); migrate bytes (defaced).
3. Re-derive: fMRIPrep → striatal multimodal parcellation → connectivity → analyses.
4. Offline/gated recovery (voxel-forge-duo, CFMI bids-oa) only if raw reprocessing is needed.
