# AGENT.md — operating rules for agents in this repository

This repository is the public home of the CLAD study. Any agent (human-directed or autonomous) working
here MUST follow these rules. They are not advisory.

## 1. NO PHI — ever
- This repo is **public**. Never commit, write, or echo: subject identifiers, the ADS-ID↔BIDS-ID
  crosswalk, dates of birth/visit, names, MRN, raw identified DICOM headers, or any subject-level
  controlled covariate (genetics, substance-use rows, survey responses).
- De-identified imaging must be **defaced** before it is ever annexed; until the data-migration pass
  wires the encrypted annex, **no imaging/subject bytes are committed at all**.
- Controlled/PHI data live in a private encrypted backend (see [`docs/data-governance.md`](docs/data-governance.md)),
  referenced here only by pointer. If a task would require reading or writing such data, stop and
  surface it — do not fetch it into this tree.
- A pre-commit / CI gate greps the staged tree for subject IDs and crosswalk values; commits must be clean.

## 2. Read the graph first
- The machine-readable research object is [`graph/`](graph/) — the **clad-glimmer** Glimmer graph.
  Load [`graph/_glimmer-index.json`](graph/_glimmer-index.json) to enumerate nodes, then read the
  relevant `concept` / `method` / `publication` nodes before reasoning about the science.
- The flagship hypothesis is `concept-corticostriatal-convergence`; follow its `decomposes-into`
  edges to the impulse-control and emotion sub-concepts.
- Node format + edge vocabulary mirror [hebbianloop/glimmer](https://github.com/hebbianloop/glimmer);
  rebuild the graph with [`graph/build_clad_graph.py`](graph/build_clad_graph.py) (idempotent).

## 3. Structure conventions
- **Specific analyses** live in `code/analyses/<name>/`; their **outputs** in `data/derivatives/<name>/`
  (same `<name>`). Pipelines (raw→BIDS, fMRIPrep, template, DWI) live in `code/pipelines/`.
- **Notebooks** in `code/notebooks/`. **Manuscripts/artifacts** in `papers/` and `dissertation/`.
- Every research question in [`docs/research-questions.md`](docs/research-questions.md) maps to a
  `code/analyses/<x>/`, a `data/derivatives/<x>/`, and a `graph/publications/` node.

## 4. Provenance & cross-study
- New empirical claims are `finding` nodes grounded in `derivative` nodes; agent-produced findings
  MUST carry a `reasoning-trace` (per the Glimmer agent protocol).
- CLAD shares its cohort with **ads-glimmer**; reuse shared `persona`/`organization`/`concept` ids
  rather than duplicating them, and cross-link with edges.
