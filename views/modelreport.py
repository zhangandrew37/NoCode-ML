import streamlit as st
from datetime import date
import math
import random
import matplotlib.pyplot as plt
import pandas as pd

example_data = open("Data-AI-1.csv")
df = pd.read_csv(example_data)
params = df.select_dtypes(['float', 'int']).columns

def load_view():
    st.title('Dashboard')
    algorithm = st.sidebar.selectbox('Select an Algorithm', ['Random Forest', 'Linear Regression', 'Logistic Regression', 'Decision Tree', 'SVM', 'Native Bayes', 'KNN', 'K-means'])

    col1, col2, col3 = st.columns(3)
    col1.text("Model Score")
    col1.info("89%")
    col2.text("Algorithm Selected")
    col2.info(algorithm)
    today = date.today()
    col3.text("Last Updated")
    col3.info(today)

    parameter = st.sidebar.selectbox('Select an Input Parameter', params)

    c1, c2 = st.columns(2)

    with c1:
        st.subheader(parameter)
        st.text("Maximum")
        st.info("$70/MG")
        st.text("Minimum")
        st.info("$58/MG")
        st.text("Mean")
        st.info("$3600")
        st.text("Count")
        st.info("1")

    with c2:
        st.bar_chart(df[parameter])
        st.line_chart(df[parameter])
        st.plotly_chart(df[parameter])
    #frequency


    ##st.subheader('Model Parameters')
    #st.write(rf.get_params())