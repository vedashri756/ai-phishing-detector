# Advanced AI Phishing Detection System

A hybrid machine learning system for detecting phishing emails using a combination of NLP, feature engineering, rule-based logic, and transformer models (BERT).

---

## Overview

This project implements a multi-layered phishing detection pipeline designed to improve real-world reliability by combining:

* Traditional machine learning (TF-IDF + Logistic Regression)
* Feature engineering (behavioral and textual signals)
* Rule-based overrides for critical phishing patterns
* Transformer model (BERT) for semantic understanding

---

## Key Features

* Real-time email analysis
* Hybrid ensemble model (ML + BERT)
* Detection of phishing indicators such as:

  * Suspicious keywords (urgent, verify, bank, etc.)
  * Click-based patterns ("click here")
  * Structural anomalies
* Explainable outputs with feature analysis
* Confidence-based prediction system

---

## Model Architecture

### 1. NLP Pipeline

* TF-IDF Vectorization
* Logistic Regression classifier

### 2. Feature Engineering

Extracted features include:

* Number of suspicious keywords
* Presence of phishing phrases
* URL detection
* Text length, digits, capitalization

### 3. Rule-Based Layer

Overrides model predictions for high-risk patterns:

* “click here + verify”
* Multiple suspicious keywords

### 4. BERT Integration

* Transformer-based semantic classification
* Improves detection of subtle phishing attempts

### 5. Final Prediction Logic

* Confidence-based weighting
* ML dominates high-confidence cases
* Hybrid combination for ambiguous inputs

---

## Project Structure

```
phishing_detector/
│
├── app.py
├── model.py
├── bert_model.py
├── utils.py
├── emails.csv
├── requirements.txt
└── README.md
```

---

## Installation

```
pip install -r requirements.txt
```

---

## Run the Application

```
streamlit run app.py
```

---

## Example

Input:

```
Urgent! Your bank account is compromised, click here to verify now
```

Output:

```
Phishing Detected (~90%)
```

---

## Performance

* Achieves ~85–90% accuracy on phishing/spam-style datasets
* Improved reliability through hybrid modeling
* Handles both obvious and moderately subtle phishing cases

---

## Key Learnings

* Real-world ML systems benefit from hybrid approaches
* Feature engineering significantly improves detection
* Transformer models enhance semantic understanding
* Rule-based systems help handle edge cases

---

## Future Improvements

* Fine-tuning BERT on phishing-specific datasets
* URL/domain reputation analysis
* Email header analysis
* Browser extension for real-time protection
* Cloud deployment

---

## Author

Vedashri Dhaneshwar
Aspiring Data Scientist | Machine Learning | AI Systems
