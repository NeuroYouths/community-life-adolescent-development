---
id: split-half-reproducibility
type: method
name: "Split-half reproducibility validation"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:26ed88f9f3b2b9a2b01f87d7c10859249d2c9fb0d9378c721fdc4abae3b03195
tool: "custom (Munkres matching + correlation)"
version: "0.1"
edges:
  - {type: in-program, target: program-clad}
description: |
  Repeated split-half ICA + Hungarian matching to select reproducible striatal model order (k~5 primary, ~8-10 fine).
---
