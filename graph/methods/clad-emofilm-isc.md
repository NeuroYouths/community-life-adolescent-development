---
id: clad-emofilm-isc
type: method
name: "Intersubject synchrony (ISC) on EmoFilm"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:bcce5b4cab209cfb67a16da257f52f94274f39c71a186f35a72ae5045e9d0950
code: "nipype/emofilm_model.py (ISC leg)"
code-repo: "github.com/hebbianloop/ads-glimmer-code"
code-commit: "cb76a3b31c9408af80e0d00c697ac1db4e8a76f7"
algorithm: "inter-subject correlation on the naturalistic film"
tool: "BrainIAK ISC"
version: "0.x"
edges:
  - {type: in-program, target: program-clad}
description: |
  CLAD-owned: intersubject correlation of W4 EmoFilm BOLD; relate pairwise synchrony to EFR-latent similarity.
---
