---
id: clad-anat-mprage
type: experiment
name: "T1w MPRAGE (Wave-4 acquisition)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:dca7a8a39259971c5ead4a6413deb4d1f3747499dab29a592caec41d139fefc7
task-name: "anat-t1w"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: analyzed-by, target: clad-wave4-sst}
  - {type: analyzed-by, target: clad-myelin-t1t2}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 T1w MPRAGE; feeds the Wave-4 SST + T1w/T2w myelin.
---
