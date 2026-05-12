# AI-Assisted Cybersecurity Analysis Framework

## Overview

This project is a secure local Agentic AI-based cybersecurity analysis framework developed using Machine Learning, Large Language Models (LLMs), and Cryptographic techniques.

The system is capable of:

- Detecting malicious cyber threats using Machine Learning
- Analyzing suspicious cybersecurity events using a local LLM
- Performing AES encryption and decryption
- Generating SHA256 hashes
- Visualizing cybersecurity analytics
- Generating downloadable prediction reports
- Comparing machine learning model performance
- Providing explainable AI-based threat analysis

The project uses the CICIDS2017 dataset for intrusion detection analysis and integrates a locally running Ollama LLM for AI-assisted cybersecurity reasoning.

---

# Features

## Machine Learning Threat Detection

- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

The system compares all models and automatically selects the best-performing model.

---

## AI Threat Analysis

The application uses a local Ollama LLM (`tinyllama`) to analyze suspicious cybersecurity events and generate:

- Threat category
- Severity level
- Technical explanation
- Recommended mitigation

---

## Encryption Module

AES encryption and decryption module for protecting sensitive cybersecurity data.

---

## Hashing Module

SHA256 hashing module for integrity verification and secure fingerprinting.

---

## Cybersecurity Dashboard

Interactive dashboard containing:

- Accuracy
- Precision
- Recall
- F1 Score
- Model comparison
- Feature importance
- Confusion matrix
- Threat distribution visualization

---

## Dataset Analysis

Upload CICIDS2017 CSV files and generate:

- Threat predictions
- Severity classifications
- Threat distribution analytics
- Downloadable CSV reports

---

# Technologies Used

## Frontend

- Streamlit

## Machine Learning

- Scikit-learn
- Random Forest
- Decision Tree
- SVM

## AI / LLM

- Ollama
- TinyLlama

## Data Processing

- Pandas
- NumPy

## Visualization

- Plotly
- Matplotlib
- Seaborn

## Cryptography

- PyCryptodome

## Database

- SQLite

---

# Project Structure

```text
agentic_ai_IDS/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── aes_key.bin
│
├── agents/
│   ├── __init__.py
│   ├── llm_agent.py
│   ├── threat_agent.py
│
├── models/
│   ├── __init__.py
│   ├── train_model.py
│   ├── saved_model.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   ├── model_metrics.pkl
│   ├── comparison_results.pkl
│   ├── confusion_matrix.pkl
│
├── utils/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── encryption.py
│   ├── hashing.py
│
├── database/
│   ├── __init__.py
│   ├── database.py
│   ├── threats.db
│
├── datasets/
│   ├── CICIDS2017.csv
│
├── reports/
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   ├── feature_importance.csv
│   ├── model_comparison.csv
```

---

# Dataset

Dataset used:

CICIDS2017 Dataset

Place dataset file inside:

```text
datasets/CICIDS2017.csv
```

---

# Step-by-Step Project Execution Guide

## Step 1 — Open Project Folder

Open terminal inside:

```text
I:\agentic_ai_IDS
```

Always run commands from the project root folder.

---

## Step 2 — Create Virtual Environment

Run:

```bash
python -m venv .venv
```

---

## Step 3 — Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

You should now see:

```text
(.venv)
```

inside terminal.

---

## Step 4 — Install Required Packages

Run:

```bash
pip install -r requirements.txt
```

---

## Step 5 — Install Ollama

Download Ollama:

https://ollama.com/download

Install normally.

---

## Step 6 — Pull TinyLlama Model

Run:

```bash
ollama pull tinyllama
```

This downloads the local LLM model.

---

## Step 7 — Add Dataset

Place:

```text
CICIDS2017.csv
```

inside:

```text
datasets/
```

Final path:

```text
datasets/CICIDS2017.csv
```

---

## Step 8 — Train Machine Learning Models

Run:

```bash
python -m models.train_model
```

This step will:

- Train Decision Tree
- Train Random Forest
- Train SVM
- Generate evaluation metrics
- Save trained model files
- Generate reports
- Create confusion matrix
- Create feature importance analysis

---

## Step 9 — Verify Generated Files

After training, verify these files exist.

### Inside `models/`

```text
saved_model.pkl
scaler.pkl
feature_names.pkl
model_metrics.pkl
comparison_results.pkl
confusion_matrix.pkl
```

### Inside `reports/`

```text
confusion_matrix.png
feature_importance.png
feature_importance.csv
model_comparison.csv
```

---

## Step 10 — Start Ollama Service

Run:

```bash
ollama serve
```

If you see:

```text
address already in use
```

ignore it.

That means Ollama is already running.

---

## Step 11 — Run Streamlit Application

Open a second terminal.

Activate virtual environment again:

```bash
.venv\Scripts\activate
```

Run:

```bash
streamlit run app.py
```

---

## Step 12 — Open Application

Open browser:

```text
http://localhost:8501
```

---

# How to Use the Application

## Threat Analysis Module

Go to:

```text
Threat Analysis
```

Enter suspicious activity such as:

```text
Multiple failed administrator login attempts detected from external IP address.
```

The AI system will generate:

- Threat category
- Severity level
- Technical explanation
- Recommended mitigation

---

## Dataset Analysis Module

Go to:

```text
Dataset Analysis
```

Upload:

```text
datasets/CICIDS2017.csv
```

The system will:

- Predict malicious traffic
- Predict benign traffic
- Generate threat severity
- Create visual analytics
- Allow downloadable reports

---

## Encryption Module

Go to:

```text
Encryption
```

Input example:

```text
username=admin password=root123
```

The system will:

- Encrypt sensitive data
- Decrypt encrypted data

---

## Hashing Module

Go to:

```text
Hashing
```

Input example:

```text
Sensitive Threat Intelligence Report
```

The system will generate:

- SHA256 cryptographic hash

---

## Dashboard Module

Go to:

```text
Dashboard
```

The dashboard displays:

- Accuracy
- Precision
- Recall
- F1 Score
- Model comparison
- Feature importance
- Confusion matrix
- Threat distribution analytics

---

# Machine Learning Models Used

| Model | Purpose |
|---|---|
| Decision Tree | Baseline classification |
| Random Forest | Main IDS classifier |
| SVM | Comparative evaluation |

---

# Explainable AI Features

The system includes explainable AI components such as:

- Feature importance analysis
- Confusion matrix visualization
- Comparative model evaluation

---

# Security Features

- AES Encryption
- SHA256 Hashing
- Local LLM inference
- SQLite threat logging

---

# Research Contribution

This project demonstrates a hybrid AI-based cybersecurity analysis framework integrating:

- Machine Learning
- Explainable AI
- Large Language Models
- Cryptographic controls
- Threat analytics visualization

---

# Important Notes

- Always run commands from project root.
- Keep Ollama running while using Threat Analysis.
- Use the same CICIDS2017 dataset structure.
- The application performs local inference only.
- No external API keys are required.
- Use Python virtual environment for all commands.

---

# Author

AI-Assisted Cybersecurity Analysis Framework

Developed for:

Module: Cyber and Artificial Intelligence (Applications)

Course: Artificial Intelligence with Professional Placement

