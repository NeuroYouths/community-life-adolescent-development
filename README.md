# Community Life & Adolescent Development (CLAD)

Permanent, public, **PHI-free** home for the **Community Life & Adolescent Development** study —
the empirical basis for the PhD dissertation *"Adolescent Neurocognitive Maturity Mediates Paths to
Altered Social Norms & Vulnerability in Emerging Adulthood"* (Shady El Damaty, Georgetown, defended
2017; NIJ 2016-R2-CX-0019, Wave-4 / Visit-7). Sibling study to **[ads-glimmer](https://github.com/hebbianloop/ads-glimmer)**
on the same N=141 cohort.

This repository is organized **research question → analysis → expected output**, follows
**BIDS / DataLad / Glimmer** standards, and carries a machine-readable research-object graph,
**`clad-glimmer`**, under [`graph/`](graph/).

> ⚠️ **No PHI, no subject-level controlled data live here.** This repo is public (CC-BY-4.0 data/docs,
> MIT code). Controlled/PHI data are referenced by pointer to a private encrypted backend — see
> [`docs/data-governance.md`](docs/data-governance.md). Agents: read [`AGENT.md`](AGENT.md) first.

## The science in one paragraph
The two strongest neurocognitive-maturity latent factors — **inhibitory/impulse control** (CPT +
Go/NoGo) and **emotional face recognition (EFR)** — each index an individual **cortico-striatal
phenotype** that converges across modalities (behavior → function → structure) onto distinct striatal
parcels: an **impulse-control axis** (dorsal/associative caudate ↔ DLPFC/IFG; Go/NoGo connectivity +
frontostriatal DWI) and an **emotion axis** (ventral/limbic striatum ↔ vmPFC/amygdala; EmoFilm
intersubject synchrony + emotion-network DWI). Multimodal striatal parcellation recovers both; individual
deviation predicts the matching parcel's connectivity; and these predict vulnerability outcomes
(substance use, violence) — consistent with the finding that baseline medial-caudate↔prefrontal
connectivity predicts substance-use initiation 18 months later. Full spine + findings:
[`docs/research-questions.md`](docs/research-questions.md).

## Layout
| Path | What |
|------|------|
| [`docs/`](docs/) | research questions (the spine), data manifest audit, governance, protocol, preregistration, grant |
| [`code/`](code/) | pipelines + one dir per analysis (`code/analyses/<x>/`); notebooks; validation |
| [`data/`](data/) | BIDS + derivatives (one dir per analysis) + templates; **OPEN tier + annex pointers only — no PHI** |
| [`graph/`](graph/) | **clad-glimmer** research-object graph (concepts / experiments / methods / publications / …) |
| [`papers/`](papers/) | manuscript outputs (pointers to the eldamaty2020a/b/c repos) + posters/abstracts |
| [`dissertation/`](dissertation/) | the defended dissertation artifact (defense materials, monograph) |

## Status
**Skeleton (first pass).** Structure + `clad-glimmer` graph + data-manifest audit + dissertation artifacts
are in place. Wave-4 BIDS byte migration, offline (voxel-forge-duo / CFMI) recovery, and the encrypted
controlled-data backend are deferred — tracked as TODOs in [`docs/data-governance.md`](docs/data-governance.md)
and [`docs/DATA-MANIFEST.md`](docs/DATA-MANIFEST.md).

## Related
- **[ads-glimmer](https://github.com/hebbianloop/ads-glimmer)** — sibling ADS striatal-parcellation program (same cohort); shared Glimmer concepts/methods/personas.
- **[hebbianloop/eldamaty2020b](https://github.com/hebbianloop/eldamaty2020b)** — the published CMI paper (Frontiers in Psych 2022, [doi:10.3389/fpsyg.2022.1017317](https://doi.org/10.3389/fpsyg.2022.1017317)).
- **[hebbianloop/glimmer](https://github.com/hebbianloop/glimmer)** — the Glimmer research-object standard this graph follows.
