---
id: fmriprep
type: method
name: "fMRIPrep preprocessing"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:d7a13fef0554959fb7d1bbc8f9459676137d72e7339d0185ad23552d94c579e2
tool: "fMRIPrep"
version: "23.x"
edges:
  - {type: requires-standard, target: standard-nicap55-sst}
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-fmriprep", role: harmonizes-with}
description: |
  Standardized BOLD/anat preprocessing; normalizes to the NICAP55 study-specific template.
---
