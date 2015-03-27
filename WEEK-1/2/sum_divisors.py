#!/usr/bin/python3
import sys


def divisors(x):
    nd = []
    for i in range(x):
        if x % int(i+1) == 0:
            nd.append(i+1)
    return nd

def sum_of_divisors(n):
    return (sum(divisors(n)))




if __name__ == '__main__':
    n = int(sys.argv[1])
    print(sum_of_divisors(n))
