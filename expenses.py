import streamlit as st

#initialize the session state variable in the they dont exist
if 'selected_exp_category' not in st.session_state:
        st.session_state.selected_exp_category = None
if 'selected_exp_account' not in st.session_state:
        st.session_state.selected_exp_account = None

def categories():
    st.header('💸 Expenses Categories')
    col1, col2 = st.columns (2)

    with col1:
        if st.button('🏠 Rent', key='rent_btn'):
            st.session_state.selected_exp_category = '🏠 Rent'
        if st.button('🍱 Food', key='food_btn'):
            st.session_state.selected_exp_category = '🍱 Food'
        if st.button('⛽️ Gas', key='gas_btn'):
            st.session_state.selected_exp_category = '⛽️ Gas'
        if st.button('📚 Education', key='education_btn'):
            st.session_state.selected_exp_category = '📚 Education'
            
    with col2:
        if st.button('😷 Health', key='health_btn'): 
            st.session_state.selected_exp_category = '😷 Health'
        if st.button('🎁 Gifts', key='gifts_btn'):
            st.session_state.selected_exp_category = '🎁 Gifts'
        if st.button('💪🏽 Gym', key='gym'):
            st.session_state.selected_exp_category = '💪🏽 Gym'
        if st.button('🍾 Free Time', key='free_time_btn'):
            st.session_state.selected_exp_category = '🍾 Free Time'
    
def form():
    st.subheader('Add Expense 💵')
    selected_exp_category = st.session_state.selected_exp_category or "Select a Category 👉"
    selected_exp_account = st.session_state.selected_account or "Select a Account 👉"
    
    expName = st.text_input('Enter Expense Name:')
    expAmount = st.number_input('Enter the expense amount ($)', min_value=0.0, format="%.2f")
    expLocation = st.text_input('Enter Location:')
    expAccount = st.selectbox('Payment Method', [selected_exp_account])
    expCategory = st.selectbox('Category', [selected_exp_category])
    expDate = st.date_input('Date')
    expNotes = st.text_area('Notes (Optional)', height=70)

    if st.button('Add Transaction'):
        st.success(f'Your Transaction has been added successfully with Category:       {expCategory},      Amount: ${expAmount}!')