#!/usr/bin/env python3
"""build_clad_graph.py — emit the clad-glimmer research-object graph (idempotent).

Writes typed Glimmer nodes (concept / experiment / method / standard / publication / persona /
organization / program / dataset) as YAML-front-matter markdown sidecars under graph/<type-dir>/,
plus _glimmer-index.json. Node format + edge vocabulary follow hebbianloop/glimmer v0.4
(adds the `program` node + `in-program` / `cross-project` universal edges for project/subproject
relationships and inter-project claims).

CLAD is a SUBPROJECT of ADS on the same cohort. Conventions applied here:
  - every node carries `in-program` -> program-clad (membership);
  - nodes inherited from / shared with the parent ADS graph carry a `cross-project` edge to the
    ADS-canonical id (namespaced `ads-glimmer:<id>`), per "resolve duplicates to the parent";
  - program-clad declares the subproject link to the parent via cross-project.

No PHI: this graph contains only de-identified study metadata, hypotheses, methods, and outputs.
Usage:  python3 graph/build_clad_graph.py
"""
import hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TS = "2026-06-11T00:00:00+00:00"          # fixed stamp (deterministic re-runs)
SCHEMA = "glimmer/v0.4.0"
DATASET = "clad-glimmer"
PROGRAM = "program-clad"

TYPE_DIR = {
    "concept": "concepts", "experiment": "experiments", "method": "methods",
    "standard": "standards", "publication": "publications", "persona": "personas",
    "organization": "organizations", "program": "programs", "dataset": "datasets",
    "derivative": "derivatives", "finding": "findings",
}

# cross-project edges (node id -> list of (namespaced-target, role)); ADS is the parent/canonical.
CROSS = {
    "persona-shady-el-damaty":       [("ads-glimmer:persona-shady-el-damaty", "inherited-from-parent")],
    "org-nij":                       [("ads-glimmer:org-nij", "inherited-from-parent")],
    "org-georgetown-university":     [("ads-glimmer:org-georgetown-university", "inherited-from-parent")],
    "org-cfmi-georgetown":           [("ads-glimmer:org-cfmi-georgetown", "inherited-from-parent")],
    "concept-emofilm-violence":      [("ads-glimmer:concept-emofilm-violence-outcome", "parent-canonical")],
    "ads-rest":                      [("ads-glimmer:experiment-ads-rest", "harmonizes-with")],
    "masked-ica-parcellation":       [("ads-glimmer:method-striatum-group-ica", "harmonizes-with")],
    "fmriprep":                      [("ads-glimmer:method-fmriprep", "harmonizes-with")],
    "pub-eldamaty-striatal-parcellation": [("ads-glimmer:pub-eldamaty-vanmeter-2018-striatum", "harmonizes-with")],
}

# ---- node spec: (id, type, name, fields{}, edges[(type,target[,role])], description) -----------
N = []
def node(id, type, name, fields=None, edges=None, desc=""):
    N.append({"id": id, "type": type, "name": name,
              "fields": fields or {}, "edges": edges or [], "desc": desc.strip()})

# ---------------- PROGRAM ----------------
node(PROGRAM, "program", "Community Life & Adolescent Development (CLAD)",
     {"program-kind": "subproject", "status": "active",
      "outcome-measure": "violence proneness & substance-use initiation (DUSI); neurocognitive maturity (CMI)"},
     [("cross-project", "ads-glimmer:program-ads", "subproject-of-parent"),
      ("led-by", "persona-shady-el-damaty"), ("funded-by", "org-nij"),
      ("addresses-concept", "concept-corticostriatal-convergence"),
      ("cited-in", "pub-eldamaty-2017-dissertation")],
     """CLAD is the NIJ 2016-R2-CX-0019 Wave-4 / Visit-7 subproject of the Adolescent Development Study
(ADS), on the same N=141 cohort. Subproject-of the parent ADS program (cross-graph). Anything touching
Wave-4 data is CLAD; nodes shared with / inherited from ADS carry a cross-project edge to the parent.""")

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
      ("tested-by-experiment", "ads-efr"), ("tested-by-experiment", "ads-emofilm"),
      ("tested-by-experiment", "ads-dwi-hardi"), ("tested-by-experiment", "ads-anat-mprage"),
      ("tested-by-experiment", "ads-anat-t2"),
      ("funded-by", "org-nij"), ("authored-by", "persona-shady-el-damaty"),
      ("cited-in", "pub-corticostriatal-convergence")],
     """The two strongest CMI latent factors — inhibitory/impulse control (CPT + Go/NoGo) and emotional
face recognition (EFR) — each index an individual cortico-striatal phenotype that converges across
modalities (behavior -> function -> structure) onto distinct striatal parcels. Impulse-control axis:
dorsal/associative caudate <-> DLPFC/IFG (Go/NoGo connectivity + frontostriatal DWI). Emotion axis:
ventral/limbic striatum <-> vmPFC/amygdala (EmoFilm intersubject synchrony + emotion-network DWI).
The STRUCTURE arm spans DWI AND T1w/T2w myelin (T2 gray/white boundary); HCP & NICAP are comparison
anchors. Multimodal striatal parcellation recovers both axes; individual latent-factor deviation
predicts the matching parcel's connectivity; and these predict vulnerability outcomes.""")

node("concept-neurocognitive-maturity", "concept",
     "Adolescent neurocognitive maturity (Cognitive Maturity Index)",
     {"concept-kind": "construct", "status": "supported", "falsifiable": True},
     [("tested-by-experiment", "ads-cpt"), ("tested-by-experiment", "ads-wof"),
      ("tested-by-experiment", "ads-efr"), ("tested-by-experiment", "ads-temporal-discounting"),
      ("funded-by", "org-nij"), ("cited-in", "pub-eldamaty-2022-cmi")],
     """Latent factors of inhibitory control, risk/reward, and emotional face recognition predict
chronological age; the residual (CMI) indexes maturational imbalance. Ridge model R2=0.51, MAE +/-10.11
months. Lower CMI tracks higher DUSI violence proneness (R=-0.28) and substance use, mediated by BAS-D.""")

node("concept-impulse-control-frontostriatal", "concept",
     "Inhibitory control and frontostriatal organization",
     {"concept-kind": "hypothesis", "status": "under-investigation", "falsifiable": True},
     [("tested-by-experiment", "ads-cpt"), ("tested-by-experiment", "ads-gonogo"),
      ("tested-by-experiment", "ads-dwi-hardi")],
     """Inhibitory/impulse control (ICLF; strongest age predictor, beta=0.72) maps onto associative
dorsal-caudate <-> prefrontal executive cortex (DLPFC/IFG/preSMA) coupling, in both functional and
structural (frontostriatal DWI) connectivity.""")

node("concept-gonogo-inhibition", "concept",
     "Go/NoGo response inhibition and the frontostriatal control loop",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "ads-gonogo")],
     """Go/NoGo response inhibition recruits and shapes the caudate<->DLPFC/IFG control loop; the
control-axis behavioral->functional bridge of the flagship hypothesis.""")

node("concept-efr-individual-differences", "concept",
     "Emotional face recognition individual differences",
     {"concept-kind": "construct", "status": "supported", "falsifiable": True},
     [("tested-by-experiment", "ads-efr"), ("tested-by-experiment", "ads-emofilm")],
     """EFR latent factors (negative/positive emotion recognition) are a strong CMI component; negative
emotion sensitivity rises with age (beta=0.35), positive-emotion recognition declines with puberty.""")

node("concept-emofilm-synchrony", "concept",
     "EFR phenotype -> EmoFilm intersubject synchrony",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "ads-emofilm"), ("tested-by-experiment", "ads-efr")],
     """Subjects whose EFR latent factor deviates similarly from the population show more similar neural
synchrony (ISC) during naturalistic EmoFilm viewing; the emotion-axis behavioral->functional bridge.""")

node("concept-violence-cascade", "concept",
     "Social-strain cascade to altered norms and violence",
     {"concept-kind": "hypothesis", "status": "under-investigation", "falsifiable": True},
     [("cited-in", "pub-eldamaty-violence-cascade")],
     """Adolescent social strain cascades through altered social norms and violence exposure into violence
proneness and vulnerability in emerging adulthood (SEM / latent growth).""")

node("concept-striatal-development", "concept",
     "Multimodal striatal functional parcellation across development",
     {"concept-kind": "research-question", "status": "under-investigation", "falsifiable": True},
     [("tested-by-experiment", "ads-rest"), ("tested-by-experiment", "ads-dwi-hardi"),
      ("cited-in", "pub-eldamaty-striatal-parcellation")],
     """Masked group-ICA functional parcellation fused with seed-based diffusion connectivity recovers
limbic (emotion) and associative (control) striatal parcels; medial-caudate<->prefrontal connectivity
relates to outcomes and predicts substance-use initiation 18 months later.""")

node("concept-structural-myelin-convergence", "concept",
     "Structural convergence: DWI + T1w/T2w myelin (T2 gray/white boundary)",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "ads-anat-mprage"), ("tested-by-experiment", "ads-anat-t2"),
      ("tested-by-experiment", "ads-dwi-hardi")],
     """The flagship's STRUCTURE arm: individual differences in the emotion/control cortico-striatal
networks are reflected not only in DWI white-matter but in T1w/T2w myelin contrast and the T2
gray/white-matter boundary (HCP-style myelin mapping). HCP (incl. HCP-D) and the NICAP55 study-specific
template are the comparison anchors.""")

node("concept-emofilm-violence", "concept",
     "EmoFilm emotion-network response -> Wave-4 violence outcome",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "ads-emofilm")],
     """Prospective prediction of Wave-4 violence/substance outcomes from EmoFilm emotion-network response.
Parent-canonical concept in ADS (cross-project).""")

# ---------------- EXPERIMENTS ----------------
# behavioral (waves 1-3); no Wave-4 BIDS realization edge
node("ads-cpt", "experiment", "Continuous Performance Task (CPT)",
     {"task-name": "cpt", "conditions": ["target", "lure-Q"], "n-trials": 150},
     [("analyzed-by", "cfa-sem")], "Inhibitory control / sustained attention; signal-detection metrics.")
node("ads-wof", "experiment", "Wheel of Fortune (WOF)",
     {"task-name": "wof", "conditions": ["high-risk", "low-risk"], "n-trials": 90},
     [("analyzed-by", "cfa-sem")], "Risk/reward decision making; fMRI in waves 1-3.")
node("ads-efr", "experiment", "Emotional Face Recognition (EFR)",
     {"task-name": "efr", "conditions": ["happy", "angry", "fearful", "sad", "disgust", "surprise", "neutral"], "n-trials": 70},
     [("analyzed-by", "cfa-sem")], "NimStim facial-emotion recognition; accuracy + RT for positive/negative affect.")
node("ads-temporal-discounting", "experiment", "Temporal Delay Discounting (TD)",
     {"task-name": "temporal-discounting"},
     [("analyzed-by", "cfa-sem")], "Preference for immediate vs delayed rewards; AUC of indifference values.")
# Wave-4 acquisitions -> realized in the Wave-4 BIDS dataset
node("ads-emofilm", "experiment", "EmoFilm naturalistic emotional film task",
     {"task-name": "emofilm", "conditions": ["REST", "NEU", "POS", "NEG"]},
     [("realized-by", "dataset-clad-bids-wave4"), ("analyzed-by", "intersubject-synchrony"),
      ("analyzed-by", "method-emofilm-bold-amplitude")],
     "Naturalistic emotional film during fMRI (Wave-4); HCP-pulse replica; supports ISC.")
node("ads-gonogo", "experiment", "Go/NoGo response-inhibition task",
     {"task-name": "gonogo", "conditions": ["go", "nogo"]},
     [("realized-by", "dataset-clad-bids-wave4"), ("analyzed-by", "gonogo-frontostriatal-glm-gppi")],
     "Response inhibition during fMRI; frontostriatal (caudate<->DLPFC/IFG) activation + connectivity.")
node("ads-rest", "experiment", "Resting-state fMRI",
     {"task-name": "rest", "duration-sec": 342},
     [("realized-by", "dataset-clad-bids-wave4"), ("analyzed-by", "masked-ica-parcellation")],
     "Resting-state BOLD; input to masked striatal group-ICA parcellation + connectivity.")
node("ads-dwi-hardi", "experiment", "Diffusion-weighted imaging (HARDI)",
     {"task-name": "dwi-hardi"},
     [("realized-by", "dataset-clad-bids-wave4"), ("analyzed-by", "seeded-diffusion-connectivity"),
      ("analyzed-by", "dwi-preprocessing")],
     "HARDI diffusion; frontostriatal + emotion-network white-matter structure + seed-based tractography.")
node("ads-anat-mprage", "experiment", "T1w MPRAGE structural acquisition",
     {"task-name": "anat-t1w"},
     [("realized-by", "dataset-clad-bids-wave4"), ("analyzed-by", "freesurfer-recon"),
      ("analyzed-by", "nicap55-template"), ("analyzed-by", "myelin-t1t2-mapping")],
     "T1w MPRAGE; feeds FreeSurfer recons, the NICAP55 study-specific template, and T1w/T2w myelin.")
node("ads-anat-t2", "experiment", "T2w structural acquisition",
     {"task-name": "anat-t2w"},
     [("realized-by", "dataset-clad-bids-wave4"), ("analyzed-by", "myelin-t1t2-mapping"),
      ("co-acquired-with", "ads-anat-mprage")],
     "T2w structural; with T1w gives the T1w/T2w ratio + T2 gray/white-matter boundary (myelin contrast).")

# ---------------- METHODS ----------------
node("cfa-sem", "method", "Confirmatory factor analysis + structural equation modeling",
     {"tool": "lavaan (R)", "version": "0.6-6"}, [],
     "CFA to estimate latent cognitive factors; SEM for factor interactions and mediation.")
node("lasso-age-prediction", "method", "Regularized (ridge/LASSO) age prediction",
     {"tool": "glmnet (R)", "version": "4.0-2"}, [],
     "Cross-validated regularized regression of latent factors on age; residual = CMI.")
node("masked-ica-parcellation", "method", "Masked group-ICA striatal parcellation",
     {"tool": "MELODIC / masked group-ICA", "version": "FSL 6.0"}, [],
     "Striatal-mask-constrained group-ICA; max-loading voxel labeling; split-half reproducibility.")
node("gonogo-frontostriatal-glm-gppi", "method", "Go/NoGo GLM + gPPI frontostriatal connectivity",
     {"tool": "fMRI GLM + gPPI", "version": "SPM12/Nilearn"}, [],
     "Task GLM + generalized psychophysiological interaction for caudate<->DLPFC/IFG connectivity.")
node("intersubject-synchrony", "method", "Intersubject correlation / synchrony (ISC)",
     {"tool": "BrainIAK ISC", "version": "0.x"}, [],
     "Intersubject correlation of EmoFilm BOLD; relate pairwise synchrony to EFR-latent similarity.")
node("seeded-diffusion-connectivity", "method", "Seed-based probabilistic tractography",
     {"tool": "MRtrix3 / FSL probtrackx", "version": "MRtrix3 3.0"}, [],
     "Striatal-parcel-seeded probabilistic tractography for structural connectivity fingerprints.")
node("multimodal-striatal-parcellation", "method", "Multimodal (functional + diffusion) striatal parcellation",
     {"tool": "ICA + diffusion fusion", "version": "0.1"},
     [("composes", "masked-ica-parcellation"), ("composes", "seeded-diffusion-connectivity")],
     "Fuse functional group-ICA parcels with seed-based diffusion connectivity to define emotion vs control striatal parcels.")
node("fmriprep", "method", "fMRIPrep preprocessing",
     {"tool": "fMRIPrep", "version": "23.x"},
     [("requires-standard", "standard-nicap55-sst")],
     "Standardized BOLD/anat preprocessing; normalizes to the NICAP55 study-specific template.")
node("freesurfer-recon", "method", "FreeSurfer / FastSurfer surface reconstruction",
     {"tool": "FastSurfer", "version": "2.x"}, [], "Cortical surface reconstruction + morphometry (recons).")
node("nicap55-template", "method", "NICAP55 study-specific template construction",
     {"tool": "ANTs multivariate template", "version": "ANTs 2.x"},
     [("requires-standard", "standard-nicap55-sst")],
     "Builds the age-appropriate multicontrast developmental template (T1w/T2w) all CLAD imaging normalizes to.")
node("dwi-preprocessing", "method", "DWI/HARDI preprocessing",
     {"tool": "QSIPrep", "version": "0.x"}, [], "Denoising, distortion/eddy correction, model fitting for HARDI.")
node("split-half-reproducibility", "method", "Split-half reproducibility validation",
     {"tool": "custom (Munkres matching + correlation)", "version": "0.1"}, [],
     "Repeated split-half ICA + Hungarian matching to select reproducible striatal model order (k~5 primary, ~8-10 fine).")
node("myelin-t1t2-mapping", "method", "T1w/T2w myelin mapping (T2 gray/white boundary)",
     {"tool": "HCP-style T1w/T2w ratio + surface g/w contrast", "version": "0.1"},
     [("requires-standard", "standard-hcp")],
     "T1w/T2w ratio + T2 gray/white-matter boundary surface contrast (HCP-style); the second structural axis alongside DWI.")
node("method-emofilm-bold-amplitude", "method", "EmoFilm BOLD amplitude / emotion-network response",
     {"tool": "fMRI GLM / amplitude extraction", "version": "0.1"}, [],
     "Wave-4 EmoFilm amygdala/PFC BOLD amplitude + emotion-network response for the violence-outcome model.")

# ---------------- STANDARDS ----------------
node("standard-bids", "standard", "Brain Imaging Data Structure (BIDS)",
     {"standard-class": "spec", "version": "1.9.0", "upstream-url": "https://bids.neuroimaging.io"}, [],
     "The de-identified imaging is organized to BIDS.")
node("standard-nicap55-sst", "standard", "NICAP55 study-specific template (SST)",
     {"standard-class": "template"}, [],
     "Age-appropriate multicontrast (T1w/T2w) developmental Study-Specific Template built from the cohort "
     "(NICAP lineage). The normalization target for CLAD imaging; built by method nicap55-template.")
node("standard-hcp", "standard", "Human Connectome Project (HCP / HCP-D) protocol",
     {"standard-class": "protocol", "upstream-url": "https://www.humanconnectome.org"}, [],
     "HCP (incl. HCP-D developmental) reference protocol/pipelines for myelin mapping + pulse-sequence "
     "lineage (EmoFilm is an HCP-pulse replica). Comparison anchor; NDA-gated, metadata only — not CLAD data.")

# ---------------- PUBLICATIONS ----------------
node("pub-eldamaty-2022-cmi", "publication",
     "Introducing an Adolescent Cognitive Maturity Index (Frontiers 2022)",
     {"pub-status": "published", "venue": "Frontiers in Psychology", "year": 2022,
      "doi": "10.3389/fpsyg.2022.1017317", "pmid": "36571021",
      "repo": "https://github.com/hebbianloop/eldamaty2020b"},
     [("authored-by", "persona-shady-el-damaty"), ("authored-by", "persona-diana-fishbein"),
      ("authored-by", "persona-john-vanmeter"),
      ("addresses-concept", "concept-neurocognitive-maturity"),
      ("cites-method", "cfa-sem"), ("cites-method", "lasso-age-prediction")],
     "Published CMI paper (RQ1). Latent-factor age prediction; CMI mediates vulnerability via BAS-D.")
node("pub-eldamaty-violence-cascade", "publication",
     "Social-strain cascade to violence & altered norms (SEM)",
     {"pub-status": "draft", "repo": "https://github.com/hebbianloop/eldamaty2020a"},
     [("authored-by", "persona-shady-el-damaty"), ("authored-by", "persona-diana-fishbein"),
      ("addresses-concept", "concept-violence-cascade")],
     "Dissertation-core SEM/latent-growth of strain -> norms -> violence (RQ2). Draft.")
node("pub-eldamaty-striatal-parcellation", "publication",
     "Multimodal parcellation of the adolescent striatum",
     {"pub-status": "draft"},
     [("authored-by", "persona-shady-el-damaty"), ("authored-by", "persona-john-vanmeter"),
      ("addresses-concept", "concept-striatal-development"),
      ("cites-method", "masked-ica-parcellation"), ("cites-method", "split-half-reproducibility")],
     "Striatal functional/diffusion parcellation (RQ3). Draft / OHBM-CCN-FLUX. eldamaty2020c.")
node("pub-corticostriatal-convergence", "publication",
     "Cortico-striatal multimodal convergence of impulse-control & emotion phenotypes (PLANNED)",
     {"pub-status": "draft"},
     [("authored-by", "persona-shady-el-damaty"),
      ("addresses-concept", "concept-corticostriatal-convergence"),
      ("cites-method", "multimodal-striatal-parcellation"),
      ("cites-method", "intersubject-synchrony"),
      ("cites-method", "seeded-diffusion-connectivity"),
      ("cites-method", "myelin-t1t2-mapping")],
     "PLANNED flagship paper: two-axis (impulse-control + emotion) cortico-striatal convergence across behavior/function/structure.")
node("pub-eldamaty-2017-dissertation", "publication",
     "Adolescent Neurocognitive Maturity Mediates Paths to Altered Social Norms & Vulnerability in Emerging Adulthood",
     {"pub-status": "published", "venue": "Georgetown University (PhD dissertation)", "year": 2017},
     [("authored-by", "persona-shady-el-damaty"),
      ("aggregates", "pub-eldamaty-2022-cmi"),
      ("aggregates", "pub-eldamaty-violence-cascade"),
      ("aggregates", "pub-eldamaty-striatal-parcellation"),
      ("addresses-concept", "concept-corticostriatal-convergence")],
     "The defended dissertation; umbrella output aggregating the component papers.")

# ---------------- PERSONAS ----------------
node("persona-shady-el-damaty", "persona", "Shady El Damaty",
     {"persona-kind": "researcher"}, [("affiliated-with", "org-georgetown-university")],
     "Dissertation author. Inherited from parent ADS (canonical: ads-glimmer:persona-shady-el-damaty).")
node("persona-john-vanmeter", "persona", "John W. VanMeter",
     {"persona-kind": "researcher"}, [("affiliated-with", "org-cfmi-georgetown")],
     "Dissertation advisor; director, CFMI.")
node("persona-diana-fishbein", "persona", "Diana H. Fishbein",
     {"persona-kind": "researcher"}, [],
     "Co-mentor (Penn State / UNC); translational prevention.")

# ---------------- ORGANIZATIONS ----------------
node("org-nij", "organization", "National Institute of Justice",
     {"org-kind": "funder"}, [], "Funder of CLAD (award 2016-R2-CX-0019). Inherited from parent ADS.")
node("org-georgetown-university", "organization", "Georgetown University",
     {"org-kind": "institution"}, [], "Degree-granting institution. Inherited from parent ADS.")
node("org-cfmi-georgetown", "organization", "Center for Functional & Molecular Imaging (CFMI), Georgetown",
     {"org-kind": "lab"}, [("part-of", "org-georgetown-university")],
     "Imaging center where ADS/CLAD data were acquired. Inherited from parent ADS.")

# ---------------- DATASETS (pointers; bytes deferred) ----------------
node("dataset-clad-bids-wave4", "dataset", "CLAD Wave-4 BIDS (de-identified)",
     {"domain": "clad", "datalad-relative-path": "data/bids", "tier": "OPEN-deid", "bytes-status": "deferred"},
     [("conforms-to", "standard-bids")],
     "Wave-4 / Visit-7 BIDS (61 subj local). Defaced + annexed in the data pass; raw DICOM stays in the private backend.")
node("dataset-clad-bids-w13", "dataset", "CLAD Waves 1-3 BIDS (de-identified)",
     {"domain": "clad", "datalad-relative-path": "data/bids", "tier": "OPEN-deid", "bytes-status": "deferred"},
     [("conforms-to", "standard-bids")],
     "Longitudinal Waves 1-3 BIDS (142 subj). Provides developmental baseline; bytes deferred.")

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
    tgt_r = '"' + tgt + '"' if ":" in str(tgt) else tgt   # quote namespaced cross-project targets
    s = f'  - {{type: {et}, target: {tgt_r}'
    return s + (f', role: {role}}}' if role else "}")

def emit(n):
    fm = ["---",
          f'id: {n["id"]}',
          f'type: {n["type"]}',
          f'name: {yaml_scalar(n["name"])}',
          f'created: {TS}',
          f'modified: {TS}']
    fm.append(f'provenance-hash: sha256:{hashlib.sha256(n["desc"].encode()).hexdigest()}')
    for k, v in n["fields"].items():
        fm.append(f'{k}: {yaml_list(v) if isinstance(v, list) else yaml_scalar(v)}')
    if n["edges"]:
        fm.append("edges:")
        fm += [_edge_line(e) for e in n["edges"]]
    if n["desc"]:
        fm.append("description: |")
        fm += ["  " + line for line in n["desc"].splitlines()]
    fm.append("---")
    d = os.path.join(HERE, TYPE_DIR[n["type"]])
    os.makedirs(d, exist_ok=True)
    rel = os.path.join(TYPE_DIR[n["type"]], n["id"] + ".md")
    with open(os.path.join(HERE, rel), "w") as f:
        f.write("\n".join(fm) + "\n")
    return rel

def main():
    ids = [x["id"] for x in N]
    assert len(ids) == len(set(ids)), "duplicate node id"
    # inject membership (in-program) on every non-program node, and cross-project edges
    for n in N:
        if n["type"] != "program":
            n["edges"].append(("in-program", PROGRAM))
        for tgt, role in CROSS.get(n["id"], []):
            n["edges"].append(("cross-project", tgt, role))
        # concept requires a `statement`; derive a one-sentence statement from the description
        if n["type"] == "concept" and "statement" not in n["fields"]:
            stmt = n["desc"].replace("\n", " ").split(". ")[0].strip().rstrip(".") + "."
            n["fields"] = {"statement": stmt, **n["fields"]}
    index_nodes = []
    for n in N:
        index_nodes.append({"id": n["id"], "type": n["type"], "path": emit(n)})
    # edge integrity: in-graph targets must be known; cross-project targets are out-of-graph
    known = set(ids)
    dangling = sorted({e[1] for n in N for e in n["edges"]
                       if e[0] != "cross-project" and e[1] not in known})
    index = {
        "schema": SCHEMA,
        "dataset-name": DATASET,
        "default-domain": "neuroimaging",
        "created": TS,
        "description": "clad-glimmer research-object graph for the Community Life & Adolescent Development study (a subproject of ADS).",
        "upstream-graph": "https://github.com/hebbianloop/ads-glimmer-graph (parent; same cohort)",
        "node-count": len(index_nodes),
        "nodes": sorted(index_nodes, key=lambda x: (x["type"], x["id"])),
    }
    with open(os.path.join(HERE, "_glimmer-index.json"), "w") as f:
        json.dump(index, f, indent=2)
        f.write("\n")
    print(f"emitted {len(N)} nodes -> _glimmer-index.json (node-count={len(index_nodes)})")
    print("dangling intra-graph edge targets:", dangling or "none")

if __name__ == "__main__":
    main()
