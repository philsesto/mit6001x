balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
months = 12

def printBalance(balance, months, annualInterestRate, monthlyPaymentRate):
    """
    
    """
    if months == 0:
        print('Remaining balance: ' + str(round(balance, 2)))
    else:
        balance -= (monthlyPaymentRate * balance)
        printBalance(balance+(balance*(annualInterestRate/12)), months-1, annualInterestRate, monthlyPaymentRate)

printBalance(balance, months, annualInterestRate, monthlyPaymentRate)