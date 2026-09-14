import streamlit as st
import pandas as pd
import joblib

# Load model
model_bundle = joblib.load("churn_model_plk")

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
    "65+": 71321.855720
}

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
  value = 30
  )

country = st.selectbox(
  "Country",
  ["France", "Germany", "Spain"]
  )

products_number = st.number_input(
  "Number of Products",
  min_value = 1,
  max_value = 10,
  value = 2, 
  )

active_member = st.selectbox(
    "Active Member",
  ["Yes","No"]
  )

balance = st.nimber_input(
    "Balance",
  min_value = 0.0,
  value = 1000.0
  )

# ------------------------------
# Prediction
# ------------------------------
[0,25,35,45,55,65,100], 
labels=['less_than_25', '25-34', '35-44', '45-54', '55-64', '65+'])
if st.button("Predict Churn:):
       # Convert active member to binary
             active_member_value = (
                  1 if active_member == "Yes" else 0
)
      # Encode gender using the encoder used during training
            gender_value = le.transform([gender])[0]

      # -------------------------
      # Create age_group
      # -------------------------

            if age < 25:
                age_group = "less_than_25"
            elif 25 <= age < 35:
                age_group = "25-34"
            elif 35 <= age < 45:
                age_group = "35-44"
            elif 45 <= age < 55:
                age_group = "45-54"
            elif 55 <= age < 65:
                age_group = "55-64"
            else:
              age_group = "65+"
        
      # -----------------------------
      # Engineer balance features
      # -----------------------------
            # Flag zero balance
            is_balance_zero = 1 if balance == 0 else 0

            # Flag moderate and high balances
            high_balance = 1 if balance
