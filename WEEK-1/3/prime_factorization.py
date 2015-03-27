#!/usr/bin/python3
from primes import is_prime


def prime_factorization(n):
    pf = []
    d = 2
    c = 0
    while not n % d == 0:
        d += 1
    while n % d == 0:
        c += 1
        n //= d
        if n % d != 0:
            pf.append((d, c))
            c = 0
            for i in range(d, n+1):
                if is_prime(i) and n % i == 0:
                    d = i
                    break
    return pf

if __name__ == '__main__':
    n = 209
    print(prime_factorization(n))
