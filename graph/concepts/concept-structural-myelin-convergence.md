---
id: concept-structural-myelin-convergence
type: concept
name: "Structural convergence: DWI + T1w/T2w myelin (T2 gray/white boundary)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:43a9190f050aa50d8711a0a9f6bab16e485ff11ed0226de6a801fe8c10bc38bb
statement: "Flagship STRUCTURE arm."
concept-kind: "research-question"
status: "open"
falsifiable: true
edges:
  - {type: tested-by-experiment, target: clad-anat-mprage}
  - {type: tested-by-experiment, target: clad-anat-t2-space}
  - {type: tested-by-experiment, target: clad-anat-dir}
  - {type: tested-by-experiment, target: clad-dwi}
  - {type: in-program, target: program-clad}
description: |
  Flagship STRUCTURE arm. (a) DIFFUSION: DTI/DWI white-matter, acquired W1-3 + W4 (the only structural
  contrast beyond T1w/MPRAGE that W1-3 has). (b) MYELIN: T1w/T2w ratio + T2 gray/white-matter boundary -
  WAVE-4 ONLY (requires T2w SPACE, which W1-3 lacks). (c) DIR (FGATIR) microstructure - WAVE-4 ONLY.
  Per the MRI Inventory, W1-3 structural = MPRAGE + DTI only (no T2w, DIR, or T2*/iron). ads56 (W1-3 SST),
  the Wave-4 SST, and external NICAP/HCP templates are comparison anchors.
---
