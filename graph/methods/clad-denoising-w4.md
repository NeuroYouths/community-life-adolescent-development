---
id: clad-denoising-w4
type: method
name: "Denoising (Wave-4 params: multiband + respiratory notch)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:4a156ef287aebc936eec1413790f5ab34bde129b6495d591ae652a1569b6f260
code: "nipype/fmriprep_confounds.py"
code-repo: "github.com/hebbianloop/ads-glimmer-code"
code-commit: "cb76a3b31c9408af80e0d00c697ac1db4e8a76f7"
algorithm: "ICA-AROMA + WM/CSF + FD-censor + respiratory notch (HCP multiband)"
tool: "ICA-AROMA + Nipype"
version: "0.1"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-ica-aroma-denoising", role: adapts-from-parent}
description: |
  ICA-AROMA + confound regression with a respiratory notch filter for the W4 multiband HCP-pulse data.
---
