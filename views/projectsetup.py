import streamlit as st
from views import data
from streamlit_multipage import MultiPage
import global_
import utils as utl

def load_view(**state):
    st.title('Create an ML project')
    with st.form(key = "create", clear_on_submit=False):
        # name_ = state["name"] if "name" in state else ""
        # possibly implement state later
        name = st.text_input(label = "Enter the model name")
        # set value = name_ if using state
        
        type = st.selectbox("Type of ML modeling", ('Regression', 'Classification'))
        global_.type = type

        df = st.file_uploader("Upload your data (CSV)")
        submit = st.form_submit_button(label= "Create Project")
        if (submit):
            st.write("If you are not being redirected or if you encounter other issues, please use the navbar at the top to navigate through the app.")

