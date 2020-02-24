# A program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

"""
Created on Thu Oct 24 05:49:53 2019

@author: Omama Elrefaei
"""

def credit_card_balance(balance, annualInterestRate, monthlyPaymentRate):
    
    """
    Returns: Remaining balance.
    balance: the outstanding balance on the credit card.
    
    annualInterestRate: annual interest rate as a decimal.

    monthlyPaymentRate - minimum monthly payment rate as a decimal.
    """
    
    Year = 12
    
    for i in range(Year):
    
        Monthly_interest_rate = (annualInterestRate) / 12.0
    
        Minimum_monthly_payment = (monthlyPaymentRate)* (balance)
    
        Monthly_unpaid_balance = (balance) - (Minimum_monthly_payment)
    
        Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
    
        balance = Updated_balance_each_month

    return str("Remaining balance: " + str(round(balance,2)))