# data/sourcedata/ — POINTER ONLY

Raw identified DICOM is **PHI** and is NOT stored here. It lives in the private controlled backend
(CFMI / voxel-forge-duo / encrypted store). De-identified, defaced BIDS derived from it is migrated
to `../bids/` via the encrypted annex in the data-migration pass.

See [`../../docs/data-governance.md`](../../docs/data-governance.md). No subject data in this directory.
