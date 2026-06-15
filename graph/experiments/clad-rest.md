---
id: clad-rest
type: experiment
name: "Resting-state BOLD (Wave-4 acquisition)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:465e42d016483276a431175d490e4f76125f8c348cef0e2a11f72a5c5f848ccf
voxel-mm: "2.2x2.2x2.0"
tr-ms: "727"
te-ms: "31"
flip-deg: "30"
slices: "60"
accel: "SMS 6"
volumes: "480"
acq-time: "5:58"
sequence: "epfid GE-EPI"
task-name: "rest"
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: analyzed-by, target: clad-masked-ica-w4}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 resting-state BOLD; input to the W4 masked striatal group-ICA (validation of W1-3 parcels).
  CONFIRMED vs the W4 Siemens Prisma protocol (materials/wave4-mri/NIJ-2016-R2-CX-0019_MR-protocol.pdf): :epfid GE-EPI, 2.2x2.2x2.0 mm, TR 727 / TE 31 ms, flip 30 deg, SMS 6, 60 slices, PE A>>P, BW 2646, 480 volumes, TA 5:58; PE-reversed BOLD fieldmaps (AP+PA SE-EPI).
---
