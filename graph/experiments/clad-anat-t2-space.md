---
id: clad-anat-t2-space
type: experiment
name: "T2w SPACE (Wave-4 acquisition)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:bbaabd6927591737cd940d4a90c5fff95dfba94f4839156cbdb3e248b539bce7
voxel-mm: "0.7x0.7x0.7"
tr-ms: "3200"
te-ms: "564"
flip-deg: "T2-var"
slices: "256"
accel: "GRAPPA 2"
acq-time: "7:46"
sequence: "spc SPACE (3D)"
task-name: "anat-t2w-space"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: co-acquired-with, target: clad-anat-mprage}
  - {type: analyzed-by, target: clad-myelin-t1t2}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 T2w SPACE; with T1w gives the T1w/T2w myelin ratio.
  CONFIRMED vs the W4 Siemens Prisma protocol (materials/wave4-mri/NIJ-2016-R2-CX-0019_MR-protocol.pdf): :spc SPACE, 0.7 mm isotropic, TR 3200 / TE 564 ms, T2-variable flip, 256 sagittal slices, GRAPPA 2, BW 744 Hz/px, echo-train 1151 ms, TA 7:46.
---
