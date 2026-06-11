---
id: ads-anat-mprage
type: experiment
name: "T1w MPRAGE structural acquisition"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:d71968cf6a852c5697c5db36ba2b1510d1e76c8d352c7083a56f44db36187053
task-name: "anat-t1w"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: analyzed-by, target: freesurfer-recon}
  - {type: analyzed-by, target: nicap55-template}
  - {type: analyzed-by, target: myelin-t1t2-mapping}
  - {type: in-program, target: program-clad}
description: |
  T1w MPRAGE; feeds FreeSurfer recons, the NICAP55 study-specific template, and T1w/T2w myelin.
---
