import streamlit as st
import pickle as pkle
import os.path
import pandas as pd
import seaborn as sb
from dataprep.eda import create_report

example_data = open("Data-AI-1.csv")
df = pd.read_csv(example_data)

def generate_report():
        left, right = st.columns(2)
        with left:
            if st.button('View detailed report in new tab'):
                report = create_report(df)
                report.show_browser()
        with right:
            if st.button('Download detailed report'):
                    report = create_report(df)
                    report.save('Report')
                    report.show_browser()

def generate_plot():
    numeric_columns = df.select_dtypes(['float', 'int']).columns
    st.sidebar.subheader("Scatter Plot Setup")
    select_box1 = st.sidebar.selectbox(label='X axis', options=numeric_columns)
    select_box2 = st.sidebar.selectbox(label='Y axis', options=numeric_columns)
    g = sb.relplot(x=select_box1, y=select_box2, data=df, height=6, aspect=11.7/8.27)
    st.pyplot()

def load_view():
    st.title('Data Pre-processing')

    # create a button in the side bar that will move to the next page/radio button choice
    next = st.sidebar.button('Next on list')

    # will use this list and next button to increment page, MUST BE in the SAME order
    # as the list passed to the radio button
    new_choice = ['Customize Input Fields','Quality Check','Data Manipulation','Data Visualization']

    # This is what makes this work, check directory for a pickled file that contains
    # the index of the page you want displayed, if it exists, then you pick up where the
    #previous run through of your Streamlit Script left off,
    # if it's the first go it's just set to 0
    if os.path.isfile('next.p'):
        next_clicked = pkle.load(open('next.p', 'rb'))
        # check if you are at the end of the list of pages
        if next_clicked == len(new_choice):
            next_clicked = 0 # go back to the beginning i.e. homepage
    else:
        next_clicked = 0 #the start

    # this is the second tricky bit, check to see if the person has clicked the
    # next button and increment our index tracker (next_clicked)
    if next:
        #increment value to get to the next page
        next_clicked = next_clicked +1

        # check if you are at the end of the list of pages again
        if next_clicked == len(new_choice):
            next_clicked = 0 # go back to the beginning i.e. homepage

    choice = st.sidebar.radio("go to",('Customize Input Fields','Quality Check', 'Data Manipulation', 'Data Visualization'), index=next_clicked)

    # pickle the index associated with the value, to keep track if the radio button has been used
    pkle.dump(new_choice.index(choice), open('next.p', 'wb'))

    if choice == 'Customize Input Fields':
        with st.form(key = "create", clear_on_submit=False):
            st.subheader("Customize Input Fields")
            choices = st.multiselect("Options", ["1", "2"])
            save = st.form_submit_button("Save Changes")
        
    elif choice == 'Quality Check':
       data_choice = st.selectbox("Data Quality Check", ["Data Preview", "Check Null Data", "Statistical Analysis"])
       if data_choice == 'Data Preview':
           generate_report()
           generate_plot()
           st.write(df)

    elif choice == 'Data Manipulation':
        st.subheader('Data Manipulation')
    elif choice == 'Data Visualization':
        st.subheader('Data Visualization')
        
def load_view_external():
    st.title('Data Pre-processing')
    
    # create a button in the side bar that will move to the next page/radio button choice
    next = st.sidebar.button('Next on list')

    # will use this list and next button to increment page, MUST BE in the SAME order
    # as the list passed to the radio button
    new_choice = ['Customize Input Fields','Quality Check','Data Manipulation','Data Visualization']

    # This is what makes this work, check directory for a pickled file that contains
    # the index of the page you want displayed, if it exists, then you pick up where the
    #previous run through of your Streamlit Script left off,
    # if it's the first go it's just set to 0
    if os.path.isfile('next.p'):
        next_clicked = pkle.load(open('next.p', 'rb'))
        # check if you are at the end of the list of pages
        if next_clicked == len(new_choice):
            next_clicked = 0 # go back to the beginning i.e. homepage
    else:
        next_clicked = 0 #the start

    # this is the second tricky bit, check to see if the person has clicked the
    # next button and increment our index tracker (next_clicked)
    if next:
        #increment value to get to the next page
        next_clicked = next_clicked +1

        # check if you are at the end of the list of pages again
        if next_clicked == len(new_choice):
            next_clicked = 0 # go back to the beginning i.e. homepage

    choice = st.sidebar.radio("go to",('Customize Input Fields','Quality Check', 'Data Manipulation', 'Data Visualization'), index=next_clicked)

    # pickle the index associated with the value, to keep track if the radio button has been used
    pkle.dump(new_choice.index(choice), open('next.p', 'wb'))
    if choice == 'Customize Input Fields':
        st.subheader("Customize Input Fields")
        choices = st.multiselect("Options", ["1", "2"])
        
    elif choice == 'Quality Check':
        st.write('Quality Check')
    elif choice == 'Data Manipulation':
        st.write('Data Manipulation')
    elif choice == 'Data Visualization':
        st.write('Data Visualization')