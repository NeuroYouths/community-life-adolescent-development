# ADS ↔ CLAD graph migration manifest

CLAD is a **subproject of ADS** on the same N=141 cohort. Partition rules (owner):
1. anything touching **Wave-4** data is **CLAD**;
2. analyses/claims/experiments that **harmonize** ADS+CLAD connect to **both** (via `cross-project`);
3. **duplicates resolve to the parent (ADS)** — ADS is being made public; CLAD keeps **inherited copies**
   that point back with `cross-project … role: inherited-from-parent`;
4. surface connections to whichever project(s) a node touches.

This manifest is **documentation only** — it does **not** edit `ads-glimmer-graph`. The destructive prune
of ADS (removing moved nodes, adding `program-ads`, rewiring) is a **separate, reviewed PR** on the
(soon-public) ADS repo. Source: node-by-node audit of `ads-glimmer-graph/research-program/`.

## Disposition of every ADS-graph node
| ADS node | type | wave-4? | disposition | CLAD handling |
|----------|------|---------|-------------|---------------|
| `experiment-emofilm-eprime` | experiment | **yes** | **MOVE → CLAD** | CLAD-canonical as `ads-emofilm` (id-map below) |
| `method-emofilm-bold-amplitude` | method | **yes** | **MOVE → CLAD** | CLAD-canonical as `method-emofilm-bold-amplitude` |
| 5× `pub-op-*` (emofilm-violence lit) | publication | **yes** | **MOVE → CLAD** | re-attach to `concept-emofilm-violence` (verify the 5 ids before move) |
| `experiment-ads-rest` | experiment | cross-wave | **SHARED** | CLAD `ads-rest` `cross-project`→ `ads-glimmer:experiment-ads-rest` (harmonizes-with) |
| `method-striatum-group-ica` | method | cross-wave | **SHARED** | CLAD `masked-ica-parcellation` `cross-project`→ `ads-glimmer:method-striatum-group-ica` |
| `method-fmriprep` | method | cross-wave | **SHARED** | CLAD `fmriprep` `cross-project`→ `ads-glimmer:method-fmriprep` |
| `pub-eldamaty-vanmeter-2018-striatum` | publication | cross-wave | **SHARED** | CLAD `pub-eldamaty-striatal-parcellation` `cross-project`→ it |
| `concept-emofilm-violence-outcome` | concept | yes | **INHERIT (parent-canonical)** | CLAD `concept-emofilm-violence` `cross-project`→ it (parent-canonical) |
| `persona-shady-el-damaty` | persona | — | **INHERIT** | inherited copy in CLAD `cross-project`→ it |
| `org-nij` / `org-cfmi-georgetown` / `org-georgetown-university` | organization | — | **INHERIT** | inherited copies in CLAD `cross-project`→ each |
| `concept-striatum-parcellation` | concept | cross-wave | **ADS-only** | referenced from CLAD striatal work by description; no move |
| `concept-cortical-thickness-qc-error` | concept | no | **ADS-only** | — |
| `method-freesurfer-recon-all` | method | cross-wave | **ADS-only** | CLAD has its own `freesurfer-recon` (recons run on Wave-4) |
| `method-glasser-parcellation` | method | no | **ADS-only** | — |
| `pub-caisc-2026-glimmer` / `pub-eldamaty-2020-mrinit` / `pub-damaty-2020-ohbm` | publication | no | **ADS-only** | — |
| `persona-ashley-vanmeter` | persona | — | **ADS-only** | (CLAD advisor is John VanMeter) |
| ~36× striatum lit-scout (`pub-oa-*`/`pub-ep-*`/`pub-op-*`) | publication | no | **ADS-only** | ADS literature backbone |

## ID map (CLAD short id ↔ ADS verbose id)
| CLAD | ADS-canonical |
|------|---------------|
| `ads-emofilm` | `ads-glimmer:experiment-emofilm-eprime` |
| `ads-rest` | `ads-glimmer:experiment-ads-rest` |
| `masked-ica-parcellation` | `ads-glimmer:method-striatum-group-ica` |
| `fmriprep` | `ads-glimmer:method-fmriprep` |
| `concept-emofilm-violence` | `ads-glimmer:concept-emofilm-violence-outcome` |
| `pub-eldamaty-striatal-parcellation` | `ads-glimmer:pub-eldamaty-vanmeter-2018-striatum` |
| `persona-shady-el-damaty` / `org-nij` / `org-cfmi-georgetown` / `org-georgetown-university` | identical ids in `ads-glimmer:` |

## Deferred ADS-prune PR (on ads-glimmer, after review)
1. Add `program-ads` (type `program`, the parent) and `program-clad` `part-of`/`cross-project` reciprocity.
2. **Remove** the MOVE nodes (`experiment-emofilm-eprime`, `method-emofilm-bold-amplitude`, the 5 emofilm-violence lit pubs); rewire any ADS edges that referenced them.
3. Add reciprocal `cross-project` edges (ADS → CLAD) on SHARED nodes, and `in-program`→`program-ads` on ADS members.
4. Re-validate ADS against Glimmer v0.4.0.

> Verify the 5 `pub-op-*` emofilm-violence lit ids and the eldamaty2020c repo location before executing the prune.
