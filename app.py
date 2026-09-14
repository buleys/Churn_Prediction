import streamlit as st
import pandas as pd
import joblib

# Load model
model_bundle = joblib.load("churn_model_pkl")

model = nodel_bundle["model"]
preprocessor = model_bundle["preprocessor"]
le = model_bundle["label_encoder"]

# -----------------------------------
# Training-derived values
# -----------------------------------


# Mean balance for each age group
age_group_balance = {
  "less_than_25": 75095.804288,
    "25-34": 74127.809091,
    "35-44": 76830.514649,
    "45-54": 81583.227071,
    "55-64": 81327.002481,
    "65+": 71321.855720}

# 75th percentile of balance from training data
balance_q75 = 127644.24

st.set_page_config(
  page_title = "Customer Churn Prediction",
  page_icon = "📊",
  layout = "centered"
)

st.title("Customer Churn Prediction")

st.write("Enter the customer's information below to predict"
         "whether they are likely to churn."
        )

# ------------------------------
# Customer inputs
# ------------------------------

gender = st.selectbox(
  "Gender",
  ["Male","Female"]
  )

age = st.selectbox(
  "Age",
  min_value = 18,
  max_value = 100,
  value = 30,
  step = 1
  )

country = st.selectbox(
  "Country",
  ["France", "Germany", "Spain"]
  )

products_number = st.number_input(
  "Number of Products",
  min_value = 1,
  max_value = 10,
  value = 1,
  step = 1
  )

active_member = st.selectbox(
    "Active Member",
  ["Yes","No"]
  )

balance = st.nimber_input(
    "Balance",
  min_value = 0.0,
  value = 50000.0,
  step = 1000.0
  )

# ------------------------------
# Prediction
# ------------------------------


if st.button("Predict Churn"):
       
      # -------------------------
      # Create age_group
      # -------------------------

    if age <= 25:
        age_group = "less_than_25"
    elif age <= 35:
        age_group = "25-34"
    elif age <= 45:
        age_group = "35-44"
    elif age <= 55:
        age_group = "45-54"
    elif age <= 65:
        age_group = "55-64"
    else:
        age_group = "65+"
      
      # -----------------------------
      # Engineer balance features
      # -----------------------------
    # Flag zero balance
    is_balance_zero = 1 if balance == 0 else 0

    # Flag moderate and high balances
    high_balance = int(
      balance > balance_q75
    )
    moderate_balance = int(
      (balance > 0) and (balance < balance_q75)
    )

    balance_per_age_group = age_group_balance[age_group]

      # -----------------------------
      # Create input dataframe
      # -----------------------------
    input_data = pd.DataFrame({
        "products_number": [products_number],
        "balance_per_age_group": [balance_per_age_group],
        "country": [country],
        "age_group": [age_group],
        "active_member": [active_member],
        "is_balance_zero": [is_balance_zero],
        "high_balance": [high_balance],
        "moderate_balance": [moderate_balance],
        "gender": [gender]
    })

        # Convert active member to binary
    active_member_value = (1 if active_member == "Yes" else 0)

      # Encode gender using the encoder used during training
    gender_value = le.transform([gender])[0]

      # -----------------------------
      # Apply preprocessing
      # -----------------------------

    input_processed = preprocessor.transform(input_data)

      # -----------------------------
      # Prediction
      # -----------------------------

    prediction = model.predict(input_processed)[0]
    probability = model.predict_proba(input_processed)[0][1]

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn")
    else: 
        st.success("✅ Customer is unlikely to churn")

    st.metric(
        "Churn Probability",
        f"{probability:.1%}"
)
