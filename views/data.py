import streamlit as st
import pickle as pkle
import os.path
    
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

    # create your radio button with the index that we loaded
    choice = st.sidebar.radio("go to",('Customize Input Fields','Quality Check', 'Data Manipulation', 'Data Visualization'), index=next_clicked)

    # pickle the index associated with the value, to keep track if the radio button has been used
    pkle.dump(new_choice.index(choice), open('next.p', 'wb'))

    # finally get to whats on each page
    if choice == 'Customize Input Fields':
        st.write('this is home')
    elif choice == 'Quality Check':
        st.write('Quality Check')
    elif choice == 'Data Manipulation':
        st.write('Data Manipulation')
    elif choice == 'Data Visualization':
        st.write('Data Visualization')
        