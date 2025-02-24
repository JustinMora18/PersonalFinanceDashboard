import streamlit as st
import pandas as pd
import incomes, expenses, investments
from PIL import Image
from streamlit_option_menu import option_menu
from rightSideInfo import allAccounts,show_date 
from dataFuntions import create_inc_dataFrame, create_exp_dataFrame, create_invstmt_dataFrame

st.set_page_config(
    page_title='Personal Finance Dashboard', page_icon='💰', 
    layout='wide',
    initial_sidebar_state='expanded')

#initialize the session state variable in case they dont exist
if 'selected_inc_category' not in st.session_state:
    st.session_state.selected_inc_category = None
if 'selected_inc_account' not in st.session_state:
    st.session_state.selected_inc_account = None
if 'selected_exp_category' not in st.session_state:
    st.session_state.selected_exp_category = None
if 'selected_exp_account' not in st.session_state:
    st.session_state.selected_exp_account = None
if 'selected_invstmt_type' not in st.session_state:
        st.session_state.selected_invstmt_type = None
if 'selected_invstmt_account' not in st.session_state:
        st.session_state.selected_invstmt_account = None

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

    colm1, colm2 = st.columns((2, .9), gap='medium')
    with colm1:
        st.info('- Fill out the form below and select a category on the right to add a new income transaction.')
    with colm2:
        show_date()

    st.divider()

    col1, col2 = st.columns((4.5, 2), gap='medium')
    with col2:
        incomes.incAccounts()
        incomes.incCategories()
    with col1:
        incomes.form()

    st.divider()
#----------------------------
elif selected == 'Expenses':
    st.title('💸 Manage Your Expenses')

    colm1, colm2 = st.columns((2, .9), gap='medium')
    with colm1:
        st.info('- Fill out the form below and select a category on the right to add a new expense transaction.')
    with colm2:
        show_date()

    st.divider()

    col1, col2 = st.columns((4.5, 2), gap='medium')
    with col2:
        expenses.expAccounts()
        expenses.categories()
    with col1:
        expenses.form()
    st.divider()
#----------------------------
elif selected == 'Investments':
    st.title('📉 Manage Your Investment')

    colmn1, colmm2 = st.columns((2, .9), gap='medium')
    with colmn1:
        st.info('- Fill out the form below and select a category on the right to add a new investment.')
    with colmm2:
        show_date()

    st.divider()

    col1, col2 = st.columns((4.5, 2), gap='medium')
    with col2:
        investments.invstmtAccounts()
        investments.invstmtType()
    with col1:
        investments.form()
    st.divider()
#----------------------------
elif selected == 'Financial Report':
    st.subheader('Generate Report')
    #add funtion to get the Financial Repoort...

