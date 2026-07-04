# ML Tutor — Week 1 lab dataset (synthetic, no PHI).
# In Colab: upload this file or run the cell that inlines it.
# 12 results; exactly 4 are out of range (potassium 6.1, sodium 128,
# creatinine 2.4, glucose 210) — checkpoint 3 expects those four.

panel = [
    {"patient_id": "MRN-1042", "analyte": "potassium",  "value": 6.1,  "unit": "mEq/L"},
    {"patient_id": "MRN-1042", "analyte": "sodium",     "value": 139,  "unit": "mEq/L"},
    {"patient_id": "MRN-2117", "analyte": "potassium",  "value": 4.2,  "unit": "mEq/L"},
    {"patient_id": "MRN-2117", "analyte": "creatinine", "value": 1.1,  "unit": "mg/dL"},
    {"patient_id": "MRN-3306", "analyte": "sodium",     "value": 128,  "unit": "mEq/L"},
    {"patient_id": "MRN-3306", "analyte": "glucose",    "value": 98,   "unit": "mg/dL"},
    {"patient_id": "MRN-4478", "analyte": "creatinine", "value": 2.4,  "unit": "mg/dL"},
    {"patient_id": "MRN-4478", "analyte": "potassium",  "value": 3.9,  "unit": "mEq/L"},
    {"patient_id": "MRN-5521", "analyte": "glucose",    "value": 210,  "unit": "mg/dL"},
    {"patient_id": "MRN-5521", "analyte": "sodium",     "value": 141,  "unit": "mEq/L"},
    {"patient_id": "MRN-6689", "analyte": "glucose",    "value": 105,  "unit": "mg/dL"},
    {"patient_id": "MRN-6689", "analyte": "creatinine", "value": 0.9,  "unit": "mg/dL"},
]
