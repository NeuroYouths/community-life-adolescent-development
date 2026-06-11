---
id: myelin-t1t2-mapping
type: method
name: "T1w/T2w myelin mapping (T2 gray/white boundary)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:76f6129396289681e9c176352fbdc871504c40a57372d52977d3f5d25443beef
tool: "HCP-style T1w/T2w ratio + surface g/w contrast"
version: "0.1"
edges:
  - {type: requires-standard, target: standard-hcp}
  - {type: in-program, target: program-clad}
description: |
  T1w/T2w ratio + T2 gray/white-matter boundary surface contrast (HCP-style); the second structural axis alongside DWI.
---
