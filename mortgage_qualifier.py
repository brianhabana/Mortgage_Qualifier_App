# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Mortgage Qualifier
# """Loan Qualifier Application.
# 
# This is a command line application to match applicants with mortgage loans.
# 
# Example:
#     $ mqa.py
# """

# %%
#import dependencies
import sys
import fire
import questionary

from pathlib import Path
from qualifier.utils.fileio import (
    load_csv,
    save_csv,
)


# %%
#import calculators
from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)


# %%
#import Zillow RapidAPI
from api.zillow.search_property_details import search_property_details

#import machine learning
from ML.machine_learning import machine_learning

# %%
#import qualifiers
#from qualifier.filters.max_loan_size import filter_max_loan_size
#from qualifier.filters.credit_score import filter_credit_score
#from qualifier.filters.debt_to_income import filter_debt_to_income
#from qualifier.filters.loan_to_value import filter_loan_to_value


# %%
#load bank data
def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = "./data/daily_rate_sheet.csv"
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


# %%
#load applicant info
def get_applicant_info():
    import pandas as pd

    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    property_link = questionary.text("What's the property url?").ask()
    loan_to_value = questionary.text("What's the requested loan to value (LTV)%?").ask()
    #Gender = questionary.text("What's your Gender? (Male/Female)?").ask()
    #Married = questionary.text("Are you Married (Yes/No)?").ask()
    #Dependents = questionary.text("How many Dependents(if any)?").ask()
    #Education = questionary.text("Did you Graduate College (Graduate/Not Graduate)?").ask()
    #Self_Employed = questionary.text("Are you self employed (Yes/No)?").ask()
    #ApplicantIncome = questionary.text("What is your monthly gross income?").ask()
    #CoapplicantIncome = questionary.text("What's your co-applicant's income (if any)?").ask()
    #Loan_Amount_Term = questionary.text("How in months is the term (360 is 30 yrs)?").ask()
    #Credit_History = questionary.text("Do you have any credit history(Yes/No)?").ask()
    #Property_Area = questionary.text("What's the property Area(Urban / Rural /Semirural)?").ask()
    
    print('Loading app data...')

    #debt = questionary.text("What's your current amount of monthly debt?").ask()
    #income = questionary.text("What's your total monthly income?").ask()
    #loan_amount = questionary.text("What's your desired loan amount?").ask()
    #home_value = questionary.text("What's your home value?").ask()

    #LoanID = str('LP002990')
    property_link = str(property_link)
    loan_to_value = float(loan_to_value)
    #Gender = str(Gender)
    #Married = str(Married)
    #Dependents = int(Dependents)
    #Education = str(Education)
    #Self_Employed = str(Self_Employed)
    #ApplicantIncome = float(ApplicantIncome)
    #CoapplicantIncome = float(CoapplicantIncome)
    #LoanAmount = float(390 * (loan_to_value/100))
    #Loan_Amount_Term = int(Loan_Amount_Term)
    #Credit_History = str(Credit_History)
    #Property_Area = str(Property_Area)

    LoanID = 'LP002990'
    Gender = 'Male'
    Married = 'Yes'
    Dependents = 0
    Education = 'Graduate'
    Self_Employed = 'No'
    ApplicantIncome = 4000
    CoapplicantIncome = 0
    LoanAmount = 290
    Loan_Amount_Term = 360
    Credit_History = 1
    Property_Area = 'Urban'

    user_input = {
     'LoanID': [LoanID], 
     'Gender': [Gender],
     'Married': [Married], 
     'Dependents' : [Dependents], 
     'Education' : [Education], 
     'Self_Employed' : [Self_Employed],
     'ApplicantIncome' : [ApplicantIncome],
     'CoapplicantIncome' : [CoapplicantIncome],
     'LoanAmount' : [LoanAmount],
     'Loan_Amount_Term' : [Loan_Amount_Term],
     'Credit_History' : [Credit_History],
     'Property_Area' : [Property_Area],
    }

    #debt = float(debt)
    #income = float(income)
    #loan_amount = float(loan_amount)
    #home_value = float(home_value)

    return property_link, loan_to_value, user_input


# %%
#find qualifying loans
def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    #Calculate the monthly debt ratio
    #monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    #print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    #loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    #print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    #bank_data_filtered = filter_max_loan_size(loan, bank_data)
    #bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    #bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    #bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    #print(f"Found {len(bank_data_filtered)} qualifying loans")

    #return bank_data_filtered


# %%
#save Qualifying loans
def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    
    if len(qualifying_loans) > 0: 

        #Would you like to save?
        save = questionary.confirm("Would you like to save?").ask()
        
        if save == True:
            #csvpath = Path('qualifying_loans.csv')
                csvpath = questionary.text("Where would you like to save?").ask()
                save_csv(csvpath, qualifying_loans)
                print('writing file...')


        if save == False:
            sys.exit(f"You chose note to save")
            
        return save
    elif len(qualifying_loans) == 0:
        sys.exit("Sorry there are no qualifying loans")


# %%
#run main function
def run():
    """The main function for running the script."""

    print('***** MORTGAGE QUALIFIER APP *****')
    # Load the latest Bank data
    #bank_data = load_bank_data()

    # Get the applicant's information
    property_link, loan_to_value, user_input = get_applicant_info()

    #test api
    search_property_details(property_link, loan_to_value)
    
    #import machine learning
    machine_learning(user_input)

    # Find qualifying loans
    # qualifying_loans = find_qualifying_loans(
    #    bank_data, credit_score, debt, income, loan_amount, home_value
    #)

    # Save qualifying loans
    # save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)


# %%



