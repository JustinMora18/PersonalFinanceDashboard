import streamlit as st

#initialize the session state variable in the they dont exist
if 'selected_category' not in st.session_state:
        st.session_state.selected_category = None
if 'selected_account' not in st.session_state:
        st.session_state.selected_account = None

def categories():
    st.header('💸 Income Categories')
    col1, col2 = st.columns (2)
    
    with col1:
        if st.button('💸 Salary', key='salary_btn'):
            st.session_state.selected_category = '💸 Salary'
        if st.button('🧑🏾‍🏫 Teaching', key='teaching_btn'):
            st.session_state.selected_category = "🧑🏾‍🏫 Teaching"
        if st.button('🧑🏾‍💻 Project', key='project_btn'):
            st.session_state.selected_category = '🧑🏾‍💻 Project'
        if st.button('💰 Financial Aid', key='financial_aid_btn'):
            st.session_state.selected_category = '💰 Financial Aid'

    with col2:
        if st.button('🎁 Gift', key='gift_btn'):
            st.session_state.selected_category = "🎁 Gift"
        if st.button('🧑‍🧑‍🧒 Parents', key='parents_btn'):
            st.session_state.selected_category = "🧑‍🧑‍🧒 Parents"
        if st.button('🧑🏾‍💻 Online Sales', key='online_sales_btn'):
            st.session_state.selected_category = 'Online Sales'
        if st.button('🤑 Others', key='others_btn'):
            st.session_state.selected_category = '🤑 Others'

def accounts():
    st.header('🏦 Accounts')
    col1, col2 = st.columns (2)

    with col1:
        if st.button('💵 Cash', key = 'cash_btn'):
            st.session_state.selected_account = ('💵 Cash')
        if st.button('💳 Card', key = 'card_btn'):
            st.session_state.selected_account = ('💳 Card')

    with col2:
        if st.button('💸 Paypal', key = 'paypal_btn'):
            st.session_state.selected_account = ('💸 Paypal')
        if st.button('🏦 Bank Account', key = 'bank_acc_btn'):
            st.session_state.selected_account = ('🏦 Bank Account')
    
    return st.session_state.selected_account


def form():
    st.subheader('Add Incomes 💵')
    selected_category = st.session_state.selected_category or 'Select a category 👉'
    selected_account = st.session_state.selected_account or 'Select an Account  👉'

    incName = st.text_input('Enter Income Name:')
    incAmount = st.number_input('Enter the income amount ($)', min_value=0.0, format='%.2f')
    incAccount = st.selectbox('Accounts', [selected_account])
    incCategory = st.selectbox('Category', [selected_category])
    incDate = st.date_input('Date:')
    incNote  = st.text_area('Notes (Optional)', height=70)
    if st.button('Add Transaction'):
        st.success(f'Your Transaction has been added successfully with Category:       {incCategory},      Amount: ${incAmount}!')

def widgets():
    print('hello word')