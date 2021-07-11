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
    #print(train_df.head(5))

    #get summary statistics
    print('Gathering summary statistics..')
    #print(train_df.describe())
    
    #encoding data
    #Build the encodeCard helper function
    #Credit card purchases should encode to 1
    #Debit card purchases should encode to 0
    print('encoding data...')
    
    def encode(Loan_Status):
        
        """
        This function encodes a loan status to either 1 or 0.
        """
        if Loan_Status == 'Y':
            return 1
        else:
            return 0

    train_df['Loan_Status'] = train_df["Loan_Status"].apply(encode)

    print(train_df.head(5))
