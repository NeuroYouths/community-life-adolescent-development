# clad-glimmer — research-object graph

Machine-readable [Glimmer](https://github.com/hebbianloop/glimmer) (**v0.4**) graph for the CLAD study,
under [`../graph/`](../graph/). Typed nodes are YAML-front-matter sidecars; `graph/_glimmer-index.json`
enumerates all nodes. **Build/regenerate** (idempotent): `python3 graph/build_clad_graph.py`.
**Validate**: `python3 <glimmer>/glimmer/tools/validate.py graph` → 0 errors.

## Node types (57 nodes)
| Dir | Type | n | What |
|-----|------|---|------|
| `programs/` | program | 1 | `program-clad` — subproject; `cross-project`→`ads-glimmer:program-ads` |
| `concepts/` | concept | 12 | flagship `concept-corticostriatal-convergence` + sub-concepts + methodological RQs (`-w13-analytic-validation`, `-scanner-harmonization`) |
| `experiments/` | experiment | 16 | **inherited W1–3 paradigms** (CPT/WOF/EFR/TD/Go-NoGo/EmoFilm) + battery (DUSI-R, BIS/BAS, context, community-life) + **CLAD W4 acquisitions** (EmoFilm, rest, T1w MPRAGE, T2w SPACE, **DIR**, DWI) |
| `methods/` | method | 12 | inherited (CFA/SEM, ridge, split-half) + **W4-adapted** (fMRIPrep-w4, denoising-w4, masked-ICA-w4, DWI-w4, EmoFilm ISC + BOLD-amplitude, T1w/T2w myelin, **Wave-4 SST**) + multimodal fusion |
| `standards/` | standard | 3 | `standard-bids`, **`standard-clad-wave4-sst`** (CLAD W4 SST, owned) , `standard-hcp` (HCP comparison); **inherits `ads-glimmer:standard-ads56-sst`** (W1–3 SST) + NICAP/NICAP55 comparisons via cross-project |
| `publications/` | publication | 5 | CMI (published), violence-cascade (draft), striatal-parcellation (draft), convergence (planned), dissertation (aggregates) |
| `personas/` | persona | 3 | El Damaty, VanMeter, Fishbein |
| `organizations/` | organization | 3 | NIJ, Georgetown, CFMI |
| `datasets/` | dataset | 2 | Wave-4 & W1–3 BIDS pointers (`domain: clad`; bytes deferred) |
| `derivatives/`, `findings/` | — | 0 | populated as analyses run |

**Wave attribution:** W1–3 paradigms/instruments are ADS-owned and *inherited* here (`cross-project … role: inherited-from-parent`) because W1–3 behavior predicts W4 outcomes; Wave-4 acquisitions + the Wave-4 SST + W4-adapted pipelines (different scanner/params) are CLAD-owned (W4-adapted methods carry `role: adapts-from-parent`).

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
