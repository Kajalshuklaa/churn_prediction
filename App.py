import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\models\model')

st.header('Churn Prediction App')

# Customer Details Input
customer_ID = st.number_input('Enter Customer ID', min_value=1, step=1)  # Will be dropped before prediction
gender = st.selectbox('Gender', ['Male', 'Female'])
senior_citizen = st.selectbox('Senior Citizen', [0, 1])  # 0 for No, 1 for Yes
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.number_input('Enter Tenure (Months)', min_value=0, step=1)

# Service Details Input
phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
multiple_lines = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
online_backup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])

# Contract & Billing Details Input
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
payment_method = st.selectbox('Payment Method', 
    ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charges = st.number_input('Enter Monthly Charges', min_value=0.0, step=0.1)
total_charges = st.number_input('Enter Total Charges', min_value=0.0, step=0.1)

# Encoding categorical variables
data = {
    "gender": [1 if gender == "Male" else 0],  # Convert to numeric
    "SeniorCitizen": [senior_citizen],
    "Partner": [1 if partner == "Yes" else 0],
    "Dependents": [1 if dependents == "Yes" else 0],
    "tenure": [tenure],
    "PhoneService": [1 if phone_service == "Yes" else 0],
    "MultipleLines": [1 if multiple_lines == "Yes" else 0 if multiple_lines == "No" else 2],
    "InternetService": [0 if internet_service == "DSL" else 1 if internet_service == "Fiber optic" else 2],
    "OnlineSecurity": [1 if online_security == "Yes" else 0 if online_security == "No" else 2],
    "OnlineBackup": [1 if online_backup == "Yes" else 0 if online_backup == "No" else 2],
    "DeviceProtection": [1 if device_protection == "Yes" else 0 if device_protection == "No" else 2],
    "TechSupport": [1 if tech_support == "Yes" else 0 if tech_support == "No" else 2],
    "StreamingTV": [1 if streaming_tv == "Yes" else 0 if streaming_tv == "No" else 2],
    "StreamingMovies": [1 if streaming_movies == "Yes" else 0 if streaming_movies == "No" else 2],
    "Contract": [0 if contract == "Month-to-month" else 1 if contract == "One year" else 2],
    "PaperlessBilling": [1 if paperless_billing == "Yes" else 0],
    "PaymentMethod": [0 if payment_method == "Electronic check" else 1 if payment_method == "Mailed check" 
                      else 2 if payment_method == "Bank transfer (automatic)" else 3],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
}

df = pd.DataFrame(data)

st.write("Processed Data for Prediction:")
st.write(df)

# Submit Button
if st.button('Predict Churn'):
    try:
        pred = model.predict(df)
        st.subheader('Churn Prediction Result:')
        st.write("Churn" if pred[0] == 1 else "No Churn")
    except Exception as e:
        st.error(f"Error in prediction: {e}")


