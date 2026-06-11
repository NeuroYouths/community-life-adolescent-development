---
id: clad-fmriprep-w4
type: method
name: "fMRIPrep (Wave-4 params)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:f1368a1c0591fadfebe225efe893d90de5f0f6ac2a5d48687fd3adc2b6dd7acd
tool: "fMRIPrep"
version: "23.x"
parameters: {output-space: "clad-wave4-sst", multiband: "yes (HCP-pulse)"}
edges:
  - {type: requires-standard, target: standard-clad-wave4-sst}
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-fmriprep", role: adapts-from-parent}
description: |
  Wave-4 fMRIPrep normalized to the Wave-4 SST; multiband/HCP-pulse settings differ from W1-3.
---
