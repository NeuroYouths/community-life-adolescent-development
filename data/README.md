# data/

BIDS inputs + derivatives for CLAD. **OPEN tier + annex pointers only — no PHI, no subject-level
controlled data live here** (see [`../docs/data-governance.md`](../docs/data-governance.md)).

- `bids/` — de-identified, **defaced** BIDS (Wave-4 + W1–3). Bytes migrated via annex in the data pass.
- `derivatives/` — analysis outputs, **one dir per analysis** (names match `code/analyses/`).
- `templates/` — study-specific NICAP55 template + reference atlases (OPEN).
- `sourcedata/` — pointer only → raw DICOM in the private backend / CFMI (never committed here).
- `tabular/` — pointer only → controlled covariates / DUSI / behavioral in the private backend.
