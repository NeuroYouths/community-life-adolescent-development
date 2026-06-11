---
id: ads-efr
type: experiment
name: "Emotional Face Recognition (EFR)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:82547ddacb868fa799a65dfe28f043bff5bbcdf091e2565369f7033ed18c17b2
task-name: "efr"
conditions: ["happy", "angry", "fearful", "sad", "disgust", "surprise", "neutral"]
n-trials: 70
edges:
  - {type: analyzed-by, target: cfa-sem}
  - {type: in-program, target: program-clad}
description: |
  NimStim facial-emotion recognition; accuracy + RT for positive/negative affect.
---
