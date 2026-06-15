---
id: multimodal-striatal-parcellation
type: method
name: "Multimodal striatal parcellation (functional + diffusion)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:6641dfc3897f649ebe790089aad85eb526c48d8b40b6ff561e1deab8a008218c
code: "analysis/make_Parcels.py + nipype/dwi_mrtrix3.py + nipype/connectivity_stats.py (functional×diffusion fusion)"
code-repo: "github.com/hebbianloop/ads-glimmer-code"
code-commit: "cb76a3b31c9408af80e0d00c697ac1db4e8a76f7"
algorithm: "fuse functional group-ICA parcels with seed-based diffusion connectivity"
tool: "ICA + diffusion fusion"
version: "0.1"
edges:
  - {type: composes, target: clad-masked-ica-w4}
  - {type: composes, target: clad-dwi-w4}
  - {type: in-program, target: program-clad}
description: |
  Fuse W4 functional group-ICA parcels with seed-based diffusion connectivity (emotion vs control parcels).
---
