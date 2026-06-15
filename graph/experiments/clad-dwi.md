---
id: clad-dwi
type: experiment
name: "DWI/HARDI (Wave-4 acquisition)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:e2935e4b7a5ec1078465a6f34ccd098ad8b8b1cbeaac1a6e92477bf730cafee3
voxel-mm: "1.8x1.8x1.8"
tr-ms: "4500"
te-ms: "102"
slices: "90"
accel: "SMS 3"
b-values: "1000/2000/3000 s/mm2"
directions: "77 vols (71 weighted: 12xb1000+24xb2000+35xb3000 + 6 b0)"
acq-time: "6:04"
sequence: "epse multi-shell HARDI"
task-name: "dwi-hardi"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: analyzed-by, target: clad-dwi-w4}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 diffusion MRI as HARDI (High Angular Resolution Diffusion Imaging): many diffusion-encoding directions sampled on the sphere so crossing/complex fibre populations can be resolved per voxel (vs a single tensor). Wave-4 is MULTI-SHELL (multiple b-value shells = 'multiple spheres per voxel'), enabling MSMT-CSD multi-tissue modelling (mrtrix3); W1-3 was single-shell 80-direction b=1100. Provides the seeded structural-connectivity arm onto the striatal parcels. Analysis: clad-dwi-w4 (mrtrix3 FBA lineage).
  CONFIRMED vs the W4 Siemens Prisma protocol (materials/wave4-mri/NIJ-2016-R2-CX-0019_MR-protocol.pdf) + the Caruyer .dvs scheme: :epse, 1.8 mm isotropic, TR 4500 / TE 102 ms, SMS 3, 90 slices, PE A>>P, BW 2066, EPI factor 110; MULTI-SHELL b=[1000,2000,3000] s/mm2, 77 volumes (71 weighted dirs 12/24/35 across shells + 6 b0), TA 6:04. PE-reversed DWI fieldmap (PA SE-EPI, R>>L).
---
