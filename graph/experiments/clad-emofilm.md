---
id: clad-emofilm
type: experiment
name: "EmoFilm BOLD (Wave-4 acquisition)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:c9b217b782483f07b93453df5aa9ec00deed581a549233e6b550f8a59fcf447a
task-name: "emofilm"
conditions: ["REST", "NEU", "POS", "NEG"]
edges:
  - {type: realized-by, target: dataset-clad-bids-wave4}
  - {type: co-acquired-with, target: clad-rest}
  - {type: analyzed-by, target: clad-emofilm-isc}
  - {type: analyzed-by, target: clad-emofilm-bold-amplitude}
  - {type: in-program, target: program-clad}
description: |
  Wave-4 naturalistic emotional-film BOLD (HCP-pulse replica, different scanner). The W4 realization of the inherited EmoFilm paradigm.
---
