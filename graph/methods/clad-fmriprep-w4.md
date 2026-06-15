---
id: clad-fmriprep-w4
type: method
name: "fMRIPrep (Wave-4 params)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:f1368a1c0591fadfebe225efe893d90de5f0f6ac2a5d48687fd3adc2b6dd7acd
code: "nipype/fmriprep_confounds.py (fMRIPrep container orchestrated in legacy-ants/main.sh — re-derive target; W1-3 used FSFAST)"
code-repo: "github.com/hebbianloop/ads-glimmer-code"
code-commit: "cb76a3b31c9408af80e0d00c697ac1db4e8a76f7"
algorithm: "fMRIPrep 23.2.0 preproc + confounds"
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
