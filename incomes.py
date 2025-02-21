import streamlit as st
from rightSideInfo import allAccounts

#initialize the session state variable in case they dont exist
if 'selected_inc_category' not in st.session_state:
        st.session_state.selected_inc_category = None
if 'selected_inc_account' not in st.session_state:
        st.session_state.selected_account = None

def incCategories():
    st.header('💸 Income Categories')
    col1, col2 = st.columns (2)
    
    with col1:
        if st.button('💸 Salary', key='salary_btn'):
            st.session_state.selected_inc_category = '💸 Salary'
        if st.button('🧑🏾‍🏫 Teaching', key='teaching_btn'):
            st.session_state.selected_inc_category = '🧑🏾‍🏫 Teaching'
        if st.button('🧑🏾‍💻 Project', key='project_btn'):
            st.session_state.selected_inc_category = '🧑🏾‍💻 Project'
        if st.button('💰 Financial Aid', key='financial_aid_btn'):
            st.session_state.selected_inc_category = '💰 Financial Aid'

    with col2:
        if st.button('🎁 Gift', key='gift_btn'):
            st.session_state.selected_inc_category = '🎁 Gift'
        if st.button('🧑‍🧑‍🧒 Parents', key='parents_btn'):
            st.session_state.selected_inc_category = '🧑‍🧑‍🧒 Parents'
        if st.button('🧑🏾‍💻 Online Sales', key='online_sales_btn'):
            st.session_state.selected_inc_category = 'Online Sales'
        if st.button('🤑 Others', key='others_btn'):
            st.session_state.selected_inc_category = '🤑 Others'

def incAccounts():
    allAccounts(account_type='incomes')
    #here we pass 'incomes' form the condition in the rightSideInfo.py

def form():
    st.subheader('Add Incomes 💵')
    selected_inc_category = st.session_state.selected_inc_category or 'Select a category 👉'
    selected_inc_account = st.session_state.selected_inc_account or 'Select an Account  👉'

    incName = st.text_input('Enter Income Name:')
    incAmount = st.number_input('Enter the income amount ($)', min_value=0.0, format='%.2f')
    incAccount = st.selectbox('Accounts', [selected_inc_account])
    incCategory = st.selectbox('Category', [selected_inc_category])
    incDate = st.date_input('Date:')
    incNote  = st.text_area('Notes (Optional)', height=70)
    if st.button('Add Transaction'):
        st.success(f'Your Transaction has been added successfully with Category:       {incCategory},      Amount: ${incAmount}!')

def widgets():
    print('hello word') #test