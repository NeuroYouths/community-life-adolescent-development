# code/

- `pipelines/` — raw→BIDS, fMRIPrep, NICAP55 template building, denoising, DWI/HARDI preproc + tractography.
- `analyses/<name>/` — one directory per **specific analysis**. Each writes its outputs to the matching
  `data/derivatives/<name>/` and is represented by a `graph/publications/` node:
  - `cmi/` → CMI latent-factor age model (RQ1)
  - `violence-cascade/` → social-strain→violence SEM (RQ2)
  - `striatal-parcellation-multimodal/` → masked group-ICA + seeded-diffusion fusion (RQ3)
  - `gonogo-frontostriatal/` → Go/NoGo frontostriatal connectivity (RQ5, control axis)
  - `efr-emofilm-synchrony/` → EFR→EmoFilm ISC (RQ4, emotion axis)
  - `corticostriatal-convergence/` → flagship multimodal convergence analysis
  - `emofilm-violence/` → EmoFilm → Wave-4 violence outcome (secondary)
- `notebooks/` — exploratory & reporting notebooks.
- `validation/` — split-half reproducibility, QC.

Code is MIT-licensed (see [`LICENSE`](LICENSE)).
