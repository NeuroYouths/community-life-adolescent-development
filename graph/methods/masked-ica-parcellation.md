---
id: masked-ica-parcellation
type: method
name: "Masked group-ICA striatal parcellation"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:9def44fcad73a1c52a43aa455c975aa214affa83671f87a8532d7c4086256799
tool: "MELODIC / masked group-ICA"
version: "FSL 6.0"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-striatum-group-ica", role: harmonizes-with}
description: |
  Striatal-mask-constrained group-ICA; max-loading voxel labeling; split-half reproducibility.
---
