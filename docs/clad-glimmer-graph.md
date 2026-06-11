# clad-glimmer — research-object graph

Machine-readable [Glimmer](https://github.com/hebbianloop/glimmer) (**v0.4**) graph for the CLAD study,
under [`../graph/`](../graph/). Typed nodes are YAML-front-matter sidecars; `graph/_glimmer-index.json`
enumerates all nodes. **Build/regenerate** (idempotent): `python3 graph/build_clad_graph.py`.
**Validate**: `python3 <glimmer>/glimmer/tools/validate.py graph` → 0 errors.

## Node types (51 nodes)
| Dir | Type | n | What |
|-----|------|---|------|
| `programs/` | program | 1 | `program-clad` — the study container; `cross-project`→`ads-glimmer:program-ads` (subproject of ADS) |
| `concepts/` | concept | 10 | RQs/hypotheses — flagship `concept-corticostriatal-convergence` `decomposes-into` the rest |
| `experiments/` | experiment | 10 | CPT, WOF, EFR, TD, EmoFilm, Go/NoGo, rest, DWI/HARDI, **T1w MPRAGE, T2w** |
| `methods/` | method | 14 | CFA/SEM, ridge, masked-ICA, gPPI, ISC, tractography, multimodal parcellation, fMRIPrep, FreeSurfer, NICAP55 template, DWI preproc, split-half, **T1w/T2w myelin**, EmoFilm BOLD amplitude |
| `standards/` | standard | 3 | **`standard-bids`**, **`standard-nicap55-sst`** (study-specific template), **`standard-hcp`** (HCP/HCP-D comparison) |
| `publications/` | publication | 5 | CMI (published), violence-cascade (draft), striatal-parcellation (draft), convergence (planned), dissertation (aggregates) |
| `personas/` | persona | 3 | El Damaty, VanMeter, Fishbein |
| `organizations/` | organization | 3 | NIJ, Georgetown, CFMI |
| `datasets/` | dataset | 2 | Wave-4 & W1–3 BIDS pointers (`domain: clad`; bytes deferred) |
| `derivatives/`, `findings/` | — | 0 | populated as analyses run |

## v0.4 project/subproject conventions
- **Membership** — every node carries `in-program`→`program-clad`.
- **Subproject** — `program-clad` links to the parent via `cross-project`→`ads-glimmer:program-ads`.
- **Inherited / shared nodes** — duplicates resolve to the **parent ADS** (canonical); CLAD keeps an
  inherited copy with `cross-project`→`ads-glimmer:<id>` (`role: inherited-from-parent` for personas/orgs/
  the emofilm-violence concept; `role: harmonizes-with` for shared experiments/methods/pubs). See
  [`migration-ads-clad.md`](migration-ads-clad.md).
- **Local profile** — `graph/_glimmer-profiles/clad.yaml` lets cohort-level `dataset` pointers opt out of
  the neuroimaging profile's per-subject fields.

## Flagship
`concept-corticostriatal-convergence` — two axes (impulse-control + emotion) × three modalities
(behavior → function → structure). The **structure arm spans DWI + T1w/T2w myelin (T2 gray/white
boundary)**; HCP & NICAP are comparison anchors. No PHI: nodes hold only de-identified study metadata.
