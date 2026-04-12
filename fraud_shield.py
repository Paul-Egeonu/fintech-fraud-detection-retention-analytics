import streamlit as st
import pandas as pd
import joblib
import plotly.express as px


# ======================
# 🔐 SIMPLE LOGIN SYSTEM
# ======================
def login():
    st.sidebar.subheader("🔐 Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username == "admin" and password == "fraud123":
            st.session_state["logged_in"] = True
        else:
            st.sidebar.error("Invalid credentials")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

login()

if not st.session_state["logged_in"]:
    st.stop()


# ======================
# ⚙️ CONFIG
# ======================
st.set_page_config(layout="wide", page_title="FraudShield AI")

st.markdown("""
    <h1 style='text-align: center;'>🛡️ FraudShield AI</h1>
    <p style='text-align: center;'>Real-Time Transaction Risk Engine</p>
""", unsafe_allow_html=True)

# ======================
# 📦 LOAD MODEL BUNDLE
# ======================
bundle = joblib.load("best_model.pkl")

model = bundle["model"]
threshold = bundle["threshold"]
model_cols = bundle["columns"]

df = pd.read_csv("clean_fintech_dataset.csv")

# ======================
# 🎛 SIDEBAR INPUTS
# ======================
st.sidebar.header("🧾 Transaction Input")

amount = st.sidebar.number_input("💰 Transaction Amount ($)", 0.0)

status = st.sidebar.selectbox("Status", ["success", "failed"])

transaction_type = st.sidebar.selectbox(
    "Transaction Type", df['transaction_type'].unique()
)

country = st.sidebar.selectbox(
    "Country", df['country'].unique()
)

device_type = st.sidebar.selectbox(
    "Device Type", df['device_type'].unique()
)

acquisition_channel = st.sidebar.selectbox(
    "Acquisition Channel", df['acquisition_channel'].unique()
)

# ======================
# ⚙️ FEATURE ENGINEERING
# ======================
high_value = int(amount > 500)
failed_txn = int(status != "success")

# ======================
# 🧠 INPUT DATA
# ======================
input_df = pd.DataFrame([{
    'amount': amount,
    'high_value': high_value,
    'failed_txn': failed_txn,
    'transaction_type': transaction_type,
    'country': country,
    'device_type': device_type,
    'acquisition_channel': acquisition_channel
}])

input_encoded = pd.get_dummies(input_df)
input_encoded = input_encoded.reindex(columns=model_cols, fill_value=0)

# ======================
# 🔍 PREDICTION
# ======================
st.subheader("🧠 Fraud Risk Assessment")

if st.button("🔍 Analyze Transaction"):

    prob = model.predict_proba(input_encoded)[0][1]
    pred = int(prob >= threshold)

    col1, col2 = st.columns(2)

    # Risk levels
    if prob > 0.6:
        risk_label = "🔴 HIGH RISK"
    elif prob > 0.3:
        risk_label = "🟠 MEDIUM RISK"
    else:
        risk_label = "🟢 LOW RISK"

    if pred == 1:
        col1.error(f"⚠️ Fraudulent Transaction\n\n{risk_label}")
    else:
        col1.success(f"✅ Legitimate Transaction\n\n{risk_label}")

    col2.metric("Fraud Probability", f"{prob:.2%}")
    st.progress(int(prob * 100))


import numpy as np

# ======================
# 📊 RETENTION CALCULATION
# ======================
if 'cohort_month' in df.columns and 'cohort_index' in df.columns:

    cohort_table = df.pivot_table(
        index='cohort_month',
        columns='cohort_index',
        values='user_id',
        aggfunc='nunique'
    )

    cohort_size = cohort_table.iloc[:, 0]
    retention = cohort_table.divide(cohort_size, axis=0)

    # Exclude first column (100%)
    retention_no_initial = retention.iloc[:, 1:]

    retention_values = retention_no_initial.values.flatten()
    retention_values = retention_values[~np.isnan(retention_values)]

    overall_retention_rate = retention_values.mean()

else:
    overall_retention_rate = None


# ======================
# 📊 KPI SECTION
# ======================
st.subheader("📊 Business Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Transactions", f"{len(df):,}")
col2.metric("Fraud Rate", f"{df['is_fraud'].mean():.2%}")
col3.metric("Avg Transaction", f"${df['amount'].mean():.2f}")
col4.metric("Total Revenue", f"${df['fee_amount'].sum():,.0f}")

if overall_retention_rate is not None:
    col5.metric("Avg Cohort Retention", f"{overall_retention_rate:.2%}")
else:
    col5.metric("Avg Cohort Retention", "N/A")

# ======================
# 📈 VISUALS
# ======================
st.subheader("📈 Fraud Insights")

colA, colB = st.columns(2)

with colA:
    fig1 = px.bar(
        df['transaction_type'].value_counts().reset_index(name='count'),
        x='transaction_type',
        y='count',
        title="Transaction Distribution"
    )
    st.plotly_chart(fig1, use_container_width=True)

with colB:
    fraud_country = df.groupby('country')['is_fraud'].mean().reset_index()

    fig2 = px.bar(
        fraud_country,
        x='country', y='is_fraud',
        title="Fraud Rate by Country"
    )
    st.plotly_chart(fig2, use_container_width=True)