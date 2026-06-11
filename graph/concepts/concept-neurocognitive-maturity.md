---
id: concept-neurocognitive-maturity
type: concept
name: "Adolescent neurocognitive maturity (Cognitive Maturity Index)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:f458ba434bb0fefe1e81d12d36c3fd8548f620d321e1dfa2e6ca21b9fa891bb5
statement: "W1-3 latent factors (inhibitory control, risk/reward, EFR) predict cognitive age; residual = CMI."
concept-kind: "construct"
status: "supported"
falsifiable: true
edges:
  - {type: tested-by-experiment, target: ads-cpt}
  - {type: tested-by-experiment, target: ads-wof}
  - {type: tested-by-experiment, target: ads-efr}
  - {type: tested-by-experiment, target: ads-temporal-discounting}
  - {type: cited-in, target: pub-eldamaty-2022-cmi}
  - {type: in-program, target: program-clad}
  - {type: cross-project, target: "ads-glimmer:concept-neurocognitive-maturity", role: inherited-from-parent}
description: |
  W1-3 latent factors (inhibitory control, risk/reward, EFR) predict cognitive age; residual = CMI.
  Inherited from ADS; the W1-3 CMI predicts W4 outcomes. Ridge R2=0.51, MAE +/-10.11mo; CMI->BAS-D->DUSI-VP.
---
