# Zecpath – AI Versioning & Retraining Dataset Plan

## 1. Model Versioning

Each AI model or processing engine will have a unique version.

Example:

ATS-v1.0
ATS-v1.1
Screening-v1.0
Interview-v1.0

The model version will be stored with every AI-generated result.

## 2. Dataset Versioning

Training and evaluation datasets will be maintained with version numbers.

Example:

dataset-v1.0
dataset-v1.1
dataset-v2.0

Each dataset version will contain the data used for a specific training or evaluation cycle.

## 3. Retraining Dataset

Relevant historical AI data can be collected into retraining datasets.

The dataset may contain:

- Candidate profiles
- Job profiles
- ATS results
- Screening results
- Interview results
- Final hiring outcomes

## 4. Retraining Process

Historical and newly collected data
        ↓
Data validation
        ↓
Dataset version created
        ↓
Model retraining
        ↓
Model evaluation
        ↓
New model version
        ↓
Deployment

## 5. Version Tracking

Each AI result should retain:

- Candidate ID
- Job ID
- Model Version
- Timestamp

This allows AI results to be traced back to the model version that generated them.

## 6. Dataset Evolution

New validated data can be added to future dataset versions.

Previous dataset versions should be retained so that model performance can be compared across different training cycles.