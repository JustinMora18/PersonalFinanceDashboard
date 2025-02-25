import pandas as pd
import os

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

#save income data to .CSv File 
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
    df = create_inc_dataFrame ('Data/investments.csv')
    new_row = pd.DataFrame([investmentData])
    df = pd.concat ([df, new_row], ignore_index=True)
    df.to_csv('Data/investments.csv', index=False)