---
id: nicap55-template
type: method
name: "NICAP55 study-specific template construction"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:4ac55759bb05f229e3e360fac1fb8acadd9c8190021827f3f520718cf16f8e4e
tool: "ANTs multivariate template"
version: "ANTs 2.x"
edges:
  - {type: requires-standard, target: standard-nicap55-sst}
  - {type: in-program, target: program-clad}
description: |
  Builds the age-appropriate multicontrast developmental template (T1w/T2w) all CLAD imaging normalizes to.
---
