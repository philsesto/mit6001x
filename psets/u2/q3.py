annualInterestRate = 0.2
b = balance = 3329
m = 12
mir = annualInterestRate / 12
epsilon = 0.0005
low = b / m
high = (b * (1 + mir)**m) / m
ans = (high+low)/2

while abs(b-0) >= epsilon:
    m = 12
    b = balance
    while m > 0:
        b -= ans
        b += b*mir
        m -= 1
    if b > 0+epsilon:
        low = ans
    else:
        high = ans
    ans = (high+low)/2
print('Lowest payment: ' + str(round(ans, 2)))