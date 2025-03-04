import streamlit as st
from datetime import datetime

#state variables
if 'selected_inc_account' not in st.session_state:
    st.session_state.selected_inc_account = None
if 'selected_exp_account' not in st.session_state:
    st.session_state.selected_exp_account = None

def allAccounts(account_type='income'):
    st.header('🏦 Accounts')
    col1, col2 = st.columns (2)
    
    session_key = ('selected_inc_account' 
                if account_type == 'incomes' 
                    else 'selected_invstmt_account' 
                if account_type == 'investments' 
                    else 'selected_exp_account')

    with col1:
        if st.button('💵 Cash', key=f'cash_btn_{account_type}'):
            st.session_state[session_key] = 'Cash'
        if st.button('💳 Card', key=f'card_btn_{account_type}'):
            st.session_state[session_key] = 'Card'

    with col2:
        if st.button('💸 Paypal', key=f'paypal_btn_{account_type}'):
            st.session_state[session_key] = 'Paypal'
        if st.button('🏦 Bank Account', key=f'bank_acc_btn_{account_type}'):
            st.session_state[session_key] = 'Bank Account'
    return st.session_state[session_key]

def show_date():
    today = datetime.now().strftime('%m-%d-%Y')
    st.markdown(f'##### 📅 Date: {today}')