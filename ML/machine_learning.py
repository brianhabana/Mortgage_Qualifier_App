def machine_learning():
    import pandas as pd
    import os

    from pathlib import Path

    loan_data_df = pd.read_csv(
        Path('./data/train.csv')
        )

    print('testing ML...')
    loan_data_df.head(5)
    