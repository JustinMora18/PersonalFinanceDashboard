import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Personal Finance Dashboard", page_icon="💰", layout="wide")

with st.sidebar:
    selected = option_menu("Main Menu", ['Home', 'Incomes', 'Expenses', 'Investments', 'Financial Report'], menu_icon= 'house', default_index=1)



if selected == 'Home':
    st.title (" 💰 Personal Fincance Dashboard 💰 ") 
    #grapg and features here 


elif selected == 'Incomes':
    st.subheader('Incomes 💵')
    amount = st.number_input('Enter the income amount ($)', min_value=0.0, format='%.2f')
    date = st.date_input('Date:')
    incName = st.text_input('Enter Income Name:')
    category = st.selectbox('Category', ['Job', 'teaching', 'Side job Two', 'Project', 'Research', 'Finantial Aid'])
    note  = st.text_area('Notes (Optional)', height=70)
    st.success('Your Transaction has been added successfully!')


elif selected == 'Expenses':
    st.subheader('  Expenses 💵')
    moneyOut = st.number_input('Enter the expense amount ($)', min_value=0.0, format="%.2f")
    location = st.text_input('Enter Location:')
    date = st.date_input('Date')
    category = st.selectbox('Category', ['Food', 'Rent', 'Hobbies', 'School', 'Others'])
    notes = st.text_area('Notes (Optional)', height=70)


elif selected == 'Financial Report':
    st.subheader('Generate Report')
    #add database, filtering, etc

