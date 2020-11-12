"""
Se dă un număr n. Să se tipărească al n-lea număr de forma 2 i 3 j 5 k 
{\displaystyle 2^{i}3^{j}5^{k}} {\displaystyle 2^{i}3^{j}5^{k}}, cu i, j, k ≥ 0. 
De exemplu, primele 10 numere sunt 1, 2, 3, 4, 5, 6, 8, 9, 10, 12.
"""

# check if x can be writen with primes 2 3 and 5
def decomposeInPrimes(x):
    primes = {}
    d = 2
    while x > 1:
        while x % d == 0:
            if d in primes:
                primes[d] += 1
            else:
                primes[d] = 1
            x = x // d
        d += 1
    return primes


def isValid(x):
    res = decomposeInPrimes(x)
    for prime in res:
        if prime not in [2,3,5]:
            return False
    return True

def check(n):
    start = 1
    while n > 1:
        start += 1
        if isValid(start):
            n -= 1
    return start

def test():
    res = check(10)
    assert (res == 12)

test()

