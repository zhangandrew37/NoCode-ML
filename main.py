import streamlit as st
import utils as utl
from views import home,projectsetup,data,modelsetup,training,prediction,modelreport,options,configuration

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import base64
import pickle as pkle
import os.path
import pandas as pd
from dataprep.eda import create_report
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, RandomForestRegressor
from sklearn.svm  import SVC, LinearSVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, KFold, GridSearchCV, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

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

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 