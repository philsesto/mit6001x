def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    tmp = 0
    while b**(tmp+1) <= x:
        tmp += 1
    return tmp

print(myLog(4500600, 3))