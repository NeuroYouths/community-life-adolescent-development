---
id: multimodal-striatal-parcellation
type: method
name: "Multimodal (functional + diffusion) striatal parcellation"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:133796b9b354d7e4df8f1d89ed4cd5312a8ddda9db00616b3717bb0e3b958568
tool: "ICA + diffusion fusion"
version: "0.1"
edges:
  - {type: composes, target: masked-ica-parcellation}
  - {type: composes, target: seeded-diffusion-connectivity}
  - {type: in-program, target: program-clad}
description: |
  Fuse functional group-ICA parcels with seed-based diffusion connectivity to define emotion vs control striatal parcels.
---
