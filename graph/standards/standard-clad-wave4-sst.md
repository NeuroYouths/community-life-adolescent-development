---
id: standard-clad-wave4-sst
type: standard
name: "CLAD Wave-4 study-specific template (SST)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:fe034880e60c611e74a688c8d83261176632b9867b750374f98b75aa83d61752
standard-class: "template"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:standard-ads56-sst", role: compared-against}
  - {type: cross-project, target: "ads-glimmer:standard-nicap55", role: compared-against}
  - {type: cross-project, target: "ads-glimmer:standard-nicap", role: compared-against}
description: |
  CLAD-OWNED. Built from Wave-4 multicontrast structural (T1w/T2w/DIR) on the W4 scanner. The W4 normalization target. Compared against ads56 (W1-3 SST, inherited) and the external NICAP/NICAP55 templates.
---
