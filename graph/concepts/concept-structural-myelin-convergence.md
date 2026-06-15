---
id: concept-structural-myelin-convergence
type: concept
name: "Structural convergence: DWI + T1w/T2w myelin (T2 gray/white boundary)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:cdb804a861395d157577dbc5b957f996f8c3b03786b000d7eacd32e6d32c8254
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
  Per the MRI Inventory, W1-3 structural = MPRAGE + DTI only (no T2w or DIR). A T2*/QSM iron (multi-echo GRE)
  sequence WAS acquired in W1-3 but never pulled (Erika Raven brain-iron sub-study) - recoverable if the
  iron axis is pursued. ads56 (W1-3 SST), the Wave-4 SST, and external NICAP/HCP templates are comparison anchors.
---
