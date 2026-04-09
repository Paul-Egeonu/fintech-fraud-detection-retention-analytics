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

This project is an end-to-end fintech analytics solution that integrates:

- 📊 Exploratory Data Analysis (EDA)
- 🤖 Machine Learning for Fraud Detection
- 👥 Cohort-Based Customer Retention Analysis
- ⚡ Real-Time Risk Scoring via Interactive Dashboard (FraudShield AI)

### 🎯 Goal

Simulate how modern fintech companies:
- Detect fraudulent transactions
- Understand user behavior
- Improve decision-making using data

---

## 📁 Project Structure

```
fintech-analytics/
│
├── data/
│   ├── transactions.csv
│   ├── users.csv
│   └── revenue.csv
│
├── notebooks/
│   └── master_analysis.ipynb
│
├── app/
│   └── fraud_shield.py
│
├── models/
│   ├── fraud_model.pkl
│   └── model_columns.pkl
│
├── images/
│   ├── dashboard.png
│   ├── cohort_heatmap.png
│   └── fraud_analysis.png
│
├── requirements.txt
└── README.md
```
---


## 🎯 Business Problem

| Challenge | Impact |
|----------|--------|
| 🛡️ Fraud Risk | Financial loss, security vulnerabilities, reduced trust |
| 📉 Customer Retention | Early churn, weak engagement, poor revenue growth |

---

## ✅ Solution Approach

- Identify high-risk transactions using ML
- Analyze user behavior (RFM, cohorts)
- Monitor retention trends
- Build real-time fraud risk dashboard

---

## 🧾 Dataset Description

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

## 🛠️ Data Integration

```python
transactions = pd.read_csv("data/transactions.csv")
users = pd.read_csv("data/users.csv")
revenue = pd.read_csv("data/revenue.csv")

df = transactions.merge(revenue, on='transaction_id', how='left')
df = df.merge(users, on='user_id', how='left')
```

---

## 💱 Currency Normalization

All transactions converted to USD:

- Nigeria → 1500 NGN = 1 USD  
- Ghana → 15 GHS = 1 USD  
- Kenya → 130 KES = 1 USD  
- South Africa → 18 ZAR = 1 USD  

---

## 🧠 Project Objectives

- Perform EDA  
- Identify fraud patterns  
- Build ML models  
- Cohort retention analysis  
- Develop real-time app  

---

## 🧪 Methodology

### 1. Data Cleaning
- Missing values
- Duplicate removal
- Type standardization

### 2. Feature Engineering

**Time Features**
- Year, Month, Day, Day Name

**User Behavior**
- Transaction frequency
- Average spend
- Amount vs user average

**Risk Features**
- Failed transaction flag
- High-value indicator
- Fraud interaction features

---

## 📊 Exploratory Data Analysis (EDA)

### 📊 Overall Trend Summary
- 🚀 2022 → Growth Phase  
- 📉 2023 → Decline Phase  

> Growth → Peak → Decline lifecycle

### 🔥 Critical Insight
> Revenue decline is driven by drop in transaction volume, not spending behavior.

---

## 📉 Retention Insights

- Sharp drop after Month 1  
- Stabilization after Month 2  
- ~76% retention across segments  
- Minimal variation across devices/channels  

> Indicates product-level issue

---

## 📊 Revenue Insights

- 93% revenue from Ghana & South Africa  
- VIP users dominate revenue  
- Sustained 2023 decline  

---

## 🔍 Fraud Insights

- High-value transactions → higher fraud  
- Failed transactions → strong signal  
- Fraud varies by country  
- Web & transfer → higher risk  

---

## 🤖 Machine Learning Models

| Model | ROC AUC | Precision | Recall | F1 |
|------|--------|----------|--------|----|
| Gradient Boost | **0.9107** | 0.96 | 0.16 | 0.28 |
| Logistic Regression | 0.9078 | 0.06 | **0.97** | 0.12 |
| Random Forest | 0.8985 | 0.93 | 0.16 | 0.27 |

### ✅ Final Model
- Gradient Boosting  
- ROC AUC: 0.9107  
- Threshold: 0.0784  

---

## ⚠️ Modeling Insights

- Class imbalance handled with `class_weight='balanced'`
- ROC AUC preferred over accuracy
- Feature quality impacts performance

---

## ⚠️ Model Limitations

- Fraud is highly **imbalanced**
- Model may **overfit historical patterns**
- Limited behavioral depth reduces accuracy

### 🔄 Important Note

> The model should be **retrained periodically with new data** to:
- Capture evolving fraud patterns  
- Reduce class imbalance issues  
- Improve prediction accuracy  
- Adapt to new user behaviors  

---

## 🖼️ Screenshots & Visuals

### 📊 Dashboard Preview
![Dashboard](images/dashboard.png)

### 📉 Cohort Retention Heatmap
<img width="952" height="547" alt="Retention_cohort_Heatmap" src="https://github.com/user-attachments/assets/c647a94f-7271-4b6f-a620-29db78f5c9d2" />


### 🚨 Fraud Analysis
<img width="708" height="471" alt="fraud_by_amount" src="https://github.com/user-attachments/assets/24c1dc85-ab7e-4e39-a594-3a9685dc1a4a" />


---

## 🧠 Executive Summary

- Fraud driven by behavior & transaction patterns  
- Severe early churn  
- Retention consistent across segments  

---

## 💼 Business Recommendations

### 🛡️ Fraud Prevention
- Flag high-value transactions  
- Monitor failed attempts  
- Geo-based controls  

### 📈 Retention Strategy
- Improve onboarding  
- Incentives & rewards  
- Habit-forming features  

### ⚙️ Risk Management
- Use probability thresholds  
- Monitor fraud segments  
- Real-time alerts  

### 📢 Growth Strategy
- Shift to retention-first  
- Fix product before scaling  

---

## 🖥️ FraudShield AI (App)

### Features
- 🔐 Authentication  
- 🔍 Real-time fraud prediction  
- 📊 KPI dashboard  
- 📉 Retention analysis  

### Run App
```bash
streamlit run fraud_shield.py
```

⚠️ FastAPI not yet implemented

---

## 📦 Requirements

Create a `requirements.txt` file:

```
pandas
numpy
matplotlib
seaborn
scikit-learn
plotly
streamlit
joblib
faker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧰 Tech Stack

- Python  
- Pandas / NumPy  
- Scikit-learn  
- Plotly  
- Streamlit  
- Joblib  

---

## 🚀 Future Improvements

- SHAP explainability  
- Churn prediction  
- Kafka pipeline  
- Feature store  
- Power BI dashboard  
- FastAPI deployment  

---

## 🎯 Project Value

- End-to-end analytics  
- Real fintech problem solving  
- ML development  
- Business insights  
- App deployment  

---

## ⭐ Final Insight

> Fraud is a **behavior problem**  
> Retention is a **product problem**

Success depends on:
- Security  
- Engagement  
- Data-driven decisions  

---

## 📬 Contact

**Paul Egeonu**  
Data Analyst | Machine Learning & Fintech Analytics
