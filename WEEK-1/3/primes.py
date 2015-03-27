#!/usr/bin/python3
import sys


def is_prime(n):
    n = abs(n)
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True



if __name__ == '__main__':
    n = int(sys.argv[1])
    print(is_prime(n))
