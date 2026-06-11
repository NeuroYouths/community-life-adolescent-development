---
id: clad-denoising-w4
type: method
name: "Denoising (Wave-4 params: multiband + respiratory notch)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:4a156ef287aebc936eec1413790f5ab34bde129b6495d591ae652a1569b6f260
tool: "ICA-AROMA + Nipype"
version: "0.1"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-ica-aroma-denoising", role: adapts-from-parent}
description: |
  ICA-AROMA + confound regression with a respiratory notch filter for the W4 multiband HCP-pulse data.
---
