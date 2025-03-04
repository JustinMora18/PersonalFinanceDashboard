import streamlit as st
from Modules.rightSideInfo import allAccounts
from Modules.dataFuntions import saveExpensesData
# Si la clave 'data_updated' no existe en session_state, la inicializamos
if 'data_updated' not in st.session_state:
    st.session_state.data_updated = False

def categories():
    st.header('💸 Expenses Categories')
    col1, col2 = st.columns (2)

    with col1:
        if st.button('🏠 Rent', key='rent_btn'):
            st.session_state.selected_exp_category = 'Rent'
        if st.button('🍱 Food', key='food_btn'):
            st.session_state.selected_exp_category = 'Food'
        if st.button('⛽️ Gas', key='gas_btn'):
            st.session_state.selected_exp_category = 'Gas'
        if st.button('📚 Education', key='education_btn'):
            st.session_state.selected_exp_category = 'Education'
            
    with col2:
        if st.button('😷 Health', key='health_btn'): 
            st.session_state.selected_exp_category = 'Health'
        if st.button('🎁 Gifts', key='gifts_btn'):
            st.session_state.selected_exp_category = 'Gifts'
        if st.button('💪🏽 Gym', key='gym'):
            st.session_state.selected_exp_category = 'Gym'
        if st.button('🍾 Free Time', key='free_time_btn'):
            st.session_state.selected_exp_category = 'Free Time'

def expAccounts():
    allAccounts('expenses')
    
def form():
    st.subheader('Add Expense 💵')
    selected_exp_category = st.session_state.selected_exp_category or 'Select a Category 👉'
    selected_exp_account = st.session_state.selected_exp_account or 'Select a Account 👉'
    
    expName = st.text_input('Enter Expense Name:')
    expAmount = st.number_input('Enter the expense amount ($)', min_value=0.0, format='%.2f')
    expLocation = st.text_input('Enter Location:')
    expPymntMth = st.selectbox('Payment Method', [selected_exp_account])
    expCategory = st.selectbox('Category', [selected_exp_category])
    expDate = st.date_input('Date')
    expNote = st.text_area('Notes (Optional)', height=70)

#----Button------------------------
    if st.button('Add Expense'):
        st.balloons()
        #Expenses dictionary 
        expensesData = {
            'Name': expName,
            'Amount': expAmount,
            'Location': expLocation,
            'ExpPaymentMthd': expPymntMth,
            'Category': expCategory,
            'Date': expDate,
            'Note': expNote
        }
        saveExpensesData (expensesData)

        #Save the message in a session state
        st.session_state.success_message_expenses = (
            f'🎈 Your Expense has been added successfully!\n\n'
            f'**➔ Expense Name:** {expName}\n\n'
            f'**➔ Amount:** ${expAmount}\n\n'
            f'**➔ Payment Method:** {expPymntMth}\n\n'
            f'**➔ Category:** {expCategory}\n\n'
            f'**➔ Date:** {expDate}'
        )
        st.session_state.data_updated = True
        
    #Save the message in session_state only if the user add a income
    if st.session_state.success_message_expenses:
        st.success(st.session_state.success_message_expenses)
        #clear the message at the end
        st.session_state.success_message_expenses = None
