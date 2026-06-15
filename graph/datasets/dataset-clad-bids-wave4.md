---
id: dataset-clad-bids-wave4
type: dataset
name: "CLAD Wave-4 BIDS (de-identified)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:09394664696f74024a1f1c16cd475af1fcb883db8bc4a4e17e7f41dba17a9f00
domain: "clad"
datalad-relative-path: "data/bids"
tier: "OPEN-deid"
bytes-status: "deferred"
edges:
  - {type: conforms-to, target: standard-bids}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 / Visit-7 BIDS: T1w MPRAGE, T2w SPACE, T2w DIR, DWI, fmap, EmoFilm BOLD, rest BOLD (61 subj local). Defaced + annexed in the data pass. Fieldmaps (W4 Prisma, PE-reversed for distortion correction): BOLD AP + PA SE-EPI (2.2x2.2x2.0, TR 4530 / TE 39, TA 0:18 each) + DWI PA SE-EPI (1.8 iso, TR 4200 / TE 76, PE R>>L, TA 0:40) — per the W4 protocol; no dedicated experiment node.
---
