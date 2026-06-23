import streamlit as st

st.set_page_config(page_title="Bank Customer Churn Dashboard")

st.title("🏦 Bank Customer Churn Prediction")

st.subheader("Project Summary")

st.write("Total Customers: 10000")
st.write("High Risk Customers: 1422")
st.write("Average Age: 38.92")
st.write("Average Balance: 76485.89")
st.write("Churn Rate: 20.37%")

st.subheader("Top Important Features")

st.write("""
1. Age
2. NumOfProducts
3. CreditScore
4. EstimatedSalary
5. AgeTenure
""")

st.image("feature_importance.png")

st.success("Random Forest Accuracy: 86.5%")