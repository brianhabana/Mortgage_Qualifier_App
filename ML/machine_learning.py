#import encode
from ML.encode import encode1
from ML.encode import encode2
from ML.encode import encode3
from ML.encode import encode4
from ML.encode import encode5
from ML.encode import encode6
#from ML.encode import encode7
#from ML.encode import encode8
#from ML.encode import encode9
#from ML.encode import encode10


def machine_learning():
    import pandas as pd
    import os

    from pathlib import Path

    #load in the dataset
    train_df = pd.read_csv(
        Path('./data/train.csv'),
        index_col='Loan_ID'
        )

    print('Loading ML Data...')
    print(train_df.head(5))

    #get summary statistics
    print('Gathering summary statistics..')
    print(train_df.describe())
    
    #encoding data
    #call the encode helper function
    print('encoding data...')
    
    train_df['Loan_Status'] = train_df["Loan_Status"].apply(encode1)
    train_df['Gender'] = train_df["Gender"].apply(encode2)
    train_df['Married'] = train_df["Married"].apply(encode3)
    train_df['Education'] = train_df["Education"].apply(encode4)
    train_df['Self_Employed'] = train_df["Self_Employed"].apply(encode5)
    train_df['Property_Area'] = train_df["Property_Area"].apply(encode6)

    print(train_df.head(5))
