import streamlit as st
import pandas as pd
import tempfile
from classify import classify_csv

st.title("Log Classification")

file = st.file_uploader("Upload a CSV file", type="csv")

if file is not None:
    classify_btn = st.button("Classify")

    if classify_btn:
        with st.spinner("Classifying..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
                temp_file.write(file.read())
                temp_path = temp_file.name

            classify_csv(temp_path)

            try:
                df = pd.read_csv('resources/output.csv')
                st.success("Classification completed!")
                st.dataframe(df)
            except Exception as e:
                st.error(f"Error reading output file: {e}")
