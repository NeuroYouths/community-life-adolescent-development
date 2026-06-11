---
id: lasso-age-prediction
type: method
name: "Ridge/LASSO age prediction [inherited]"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:5078393a28a5684de42c37d5f1d5d7a0afbdefe66f025cbd7203f9264b6b9837
tool: "glmnet (R)"
version: "4.0-2"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-lasso-age-prediction", role: inherited-from-parent}
description: |
  Inherited W1-3 CMI age model; residual = CMI.
---
