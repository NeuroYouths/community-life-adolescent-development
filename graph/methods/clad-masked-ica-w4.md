---
id: clad-masked-ica-w4
type: method
name: "Masked group-ICA striatal parcellation (Wave-4)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:91e16decd8c6688fc0773cf5f5df1432424f5bb65b8b1d3bc368c34ccc242ad3
tool: "MELODIC"
version: "FSL 6.0"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-striatum-group-ica", role: adapts-from-parent}
description: |
  W4 masked group-ICA; validates/applies the W1-3 striatal parcels to the (incomplete, different-scanner) W4 rest data.
---
