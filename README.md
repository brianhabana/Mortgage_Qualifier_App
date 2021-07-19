# Mortgage Qualifier Application

This is a python command-line interface application that reduces underwriting time and labor for loan. Inputting applicants' information and calls Zillow API to determine loan amount. The app predicts mortgage loan approval based on logistist regression classification and Naive Baynes alogrithim machine learning.


---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [numpy](https://numpy.org) - NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more.


---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
  pip install NumPy
```

---

## Usage

To use the mortgage qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```

Upon launching the loan qualifier application you will be greeted with the following prompts.

![Mortgage Qualifier Prompts]()
Answers must match exactly and are case sensitive

What's the property link (enter zillow public link)
What's the requested loan to value (LTV)%? 
What's your Gender? (Male/Female)?
Are you Married (Yes/No)? 
How many Dependents(if any)?
Did you Graduate College (Graduate/Not Graduate)?
Are you self employed (Yes/No)?
What is your monthly gross income?
What's your co-applicant's income (if any)?
How in months is the term (360 is 30 yrs)?
Do you have any credit history(1 for Yes /0 for No)?
What's the property Area(Urban / Rural /Semirural)?

---

## Contributors

Brought to you by UC Berkeley Extension.

---

## License

MIT

## Screenshots

![alt text](https://github.com/brianhabana/Mortgage_Qualifier_App/blob/main/images/screenshot1.png)
