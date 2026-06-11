---
id: split-half-reproducibility
type: method
name: "Split-half ICA reproducibility [harmonized]"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:65c5d0d151acc3f8475d91e5dd4fae10b575afdb1c1cdcd7a976b22f98fc3311
tool: "Munkres + Dice"
version: "0.1"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-split-half-ica-reproducibility", role: harmonizes-with}
description: |
  Harmonized with the ADS split-half method; applied to W4 parcels.
---
