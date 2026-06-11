---
id: clad-anat-t2-space
type: experiment
name: "T2w SPACE (Wave-4 acquisition)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:bbaabd6927591737cd940d4a90c5fff95dfba94f4839156cbdb3e248b539bce7
task-name: "anat-t2w-space"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: co-acquired-with, target: clad-anat-mprage}
  - {type: analyzed-by, target: clad-myelin-t1t2}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 T2w SPACE; with T1w gives the T1w/T2w myelin ratio.
---
