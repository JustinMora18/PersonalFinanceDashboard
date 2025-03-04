import streamlit as st
from Modules.rightSideInfo import allAccounts
from Modules.dataFuntions import saveIncomeData

def incCategories():
    st.header('💸 Income Categories')
    col1, col2 = st.columns (2)
    
    with col1:
        if st.button('💸 Salary', key='salary_btn'):
            st.session_state.selected_inc_category = 'Salary'
        if st.button('🧑🏾‍🏫 Teaching', key='teaching_btn'):
            st.session_state.selected_inc_category = ' Teaching'
        if st.button('🧑🏾‍💻 Project', key='project_btn'):
            st.session_state.selected_inc_category = 'Project'
        if st.button('💰 Financial Aid', key='financial_aid_btn'):
            st.session_state.selected_inc_category = 'Financial Aid'

    with col2:
        if st.button('🎁 Gift', key='gift_btn'):
            st.session_state.selected_inc_category = 'Gift'
        if st.button('🧑‍🧑‍🧒 Parents', key='parents_btn'):
            st.session_state.selected_inc_category = 'Parents'
        if st.button('🧑🏾‍💻 Online Sales', key='online_sales_btn'):
            st.session_state.selected_inc_category = 'Online Sales'
        if st.button('🤑 Others', key='others_btn'):
            st.session_state.selected_inc_category = 'Others'

def incAccounts():
    allAccounts(account_type='incomes')

def form():
    st.subheader('Add Incomes 💵')
    selected_inc_category = st.session_state.selected_inc_category or 'Select a category 👉'
    selected_inc_account = st.session_state.selected_inc_account or 'Select an Account  👉'

    incName = st.text_input('Enter Income Name:')
    incAmount = st.number_input('Enter the income amount ($)', min_value=0.0, format='%.2f')
    incAccount = st.selectbox('Account', [selected_inc_account])
    incCategory = st.selectbox('Category', [selected_inc_category])
    incDate = st.date_input('Date:')
    incNote  = st.text_area('Notes (Optional)', height=70)

#----Button------------------------
    if st.button('Add Income'):
        st.balloons()
        #Income Dictionary
        incomeData = {
            'Name': incName,
            'Amount': incAmount,
            'Account': incAccount,
            'Category': incCategory,
            'Date': incDate,
            'Note': incNote
        }
        saveIncomeData (incomeData)

        st.session_state.success_message_income = (
            f'🎈 Your Income has been added successfully!\n\n'
            f'**➔ Income Name:** {incName}\n\n'
            f'**➔ Amount:** ${incAmount}\n\n'
            f'**➔ Payment Method:** {incAccount}\n\n'
            f'**➔ Category:** {incCategory}\n\n'
            f'**➔ Date:** {incDate}'
        )
        st.rerun()
    #Save the message in session_state only if the user add a income
    if st.session_state.success_message_income:
        st.success(st.session_state.success_message_income)
        #clear the message at the end
        st.session_state.success_message_income = ''