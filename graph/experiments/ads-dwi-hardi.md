---
id: ads-dwi-hardi
type: experiment
name: "Diffusion-weighted imaging (HARDI)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:f9ea7c5fba138108be0310bb74fa20c4d3534e597632c661e4cb24562e1027f5
task-name: "dwi-hardi"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: analyzed-by, target: seeded-diffusion-connectivity}
  - {type: analyzed-by, target: dwi-preprocessing}
  - {type: in-program, target: program-clad}
description: |
  HARDI diffusion; frontostriatal + emotion-network white-matter structure + seed-based tractography.
---
