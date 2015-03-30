#!/usr/bin/python3.4
import sys


def fact_digits(n):
    s = 0
    if n == 0:
        print (1)
        return 1
    else:
        n = abs(n)
        while n:
            f = 1
            z = n % 10
            for i in range(z):
                f = f * (i + 1)
            s += f
            n //= 10
        print (s)
        return s

if __name__ == '__main__':
    n = int(sys.argv[1])
    fact_digits(n)
