#!/usr/bin/env python3
"""build_clad_graph.py — emit the clad-glimmer research-object graph (idempotent).

CLAD is the Wave-4 / Visit-7 SUBPROJECT of ADS (same cohort). Glimmer v0.4 conventions:
  - every node `in-program` -> program-clad (membership);
  - W1-3 paradigms/instruments are ADS-owned and INHERITED here via `cross-project` -> ads-glimmer:<id>
    (role inherited-from-parent) — W1-3 behavior predicts W4 outcomes (forward direction);
  - W4 acquisitions + the Wave-4 SST + W4-adapted pipelines are CLAD-OWNED; W4-adapted methods
    `cross-project` -> the ADS lineage method (role adapts-from-parent), bodies note the W4 param diffs;
  - templates: ads56 = ADS W1-3 SST (inherited); standard-clad-wave4-sst = CLAD W4 SST (owned, different
    scanner); NICAP/NICAP55 + HCP are EXTERNAL comparison projects (cross-project to ADS canonical).

No PHI. Usage: python3 graph/build_clad_graph.py
"""
import hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TS = "2026-06-11T00:00:00+00:00"
SCHEMA = "glimmer/v0.4.0"
DATASET = "clad-glimmer"
PROGRAM = "program-clad"

TYPE_DIR = {
    "concept": "concepts", "experiment": "experiments", "method": "methods",
    "standard": "standards", "publication": "publications", "persona": "personas",
    "organization": "organizations", "program": "programs", "dataset": "datasets",
    "derivative": "derivatives", "finding": "findings",
}

# cross-project edges (node id -> [(namespaced-target, role)]). ADS is the parent / canonical owner.
CROSS = {
    # subproject link
    "program-clad": [("ads-glimmer:program-ads", "subproject-of-parent")],
    # inherited identities
    "persona-shady-el-damaty":   [("ads-glimmer:persona-shady-el-damaty", "inherited-from-parent")],
    "org-nij":                   [("ads-glimmer:org-nij", "inherited-from-parent")],
    "org-georgetown-university": [("ads-glimmer:org-georgetown-university", "inherited-from-parent")],
    "org-cfmi-georgetown":       [("ads-glimmer:org-cfmi-georgetown", "inherited-from-parent")],
    # inherited W1-3 paradigms (forward: predict W4 outcomes)
    "ads-cpt":                   [("ads-glimmer:experiment-cpt", "inherited-from-parent")],
    "ads-wof":                   [("ads-glimmer:experiment-wof", "inherited-from-parent")],
    "ads-efr":                   [("ads-glimmer:experiment-efr", "inherited-from-parent")],
    "ads-temporal-discounting":  [("ads-glimmer:experiment-temporal-discounting", "inherited-from-parent")],
    "ads-gonogo":                [("ads-glimmer:experiment-gonogo", "inherited-from-parent")],
    "ads-emocountstroop":        [("ads-glimmer:experiment-emocountstroop", "inherited-from-parent")],
    "ads-emofilm-paradigm":      [("ads-glimmer:experiment-emofilm-eprime", "inherited-from-parent")],
    # inherited battery + environmental/community-life assessment
    "ads-dusi-r":                [("ads-glimmer:experiment-dusi-r", "inherited-from-parent")],
    "ads-bisbas":                [("ads-glimmer:experiment-bisbas", "inherited-from-parent")],
    "ads-context-battery":       [("ads-glimmer:experiment-context-battery", "inherited-from-parent")],
    "ads-community-life":        [("ads-glimmer:experiment-community-life-assessment", "inherited-from-parent")],
    # inherited methods (W1-3 CMI + shared infrastructure)
    "cfa-sem":                   [("ads-glimmer:method-cfa-sem", "inherited-from-parent")],
    "lasso-age-prediction":      [("ads-glimmer:method-lasso-age-prediction", "inherited-from-parent")],
    "split-half-reproducibility":[("ads-glimmer:method-split-half-ica-reproducibility", "harmonizes-with")],
    # W4-adapted methods (different params) -> ADS lineage
    "clad-fmriprep-w4":          [("ads-glimmer:method-fmriprep", "adapts-from-parent")],
    "clad-denoising-w4":         [("ads-glimmer:method-ica-aroma-denoising", "adapts-from-parent")],
    "clad-masked-ica-w4":        [("ads-glimmer:method-striatum-group-ica", "adapts-from-parent")],
    "clad-emofilm-bold-amplitude":[("ads-glimmer:method-emofilm-bold-amplitude", "adapts-from-parent")],
    "clad-myelin-t1t2":          [("ads-glimmer:method-myelin-t1t2", "adapts-from-parent")],
    "clad-dwi-w4":               [("ads-glimmer:method-dwi-fba-mrtrix3", "adapts-from-parent")],
    "clad-wave4-sst":            [("ads-glimmer:method-ads-sst-mvtc2", "adapts-from-parent")],
    # concepts: inherited / parent-canonical
    "concept-neurocognitive-maturity": [("ads-glimmer:concept-neurocognitive-maturity", "inherited-from-parent")],
    "concept-violence-cascade":        [("ads-glimmer:concept-violence-cascade", "inherited-from-parent")],
    "concept-striatal-development":    [("ads-glimmer:concept-striatum-parcellation", "parent-canonical")],
    "concept-emofilm-violence":        [("ads-glimmer:concept-emofilm-violence-outcome", "parent-canonical")],
    "concept-w13-analytic-validation": [("ads-glimmer:concept-w13-analytic-validation", "inherited-from-parent")],
    "concept-scanner-harmonization":   [("ads-glimmer:concept-scanner-harmonization", "inherited-from-parent")],
    # standards: inherited W1-3 SST + external comparisons
    "standard-clad-wave4-sst":   [("ads-glimmer:standard-ads56-sst", "compared-against"),
                                  ("ads-glimmer:standard-nicap55", "compared-against"),
                                  ("ads-glimmer:standard-nicap", "compared-against")],
    "standard-bids":             [("ads-glimmer:standard-bids", "inherited-from-parent")],
    "standard-hcp":              [("ads-glimmer:standard-hcp", "compared-against")],
    # publications: parent-canonical / harmonizing
    "pub-eldamaty-2022-cmi":     [("ads-glimmer:pub-ads-cmi", "parent-canonical")],
    "pub-eldamaty-striatal-parcellation": [("ads-glimmer:pub-ads-masked-ica-parcellation", "harmonizes-with")],
}

N = []
def node(id, type, name, fields=None, edges=None, desc=""):
    N.append({"id": id, "type": type, "name": name,
              "fields": fields or {}, "edges": edges or [], "desc": desc.strip()})

# ---------------- PROGRAM ----------------
node(PROGRAM, "program", "Community Life & Adolescent Development (CLAD)",
     {"program-kind": "subproject", "status": "active",
      "outcome-measure": "violence proneness & substance-use initiation (DUSI-VP); neurocognitive maturity (CMI)"},
     [("led-by", "persona-shady-el-damaty"), ("funded-by", "org-nij"),
      ("addresses-concept", "concept-corticostriatal-convergence"),
      ("cited-in", "pub-eldamaty-2017-dissertation")],
     """The NIJ 2016-R2-CX-0019 Wave-4 / Visit-7 subproject of the Adolescent Development Study (ADS),
same N=141 cohort. Subproject-of the parent ADS program (cross-graph). W1-3 paradigms/instruments are
inherited from ADS (they predict W4 outcomes); Wave-4 acquisitions, the Wave-4 SST, and W4-adapted
pipelines (different scanner/params) are CLAD-owned.""")

# ---------------- CONCEPTS ----------------
node("concept-corticostriatal-convergence", "concept",
     "Cortico-striatal multimodal convergence (flagship)",
     {"concept-kind": "hypothesis", "status": "under-investigation", "falsifiable": True},
     [("decomposes-into", "concept-neurocognitive-maturity"),
      ("decomposes-into", "concept-impulse-control-frontostriatal"),
      ("decomposes-into", "concept-gonogo-inhibition"),
      ("decomposes-into", "concept-efr-individual-differences"),
      ("decomposes-into", "concept-emofilm-synchrony"),
      ("decomposes-into", "concept-striatal-development"),
      ("decomposes-into", "concept-structural-myelin-convergence"),
      ("tested-by-experiment", "ads-cpt"), ("tested-by-experiment", "ads-gonogo"),
      ("tested-by-experiment", "ads-efr"), ("tested-by-experiment", "clad-emofilm"),
      ("tested-by-experiment", "clad-dwi"), ("tested-by-experiment", "clad-anat-mprage"),
      ("tested-by-experiment", "clad-anat-dir"),
      ("funded-by", "org-nij"), ("authored-by", "persona-shady-el-damaty"),
      ("cited-in", "pub-corticostriatal-convergence")],
     """Two strongest CMI latent factors — inhibitory/impulse control (CPT + Go/NoGo, W1-3) and emotional
face recognition (EFR, W1-3) — each index a cortico-striatal phenotype converging across modalities
(behavior -> function -> structure) onto distinct striatal parcels. Impulse-control axis: dorsal/associative
caudate <-> DLPFC/IFG. Emotion axis: ventral/limbic striatum <-> vmPFC/amygdala (EmoFilm ISC). STRUCTURE arm
spans DWI AND T1w/T2w myelin (T2 gray/white boundary). W1-3 behavior (inherited from ADS) predicts the W4
imaging/connectivity phenotypes; this is the forward-inheritance design.""")
node("concept-neurocognitive-maturity", "concept",
     "Adolescent neurocognitive maturity (Cognitive Maturity Index)",
     {"concept-kind": "construct", "status": "supported", "falsifiable": True},
     [("tested-by-experiment", "ads-cpt"), ("tested-by-experiment", "ads-wof"),
      ("tested-by-experiment", "ads-efr"), ("tested-by-experiment", "ads-temporal-discounting"),
      ("cited-in", "pub-eldamaty-2022-cmi")],
     """W1-3 latent factors (inhibitory control, risk/reward, EFR) predict cognitive age; residual = CMI.
Inherited from ADS; the W1-3 CMI predicts W4 outcomes. Ridge R2=0.51, MAE +/-10.11mo; CMI->BAS-D->DUSI-VP.""")
node("concept-impulse-control-frontostriatal", "concept",
     "Inhibitory control and frontostriatal organization",
     {"concept-kind": "hypothesis", "status": "under-investigation", "falsifiable": True},
     [("tested-by-experiment", "ads-cpt"), ("tested-by-experiment", "ads-gonogo"),
      ("tested-by-experiment", "clad-dwi")],
     """Inhibitory/impulse control (ICLF; strongest age predictor beta=0.72, W1-3) maps onto associative
dorsal-caudate <-> DLPFC/IFG coupling — functional (Go/NoGo gPPI) + structural (frontostriatal DWI).""")
node("concept-gonogo-inhibition", "concept",
     "Go/NoGo response inhibition and the frontostriatal control loop",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "ads-gonogo")],
     """Go/NoGo (W1-3) response inhibition recruits caudate<->DLPFC/IFG. Behavior is an important predictor;
the GLM/gPPI method applies forward to W4 rest / EmoFilm where W4 behavior is absent.""")
node("concept-efr-individual-differences", "concept",
     "Emotional face recognition individual differences",
     {"concept-kind": "construct", "status": "supported", "falsifiable": True},
     [("tested-by-experiment", "ads-efr"), ("tested-by-experiment", "clad-emofilm")],
     """EFR latent factors (W1-3) are a strong CMI component; negative-emotion sensitivity rises with age.
EFR deviation indexes an emotion-processing phenotype predicting W4 EmoFilm synchrony.""")
node("concept-emofilm-synchrony", "concept",
     "EFR phenotype -> EmoFilm intersubject synchrony",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "clad-emofilm"), ("tested-by-experiment", "ads-efr")],
     """Subjects with similar EFR-latent deviation (W1-3) show more similar neural synchrony (ISC) during W4
EmoFilm viewing; the emotion-axis behavior(W1-3)->function(W4) bridge.""")
node("concept-violence-cascade", "concept",
     "Social-strain cascade to altered norms and violence",
     {"concept-kind": "hypothesis", "status": "under-investigation", "falsifiable": True},
     [("tested-by-experiment", "ads-community-life"), ("tested-by-experiment", "ads-dusi-r"),
      ("cited-in", "pub-eldamaty-violence-cascade")],
     """Adolescent social strain (neighborhood/family adversity, exposure to violence) -> altered norms ->
violence proneness/vulnerability in emerging adulthood (SEM/latent growth, W1-4). Inherited from ADS.""")
node("concept-striatal-development", "concept",
     "Striatal functional parcellation across development (W1-3) + W4 validation",
     {"concept-kind": "research-question", "status": "under-investigation", "falsifiable": True},
     [("tested-by-experiment", "clad-rest"), ("tested-by-experiment", "clad-dwi"),
      ("cited-in", "pub-eldamaty-striatal-parcellation")],
     """The masked group-ICA striatal parcellation was done with WAVES 1-3 (parent-canonical in ADS). Wave-4
was NOT complete and used a DIFFERENT scanner/data — so the CLAD question is validating + applying the W1-3
parcels to W4 (multimodal: functional + seeded diffusion).""")
node("concept-structural-myelin-convergence", "concept",
     "Structural convergence: DWI + T1w/T2w myelin (T2 gray/white boundary)",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "clad-anat-mprage"), ("tested-by-experiment", "clad-anat-t2-space"),
      ("tested-by-experiment", "clad-anat-dir"), ("tested-by-experiment", "clad-dwi")],
     """Flagship STRUCTURE arm: emotion/control networks differ structurally across (a) DWI white-matter
(HARDI 80-dir), (b) T1w/T2w myelin + the T2 gray/white-matter boundary (incl. the multi-TI DIR contrast),
and (c) T2*/QSM iron (W1-3 multi-echo GRE; striatal iron). ads56 (W1-3 SST), the Wave-4 SST, and the
external NICAP/HCP templates are comparison anchors.""")
node("concept-emofilm-violence", "concept",
     "EmoFilm emotion-network response -> Wave-4 violence outcome",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "clad-emofilm")],
     """Prospective prediction of Wave-4 violence/substance outcomes (DUSI-VP) from W4 EmoFilm emotion-network
response. Parent-canonical concept in ADS.""")
# methodological RQs
node("concept-w13-analytic-validation", "concept",
     "Validating W1-3 analytic choices before forward application to W4",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "clad-rest"), ("tested-by-experiment", "clad-anat-mprage")],
     """Methodological: validate the W1-3 analytic choices (denoising, ICA model order, parcellation,
template) and their robustness (multiverse) before applying them to Wave-4 data.""")
node("concept-scanner-harmonization", "concept",
     "Wave-1-3 vs Wave-4 scanner / sequence harmonization",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "clad-anat-mprage"), ("tested-by-experiment", "clad-rest")],
     """Methodological: Wave-4 used a DIFFERENT (incomplete) scanner. Quantify and harmonize W1-3-vs-W4
scanner/sequence differences (own Wave-4 SST + cross-scanner QC) before pooling or transferring W1-3 models.""")

# ---------------- INHERITED W1-3 paradigms (ADS-owned; cross-project injected) ----------------
for eid, nm, body in [
    ("ads-cpt", "Continuous Performance Task (CPT) [W1-3, inherited]", "W1-3 ADS paradigm (inhibitory control). Inherited; predicts W4 outcomes."),
    ("ads-wof", "Wheel of Fortune (WOF) [W1-3, inherited]", "W1-3 ADS paradigm (risk/reward). Inherited."),
    ("ads-efr", "Emotional Face Recognition (EFR) [W1-3, inherited]", "W1-3 ADS paradigm (emotion recognition). Inherited; bridges to W4 EmoFilm synchrony."),
    ("ads-temporal-discounting", "Temporal Delay Discounting (TD) [W1-3, inherited]", "W1-3 ADS paradigm (delay discounting). Inherited."),
    ("ads-gonogo", "Go/NoGo [W1-3, inherited]", "W1-3 ADS in-scanner inhibition paradigm (1 run, ~4:25). Inherited; method applies forward to W4 rest/EmoFilm."),
    ("ads-emocountstroop", "Emotional Counting Stroop [W1-3, inherited]", "W1-3 ADS in-scanner affective-interference task (alcohol-related words). Inherited; the W1-3 emotional-control paradigm (note: the W1-3 scanner protocol lists EmoCountStroop, NOT EmoFilm)."),
    ("ads-emofilm-paradigm", "EmoFilm paradigm [wave attribution OPEN]", "EmoFilm task design. PROTOCOL QC: EmoFilm is absent from the W1-3 scanner card/field manual and present only in the W4 BIDS -> evidence says EmoFilm is WAVE-4 (clad-emofilm). Kept pending owner confirmation of the PR comment."),
    ("ads-dusi-r", "DUSI substance/violence screening [inherited]", "W1-4 ACASI survey; the high-risk screener (cutoff>=5) + violence-proneness (DUSI-VP) + substance subscales (child direct; parent indirect). The outcome measure."),
    ("ads-bisbas", "BIS/BAS scales [inherited]", "W1-4 reinforcement-sensitivity (approach/inhibition); BAS-D mediates CMI->violence. Inherited."),
    ("ads-context-battery", "Development + cognition battery (Scale of Physical Development, KBIT, AUDIT, BRIEF) [inherited]", "W1-4: Scale of Physical Development (puberty), KBIT (IQ: verbal/matrices/riddles), AUDIT (W2/3), parent BRIEF, demographic + responsibility inventories. Inherited."),
    ("ads-community-life", "Community-life / environmental assessment [inherited]", "W1-4 'Community Life' battery: exposure to violence (school + neighborhood), neighborhood structure, family structure/climate, social-norm perceptions. Inherited; drives the violence cascade. (Exact instrument editions pending appendix QC.)"),
]:
    node(eid, "experiment", nm, {"task-name": eid}, [], body)

# ---------------- CLAD-owned W4 acquisitions (realized in the Wave-4 BIDS) ----------------
node("clad-emofilm", "experiment", "EmoFilm BOLD (Wave-4 acquisition)",
     {"task-name": "emofilm", "conditions": ["REST", "NEU", "POS", "NEG"]},
     [("realized-by", "dataset-clad-bids-wave4"), ("co-acquired-with", "clad-rest"),
      ("analyzed-by", "clad-emofilm-isc"), ("analyzed-by", "clad-emofilm-bold-amplitude")],
     "Wave-4 naturalistic emotional-film BOLD (HCP-pulse replica, different scanner). The W4 realization of the inherited EmoFilm paradigm.")
node("clad-rest", "experiment", "Resting-state BOLD (Wave-4 acquisition)",
     {"task-name": "rest"},
     [("realized-by", "dataset-clad-bids-wave4"), ("analyzed-by", "clad-masked-ica-w4")],
     "Wave-4 resting-state BOLD; input to the W4 masked striatal group-ICA (validation of W1-3 parcels).")
node("clad-anat-mprage", "experiment", "T1w MPRAGE (Wave-4 acquisition)",
     {"task-name": "anat-t1w"},
     [("realized-by", "dataset-clad-bids-wave4"), ("analyzed-by", "clad-wave4-sst"),
      ("analyzed-by", "clad-myelin-t1t2")],
     "Wave-4 T1w MPRAGE; feeds the Wave-4 SST + T1w/T2w myelin.")
node("clad-anat-t2-space", "experiment", "T2w SPACE (Wave-4 acquisition)",
     {"task-name": "anat-t2w-space"},
     [("realized-by", "dataset-clad-bids-wave4"), ("co-acquired-with", "clad-anat-mprage"),
      ("analyzed-by", "clad-myelin-t1t2")],
     "Wave-4 T2w SPACE; with T1w gives the T1w/T2w myelin ratio.")
node("clad-anat-dir", "experiment", "T2w FGATIR / DIR (Wave-4 acquisition)",
     {"task-name": "anat-dir"},
     [("realized-by", "dataset-clad-bids-wave4"), ("co-acquired-with", "clad-anat-mprage")],
     "Wave-4 double-inversion-recovery (FGATIR/DIR) structural; the T2 gray/white-matter boundary + WM/GM microstructure contrast.")
node("clad-dwi", "experiment", "DWI/HARDI (Wave-4 acquisition)",
     {"task-name": "dwi-hardi"},
     [("realized-by", "dataset-clad-bids-wave4"), ("analyzed-by", "clad-dwi-w4")],
     "Wave-4 HARDI diffusion; seeded structural connectivity for the structure arm.")

# ---------------- METHODS: inherited (W1-3) + W4-adapted ----------------
node("cfa-sem", "method", "CFA + SEM (latent cognitive factors) [inherited]",
     {"tool": "lavaan (R)", "version": "0.6-6"}, [], "Inherited W1-3 CMI method.")
node("lasso-age-prediction", "method", "Ridge/LASSO age prediction [inherited]",
     {"tool": "glmnet (R)", "version": "4.0-2"}, [], "Inherited W1-3 CMI age model; residual = CMI.")
node("split-half-reproducibility", "method", "Split-half ICA reproducibility [harmonized]",
     {"tool": "Munkres + Dice", "version": "0.1"}, [], "Harmonized with the ADS split-half method; applied to W4 parcels.")
node("clad-wave4-sst", "method", "Wave-4 study-specific template construction (W4 params)",
     {"tool": "antsMultivariateTemplateConstruction2", "version": "ANTs 2.x",
      "parameters": {"k": "T1w+T2w+DIR", "scanner": "wave-4 (differs from W1-3)"}},
     [("requires-standard", "standard-clad-wave4-sst")],
     "Builds the CLAD Wave-4 SST from W4 multicontrast structural (different scanner). Adapts the ADS ads56 MVTC2 recipe with W4 params; produces standard-clad-wave4-sst.")
node("clad-fmriprep-w4", "method", "fMRIPrep (Wave-4 params)",
     {"tool": "fMRIPrep", "version": "23.x", "parameters": {"output-space": "clad-wave4-sst", "multiband": "yes (HCP-pulse)"}},
     [("requires-standard", "standard-clad-wave4-sst")],
     "Wave-4 fMRIPrep normalized to the Wave-4 SST; multiband/HCP-pulse settings differ from W1-3.")
node("clad-denoising-w4", "method", "Denoising (Wave-4 params: multiband + respiratory notch)",
     {"tool": "ICA-AROMA + Nipype", "version": "0.1"}, [],
     "ICA-AROMA + confound regression with a respiratory notch filter for the W4 multiband HCP-pulse data.")
node("clad-masked-ica-w4", "method", "Masked group-ICA striatal parcellation (Wave-4)",
     {"tool": "MELODIC", "version": "FSL 6.0"}, [],
     "W4 masked group-ICA; validates/applies the W1-3 striatal parcels to the (incomplete, different-scanner) W4 rest data.")
node("clad-dwi-w4", "method", "DWI tractography (Wave-4)",
     {"tool": "MRtrix3 / probtrackx", "version": "MRtrix3 3.0"}, [],
     "W4 seeded probabilistic tractography for striatal structural connectivity.")
node("clad-emofilm-isc", "method", "Intersubject synchrony (ISC) on EmoFilm",
     {"tool": "BrainIAK ISC", "version": "0.x"}, [],
     "CLAD-owned: intersubject correlation of W4 EmoFilm BOLD; relate pairwise synchrony to EFR-latent similarity.")
node("clad-emofilm-bold-amplitude", "method", "EmoFilm BOLD amplitude (Wave-4)",
     {"tool": "fMRI amplitude extraction", "version": "0.1"}, [],
     "W4 EmoFilm amygdala/PFC BOLD amplitude for the violence-outcome model.")
node("clad-myelin-t1t2", "method", "T1w/T2w myelin (Wave-4; T2 gray/white boundary)",
     {"tool": "HCP-style T1w/T2w ratio", "version": "0.1"},
     [("requires-standard", "standard-hcp")],
     "W4 T1w/T2w ratio + T2 gray/white-matter boundary surface contrast; the second structural axis.")
node("multimodal-striatal-parcellation", "method", "Multimodal striatal parcellation (functional + diffusion)",
     {"tool": "ICA + diffusion fusion", "version": "0.1"},
     [("composes", "clad-masked-ica-w4"), ("composes", "clad-dwi-w4")],
     "Fuse W4 functional group-ICA parcels with seed-based diffusion connectivity (emotion vs control parcels).")

# ---------------- STANDARDS ----------------
node("standard-clad-wave4-sst", "standard", "CLAD Wave-4 study-specific template (SST)",
     {"standard-class": "template"}, [],
     "CLAD-OWNED. Built from Wave-4 multicontrast structural (T1w/T2w/DIR) on the W4 scanner. The W4 "
     "normalization target. Compared against ads56 (W1-3 SST, inherited) and the external NICAP/NICAP55 templates.")
node("standard-bids", "standard", "Brain Imaging Data Structure (BIDS)",
     {"standard-class": "spec", "version": "1.9.0"}, [], "De-identified imaging organized to BIDS.")
node("standard-hcp", "standard", "Human Connectome Project (HCP / HCP-D)",
     {"standard-class": "protocol"}, [],
     "External comparison: HCP/HCP-D myelin-mapping + pulse-sequence lineage (EmoFilm is an HCP-pulse replica). NDA-gated; metadata only.")

# ---------------- PUBLICATIONS ----------------
node("pub-eldamaty-2022-cmi", "publication",
     "Introducing an Adolescent Cognitive Maturity Index (Frontiers 2022)",
     {"pub-status": "published", "venue": "Frontiers in Psychology", "year": 2022,
      "doi": "10.3389/fpsyg.2022.1017317", "pmid": "36571021"},
     [("authored-by", "persona-shady-el-damaty"), ("authored-by", "persona-diana-fishbein"),
      ("authored-by", "persona-john-vanmeter"),
      ("addresses-concept", "concept-neurocognitive-maturity"),
      ("cites-method", "cfa-sem"), ("cites-method", "lasso-age-prediction")],
     "Published CMI paper (W1-3, RQ1). Latent-factor age prediction; CMI->BAS-D->DUSI-VP mediation. Parent-canonical in ADS.")
node("pub-eldamaty-violence-cascade", "publication",
     "Social-strain cascade to violence & altered norms (SEM)",
     {"pub-status": "draft"},
     [("authored-by", "persona-shady-el-damaty"), ("authored-by", "persona-diana-fishbein"),
      ("addresses-concept", "concept-violence-cascade"),
      ("cites-method", "cfa-sem")],
     "Dissertation-core SEM/latent-growth: strain -> norms -> violence (RQ2). Draft.")
node("pub-eldamaty-striatal-parcellation", "publication",
     "Multimodal parcellation of the adolescent striatum",
     {"pub-status": "draft"},
     [("authored-by", "persona-shady-el-damaty"), ("authored-by", "persona-john-vanmeter"),
      ("addresses-concept", "concept-striatal-development"),
      ("cites-method", "clad-masked-ica-w4"), ("cites-method", "split-half-reproducibility")],
     "Striatal functional/diffusion parcellation (RQ3). Parcellation was W1-3 (parent); W4 validation. Draft.")
node("pub-corticostriatal-convergence", "publication",
     "Cortico-striatal multimodal convergence of impulse-control & emotion phenotypes (PLANNED)",
     {"pub-status": "draft"},
     [("authored-by", "persona-shady-el-damaty"),
      ("addresses-concept", "concept-corticostriatal-convergence"),
      ("cites-method", "multimodal-striatal-parcellation"),
      ("cites-method", "clad-emofilm-isc"), ("cites-method", "clad-dwi-w4"),
      ("cites-method", "clad-myelin-t1t2")],
     "PLANNED flagship: two-axis cortico-striatal convergence across behavior(W1-3)/function/structure(W4).")
node("pub-eldamaty-2017-dissertation", "publication",
     "Adolescent Neurocognitive Maturity Mediates Paths to Altered Social Norms & Vulnerability in Emerging Adulthood",
     {"pub-status": "published", "venue": "Georgetown University (PhD dissertation)", "year": 2017},
     [("authored-by", "persona-shady-el-damaty"),
      ("aggregates", "pub-eldamaty-2022-cmi"),
      ("aggregates", "pub-eldamaty-violence-cascade"),
      ("aggregates", "pub-eldamaty-striatal-parcellation"),
      ("addresses-concept", "concept-corticostriatal-convergence")],
     "The defended dissertation; umbrella output aggregating the component papers.")

# ---------------- PERSONAS / ORGANIZATIONS ----------------
node("persona-shady-el-damaty", "persona", "Shady El Damaty",
     {"persona-kind": "researcher"}, [("affiliated-with", "org-georgetown-university")],
     "Dissertation author. Inherited copy (canonical: ads-glimmer:persona-shady-el-damaty).")
node("persona-john-vanmeter", "persona", "John W. VanMeter",
     {"persona-kind": "researcher"}, [("affiliated-with", "org-cfmi-georgetown")], "Dissertation advisor; director, CFMI.")
node("persona-diana-fishbein", "persona", "Diana H. Fishbein",
     {"persona-kind": "researcher"}, [], "Co-mentor (Penn State / UNC); translational prevention.")
node("org-nij", "organization", "National Institute of Justice",
     {"org-kind": "funder"}, [], "Funder (award 2016-R2-CX-0019). Inherited from parent ADS.")
node("org-georgetown-university", "organization", "Georgetown University",
     {"org-kind": "institution"}, [], "Degree-granting institution. Inherited from parent ADS.")
node("org-cfmi-georgetown", "organization", "Center for Functional & Molecular Imaging (CFMI), Georgetown",
     {"org-kind": "lab"}, [("part-of", "org-georgetown-university")], "Imaging center. Inherited from parent ADS.")

# ---------------- DATASETS ----------------
node("dataset-clad-bids-wave4", "dataset", "CLAD Wave-4 BIDS (de-identified)",
     {"domain": "clad", "datalad-relative-path": "data/bids", "tier": "OPEN-deid", "bytes-status": "deferred"},
     [("conforms-to", "standard-bids")],
     "Wave-4 / Visit-7 BIDS: T1w MPRAGE, T2w SPACE, T2w DIR, DWI, fmap, EmoFilm BOLD, rest BOLD (61 subj local). Defaced + annexed in the data pass.")
node("dataset-clad-bids-w13", "dataset", "CLAD Waves 1-3 BIDS (de-identified)",
     {"domain": "clad", "datalad-relative-path": "data/bids", "tier": "OPEN-deid", "bytes-status": "deferred"},
     [("conforms-to", "standard-bids")],
     "Longitudinal Waves 1-3 BIDS (142 subj). Developmental baseline; bytes deferred.")

# ----------------------------- emit -----------------------------
def yaml_scalar(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    return '"' + str(v).replace('"', '\\"') + '"'

def yaml_list(vals):
    return "[" + ", ".join(yaml_scalar(v) for v in vals) + "]"

def _edge_line(e):
    et, tgt = e[0], e[1]
    role = e[2] if len(e) > 2 else None
    tgt_r = '"' + tgt + '"' if ":" in str(tgt) else tgt
    s = f'  - {{type: {et}, target: {tgt_r}'
    return s + (f', role: {role}}}' if role else "}")

def emit(n):
    fm = ["---", f'id: {n["id"]}', f'type: {n["type"]}', f'name: {yaml_scalar(n["name"])}',
          f'created: {TS}', f'modified: {TS}']
    fm.append(f'provenance-hash: sha256:{hashlib.sha256(n["desc"].encode()).hexdigest()}')
    for k, v in n["fields"].items():
        if isinstance(v, dict):
            fm.append(f"{k}: {{" + ", ".join(f'{ik}: {yaml_scalar(iv)}' for ik, iv in v.items()) + "}")
        else:
            fm.append(f'{k}: {yaml_list(v) if isinstance(v, list) else yaml_scalar(v)}')
    if n["edges"]:
        fm.append("edges:")
        fm += [_edge_line(e) for e in n["edges"]]
    if n["desc"]:
        fm.append("description: |")
        fm += ["  " + line for line in n["desc"].splitlines()]
    fm.append("---")
    rel = os.path.join(TYPE_DIR[n["type"]], n["id"] + ".md")
    os.makedirs(os.path.join(HERE, TYPE_DIR[n["type"]]), exist_ok=True)
    with open(os.path.join(HERE, rel), "w") as f:
        f.write("\n".join(fm) + "\n")
    return rel

def main():
    ids = [x["id"] for x in N]
    assert len(ids) == len(set(ids)), "duplicate node id: " + ",".join(sorted({x for x in ids if ids.count(x) > 1}))
    for n in N:
        if n["type"] != "program":
            n["edges"].append(("in-program", PROGRAM))
        for tgt, role in CROSS.get(n["id"], []):
            n["edges"].append(("cross-project", tgt, role))
        if n["type"] == "concept" and "statement" not in n["fields"]:
            stmt = n["desc"].replace("\n", " ").split(". ")[0].strip().rstrip(".") + "."
            n["fields"] = {"statement": stmt, **n["fields"]}
    index_nodes = [{"id": n["id"], "type": n["type"], "path": emit(n)} for n in N]
    known = set(ids)
    dangling = sorted({e[1] for n in N for e in n["edges"] if e[0] != "cross-project" and e[1] not in known})
    index = {"schema": SCHEMA, "dataset-name": DATASET, "default-domain": "neuroimaging", "created": TS,
             "description": "clad-glimmer research-object graph for the Community Life & Adolescent Development study (a subproject of ADS).",
             "upstream-graph": "https://github.com/hebbianloop/ads-glimmer-graph (parent; same cohort)",
             "node-count": len(index_nodes),
             "nodes": sorted(index_nodes, key=lambda x: (x["type"], x["id"]))}
    with open(os.path.join(HERE, "_glimmer-index.json"), "w") as f:
        json.dump(index, f, indent=2); f.write("\n")
    print(f"emitted {len(N)} nodes (node-count={len(index_nodes)})")
    print("dangling intra-graph edge targets:", dangling or "none")

if __name__ == "__main__":
    main()
