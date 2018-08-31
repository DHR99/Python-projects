from itertools import chain
from collections import Counter

def primeFactors(n):
    primes = []
    res = ''
    
    for i in chain([2],range(3,n+1,2)):
        s = 0
        while n%i == 0: 
            n /= i
            s += 1
        primes.extend([i]*s) 
        if n==1:
            countings = Counter(primes)
            for i in countings:
                res += '('+str(i)+'**'+str(countings[i])+')'
            return res
