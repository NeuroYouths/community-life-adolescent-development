---
id: clad-dwi-w4
type: method
name: "DWI tractography (Wave-4)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:863b2bf4d3f7e1edeaa1602281363e44b0f19683ec3f80b596f68a12ba22810d
tool: "MRtrix3 / probtrackx"
version: "MRtrix3 3.0"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-dwi-fba-mrtrix3", role: adapts-from-parent}
description: |
  W4 seeded probabilistic tractography for striatal structural connectivity.
---
