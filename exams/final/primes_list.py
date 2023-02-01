def primes_list(N):
    '''
    N: an integer
    '''
    def genPrimes():
        num = 2
        primes = []
        while True:
            yes = True
            for each in primes:
                if num%each == 0:
                    yes = False
            if yes or num == 2:
                yield num
                primes.append(num)
            num += 1
            
    li = []
    geni = genPrimes()
    for num in geni:
        if num <= N:
            li.append(num)
        else:
            break

    return li

print(primes_list(10))