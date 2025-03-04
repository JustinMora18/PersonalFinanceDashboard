import streamlit as st
from Modules.rightSideInfo import allAccounts
from Modules.dataFuntions import saveInvestmtData

def invstmtType():
    st.header('💸 Investment Type')
    col1, col2 = st.columns (2)
    
    with col1:
        if st.button('📊 Stocks', key='stocks_btn'):
            st.session_state.selected_invstmt_type = 'Stocks'
        if st.button('📑 Mutual funds', key='mutual_funds_btn'):
            st.session_state.selected_invstmt_type = 'Mutual funds'
        if st.button('📉 ETFs', key='ETFs_btn'):
            st.session_state.selected_invstmt_type = 'ETFs'
        if st.button('🎨 Collectibles', key='collectible_btn'):
            st.session_state.selected_invstmt_type = 'Collectibles'

    with col2:
        if st.button('🚀 Startup', key='startup_btn'):
            st.session_state.selected_invstmt_type = 'Startup'
        if st.button('🪙 Cryptocurrency', key='cryptocurrency_btn'):
            st.session_state.selected_invstmt_type= 'Cryptocurrency'
        if st.button('⚱️ Gold', key='gold_btn'):
            st.session_state.selected_invstmt_type = 'Gold'
        if st.button('🤑 Other invts', key='other_invstmts-btn'):
            st.session_state.selected_invstmt_type = 'Other invts'

def invstmtAccounts():
    allAccounts(account_type='investments')

def form():
    st.subheader('Add Investment 💵')
    selected_invstmt_type = st.session_state.selected_invstmt_type or 'Select a category 👉'
    selected_invstmt_account = st.session_state.selected_invstmt_account or 'Enter the payment method you used? 👉'

    invstmtName = st.text_input('Enter Invest Name:')
    invstmtAmount = st.number_input('Amount ($)', min_value=0.0, format='%.2f')
    invstmtAccount = st.selectbox('Account', [selected_invstmt_account])
    invstmtType = st.selectbox('Type', [selected_invstmt_type])
    invstmtDate = st.date_input('Date:')
    invstmtNote  = st.text_area('Notes (Optional)', height=70)

    #----Button------------------------
    if st.button('Add Investment'):
        st.balloons()
        #Invesment dictionary 
        investmentData = {
            'Name': invstmtName,
            'Amount': invstmtAmount,
            'InvPaymentMthd': invstmtAccount,
            'type': invstmtType,
            'Date': invstmtDate,
            'Note': invstmtNote
        }
        saveInvestmtData (investmentData)
        
        #Save the message in a session state
        st.session_state.success_message_investmt = (f'🎈 Your Investment has been added successfully!\n\n'f'**➔ Name:** {invstmtName}\n\n'f'**➔ Amount:** ${invstmtAmount}\n\n'f'**➔ Payment Method:** {invstmtAccount}\n\n'f'**➔ Type:** {invstmtType}\n\n'f'**➔ Date:** {invstmtDate}\n\n'f'**➔ Note:**{invstmtNote}'
        )
        st.experimental_rerun()

        #Save the message in session_state only if the user add a income
    if st.session_state.success_message_investmt:
        st.success(st.session_state.success_message_investmt)
        #clear the message at the end
        st.session_state.success_message_investmt = None
