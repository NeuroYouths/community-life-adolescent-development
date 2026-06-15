---
id: clad-myelin-t1t2
type: method
name: "T1w/T2w myelin (Wave-4; T2 gray/white boundary)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:726064e8948d41f109b963679cf8520fc36e044e9a2ebe89b12614920cd21588
code: "none committed — planned (HCP-style T1w/T2w myelin ratio + T2 gray/white boundary; nipype/surface_correspondence.py is the closest leg)"
code-repo: "github.com/hebbianloop/ads-glimmer-code"
code-commit: "cb76a3b31c9408af80e0d00c697ac1db4e8a76f7"
algorithm: "HCP-style T1w/T2w myelin mapping over the FreeSurfer recons"
tool: "HCP-style T1w/T2w ratio"
version: "0.1"
edges:
  - {type: requires-standard, target: standard-hcp}
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-myelin-t1t2", role: adapts-from-parent}
description: |
  W4 T1w/T2w ratio + T2 gray/white-matter boundary surface contrast; the second structural axis.
---
