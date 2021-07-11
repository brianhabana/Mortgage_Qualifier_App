#import encode

#from seaborn.matrix import heatmap
from ML.encode import encode1
from ML.encode import encode2
from ML.encode import encode3
from ML.encode import encode4
from ML.encode import encode5
from ML.encode import encode6
from ML.encode import encode7

def machine_learning():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os

    from pathlib import Path

    #load in the dataset
    train_df = pd.read_csv(
        Path('./data/train.csv')       
        )
    test_df = pd.read_csv(
        Path('./data/test.csv')
        )
    
    print('Loading ML Data...')
    #print(train_df.head(5))

    #get summary statistics
    print('Gathering summary statistics..')
    #print(train_df.describe())
    
    #encoding data
    #call the encode helper function
    print('encoding data...')
    
    train_df['Loan_Status'] = train_df["Loan_Status"].apply(encode1)
    train_df['Gender'] = train_df["Gender"].apply(encode2)
    train_df['Married'] = train_df["Married"].apply(encode3)
    train_df['Education'] = train_df["Education"].apply(encode4)
    train_df['Self_Employed'] = train_df["Self_Employed"].apply(encode5)
    train_df['Property_Area'] = train_df["Property_Area"].apply(encode6)
    train_df['Dependents'] = train_df["Dependents"].apply(encode7)

    #test_df['Loan_Status'] = test_df["Loan_Status"].apply(encode1)
    test_df['Gender'] = test_df["Gender"].apply(encode2)
    test_df['Married'] = test_df["Married"].apply(encode3)
    test_df['Education'] = test_df["Education"].apply(encode4)
    test_df['Self_Employed'] = test_df["Self_Employed"].apply(encode5)
    test_df['Property_Area'] = test_df["Property_Area"].apply(encode6)
    test_df['Dependents'] = test_df["Dependents"].apply(encode7)

    print(train_df)

    #check for missing values
    #print('Checking for missing values...')
    #print(train_df.isnull().sum())
    #print(test_df.isnull().sum())

    #print('drop columns that we do not need...')
    #train_df = train_df.drop('Loan_Status', axis=1)

    #print(train_df.head(5))
    #print('append test data to train data...')
    
    loan_data_df = train_df.append(test_df)

    #print(loan_data_df.describe())

    #check for missing data on appended dataset
    #print('check for missing data on appended data set..')
    #print(loan_data_df)

    #print(loan_data_df.isnull().sum())

    #print('drop missing values...')
    #loan_data_df = loan_data_df.dropna()
    #loan_data_df = loan_data_df.drop('Loan_ID', axis=1)
    
    #print(loan_data_df.isnull().sum())
    #print(loan_data_df.head)
    #print(loan_data_df.tail)

    



