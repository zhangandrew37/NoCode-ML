import streamlit as st
import main
import utils as utl

def load_view():   
    empty0 = st.empty() 
    empty0.title('Create an ML project')
    with st.form(key = "create", clear_on_submit=False):
        empty1 = st.empty()
        empty2 = st.empty()
        empty4 = st.empty()
        name = empty1.text_input(label = "Enter the model name")
        type = empty2.selectbox("Type of ML modeling (Algorithm)", ["Random Forest Regressor"])
        datafile = load_df()
        submit = empty4.form_submit_button(label= "Create Project")
        if (submit):
            empty0.empty()
            empty1.empty()
            empty2.empty()
            empty3.empty()
            empty4.empty()
            submit = st.form_submit_button(label= "Cancel")
    return df

def load_df():
    empty3 = st.empty()
    df = empty3.file_uploader("Upload your data (CSV)")
    return df

df = load_df()
        