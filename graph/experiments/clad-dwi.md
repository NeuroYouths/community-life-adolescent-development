---
id: clad-dwi
type: experiment
name: "DWI/HARDI (Wave-4 acquisition)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:e2935e4b7a5ec1078465a6f34ccd098ad8b8b1cbeaac1a6e92477bf730cafee3
task-name: "dwi-hardi"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: analyzed-by, target: clad-dwi-w4}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 diffusion MRI as HARDI (High Angular Resolution Diffusion Imaging): many diffusion-encoding directions sampled on the sphere so crossing/complex fibre populations can be resolved per voxel (vs a single tensor). Wave-4 is MULTI-SHELL (multiple b-value shells = 'multiple spheres per voxel'), enabling MSMT-CSD multi-tissue modelling (mrtrix3); W1-3 was single-shell 80-direction b=1100. Provides the seeded structural-connectivity arm onto the striatal parcels. Analysis: clad-dwi-w4 (mrtrix3 FBA lineage).
---
