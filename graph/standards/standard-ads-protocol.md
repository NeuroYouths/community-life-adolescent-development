---
id: standard-ads-protocol
type: standard
name: "ADS / CLAD study protocol (scan card + IRB protocol + field manual)"
created: 2026-06-11T00:00:00+00:00
modified: 2026-06-11T00:00:00+00:00
provenance-hash: sha256:f8202de9390cf07858596b3e4d9a261ebffee0e3dbc6aa9e3a70476e6bb3ffd8
standard-class: "protocol"
edges:
  - {type: in-program, target: program-clad}
description: |
  The canonical study protocol, the ground truth experiments conform to. Sources (NeuroYouths Box + ADS-MASTER): ADS-protocol.pdf (Siemens TrioTim W1-3 scanner card), IRB-Protocol-v4.docx, ADS-Field-Manual.docx (per-instrument administration), and the ADS-MASTER-SHEET task x wave matrix. Per the MRI Inventory, W1-3 imaging = MPRAGE (T1w) + DTI + Rest + EmoStroop + GoNoGo + WOFx3 (all three waves); W4 adds EmoFilm + T2w SPACE + T2w FGATIR/DIR (different scanner). No T2w/DIR in W1-3. IRON: a multi-echo GRE (T2*/QSM) sequence WAS acquired in W1-3 but NEVER PULLED into this dataset - it belonged to a separate brain-iron sub-study (Erika Raven) and was ignored; recoverable if needed. Actual W1-3 analysis pipeline (per the bashscripts repo) was FreeSurfer recon-all + FSFAST + FSQC, not fMRIPrep (the latter is the modernization target).
---
