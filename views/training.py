import streamlit as st
import pandas as pd
from PIL import Image

def load_view():    
    st.title('Training')
    algo_choice = st.selectbox("Algorithm", ['Random Forest', 'Linear Regression', 'Logistic Regression', 'Decision Tree', 'SVM', 'Native Bayes', 'KNN', 'K-means'])
    col1, col2 = st.columns(2)
    col1.metric("Coefficient of determination ($R^2$)", "70 °F", "1.2 °F")
    col2.metric("Error (MSE or MAE)", "9 mph", "-8%")

    #Y_pred_train = rf.predict(X_train)
    #st.info( r2_score(Y_train, Y_pred_train) )
    #st.info( mean_squared_error(Y_train, Y_pred_train) )

    st.write("Compare with other algorithms: ")

    example_data = open("Data-AI-1.csv")
    df = pd.read_csv(example_data)
    st.dataframe(df.style.highlight_max(axis=0))

# temporarily use image while finding fixes for XGBoost on M1 Mac

