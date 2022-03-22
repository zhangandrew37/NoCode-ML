import streamlit as st
import utils as utl
from views import home,projectsetup,data,modelsetup,training,prediction,modelreport,options,configuration

st.set_page_config(layout="wide", page_title='W & WW Optimization ML Modeling')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "projectsetup":
        projectsetup.load_view()
    elif route == "data":
        data.load_view()
    elif route == "modelsetup":
        modelsetup.load_view()
    elif route == "training":
        training.load_view()
    elif route == "prediction":
        prediction.load_view()
    elif route == "modelreport":
        modelreport.load_view()
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()
        
navigation()