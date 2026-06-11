---
id: clad-emofilm-bold-amplitude
type: method
name: "EmoFilm BOLD amplitude (Wave-4)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:af64544a07a17f7b418cf68b0692ee61491b4ad55632995fcdc9fc7d0e65b83e
tool: "fMRI amplitude extraction"
version: "0.1"
edges:
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:method-emofilm-bold-amplitude", role: adapts-from-parent}
description: |
  W4 EmoFilm amygdala/PFC BOLD amplitude for the violence-outcome model.
---
