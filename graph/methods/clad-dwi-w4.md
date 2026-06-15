---
id: clad-dwi-w4
type: method
name: "DWI tractography (Wave-4)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:863b2bf4d3f7e1edeaa1602281363e44b0f19683ec3f80b596f68a12ba22810d
code: "nipype/dwi_mrtrix3.py"
code-repo: "github.com/hebbianloop/ads-glimmer-code"
code-commit: "cb76a3b31c9408af80e0d00c697ac1db4e8a76f7"
algorithm: "multi-shell HARDI: dwidenoise→mrdegibbs→dwifslpreproc→dhollander→MSMT-CSD→iFOD2→SIFT2→tck2connectome + FBA (mrtrix3)"
tool: "MRtrix3 / probtrackx"
version: "MRtrix3 3.0"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-dwi-fba-mrtrix3", role: adapts-from-parent}
description: |
  W4 seeded probabilistic tractography for striatal structural connectivity.
---
