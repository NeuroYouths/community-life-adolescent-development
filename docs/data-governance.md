# CLAD — Data Governance

This repository is **public**. The binding rule is simple: **no PHI and no subject-level controlled
data are committed here, ever.** This document defines the tiers, where each lives, and how the rule
is enforced.

## Tiers
| Tier | Definition | Examples | Home |
|------|------------|----------|------|
| **OPEN** | De-identified, shareable, no subject-level sensitivity | research questions, methods/code, protocols, data dictionary, parcellation atlases, NICAP55 template, EmoFilm timing, the clad-glimmer graph, **defaced** group-level derivatives | **this public repo** (git; large binaries → encrypted annex by pointer) |
| **CONTROLLED** | No direct identifiers but subject-level & sensitive (requires data-use agreement under NIJ terms) | master covariates, DUSI scores, Go/NoGo & BIS/BAS rows, EmoFilm E-Prime logs, subject-level BIDS niftis | **private encrypted backend** (referenced here by pointer only) |
| **PHI** | Identifiable | raw identified DICOM, ADS-ID↔BIDS-ID crosswalk, dates of birth/visit, names/MRN | **private encrypted backend / CFMI**; never leaves controlled storage |

## Where controlled/PHI data live (the backend)
This pass references — but does not build — the controlled/PHI backend. Recommended:
- **Revive `NeuroYouths/clad-master`** (already a modular, git-crypt-encrypted DataLad superdataset) as
  the private controlled/PHI home; and/or
- An **encrypted git-annex special remote** (Hetzner Storage Box, as in ads-glimmer), holding only
  **defaced, de-identified** content; identified raw stays on CFMI / offline storage.

Pointers in this repo (`data/sourcedata/README.md`, `data/tabular/README.md`) name the backend location;
they contain **no** subject data.

## Enforcement
1. **No imaging/subject bytes committed in the skeleton pass.** De-identified BIDS is migrated only
   after defacing, via the annex, in a later pass.
2. **Defacing** (`pydeface` / `mri_deface`) is mandatory on all anatomicals before annex/publication.
3. **Pre-commit / CI NO-PHI gate**: the staged tree is grepped for subject IDs, crosswalk values, and
   known identifier patterns; a non-empty match fails the commit/PR. (To be wired as a hook;
   `git grep` check documented in the repo verification steps meanwhile.)
4. **Agents** must obey [`../AGENT.md`](../AGENT.md) §1 (NO PHI) — stop and surface rather than fetch
   controlled data into this tree.

## TODO (data-migration pass)
- [ ] Wire DataLad + encrypted annex special remote; set `annex.numcopies`.
- [ ] Revive `clad-master` as the controlled/PHI backend; document the exact pointer targets.
- [ ] Deface + de-identify Wave-4 BIDS; migrate the OPEN tier into `data/bids/` via annex.
- [ ] Implement the NO-PHI pre-commit hook + CI check.
- [ ] Confirm NIJ data-use-agreement language for the CONTROLLED tier release.
