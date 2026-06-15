---
id: ads-efr
type: experiment
name: "Emotion Recognition Task (ERT) [W1-2 consolidated, inherited]"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:73bffb7c9de463621eab741d2bc1c9f92423d4f6f645d8476d8d5eae37808284
task-name: "ads-efr"
edges:
  - {type: conforms-to, target: standard-ads-protocol}
  - {type: analyzed-by, target: cfa-sem}
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:experiment-efr", role: inherited-from-parent}
  - {type: cross-project, target: "ads-glimmer:instrument-emotion-recognition", role: instrument}
description: |
  Off-scanner emotion-recognition task (master sheet: ERT; CMI 'EFR') using NimStim faces (Tottenham 2009). ADMINISTERED at W1-3, but usable data were CONSOLIDATED only for W1-2 (per 'Data Consolidation Status') -- W3 is a consolidation gap, NOT a non-administration. Instrument + materials: ads-glimmer:instrument-emotion-recognition (NimStim; E-Prime on the stimulus computer). Bridges to W4 EmoFilm synchrony. Inherited.
---
