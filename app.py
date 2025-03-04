import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import incomes, expenses, investments
from PIL import Image
from streamlit_option_menu import option_menu
from Modules.rightSideInfo import allAccounts,show_date 
from Modules.dataFuntions import (
    create_inc_dataFrame, create_exp_dataFrame, create_invstmt_dataFrame, income_current_year, expenses_current_year, investments_current_year, income_by_current_year, expenses_by_current_year, investments_by_current_year,    investments_df, income_df, expenses_df, accounts, expense_distribution, investment_distribution, income_distribution, latest_income, latest_expenses, latest_investments, monthly_income_df, monthly_expenses_df, monthly_investments_df, monthly_total_income, monthly_total_expenses, monthly_total_investments, merged_df, investment_trends
)

st.set_page_config(
    page_title='Personal Finance Dashboard', page_icon='💰', 
    layout='wide',
    initial_sidebar_state='expanded')

#initialize the session states variable in case they dont exist
if 'selected_inc_category' not in st.session_state:
    st.session_state.selected_inc_category = ''
if 'selected_exp_category' not in st.session_state:
    st.session_state.selected_exp_category = ''
if 'selected_invstmt_type' not in st.session_state:
    st.session_state.selected_invstmt_type = ''

if 'selected_inc_account' not in st.session_state:
    st.session_state.selected_inc_account = ''
if 'selected_exp_account' not in st.session_state:
    st.session_state.selected_exp_account = ''
if 'selected_invstmt_account' not in st.session_state:
    st.session_state.selected_invstmt_account = ''

if 'success_message_income' not in st.session_state:
    st.session_state.success_message_income = '' 
if 'success_message_expenses' not in st.session_state:
    st.session_state.success_message_expenses = '' 
if 'success_message_investmt' not in st.session_state:
    st.session_state.success_message_investmt = '' 

#----Sidebar------------------------
with st.sidebar:
    st.markdown('<h1 style="font-size: 50px;">🏦 Personal Finance Dashboard</h1>', unsafe_allow_html=True)

    st.divider()
#---------
    selected = option_menu('Manage Your Money!', ['Home', 'Incomes', 'Expenses', 'Investments', 'Spreadsheets'], menu_icon= 'bi bi-wallet-fill', default_index=0)
    st.divider()
    st.markdown(' 👨🏻‍💻 Made by: \nJustin Mora')

#-------home page header------------
if selected == 'Home':
    st.header ('Hey, Welcome 👋')

    co1, co2 = st.columns(2)
    with co1:
        st.info ('- Take a general look at your finances 🤑')

    with co2:
        show_date()

#---------
#---------
    st.divider()
    c1, c2, c3, c4 = st.columns (4)
    col1, col2, col3, col4 = st.columns (4)
    with c2:
            st.markdown('#### - Total by year')

    with col1:
            #expander show b. acc. 
            with st.expander('💵 Your Money'):
                st.subheader('🏦 Account Balances')
                for icon, balance in accounts.items():
                    st.metric(label=icon, value=f'${balance:,.2f}')
                st.error('This funtion will be available soon 😀')
#---------
            #graph1
            st.markdown('### 💸 Income vs Expenses')
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.pie([income_current_year, expenses_current_year], labels=['Incomes', 'Expenses'], autopct='%1.1f%%', colors=['#B880FF', '#E7D3FF'])
            st.pyplot(fig)

            st.divider()
#---------
            st.markdown('### 📊 Over Time')

            #merge dataframes 
            combined_df = pd.merge(monthly_income_df, monthly_expenses_df, on='Month', how='outer')
            combined_df = pd.merge(combined_df, monthly_investments_df, on='Month', how='outer')

            #fill empty espaces in the df with 0
            combined_df.fillna(0, inplace=True)

            #making sure 'Month' is in date format
            combined_df['Month'] = pd.to_datetime(combined_df['Month'].astype(str))

            #selecting the data to show in the chart
            data_for_area_chart = combined_df[['Month', 'Total Income', 'Total Expenses', 'Total Investments']]

            #setting the month to index
            data_for_area_chart.set_index('Month', inplace=True)

            #print the graoh
            st.area_chart(data_for_area_chart)

            st.divider()
#---------
#---------
    with col2:
            st.metric(label='📥 Incomes (2025)', value=f'${income_current_year:,.2f}')

            with st.expander('Total (2025) Incomes By Category'):
                #print the totals in 2025
                for category, total in income_by_current_year.items():
                    st.metric(label=category, value=f'${total:,.2f}')
            st.divider()
#--------
            st.metric(label='💵🗓️ Incomes This month', value=f'${monthly_total_income:,.2f}')
            with st.popover('Show Last 5 Incomes'):
                # Últimos 5 ingresos
                st.write(latest_income)

            st.divider()

            #monthly incomes by category chart
            st.markdown('### 💵 Monthy Incomes By Category ')
            monthly_income_by_category = income_df.groupby([income_df['Date'].dt.to_period('M'), 'Category'])['Amount'].sum().unstack().fillna(0)
            #create graph
            fig, ax = plt.subplots(figsize=(7, 5))
            #draw bar graph
            monthly_income_by_category.plot(kind='bar', stacked=True, ax=ax, colormap='Set3')
            ax.set_xlabel('Month')
            ax.set_ylabel('Amount ($)')
            st.pyplot(fig)
            st.divider()
#---------
#---------
    with col3:
            st.metric(label='📤 Expenses (2025)', value=f'${expenses_current_year:,.2f}')

            with st.expander('Total (2025) Expenses By Category'):
                #print the totals in 2025
                for category, total in expenses_by_current_year.items():
                    st.metric(label=category, value=f'${total:,.2f}')
            st.divider()
#--------- 
            st.metric(label='💵🗓️ Expenses This month', value=f'${monthly_total_expenses:,.2f}')
            with st.popover('Show Last 5 expenses'):
                # Últimos 5 ingresos
                st.write(latest_expenses)
            st.divider()
#---------
            #graph 3
            st.markdown('### 💰 Expense Distribution by Category')
            fig, ax = plt.subplots(figsize=(7, 5))
            ax.pie(expense_distribution.values, 
                labels=expense_distribution.index, 
                autopct='%1.1f%%', 
                startangle=90, 
                colors=sns.color_palette('Set3', len(expense_distribution)))
            st.pyplot(fig)
            st.divider()
#---------
#---------
    with col4:
            st.metric(label='📤 invested (2025)', value=f'${investments_current_year:,.2f}')

            with st.expander('Total (2025) Invested By Category'):
                #take the data and group it 
                #print the totals 
                for Type, total in investments_by_current_year.items():
                    st.metric(label=Type, value=f'${total:,.2f}')

            st.markdown('### 📈 Investment Trend Over Time')
            st.line_chart(investments_df.set_index('Date')['Amount'])

            st.divider()
#---------
            st.metric(label='💵🗓️ Invested This month', value=f'${monthly_total_investments:,.2f}')

            with st.popover('Show Last 5 Investments'):
                # Últimos 5 ingresos
                st.write(latest_investments)
            st.divider()
    st.warning( "⚠️ Please note: The data and charts displayed on this page will not update in real-time. "
        "To view the most up-to-date information, please either refresh the page or restart the app."
)
#----------------------------
elif selected == 'Incomes':
    st.title('💰 Manage Your Incomes')

    colm1, colm2 = st.columns((2, .9), gap='medium')
    with colm1:
        st.info('- Fill out the form below and select a category on the right to add a new income transaction.')
    with colm2:
        show_date()

    st.divider()

    col1, col2 = st.columns((4.5, 2), gap='medium')
    with col2:
        incomes.incAccounts()
        incomes.incCategories()
    with col1:
        incomes.form()

    st.divider()
#----------------------------
elif selected == 'Expenses':
    st.title('💸 Manage Your Expenses')

    colm1, colm2 = st.columns((2, .9), gap='medium')
    with colm1:
        st.info('- Fill out the form below and select a category on the right to add a new expense transaction.')
    with colm2:
        show_date()

    st.divider()

    col1, col2 = st.columns((4.5, 2), gap='medium')
    with col2:
        expenses.expAccounts()
        expenses.categories()
    with col1:
        expenses.form()
    st.divider()
#----------------------------
elif selected == 'Investments':
    st.title('📉 Manage Your Investment')

    colmn1, colmm2 = st.columns((2, .9), gap='medium')
    with colmn1:
        st.info('- Fill out the form below and select a category on the right to add a new investment.')
    with colmm2:
        show_date()

    st.divider()

    col1, col2 = st.columns((4.5, 2), gap='medium')
    with col2:
        investments.invstmtAccounts()
        investments.invstmtType()
    with col1:
        investments.form()
    st.divider()
#----------------------------
elif selected == 'Spreadsheets':
    st.markdown('## 📂 Spreadsheets Viewer')

    # create tabs for each section
    tab1, tab2, tab3 = st.tabs(['📥 Incomes', '📤 Expenses', '📈 Investments'])

    with tab1:
        st.subheader('📥 Incomes')
        income_df = pd.read_csv('Data/incomes.csv')
        st.dataframe(income_df, use_container_width=True)

        st.divider()
        st.subheader('🗓️ Monthly Income Summary')
        st.dataframe(monthly_income_df, use_container_width=True)
        st.divider()
        # st.subheader('🗓️ Yearly Incomes Summary')
        #next feature 
    with tab2:
        st.subheader('📤 Expenses')
        expenses_df = pd.read_csv('Data/expenses.csv')
        st.dataframe(expenses_df, use_container_width=True)

        st.divider()
        st.subheader('🗓️ Monthly Expenses Summary')
        st.dataframe(monthly_expenses_df, use_container_width=True)
        # st.subheader('🗓️ Yearly Expenses Summary')
        #next feature 

    with tab3:
        st.subheader('📈 Investments')
        investments_df = pd.read_csv('Data/investments.csv')
        st.dataframe(investments_df, use_container_width=True)

        st.divider()
        st.subheader('🗓️ Monthly Investments Summary')
        st.dataframe(monthly_investments_df, use_container_width=True)
        # st.subheader('🗓️ Yearly Investments Summary')
        #next feature 
