# 🛡️ Fintech Analytics: Fraud Detection, Retention & Risk Intelligence System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/App-Streamlit-red)
![Status](https://img.shields.io/badge/Project-Complete-success)

> **Author:** Paul Egeonu  
> *Data Analyst | Machine Learning & Fintech Analytics Specialist*

---

## 📌 Project Overview

An end-to-end fintech analytics system combining:
- 📊 Exploratory Data Analysis (EDA)
- 🤖 Fraud Detection (Machine Learning)
- 👥 Customer Retention Analysis (Cohorts)
- ⚡ Real-Time Risk Dashboard (FraudShield AI)

---

## 🎯 Business Problem

| Challenge | Impact |
|----------|--------|
| Fraudulent Transactions | Financial loss & security risks |
| Customer Retention | Poor growth & revenue instability |

---

## 🧾 Dataset Features

| Feature | Description |
|--------|-------------|
| transaction_id | Unique transaction ID |
| user_id | Customer ID |
| amount | Transaction value |
| transaction_type | Type of transaction |
| status | Success/Failure |
| device_type | Device used |
| country | Location |
| acquisition_channel | Source |
| is_fraud | Target variable |

---

## 🧪 Methodology

1. Data Cleaning  
2. Feature Engineering  
3. Exploratory Data Analysis  
4. Model Training  
5. Evaluation (ROC AUC, Recall, Precision)  
6. Retention Analysis  
7. Dashboard Development  

---

## 📊 Key Insights

### 🔍 Fraud Insights
- High-value transactions → higher fraud risk  
- Failed transactions → strong fraud signal  
- Fraud varies by country & device  

---

### 📉 Retention Insights
- Sharp drop after Month 1  
- Retention ~76% across all segments  
- Problem is product experience, not acquisition  

---

### 📊 Revenue Insights
- 93% revenue from Ghana & South Africa  
- Heavy reliance on VIP users  
- 2023 shows major decline  

---

## 🤖 Model Performance

| Model | ROC AUC | Precision | Recall | F1 |
|------|--------|----------|--------|----|
| Gradient Boost | **0.9107** | 0.96 | 0.16 | 0.28 |
| Logistic Regression | 0.9078 | 0.06 | **0.97** | 0.12 |
| Random Forest | 0.8985 | 0.93 | 0.16 | 0.27 |

---

## 🖥️ FraudShield AI (App)

### Features
- 🔐 Login System  
- 🔍 Real-Time Fraud Prediction  
- 📊 KPI Dashboard  
- 📉 Retention Insights  

### Run App
```bash
streamlit run fraud_shield.py
```

---

## 🧰 Tech Stack

- Python
- Pandas / NumPy
- Scikit-learn
- Plotly
- Streamlit

---

## 🚀 Future Improvements

- SHAP Explainability  
- Churn Prediction Model  
- FastAPI Deployment  
- Power BI Dashboard  

---

## 🎯 Final Insight

> Fraud is a **security problem**, retention is a **product problem**.

Success depends on:
- Secure platform
- Strong user experience
- Data-driven decision making

---

## 📬 Contact

**Paul Egeonu**  
Data Analyst | Machine Learning & Fintech Analytics
