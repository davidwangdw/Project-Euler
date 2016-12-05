import math

def primes_sieve(n):
    p_n = int(2 * n * math.log(n))     
    sieve = [True] * p_n                 # everything is prime to start
    count = 0

primes_sieve(10001)

for i in range(2, p_n):
    if sieve[i]:                       # still prime?
        count += 1                     # count it!
        if count == n:                 # done!
            print(i)
        for j in range(2*i, p_n, i):   # cross off all multiples of i
            sieve[j] = False

