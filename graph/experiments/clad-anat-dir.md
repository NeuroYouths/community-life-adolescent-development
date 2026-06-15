---
id: clad-anat-dir
type: experiment
name: "T2w DIR double-inversion-recovery (Wave-4 acquisition)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:5c9366cf2238f2e12e6863f884d5673fe64a3a3357be86242fa3ed043abb64bf
voxel-mm: "0.9x0.9x0.9"
tr-ms: "7500"
te-ms: "318"
ti1-ms: "3000"
ti2-ms: "450"
flip-deg: "T2-var"
slices: "256"
accel: "GRAPPA PAT 4"
acq-time: "6:32"
sequence: "spcir SPACE double-IR (DIR)"
task-name: "anat-dir"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: co-acquired-with, target: clad-anat-mprage}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 double-inversion-recovery (FGATIR/DIR) structural; the T2 gray/white-matter boundary + WM/GM microstructure contrast.
  CONFIRMED vs the W4 Siemens Prisma protocol (materials/wave4-mri/NIJ-2016-R2-CX-0019_MR-protocol.pdf): :spcir SPACE double-inversion-recovery (DIR), 0.9 mm isotropic, TR 7500 / TE 318 ms, Non-sel DIR TI1 3000 / TI2 450 ms, 256 sagittal slices, GRAPPA 3D PAT 4, BW 376 Hz/px, TA 6:32. NAMING: the Wave-4 BIDS names `dir` (DIR); the protocol's separate FGATIR cards (single-IR :tfl) are NOT the W4 BIDS sequence — corrected from the earlier 'FGATIR/DIR' label.
---
