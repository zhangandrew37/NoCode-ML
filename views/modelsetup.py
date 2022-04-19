import streamlit as st
import pandas as pd
import seaborn as sb
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

def load_view():
    st.title('Model Setup')
    example_data = open("Data-AI-1.csv")
    df = pd.read_csv(example_data)

    with st.sidebar.header('Set Parameters'):
        st.sidebar.write("Model Input")

    with st.sidebar.subheader('Learning Parameters'):
        parameter_n_estimators = st.sidebar.slider('Number of estimators (n_estimators)', 0, 1000, 100, 100)
        parameter_max_features = st.sidebar.select_slider('Max features (max_features)', options=['auto', 'sqrt', 'log2'])
        parameter_min_samples_split = st.sidebar.slider('Minimum number of samples required to split an internal node (min_samples_split)', 1, 10, 2, 1)
        parameter_min_samples_leaf = st.sidebar.slider('Minimum number of samples required to be at a leaf node (min_samples_leaf)', 1, 10, 2, 1)

    with st.sidebar.subheader('General Parameters'):
        parameter_random_state = st.sidebar.slider('Seed number (random_state)', 0, 1000, 42, 1)
        parameter_criterion = st.sidebar.select_slider('Performance measure (criterion)', options=['mse', 'mae'])
        parameter_bootstrap = st.sidebar.select_slider('Bootstrap samples when building trees (bootstrap)', options=[True, False])
        parameter_oob_score = st.sidebar.select_slider('Whether to use out-of-bag samples to estimate the R^2 on unseen data (oob_score)', options=[False, True])
        parameter_n_jobs = st.sidebar.select_slider('Number of jobs to run in parallel (n_jobs)', options=[1, -1])

    choice = st.selectbox("Select setup option", ["Split Data", "Data Scaling", "ML Algorithms", "ML Accuracy Metrics"])

    if choice == "Split Data":
        size_split = st.slider('Data Split Ratio (% for Training Set)', 10, 90, 80, 5)
        st.markdown('**Data splits**')
        st.write('Training set')
        # st.info(X_train.shape) 
        st.write('Test set')
        #st.info(X_test.shape)

        st.markdown('**Variable details**:')
        st.write('X variable')
        #st.info(list(X.columns))
        st.write('Y variable')
        #st.info(Y.name)
    elif choice == "Data Scaling":
        st.write("Coming Soon")
    elif choice == "ML Algorithms":
        algorithm = st.radio("Choose an algorithm for the model:", ('Random Forest', 'Linear Regression', 'Logistic Regression', 'Decision Tree', 'SVM', 'Native Bayes', 'KNN', 'K-means'))
        st.write("You chose: " + algorithm)
    elif choice == "ML Accuracy Metrics":
        st.write("h")

    