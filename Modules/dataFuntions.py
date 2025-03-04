import pandas as pd
import os
from datetime import datetime


#get date 
current_month = datetime.now().month
current_year = datetime.now().year

# empty dataframes for each section to store the data in case it doesnt exist  / .CSV files
def create_inc_dataFrame(fileName):
    if os.path.exists(fileName):
        df = pd.read_csv(fileName)
    else: 
        df = pd.DataFrame(columns=['Name', 'Amount', 'Account', 'Category', 'Date', 'Note'])
        df.to_csv(fileName, index=False)
    return df

def create_exp_dataFrame(fileName):
    if os.path.exists(fileName):
        df = pd.read_csv(fileName)
    else: 
        df = pd.DataFrame(columns=['Name', 'Amount', 'Location', 'ExpPaymentMthd', 'Category', 'Date', 'Note'])
        df.to_csv(fileName, index=False)
    return df

def create_invstmt_dataFrame(fileName):
    if os.path.exists(fileName):
        df = pd.read_csv(fileName)
    else:
        df = pd.DataFrame(columns=['Name', 'Amount', 'InvPaymentMthd', 'type', 'Date', 'Note'])
        df.to_csv(fileName, index=False)
    return df

#-----------------------------------------------
#save data to .CSv File 
def saveIncomeData(incomeData):
    #create or read rhe dataframe
    df = create_inc_dataFrame('Data/incomes.csv')
    #convert incomeData to a framework
    new_row = pd.DataFrame ([incomeData])
    #appen row to dataframe
    df = pd.concat ([df, new_row], ignore_index=True)
    #save updated dataframe into the csv file
    df.to_csv('Data/incomes.csv', index=False)

def saveExpensesData(expensesData):
    df = create_exp_dataFrame('Data/expenses.csv')
    new_row = pd.DataFrame ([expensesData])
    df = pd.concat ([df, new_row], ignore_index=True)
    df.to_csv('Data/expenses.csv', index=False)

def saveInvestmtData(investmentData):
    df = create_invstmt_dataFrame ('Data/investments.csv')
    new_row = pd.DataFrame([investmentData])
    df = pd.concat ([df, new_row], ignore_index=True)
    df.to_csv('Data/investments.csv', index=False)

#-----------------------------------------------
#load data from each section form csv files
income_df = create_inc_dataFrame('Data/incomes.csv')
expenses_df = create_exp_dataFrame('Data/expenses.csv')
investments_df = create_invstmt_dataFrame('Data/investments.csv')

#convert 'Amount' column to numeric (handling empty files)
income_df['Amount'] = pd.to_numeric(income_df['Amount'], errors='coerce').fillna(0)
expenses_df['Amount'] = pd.to_numeric(expenses_df['Amount'], errors='coerce').fillna(0)
investments_df['Amount'] = pd.to_numeric(investments_df['Amount'], errors='coerce').fillna(0)

#convert 'Date' column to date type
income_df['Date'] = pd.to_datetime(income_df['Date'], errors='coerce')
expenses_df['Date'] = pd.to_datetime(expenses_df['Date'], errors='coerce')
investments_df['Date'] = pd.to_datetime(investments_df['Date'], errors='coerce')

#-----------------------------------------------
#grouping df by year and category/type
#this this to show amount by category in expander 
income_by_year_category = income_df.groupby([income_df['Date'].dt.year, 'Category'])['Amount'].sum().unstack(fill_value=0)
expenses_by_year_category = expenses_df.groupby([expenses_df['Date'].dt.year, 'Category'])['Amount'].sum().unstack(fill_value=0)
investments_by_year_category = investments_df.groupby([investments_df['Date'].dt.year, 'Type'])['Amount'].sum().unstack(fill_value=0)

#filter by year and category/type
income_by_current_year = income_by_year_category.loc[current_year]
expenses_by_current_year = expenses_by_year_category.loc[current_year]
investments_by_current_year = investments_by_year_category.loc[current_year]


#-----------------------------------------------
current_year = 2025

#filter df by the year 2025 to show in metric
income_current_year = income_df[income_df['Date'].dt.year == current_year]['Amount'].sum()
expenses_current_year = expenses_df[expenses_df['Date'].dt.year == current_year]['Amount'].sum()
investments_current_year = investments_df[investments_df['Date'].dt.year == current_year]['Amount'].sum()


#-----------------------------------------------
#get the amount for each account

#dictionary to store the amounts
accounts = {
    '💵 Cash': 0,
    '💳 Card': 0,
    '💸 Paypal': 0,
    '🏦 Bank Account': 0
}

# #add income by acc
# for account in accounts.keys():
#     accounts[account] += income_df[income_df['Account'] == account]['Amount'].sum()
# #add expenses by acc
# for account in accounts.keys():
#     accounts[account] -= expenses_df[expenses_df['ExpPaymentMthd'] == account]['Amount'].sum()  
# #add investments by acc
# for account in accounts.keys():
#     accounts[account] -= investments_df[investments_df['InvPaymentMthd'] == account]['Amount'].sum()
    
#-----------------------------------------------
#grouping by namess, amount and month
monthly_income = income_df.groupby([income_df['Date'].dt.to_period('M'), 'Name'])['Amount'].sum().reset_index()
monthly_income.columns = ['Month', 'Income Name', 'Total Income']

monthly_expenses = expenses_df.groupby([expenses_df['Date'].dt.to_period('M'), 'Name'])['Amount'].sum().reset_index()
monthly_expenses.columns = ['Month', 'Expense Name', 'Total Expenses']

monthly_investments = investments_df.groupby([investments_df['Date'].dt.to_period('M'), 'Name'])['Amount'].sum().reset_index()
monthly_investments.columns = ['Month', 'Investment Name', 'Total Investments']

#grouping by month adding the values
monthly_income_df = monthly_income.groupby('Month').agg({'Income Name': ' , '.join, 'Total Income': 'sum'}).reset_index()
monthly_expenses_df = monthly_expenses.groupby('Month').agg({'Expense Name': ' '.join, 'Total Expenses': 'sum'}).reset_index()
monthly_investments_df = monthly_investments.groupby('Month').agg({'Investment Name': ' '.join, 'Total Investments': 'sum'}).reset_index()

#merge the DataFrames by month
merged_df = pd.merge(monthly_income_df, monthly_expenses_df, on='Month', how='outer')
merged_df = pd.merge(merged_df, monthly_investments_df, on='Month', how='outer')

#--------------------------
#to avoid errorrs with different date lengths
#make sure both(inconme & expenses) got the same date set 
all_dates = pd.concat([monthly_income_df['Month'], monthly_expenses_df['Month']]).unique()

#reindex to make sure sure each serie has the same dates
monthly_income_df = monthly_income_df.set_index('Month').reindex(all_dates, fill_value=0).reset_index()
monthly_expenses_df = monthly_expenses_df.set_index('Month').reindex(all_dates, fill_value=0).reset_index()
monthly_investments_df = monthly_investments_df.set_index('Month').reindex(all_dates, fill_value=0).reset_index()


#-----------------------------------------------
#distributions
income_distribution = income_df.groupby('Category')['Amount'].sum()
expense_distribution = expenses_df.groupby('Category')['Amount'].sum()
investment_distribution = investments_df.groupby('Type')['Amount'].sum()


#get last 5 transact. for each section (sorted)
latest_income = income_df.sort_values(by='Date', ascending=False).head(5)
latest_expenses = expenses_df.sort_values(by='Date', ascending=False).head(5)
latest_investments = investments_df.sort_values(by='Date', ascending=False).head(5)

#-----------------------------------------------
#grouping 
investment_trends = investments_df.groupby(['Date', 'Type'])['Amount'].sum().unstack()

#-----------------------------------------------

#filter data by month
monthly_total_income = income_df[
    (income_df['Date'].dt.month == current_month) & (income_df['Date'].dt.year == current_year)
]['Amount'].sum()

monthly_total_expenses = expenses_df[
    (expenses_df['Date'].dt.month == current_month) & (expenses_df['Date'].dt.year == current_year)
]['Amount'].sum()

monthly_total_investments = investments_df[
    (investments_df['Date'].dt.month == current_month) & (investments_df['Date'].dt.year == current_year)
]['Amount'].sum()


