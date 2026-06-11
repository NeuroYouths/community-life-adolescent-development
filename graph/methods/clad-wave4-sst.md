---
id: clad-wave4-sst
type: method
name: "Wave-4 study-specific template construction (W4 params)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:63b0f1c816c93a31abd78ee777f6e0af8f5ba57021ebbefcfc3d818418c7177b
tool: "antsMultivariateTemplateConstruction2"
version: "ANTs 2.x"
parameters: {k: "T1w+T2w+DIR", scanner: "wave-4 (differs from W1-3)"}
edges:
  - {type: requires-standard, target: standard-clad-wave4-sst}
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-ads-sst-mvtc2", role: adapts-from-parent}
description: |
  Builds the CLAD Wave-4 SST from W4 multicontrast structural (different scanner). Adapts the ADS ads56 MVTC2 recipe with W4 params; produces standard-clad-wave4-sst.
---
