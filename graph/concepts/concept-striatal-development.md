---
id: concept-striatal-development
type: concept
name: "Striatal functional parcellation across development (W1-3) + W4 validation"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:3e9bfed0b48e9454befc7d10303a9b0100023eda0554e3da0636fa39c747c562
statement: "The masked group-ICA striatal parcellation was done on WAVE-1 resting-state (parent-canonical in ADS; the 2017 dissertation)."
concept-kind: "research-question"
status: "under-investigation"
falsifiable: true
edges:
  - {type: tested-by-experiment, target: clad-rest}
  - {type: tested-by-experiment, target: clad-dwi}
  - {type: cited-in, target: pub-eldamaty-striatal-parcellation}
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:concept-striatum-parcellation", role: parent-canonical}
description: |
  The masked group-ICA striatal parcellation was done on WAVE-1 resting-state (parent-canonical in ADS; the 2017 dissertation). Wave-4
  was NOT complete and used a DIFFERENT scanner/data — so the CLAD question is validating + applying the W1-3
  parcels to W4 (multimodal: functional + seeded diffusion).
---
