#!/usr/bin/python3
import sys
from sum_divisors import divisors
from primes import is_prime


def prime_number_of_divisors(n):
    return is_prime(len(divisors(n)))



if __name__ == '__main__':
    n = int(sys.argv[1])
    print(prime_number_of_divisors(n))
