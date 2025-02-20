import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(
    page_title="Personal Finance Dashboard", page_icon="💰", 
    layout="wide",
    initial_sidebar_state="expanded")

    #add funtion here

with st.sidebar:
    selected = option_menu("Main Menu", ['Home', 'Incomes', 'Expenses', 'Investments', 'Financial Report'], menu_icon= 'house', default_index=1)

if selected == 'Home':
    st.title (" 💰 Personal Fincance Dashboard 💰 ") 
    
    #graph and features here 

elif selected == 'Incomes':
    col = st.columns((1.5, 4.5, 2), gap='medium')
    with col[0]:
        st.header("Income Categories")
        col1, col2 = st.columns (2)
        with col1:
            st.button("💸 Salary")
            st.button("🧑🏾‍🏫 Teaching")
            st.button("🧑🏾‍💻 Project")
            st.button("💰 Finantial Aid")
        with col2:
            st.button("🎁 Gift")
            st.button("🧑‍🧑‍🧒 Parents")
            st.button("🧑🏾‍💻 Online Sales")
            st.button("🤑 Others")
            
    with col[1]:
        st.subheader('Incomes 💵')
        incAmount = st.number_input('Enter the income amount ($)', min_value=0.0, format='%.2f')
        incDate = st.date_input('Date:')
        incName = st.text_input('Enter Income Name:')
        incCategory = st.selectbox('Category', ['Job', 'teaching', 'Side job Two', 'Project', 'Research', 'Finantial Aid'])
        incNote  = st.text_area('Notes (Optional)', height=70)
        st.success('Your Transaction has been added successfully!')


elif selected == 'Expenses':
    col = st.columns((1.5, 4.5, 2), gap='medium')
    with col[0]:
        st.header("Expenses Categories")
        col1, col2 = st.columns (2)
        with col1:
            st.button("🏠 Rent")
            st.button("🍱 Food")
            st.button("⛽️ Gas")
            st.button("📚 Education")
        with col2:
            st.button("😷 Health")
            st.button("🎁 Gifts")
            st.button("💪🏽 Gym")
            st.button("🍾 Free Time")
    
    with col[1]:
        st.subheader('  Expenses 💵')
        expAmount = st.number_input('Enter the expense amount ($)', min_value=0.0, format="%.2f")
        expLocation = st.text_input('Enter Location:')
        expDate = st.date_input('Date')
        expCategory = st.selectbox('Category', ['Food', 'Rent', 'Hobbies', 'School', 'Others'])
        expNotes = st.text_area('Notes (Optional)', height=70)


elif selected == 'Financial Report':
    st.subheader('Generate Report')
    #add database, filtering, etc

