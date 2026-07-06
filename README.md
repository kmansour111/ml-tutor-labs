# ML Tutor — Lab Notebooks
Companion repo for the **ML Tutor** platform (PHSC-TXCL-PHOR 7304 — Intro to ML for
Health & Pharmacy Using Python). Structure mirrors the app:

Week 0 is the on-ramp: it opens with a concise Colab quick-start first, then a concise
Pyodide quick-start, before the first intro-to-Python material appears.

Some of the lab-style exercises are rewritten from the Fall 2025 source pool, but only
after they are remapped into the current scaffolded workflow. Old notebook order and
terminal-style execution are not preserved.

- `notebooks/week-NN.ipynb` — generated from `ml-tutor/src/data/lectures/week-NN.ts`
  (single source of truth; regenerate with `node scripts/generate-notebooks.mjs`)
- `data/week-NN/` — lab datasets (synthetic, no PHI)

Buttons in the app deep-link via `colab.research.google.com/github/kmansour111/ml-tutor-labs/...`
— each student click opens a fresh copy in Colab.

| Wk | Topic | Pharmacy application | Track | COs | Lab |
|----|-------|----------------------|-------|-----|-----|
| 0 | Python primer from absolute zero + Colab/Pyodide orientation | — | On-ramp | CO1 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-00.ipynb) |
| 1 | Python for data — in one week | Out-of-range lab flagger; UCI mini-analysis | Foundation | CO1, CO4 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-01.ipynb) |
| 2 | ML starts: basics & first models (trees) | Medication adherence | Core ML | CO2, CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-02.ipynb) |
| 3 | Regression & data cleaning | Drug clearance from PK data | Core ML | CO4, CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-03.ipynb) |
| 4 | Classification, imbalance & metrics | Adverse-drug-reaction prediction | Core ML | CO2, CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-04.ipynb) |
| 5 | Feature engineering & validation | Readmission prediction | Core ML | CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-05.ipynb) |
| 6 | Tuning, fairness & explainability | Equitable treatment recommendations | Core ML | CO5, CO6 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-06.ipynb) |
| 7 | Ensembles & friends | Antibiotic resistance | Core ML | CO2, CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-07.ipynb) |
| 8 | Unsupervised learning + Checkpoint 1 | Patient phenotyping; compound similarity | Core ML | CO2, CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-08.ipynb) |
| 9 | DL starts: neural network fundamentals | ADR signal detection | DL & GenAI | CO2, CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-09.ipynb) |
| 10 | Deep learning in practice (training & CNNs) | Pill-image classification | DL & GenAI | CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-10.ipynb) |
| 11 | NLP, embeddings & transformers | Clinical-notes mining | DL & GenAI | CO2, CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-11.ipynb) |
| 12 | LLMs & GenAI, critically | Verify AI output; protect data/IP | DL & GenAI | CO3, CO6 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-12.ipynb) |
| 13 | RAG, fine-tuning & agentic AI | Grounded pharmacy assistant | DL & GenAI | CO4, CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-13.ipynb) |
| 14 | MLOps & deployment | Medication dashboard, shipped | DL & GenAI | CO4, CO5 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-14.ipynb) |
| 15 | Open-source LLMs & AI coding tools | HF clinical-text model; verified AI-assisted script | DL & GenAI | CO3, CO5, CO6 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-15.ipynb) |
| 16 | Course review & synthesis + Checkpoint 2 | End-to-end recap on a fresh pharmacy dataset | Review | CO2, CO3, CO4, CO5, CO6 | [open](https://colab.research.google.com/github/kmansour111/ml-tutor-labs/blob/main/notebooks/week-16.ipynb) |

© 2026 Dr. Khalid Mansour. Course material — do not redistribute.
