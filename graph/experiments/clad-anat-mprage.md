---
id: clad-anat-mprage
type: experiment
name: "T1w MPRAGE (Wave-4 acquisition)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:dca7a8a39259971c5ead4a6413deb4d1f3747499dab29a592caec41d139fefc7
voxel-mm: "0.7x0.7x0.7"
tr-ms: "2400"
te-ms: "2.32"
ti-ms: "1110"
flip-deg: "8"
slices: "256"
accel: "GRAPPA 2"
acq-time: "6:47"
sequence: "tfl MPRAGE"
task-name: "anat-t1w"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: analyzed-by, target: clad-wave4-sst}
  - {type: analyzed-by, target: clad-myelin-t1t2}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 T1w MPRAGE; feeds the Wave-4 SST + T1w/T2w myelin.
  CONFIRMED vs the W4 Siemens Prisma protocol (materials/wave4-mri/NIJ-2016-R2-CX-0019_MR-protocol.pdf): :tfl MPRAGE, 0.7 mm isotropic, TR 2400 / TE 2.32 / TI 1110 ms (non-sel IR), flip 8 deg, 256 sagittal slices, GRAPPA 2, BW 210 Hz/px, water-excitation fat-suppr, TA 6:47.
---
