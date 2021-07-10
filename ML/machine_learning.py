def machine_learning():
    import pandas as pd
    from pathlib import Path

    loan_data_df = pd.read_csv(
        Path('./data/train.csv')
    )

    loan_data_df
    