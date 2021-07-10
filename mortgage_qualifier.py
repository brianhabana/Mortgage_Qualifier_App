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
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    property_link = questionary.text("What's the property url?").ask()
    loan_to_value = questionary.text("What's the requested loan to value %?").ask()

    #debt = questionary.text("What's your current amount of monthly debt?").ask()
    #income = questionary.text("What's your total monthly income?").ask()
    #loan_amount = questionary.text("What's your desired loan amount?").ask()
    #home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    property_link = str(property_link)
    loan_to_value = float(loan_to_value)
    #debt = float(debt)
    #income = float(income)
    #loan_amount = float(loan_amount)
    #home_value = float(home_value)

    return credit_score, property_link, loan_to_value


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

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


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

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, property_link, loan_to_value = get_applicant_info()

    #test api
    search_property_details(property_link, loan_to_value)
    
    #import machine learning

    # Find qualifying loans
    # qualifying_loans = find_qualifying_loans(
    #    bank_data, credit_score, debt, income, loan_amount, home_value
    #)

    # Save qualifying loans
    # save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)


# %%



