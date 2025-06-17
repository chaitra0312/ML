import streamlit as st
import joblib
model = joblib.load('model.pkl')
st.title('House Price Estimator')
size = st.number_input("Enter House Size(in sq ft):",min_value = 100 ,max_value = 10000 ,step = 100)
if st.button("Predict price"):
    prediction = model.predict([[size]])[0]
    st.success(f"EStimated Price : ${prediction:.2f}lakhs")
