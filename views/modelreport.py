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
        st.text("Current")
        st.info("$70/MG")
        st.text("Otpimized")
        st.info("$58/MG")
        st.text("Savings/month")
        st.info("$3600")

    with c2:
        # create random data
        no_of_balls = 25
        x = [random.triangular() for i in range(no_of_balls)]
        y = [random.gauss(0.5, 0.25) for i in range(no_of_balls)]
        colors = [random.randint(1, 4) for i in range(no_of_balls)]
        areas = [math.pi * random.randint(5, 15)**2 for i in range(no_of_balls)]
        # draw the plot
        plt.figure()
        plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
        plt.axis([0.0, 1.0, 0.0, 1.0])
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
        st.pyplot()


    st.subheader('Model Parameters')
    #st.write(rf.get_params())