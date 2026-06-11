---
id: clad-myelin-t1t2
type: method
name: "T1w/T2w myelin (Wave-4; T2 gray/white boundary)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:726064e8948d41f109b963679cf8520fc36e044e9a2ebe89b12614920cd21588
tool: "HCP-style T1w/T2w ratio"
version: "0.1"
edges:
  - {type: requires-standard, target: standard-hcp}
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-myelin-t1t2", role: adapts-from-parent}
description: |
  W4 T1w/T2w ratio + T2 gray/white-matter boundary surface contrast; the second structural axis.
---
