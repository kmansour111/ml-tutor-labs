# ML Tutor — Lab Notebooks
Companion repo for the **ML Tutor** platform (PHSC-TXCL-PHOR 7304 — Intro to ML for
Health & Pharmacy Using Python). Structure mirrors the app:

- `notebooks/week-NN.ipynb` — generated from `ml-tutor/src/data/lectures/week-NN.ts`
  (single source of truth; regenerate with `node scripts/generate-notebooks.mjs`)
- `data/week-NN/` — lab datasets (synthetic, no PHI)

Buttons in the app deep-link via `colab.research.google.com/github/kmansour111/ml-tutor-labs/...`
— each student click opens a fresh copy in Colab.

| Wk | Topic | Pharmacy application | Track | COs | Lab |
|----|-------|----------------------|-------|-----|-----|
| 0 | Your first 30 minutes of Python (orientation, hand-authored) | — | On-ramp | CO1 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-00.ipynb) |
| 1 | Python basics | Flag out-of-range labs | Bootcamp | CO1 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-01.ipynb) |
| 2 | Functions, pandas & numpy | EHR CSVs; profile labs | Bootcamp | CO1, CO4 | _authoring_ |
| 3 | Data wrangling & plots (UCI project) | Dispensing patterns | Bootcamp | CO1, CO4 | _authoring_ |
| 4 | ML basics & first models (trees) | Medication adherence | Core ML | CO2, CO5 | _authoring_ |
| 5 | Regression, cleaning & data quality | Drug clearance from PK data | Core ML | CO4, CO5 | _authoring_ |
| 6 | Supervised learning, imbalance & metrics | Adverse-drug-reaction prediction | Core ML | CO2, CO5 | _authoring_ |
| 7 | Feature engineering & cross-validation | Readmission prediction | Core ML | CO5 | _authoring_ |
| 8 | Tuning, fairness & explainability (SHAP/LIME) | Equitable treatment recs | Core ML | CO5, CO6 | _authoring_ |
| 9 | Ensembles & unsupervised (clustering/PCA) | Antibiotic resistance; patient phenotyping | Core ML | CO2, CO5 | _authoring_ |
| 10 | Neural networks fundamentals (MLP & backprop) | ADR signal detection | DL & GenAI | CO2, CO5 | _authoring_ |
| 11 | Deep learning in practice (training & CNNs) | Pill-image classification | DL & GenAI | CO5 | _authoring_ |
| 12 | NLP, embeddings & transformers | Clinical-notes mining | DL & GenAI | CO2, CO5 | _authoring_ |
| 13 | LLMs & GenAI: prompting, limits, data/IP | Verify AI output; protect data/IP | DL & GenAI | CO3, CO6 | _authoring_ |
| 14 | RAG, fine-tuning, agentic AI & deployment | Pharmacy assistant; Streamlit dashboard | DL & GenAI | CO4, CO5 | _authoring_ |
| 15 | Capstone build (end-to-end ML/DL) | Pharmacy capstone project | DL & GenAI | CO5, CO4 | _authoring_ |
| 16 | Capstone presentations & governance review | Ethics; data excellence | DL & GenAI | CO4, CO3, CO6 | _authoring_ |

© 2026 Dr. Khalid Mansour. Course material — do not redistribute.
