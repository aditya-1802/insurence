
import streamlit as st
import pickle
import sklearn

# Load the trained model
with open('health_insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the user input form
st.write("# Health Insurance Cost Prediction")
age = st.slider("Age", 18, 100, step=1)
# sex = st.radio("Sex", ["Male", "Female"])
bmi = st.slider("BMI", 15.0, 50.0, step=0.1)
children = st.slider("Number of Children", 0, 10, step=1)
smoker = st.radio("Smoker", ["Yes", "No"])
region = st.selectbox(
    "Region", ["North", "South", "West", "East"])

# Convert categorical inputs to numerical values
# sex = 0 if sex == "Male" else 1
smoker = 1 if smoker == "Yes" else 0

if region == "North":
    region_code = 0
elif region == "South":
    region_code = 1
elif region == "West":
    region_code = 2
else:
    region_code = 3

# Make a prediction using the model
inputs = [[age, bmi, children, smoker, region_code]]
predicted_cost = model.predict(inputs)[0]

# Display the predicted cost to the user
submit_button = st.button("Submit")

if submit_button:
    st.write("## Predicted Cost of Health Insurance:")
    st.write(f"Predicted cost: ₹{round(predicted_cost, 2)}")
