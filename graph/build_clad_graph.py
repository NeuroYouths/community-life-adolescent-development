#!/usr/bin/env python3
"""build_clad_graph.py — emit the clad-glimmer research-object graph (idempotent).

Writes typed Glimmer nodes (concept / experiment / method / publication / persona / organization /
dataset) as YAML-front-matter markdown sidecars under graph/<type-dir>/, plus _glimmer-index.json.
Node format + edge vocabulary mirror hebbianloop/glimmer (v0.3). Re-running rewrites graph/ only.

No PHI: this graph contains only de-identified study metadata, hypotheses, methods, and outputs.
Usage:  python3 graph/build_clad_graph.py
"""
import hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TS = "2026-06-10T00:00:00+00:00"          # fixed stamp (deterministic re-runs)
SCHEMA = "glimmer/v0.3"
DATASET = "clad-glimmer"

TYPE_DIR = {
    "concept": "concepts", "experiment": "experiments", "method": "methods",
    "publication": "publications", "persona": "personas", "organization": "organizations",
    "dataset": "datasets", "derivative": "derivatives", "finding": "findings",
}

# ---- node spec: (id, type, name, fields{}, edges[(type,target)], description) -----------------
N = []
def node(id, type, name, fields=None, edges=None, desc=""):
    N.append({"id": id, "type": type, "name": name,
              "fields": fields or {}, "edges": edges or [], "desc": desc.strip()})

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
      ("tested-by-experiment", "ads-cpt"), ("tested-by-experiment", "ads-gonogo"),
      ("tested-by-experiment", "ads-efr"), ("tested-by-experiment", "ads-emofilm"),
      ("tested-by-experiment", "ads-dwi-hardi"),
      ("cited-in", "pub-corticostriatal-convergence")],
     """The two strongest CMI latent factors — inhibitory/impulse control (CPT + Go/NoGo) and emotional
face recognition (EFR) — each index an individual cortico-striatal phenotype that converges across
modalities (behavior -> function -> structure) onto distinct striatal parcels. Impulse-control axis:
dorsal/associative caudate <-> DLPFC/IFG (Go/NoGo connectivity + frontostriatal DWI). Emotion axis:
ventral/limbic striatum <-> vmPFC/amygdala (EmoFilm intersubject synchrony + emotion-network DWI).
Multimodal striatal parcellation recovers both; individual latent-factor deviation predicts the matching
parcel's connectivity; and these predict vulnerability outcomes (substance use, violence).""")

node("concept-neurocognitive-maturity", "concept",
     "Adolescent neurocognitive maturity (Cognitive Maturity Index)",
     {"concept-kind": "construct", "status": "supported", "falsifiable": True},
     [("tested-by-experiment", "ads-cpt"), ("tested-by-experiment", "ads-wof"),
      ("tested-by-experiment", "ads-efr"), ("tested-by-experiment", "ads-temporal-discounting"),
      ("cited-in", "pub-eldamaty-2022-cmi")],
     """Latent factors of inhibitory control, risk/reward, and emotional face recognition predict
chronological age; the residual (CMI) indexes maturational imbalance. Ridge model R2=0.51, MAE +/-10.11
months. Lower CMI tracks higher DUSI violence proneness (R=-0.28) and substance use, mediated by BAS-D.""")

node("concept-impulse-control-frontostriatal", "concept",
     "Inhibitory control and frontostriatal organization",
     {"concept-kind": "hypothesis", "status": "under-investigation", "falsifiable": True},
     [("tested-by-experiment", "ads-cpt"), ("tested-by-experiment", "ads-gonogo"),
      ("tested-by-experiment", "ads-dwi-hardi")],
     """Inhibitory/impulse control (ICLF; the strongest age predictor, beta=0.72) maps onto associative
dorsal-caudate <-> prefrontal executive cortex (DLPFC/IFG/preSMA) coupling, expressed in both functional
and structural (frontostriatal DWI) connectivity.""")

node("concept-gonogo-inhibition", "concept",
     "Go/NoGo response inhibition and the frontostriatal control loop",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "ads-gonogo")],
     """Individual differences in Go/NoGo response inhibition recruit and shape the caudate<->DLPFC/IFG
control loop; the control-axis behavioral->functional bridge of the flagship hypothesis.""")

node("concept-efr-individual-differences", "concept",
     "Emotional face recognition individual differences",
     {"concept-kind": "construct", "status": "supported", "falsifiable": True},
     [("tested-by-experiment", "ads-efr"), ("tested-by-experiment", "ads-emofilm")],
     """EFR latent factors (negative/positive emotion recognition) are a strong component of CMI; negative
emotion sensitivity rises with age (beta=0.35) while positive-emotion recognition declines with puberty.
Individual EFR deviation indexes an emotion-processing phenotype.""")

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
     """Adolescent social strain (neighborhood/family adversity) cascades through altered social norms and
violence exposure into violence proneness and vulnerability in emerging adulthood (SEM / latent growth).""")

node("concept-striatal-development", "concept",
     "Multimodal striatal functional parcellation across development",
     {"concept-kind": "research-question", "status": "under-investigation", "falsifiable": True},
     [("tested-by-experiment", "ads-rest"), ("tested-by-experiment", "ads-dwi-hardi"),
      ("cited-in", "pub-eldamaty-striatal-parcellation")],
     """Masked group-ICA functional parcellation fused with seed-based diffusion connectivity recovers
limbic (emotion) and associative (control) striatal parcels; medial-caudate<->prefrontal connectivity
relates to outcomes and predicts substance-use initiation 18 months later.""")

node("concept-emofilm-violence", "concept",
     "EmoFilm emotion-network response -> Wave-4 violence outcome",
     {"concept-kind": "research-question", "status": "open", "falsifiable": True},
     [("tested-by-experiment", "ads-emofilm")],
     """Prospective prediction of Wave-4 violence/substance outcomes from EmoFilm emotion-network response.
Cross-links to ads-glimmer:concept-emofilm-violence-outcome (sibling study, same cohort).""")

# ---------------- EXPERIMENTS ----------------
node("ads-cpt", "experiment", "Continuous Performance Task (CPT)",
     {"task-name": "cpt", "conditions": ["target", "lure-Q"], "n-trials": 150},
     [], "Inhibitory control / sustained attention; signal-detection metrics (d', response bias, RT SD).")
node("ads-wof", "experiment", "Wheel of Fortune (WOF)",
     {"task-name": "wof", "conditions": ["high-risk", "low-risk"], "n-trials": 90},
     [], "Risk/reward decision making under varied win probabilities; fMRI in waves 1-3.")
node("ads-efr", "experiment", "Emotional Face Recognition (EFR)",
     {"task-name": "efr", "conditions": ["happy", "angry", "fearful", "sad", "disgust", "surprise", "neutral"], "n-trials": 70},
     [], "NimStim facial-emotion recognition; accuracy + RT for positive/negative affect (behavioral).")
node("ads-temporal-discounting", "experiment", "Temporal Delay Discounting (TD)",
     {"task-name": "temporal-discounting"},
     [], "Preference for immediate vs delayed rewards; area-under-curve of indifference values.")
node("ads-emofilm", "experiment", "EmoFilm naturalistic emotional film task",
     {"task-name": "emofilm", "conditions": ["REST", "NEU", "POS", "NEG"]},
     [], "Naturalistic emotional film viewing during fMRI (Wave-4); block design; supports intersubject-synchrony analysis.")
node("ads-gonogo", "experiment", "Go/NoGo response-inhibition task",
     {"task-name": "gonogo", "conditions": ["go", "nogo"]},
     [], "Response inhibition during fMRI; frontostriatal (caudate<->DLPFC/IFG) activation + connectivity.")
node("ads-rest", "experiment", "Resting-state fMRI",
     {"task-name": "rest", "duration-sec": 342},
     [], "Resting-state BOLD; input to masked striatal group-ICA parcellation and connectivity.")
node("ads-dwi-hardi", "experiment", "Diffusion-weighted imaging (HARDI)",
     {"task-name": "dwi-hardi"},
     [], "HARDI diffusion acquisition; frontostriatal + emotion-network white-matter structure and seed-based tractography.")

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
     {"tool": "fMRIPrep", "version": "23.x"}, [], "Standardized BOLD/anat preprocessing onto NICAP55/MNI.")
node("freesurfer-recon", "method", "FreeSurfer / FastSurfer surface reconstruction",
     {"tool": "FastSurfer", "version": "2.x"}, [], "Cortical surface reconstruction + morphometry.")
node("nicap55-template", "method", "NICAP55 study-specific template construction",
     {"tool": "ANTs multivariate template", "version": "ANTs 2.x"}, [],
     "Age-appropriate multicontrast developmental template (T1w/T2w) for normalization.")
node("dwi-preprocessing", "method", "DWI/HARDI preprocessing",
     {"tool": "QSIPrep", "version": "0.x"}, [], "Denoising, distortion/eddy correction, model fitting for HARDI.")
node("split-half-reproducibility", "method", "Split-half reproducibility validation",
     {"tool": "custom (Munkres matching + correlation)", "version": "0.1"}, [],
     "Repeated split-half ICA with Hungarian matching to select reproducible striatal model order (k~5 primary, ~8-10 fine).")

# ---------------- PUBLICATIONS ----------------
node("pub-eldamaty-2022-cmi", "publication",
     "Introducing an Adolescent Cognitive Maturity Index (Frontiers 2022)",
     {"pub-status": "published", "venue": "Frontiers in Psychology", "year": 2022,
      "doi": "10.3389/fpsyg.2022.1017317", "pmid": "36571021",
      "repo": "https://github.com/hebbianloop/eldamaty2020b"},
     [("authored-by", "persona-shady-el-damaty"), ("authored-by", "persona-diana-fishbein"),
      ("authored-by", "persona-john-vanmeter"),
      ("addresses-concept", "concept-neurocognitive-maturity"),
      ("cites-method", "cfa-sem"), ("cites-method", "lasso-age-prediction"),
      ("funded-by", "org-nij")],
     "Published CMI paper (RQ1). Latent-factor age prediction; CMI mediates vulnerability via BAS-D.")
node("pub-eldamaty-violence-cascade", "publication",
     "Social-strain cascade to violence & altered norms (SEM)",
     {"pub-status": "draft", "repo": "https://github.com/hebbianloop/eldamaty2020a"},
     [("authored-by", "persona-shady-el-damaty"), ("authored-by", "persona-diana-fishbein"),
      ("addresses-concept", "concept-violence-cascade"), ("funded-by", "org-nij")],
     "Dissertation-core SEM/latent-growth of strain -> norms -> violence (RQ2). Draft.")
node("pub-eldamaty-striatal-parcellation", "publication",
     "Multimodal parcellation of the adolescent striatum",
     {"pub-status": "draft"},
     [("authored-by", "persona-shady-el-damaty"), ("authored-by", "persona-john-vanmeter"),
      ("addresses-concept", "concept-striatal-development"),
      ("cites-method", "masked-ica-parcellation"), ("cites-method", "split-half-reproducibility"),
      ("funded-by", "org-nij")],
     "Striatal functional/diffusion parcellation (RQ3). Draft / OHBM-CCN-FLUX. eldamaty2020c.")
node("pub-corticostriatal-convergence", "publication",
     "Cortico-striatal multimodal convergence of impulse-control & emotion phenotypes (PLANNED)",
     {"pub-status": "draft"},
     [("authored-by", "persona-shady-el-damaty"),
      ("addresses-concept", "concept-corticostriatal-convergence"),
      ("cites-method", "multimodal-striatal-parcellation"),
      ("cites-method", "intersubject-synchrony"),
      ("cites-method", "seeded-diffusion-connectivity")],
     "PLANNED flagship paper: two-axis (impulse-control + emotion) cortico-striatal convergence across behavior/function/structure.")
node("pub-eldamaty-2017-dissertation", "publication",
     "Adolescent Neurocognitive Maturity Mediates Paths to Altered Social Norms & Vulnerability in Emerging Adulthood",
     {"pub-status": "published", "venue": "Georgetown University (PhD dissertation)", "year": 2017},
     [("authored-by", "persona-shady-el-damaty"),
      ("aggregates", "pub-eldamaty-2022-cmi"),
      ("aggregates", "pub-eldamaty-violence-cascade"),
      ("aggregates", "pub-eldamaty-striatal-parcellation"),
      ("addresses-concept", "concept-corticostriatal-convergence"),
      ("funded-by", "org-nij")],
     "The defended dissertation; umbrella output aggregating the component papers.")

# ---------------- PERSONAS ----------------
node("persona-shady-el-damaty", "persona", "Shady El Damaty",
     {"persona-kind": "researcher"}, [("affiliated-with", "org-georgetown-university")],
     "Dissertation author; shared with ads-glimmer (same id).")
node("persona-john-vanmeter", "persona", "John W. VanMeter",
     {"persona-kind": "researcher"}, [("affiliated-with", "org-cfmi-georgetown")],
     "Dissertation advisor; director, CFMI.")
node("persona-diana-fishbein", "persona", "Diana H. Fishbein",
     {"persona-kind": "researcher"}, [],
     "Co-mentor (Penn State / UNC); translational prevention.")

# ---------------- ORGANIZATIONS ----------------
node("org-nij", "organization", "National Institute of Justice",
     {"org-kind": "funder"}, [], "Funder of CLAD (award 2016-R2-CX-0019). Shared with ads-glimmer.")
node("org-georgetown-university", "organization", "Georgetown University",
     {"org-kind": "institution"}, [], "Degree-granting institution. Shared with ads-glimmer.")
node("org-cfmi-georgetown", "organization", "Center for Functional & Molecular Imaging (CFMI), Georgetown",
     {"org-kind": "lab"}, [("part-of", "org-georgetown-university")],
     "Imaging center where ADS/CLAD data were acquired. Shared with ads-glimmer.")

# ---------------- DATASETS (pointers; bytes deferred) ----------------
node("dataset-clad-bids-wave4", "dataset", "CLAD Wave-4 BIDS (de-identified)",
     {"datalad-relative-path": "data/bids", "tier": "OPEN-deid", "bytes-status": "deferred"},
     [("conforms-to-standard", "bids"), ("realized-by", "ads-emofilm"),
      ("realized-by", "ads-gonogo"), ("realized-by", "ads-rest"), ("realized-by", "ads-dwi-hardi")],
     "Wave-4 / Visit-7 BIDS (61 subj local). Defaced + annexed in the data pass; raw DICOM stays in the private backend.")
node("dataset-clad-bids-w13", "dataset", "CLAD Waves 1-3 BIDS (de-identified)",
     {"datalad-relative-path": "data/bids", "tier": "OPEN-deid", "bytes-status": "deferred"},
     [("conforms-to-standard", "bids")],
     "Longitudinal Waves 1-3 BIDS (142 subj). Provides developmental baseline; bytes deferred.")

# ----------------------------- emit -----------------------------
def yaml_scalar(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    return '"' + s.replace('"', '\\"') + '"'

def yaml_list(vals):
    return "[" + ", ".join(yaml_scalar(v) for v in vals) + "]"

def emit(n):
    fm = ["---",
          f'id: {n["id"]}',
          f'type: {n["type"]}',
          f'name: {yaml_scalar(n["name"])}',
          f'created: {TS}',
          f'modified: {TS}']
    phash = hashlib.sha256(n["desc"].encode()).hexdigest()
    fm.append(f'provenance-hash: sha256:{phash}')
    for k, v in n["fields"].items():
        if isinstance(v, list):
            fm.append(f'{k}: {yaml_list(v)}')
        else:
            fm.append(f'{k}: {yaml_scalar(v)}')
    if n["edges"]:
        fm.append("edges:")
        for et, tgt in n["edges"]:
            fm.append(f'  - {{type: {et}, target: {tgt}}}')
    if n["desc"]:
        fm.append("description: |")
        for line in n["desc"].splitlines():
            fm.append("  " + line)
    fm.append("---")
    body = "\n".join(fm) + "\n"
    d = os.path.join(HERE, TYPE_DIR[n["type"]])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, n["id"] + ".md"), "w") as f:
        f.write(body)
    return os.path.join(TYPE_DIR[n["type"]], n["id"] + ".md")

def main():
    ids = [x["id"] for x in N]
    assert len(ids) == len(set(ids)), "duplicate node id"
    index_nodes = []
    for n in N:
        rel = emit(n)
        index_nodes.append({"id": n["id"], "type": n["type"], "path": rel})
    # edge integrity (intra-graph targets; cross-graph 'bids'/ads-glimmer noted in descriptions)
    known = set(ids) | {"bids"}
    dangling = sorted({t for n in N for _, t in n["edges"] if t not in known})
    index = {
        "schema": SCHEMA,
        "dataset-name": DATASET,
        "default-domain": "neuroimaging",
        "created": TS,
        "description": "clad-glimmer research-object graph for the Community Life & Adolescent Development study.",
        "upstream-graph": "https://github.com/hebbianloop/ads-glimmer-graph (sibling; same cohort)",
        "nodes": sorted(index_nodes, key=lambda x: (x["type"], x["id"])),
    }
    with open(os.path.join(HERE, "_glimmer-index.json"), "w") as f:
        json.dump(index, f, indent=2)
        f.write("\n")
    print(f"emitted {len(N)} nodes -> _glimmer-index.json")
    print("dangling intra-graph edge targets:", dangling or "none")

if __name__ == "__main__":
    main()
