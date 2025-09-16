import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load("model/loan_default_model.pkl")

st.title("🏦 Loan Default Prediction App")
st.write("Enter details below to check probability of default.")

# --- User Inputs ---
bank_balance = st.number_input("Bank Balance", min_value=0, value=20000, step=1000)
annual_salary = st.number_input("Annual Salary", min_value=0, value=500000, step=5000)
employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed"])

if st.button("Predict Default"):
    # ✅ Create dataframe with features
    df = pd.DataFrame([{
        "Employed": 1 if employment_status == "Employed" else 0,
        "Bank Balance": bank_balance,
        "Annual Salary": annual_salary
    }])

    # --- Feature Engineering (must match training) ---
    df["Balance_to_Salary"] = df["Bank Balance"] / (df["Annual Salary"] + 1)
    df["Log_Salary"] = np.log1p(df["Annual Salary"])
    df["Log_Balance"] = np.log1p(df["Bank Balance"])

    # ✅ Reorder columns exactly like training
    df = df[[
        "Employed",
        "Bank Balance",
        "Annual Salary",
        "Balance_to_Salary",
        "Log_Salary",
        "Log_Balance"
    ]]

    # --- Prediction ---
    proba = model.predict_proba(df)[:, 1][0]
    pred = int(proba > 0.5)

    st.subheader("📊 Prediction Result")
    if pred == 1:
        st.error(f"⚠️ High Risk of Default (Probability: {proba:.2f})")
    else:
        st.success(f"✅ Low Risk of Default (Probability: {proba:.2f})")
