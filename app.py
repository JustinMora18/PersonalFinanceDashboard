import streamlit as st

st.set_page_config(page_title="Personal Finance Dashboard", page_icon="💰", layout="wide")

st.title (" 💰 Personal Fincance Dashboard 💰 ") 

st.sidebar.header('Menu')
menu = st.sidebar.radio("Chose an option: ", ['Dashboard', 'Transactions', 'Financial Report'])

if menu == 'Dashboard':
    st.subheader('Dashboard')
    st.write("Aquí se mostrarán los datos financieros.")

elif menu == 'Transactions':
    st.subheader('Manage your money!')
    st.subheader('- What Do You Want to do?')

    with st.expander('Money in'):
        # transaction_type = st.selectbox("Transaction Type", ["Money In!", "Money Out!"])
        moneyIn = st.number_input('Enter the income amount ($)', min_value=0.0, format='%.2f')
        category = st.selectbox('Category', ['Job', 'investment', 'Side job', 'Project', 'Research'])
        date = st.date_input('Date:')
        notes = st.text_area('Notes (Optional)', height=70)


    with st.expander('Money out'):
        moneyOut = st.number_input('Enter the expend amount ($)', min_value=0.0, format="%.2f")
        category = st.selectbox('Category', ['Food', 'Rent', 'Hobbies', 'School', 'Others'])
        date = st.date_input('Date')
        notes = st.text_area('Notes (Optional)', height=70)

    st.success('Your Transaction has been added successfully!')

elif menu == 'Financial Report':
    st.subheader('Generate Report')
    st.write('Analysis')
