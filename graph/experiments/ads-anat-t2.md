---
id: ads-anat-t2
type: experiment
name: "T2w structural acquisition"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:c14e86eebc2b781aff5d8fbce946b1515e0d92cbbf6c22e54a16b746685cabcb
task-name: "anat-t2w"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: analyzed-by, target: myelin-t1t2-mapping}
  - {type: co-acquired-with, target: ads-anat-mprage}
  - {type: in-program, target: program-clad}
description: |
  T2w structural; with T1w gives the T1w/T2w ratio + T2 gray/white-matter boundary (myelin contrast).
---
