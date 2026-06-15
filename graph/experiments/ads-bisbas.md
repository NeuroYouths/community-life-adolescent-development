---
id: ads-bisbas
type: experiment
name: "BIS/BAS scales [W1-3, inherited]"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:fcae59d1756a0a4f58e30f5b6efefac02feb2c2f5cffd89edeaa0869a7385b5c
task-name: "ads-bisbas"
edges:
  - {type: conforms-to, target: standard-ads-protocol}
  - {type: in-program, target: program-clad}
  - {type: analyzed-by, target: cfa-sem}
  - {type: cross-project, target: "ads-glimmer:experiment-bisbas", role: inherited-from-parent}
  - {type: cross-project, target: "ads-glimmer:instrument-bisbas", role: instrument}
description: |
  Reinforcement-sensitivity self-report (approach/inhibition), W1-3; BAS-D mediates CMI->violence (RQ1 mediation). Instrument: Carver & White 1994 BIS/BAS -- materials at ads-glimmer:instrument-bisbas (Box: BIS:BAS/ BIS_BAS.doc + BISBAS_scoring.pdf). Analyzed by cfa-sem (BAS-D indicator). Inherited.
---
