# docs/protocol

OPEN parts of the scan/visit protocol (Visit-7 / Wave-4). Participant-facing and identifiable materials
stay in the private backend.

## Imaging protocol (de-identified summary)
Siemens 3T acquisition per session:
- **Structural** — T1w MPRAGE + **T2w**. The T1w/T2w pair gives the **T1w/T2w ratio and the T2
  gray/white-matter boundary** (HCP-style myelin-sensitive contrast) — a worthwhile structural readout
  for the emotion/control networks, complementary to DWI. Surfaces from FreeSurfer/FastSurfer recons.
- **Functional** — resting-state BOLD, **EmoFilm** (naturalistic emotional film; HCP-pulse replica),
  Go/NoGo.
- **Diffusion** — DWI/HARDI + fieldmaps.
- **Normalization** — W1–3 imaging registers to the **ads56** study-specific template (ADS W1–3 SST,
  inherited); Wave-4 imaging registers to the **CLAD Wave-4 SST** (built from W4 data, different scanner),
  not adult MNI.

## Comparison anchors (external)
- **Human Connectome Project (HCP / HCP-D)** — reference protocol/pipelines for myelin mapping and
  pulse-sequence lineage (EmoFilm is an HCP-pulse replica). HCP-D is NDA-gated; comparison only, not CLAD data.
- **NICAP** — a *separate 3rd-party validation dataset/project*; its **NICAP55** template is a comparison
  template (NOT the ADS SST). External comparison only.

Full protocol documents (scan parameters, visit checklists) are recovered from the offline lab archive in
the data-migration pass; see [`../DATA-MANIFEST.md`](../DATA-MANIFEST.md).
