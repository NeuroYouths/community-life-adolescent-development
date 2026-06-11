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
- **Normalization** — all imaging registers to the **NICAP55 study-specific template** (developmental,
  multicontrast), not adult MNI.

## Comparison anchors
- **Human Connectome Project (HCP / HCP-D)** — reference protocol/pipelines for myelin mapping and
  pulse-sequence lineage. HCP-D is NDA-gated; used as a comparison/validation reference (metadata only),
  not CLAD data.
- **NICAP** — the lineage of the NICAP55 study-specific template.

Full protocol documents (scan parameters, visit checklists) are recovered from the offline lab archive in
the data-migration pass; see [`../DATA-MANIFEST.md`](../DATA-MANIFEST.md).
