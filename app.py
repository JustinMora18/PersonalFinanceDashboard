import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
import incomes, expenses

st.set_page_config(
    page_title="Personal Finance Dashboard", page_icon="💰", 
    layout="wide",
    initial_sidebar_state="expanded")

#initialice session_state
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

if "selected_account" not in st.session_state:
    st.session_state.selected_account = None

if "selected_exp_category" not in st.session_state:
    st.session_state.selected_exp_category = None

if "selected_exp_account" not in st.session_state:
    st.session_state.selected_exp_account = None



#----Sidebar------------------------
with st.sidebar:
    selected = option_menu('Manage Your Money!', ['Home', 'Incomes', 'Expenses', 'Investments', 'Financial Report'], menu_icon= 'bi bi-wallet-fill', default_index=0)
#----------------------------
if selected == 'Home':
    st.title (' 💰 Personal Fincance Dashboard 💰 ') 
    #add features here 
#----------------------------
elif selected == 'Incomes':
    st.title('💸 Manage Your Incomes')
    st.info("- Fill out the form below and select a category on the right to add a new income transaction.")
    col1, col2 = st.columns((4.5, 2), gap='medium')
    with col2:
        incomes.accounts()
        incomes.categories()

    with col1:
        incomes.form()
    st.divider()
#----------------------------
elif selected == 'Expenses':
    st.title('💸 Manage Your Expenses')
    st.info("- Fill out the form below and select a category on the right to add a new expense transaction.")
    col1, col2 = st.columns((4.5, 2), gap='medium')
    with col2:
        incomes.accounts()
        expenses.categories()
    with col1:
        expenses.form()
    st.divider()

#----------------------------
elif selected == 'Financial Report':
    st.subheader('Generate Report')
    #add funtion to get the Financial Repoort...

