annualInterestRate = 0.2
b = balance = 3329
guess = increment = epsilon = 10

while b > 0+epsilon:
    m = 12
    b = balance
    while m > 0:
        b -= guess
        b += b*(annualInterestRate/12)
        m -= 1
    if b > 0+epsilon:
        guess += increment
print('Lowest payment: ' + str(guess))