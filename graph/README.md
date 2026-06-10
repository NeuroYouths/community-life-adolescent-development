# clad-glimmer — research-object graph

Machine-readable [Glimmer](https://github.com/hebbianloop/glimmer) (v0.3) graph for the CLAD study.
Typed nodes as YAML-front-matter sidecars; [`_glimmer-index.json`](_glimmer-index.json) enumerates all
nodes. **Build/regenerate** (idempotent): `python3 graph/build_clad_graph.py`.

## Node types
| Dir | Type | n | What |
|-----|------|---|------|
| `concepts/` | concept | 9 | research questions / hypotheses — flagship `concept-corticostriatal-convergence` `decomposes-into` the rest |
| `experiments/` | experiment | 8 | tasks/acquisitions (CPT, WOF, EFR, TD, EmoFilm, Go/NoGo, rest, DWI/HARDI) |
| `methods/` | method | 12 | CFA/SEM, ridge age-prediction, masked-ICA, gPPI, ISC, tractography, multimodal parcellation, fMRIPrep, FreeSurfer, NICAP55, DWI preproc, split-half |
| `publications/` | publication | 5 | CMI (published), violence-cascade (draft), striatal-parcellation (draft), convergence (planned), dissertation (aggregates) |
| `personas/` | persona | 3 | El Damaty, VanMeter, Fishbein |
| `organizations/` | organization | 3 | NIJ, Georgetown, CFMI |
| `datasets/` | dataset | 2 | Wave-4 & W1–3 BIDS pointers (bytes deferred) |
| `derivatives/`, `findings/` | derivative, finding | 0 | populated as analyses run (each `finding` grounded in a `derivative`, with `reasoning-trace` for agent outputs) |

## Conventions
- Edge vocabulary mirrors Glimmer: `decomposes-into`, `tested-by-experiment`, `addresses-concept`,
  `authored-by`, `aggregates`, `cites-method`, `funded-by`, `composes`, `realized-by`, `conforms-to-standard`,
  `part-of`, `affiliated-with`, `cited-in`.
- Shared ids with **ads-glimmer** (`persona-shady-el-damaty`, `org-nij`, `org-georgetown-university`,
  `org-cfmi-georgetown`) are intentional — same cohort, one identity. `upstream-graph` in the index points
  to ads-glimmer-graph. Cross-study concept links (e.g. ads-glimmer `concept-emofilm-violence-outcome`,
  `concept-striatum-parcellation`) are noted in node descriptions; hard cross-graph edges await a merged index.
- No PHI: nodes hold only de-identified study metadata, hypotheses, methods, and outputs.
