---
id: ads-rest
type: experiment
name: "Resting-state fMRI"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:aaa867fa295b0ae8d1d90fcd46a28238062d979676d91b020ee14cfa038e4a0b
task-name: "rest"
duration-sec: 342
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: analyzed-by, target: masked-ica-parcellation}
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:experiment-ads-rest", role: harmonizes-with}
description: |
  Resting-state BOLD; input to masked striatal group-ICA parcellation + connectivity.
---
