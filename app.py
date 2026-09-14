import streamlit as st
import pandas as pd
import joblib

# Load model
model_bundle = joblib.load("churn_model.pkl")

model = model_bundle["model"]
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

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

h1 {
    font-size: 2.5rem;
}

.stButton > button {
    width: 100%;
    height: 3rem;
    font-size: 1.1rem;
    font-weight: bold;
}

.result-box {
    padding: 1.5rem;
    border-radius: 10px;
    margin-top: 1rem;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

st.title("Customer Churn Prediction")

st.write("Enter the customer's information below to predict"
         "whether they are likely to churn."
        )

# ------------------------------
# Customer inputs
# ------------------------------

st.subheader("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col2:
    country = st.selectbox(
        "Country",
        ["France", "Germany", "Spain"]
    )

    active_member = st.selectbox(
        "Active Member",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

st.subheader("💳 Account Information")

col1, col2 = st.columns(2)

with col1:
    products_number = st.number_input(
        "Number of Products",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )

with col2:
    balance = st.number_input(
        "Balance",
        min_value=0.0,
        value=50000.0,
        step=1000.0
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
            # Convert active member to binary
    active_member_value = (1 if active_member == "Yes" else 0)

      # Encode gender using the encoder used during training
    gender_value = le.transform([gender])[0]
  
      # -----------------------------
      # Create input dataframe
      # -----------------------------
    input_data = pd.DataFrame({
        "products_number": [products_number],
        "balance_per_age_group": [balance_per_age_group],
        "country": [country],
        "age_group": [age_group],
        "active_member": [active_member_value],
        "is_balance_zero": [is_balance_zero],
        "high_balance": [high_balance],
        "moderate_balance": [moderate_balance],
        "gender": [gender_value]
    })


      # -----------------------------
      # Apply preprocessing
      # -----------------------------

    input_processed = preprocessor.transform(input_data)

      # -----------------------------
      # Prediction
      # -----------------------------
    prediction = model.predict(input_processed)[0]

    probability = model.predict_proba(input_processed)[0][1]
  
    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ **Customer is likely to churn**")
    else:
        st.success("✅ **Customer is unlikely to churn**")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Churn Probability",
            f"{probability:.1%}"
        )

    with col2:
        st.metric(
            "Prediction",
            "Churn" if prediction == 1 else "No Churn"
        )

    st.progress(float(probability))

    st.caption(
        "The probability represents the model's estimated likelihood "
        "that the customer will churn."
    )


st.divider()

st.subheader("ℹ️ About This Model")

st.write(
    """
    This application uses a machine learning classification model
    to predict customer churn based on customer demographics,
    account characteristics and engagement indicators.

    The model uses engineered features including age groups,
    balance categories and balance statistics to identify
    patterns associated with customer churn.
    """
)

st.markdown(
    """
    **Model inputs include:**

    - Country
    - Gender
    - Age group
    - Number of products
    - Account balance characteristics
    - Active membership
    - Balance-related features
    """
)
