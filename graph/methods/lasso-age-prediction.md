---
id: lasso-age-prediction
type: method
name: "Regularized (ridge/LASSO) age prediction"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:0ed3bbf37fb3f5203851c40346fd061a16cdbba4358f00919c90389a626b4e62
tool: "glmnet (R)"
version: "4.0-2"
edges:
  - {type: in-program, target: program-clad}
description: |
  Cross-validated regularized regression of latent factors on age; residual = CMI.
---
