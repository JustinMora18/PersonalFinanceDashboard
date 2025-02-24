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
        df = pd.DataFrame(columns=['Name', 'Amount', 'Location', 'Payment Method', 'Category', 'Date', 'Note'])
        df.to_csv(fileName, index=False)
    return df

def create_invstmt_dataFrame(fileName):
    if os.path.exists(fileName):
        df = pd.read_csv(fileName)
    else:
        df = pd.DataFrame(columns=['Name', 'Amount', 'Account', 'type', 'Date', 'Note'])
        df.to_csv(fileName, index=False)
    return df

#save income data to .CSv File 
def saveIncomeData(incomeData):
    #create or read rhe dataframe
    df = create_inc_dataFrame('Data/incomes.csv')
    #add data to dataframe
    df = df.append(incomeData, ignore_index=True)
    #save data into the csv file
    df.to_csv('Data/incomes.csv')

def saveExpensesData(expensesData):
    df = create_exp_dataFrame('Data/expenses.csv')
    df = df.append(expensesData, ignore_index=True)
    df.to_csv('Data/expenses.csv')

def saveInvestmtData(investmentData):
    df = create_inc_dataFrame ('Data/investments.csv')
    df = df.append(investmentData, ignore_index=True) 
    df.to_csv('Data/investments.csv')