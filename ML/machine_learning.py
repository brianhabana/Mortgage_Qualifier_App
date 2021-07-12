from ML.encode import encode1
from ML.encode import encode2
from ML.encode import encode3
from ML.encode import encode4
from ML.encode import encode5
from ML.encode import encode6
from ML.encode import encode7
from sklearn import metrics

def machine_learning(user_input):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import os
    
    from pathlib import Path

    #create user input dataframe
    #user_df = pd.DataFrame(data=user_input)
    #print(user_df)

    #import train data
    train_df = pd.read_csv(
        Path('./data/train.csv')
        )

    test_df = pd.read_csv(
        Path('./data/test.csv')
        )

    test_df.loc[-1] = user_input

    test_df = test_df.reset_index(drop=True)

    print(test_df.tail(5))

    print('Checking for null values..')
    test_df.isnull().sum()
    train_df.isnull().sum()

    #print('adding userdata to test...')
    #test_df = test_df.append(user_df)
        
    print('Loading ML Data...')
    loan_data_df = train_df.append(test_df)
    
    print('checking for high correlation')
    corrmat=loan_data_df.corr()
    f, ax = plt.subplots(figsize=(15,10))
    sns.heatmap(corrmat, vmax=.8, square=True)

    print('checking summary statistics...')
    loan_data_df.Married.value_counts()
    loan_data_df.Gender.value_counts()
    loan_data_df.Dependents.value_counts()
    loan_data_df.Education.value_counts()
    loan_data_df.Self_Employed.value_counts()
    loan_data_df.ApplicantIncome.describe()
    loan_data_df.LoanAmount.describe()
    loan_data_df.Credit_History.value_counts()
    loan_data_df.Property_Area.value_counts()

    print('normalizing...')
    loan_data_df['LoanAmount_log']= np.log(loan_data_df['LoanAmount'])
    train_df['ApplicantIncome_log']= np.log(train_df['ApplicantIncome'])

    print('fill missing values...')
    loan_data_df['Gender'].fillna(value=loan_data_df['LoanAmount'].mode()[0], inplace=True)
    loan_data_df['LoanAmount'].fillna(value=loan_data_df['LoanAmount'].mean(), inplace=True)
    loan_data_df['LoanAmount_log'].fillna(value=loan_data_df['LoanAmount_log'].mean(), inplace=True)
    loan_data_df['Married'].fillna(value=loan_data_df['Married'].mode()[0], inplace=True)
    loan_data_df['Loan_Amount_Term'].fillna(value=loan_data_df['Loan_Amount_Term'].mean(), inplace=True)
    loan_data_df['Credit_History'].fillna(value=loan_data_df['Credit_History'].mode()[0], inplace=True)
    loan_data_df['Self_Employed'].fillna(value=loan_data_df['Self_Employed'].mode()[0], inplace=True)
    loan_data_df['Dependents'].fillna(value=loan_data_df['Dependents'].mode()[0], inplace=True)
    loan_data_df['Loan_Amount_Term'].fillna(value=loan_data_df['Loan_Amount_Term'].mode()[0], inplace=True)


    #encoding data
    #call the encode helper function
    print('encoding loan data...')
    
    loan_data_df['Loan_Status'] = loan_data_df["Loan_Status"].apply(encode1)
    loan_data_df['Gender'] = loan_data_df["Gender"].apply(encode2)
    loan_data_df['Married'] = loan_data_df["Married"].apply(encode3)
    loan_data_df['Education'] = loan_data_df["Education"].apply(encode4)
    loan_data_df['Self_Employed'] = loan_data_df["Self_Employed"].apply(encode5)
    loan_data_df['Property_Area'] = loan_data_df["Property_Area"].apply(encode6)
    loan_data_df['Dependents'] = loan_data_df["Dependents"].apply(encode7)
    

    train_df = loan_data_df.iloc[:614]
    X = train_df.iloc[:,np.r_[1:5,9:11,13:14]].values

    y = train_df.iloc[:,12].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    y_train

    y_test

    print('Scaling data StandardScaler...')
    from sklearn.preprocessing import StandardScaler
    ss=StandardScaler()

    X_train=ss.fit_transform(X_train)
    X_test=ss.fit_transform(X_test)

    print('Training ML Algo Logistic Regression...')

    from sklearn.linear_model import LogisticRegression
    logistic_regression_model = LogisticRegression(random_state=0)
    SGDClassifier= LogisticRegression()
    SGDClassifier.fit(X_train, y_train)

    y_pred=SGDClassifier.predict(X_test)
    y_pred

    print('The accuracy of Logistic Regression is ', metrics.accuracy_score(y_pred,y_test))

    test_df = loan_data_df[615:982]
    test_df = test_df.iloc[:,np.r_[1:5, 9:11, 13:14]].values

    print('Scaling test data')
    test_df = ss.fit_transform(test_df)

    print('Predicting Loan Approval on user data...')
    pred = SGDClassifier.predict(test_df)

    
    print(pred)

    print(pred.shape)

    if pred[366] == 1:
        print('Congats, your Loan is Approved!')
    else:
        print('Sorry...please stack more stats!')

    #----user data------#
    

    #print('Predicting Loan Approval on user data...')


    

    """"
    print('Checking User data for null values..')
    #print(user_df.isnull().sum())

    print('normalizing user data...')
    user_df['LoanAmount_log']= np.log(user_df['LoanAmount'])
    user_df['ApplicantIncome_log']= np.log(user_df['ApplicantIncome'])

    print('encoding user data...')
    
    #user_df['Loan_Status'] = user_df["Loan_Status"].apply(encode1)
    user_df['Gender'] = user_df["Gender"].apply(encode2)
    user_df['Married'] = user_df["Married"].apply(encode3)
    user_df['Education'] = user_df["Education"].apply(encode4)
    user_df['Self_Employed'] = user_df["Self_Employed"].apply(encode5)
    user_df['Property_Area'] = user_df["Property_Area"].apply(encode6)
    user_df['Dependents'] = user_df["Dependents"].apply(encode7)

    print('setting user data')
    user_df = user_df[:1]
    user_df = user_df.iloc[:,np.r_[1:5, 9:11, 13:14]].values

    test_df = test_df(user_df)

    print('Scaling user data')
    test_df = ss.fit_transform(test_df)

    print('Predicting Loan Approval on USER data...')
    pred = SGDClassifier.predict(test_df)

    print(pred)

    if pred[35] == 1:
        print('Congats, your Loan is Approved!')
    else:
        print('Sorry...please stack more stats!')
"""