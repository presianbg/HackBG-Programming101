#!/usr/bin/python3.4
import sys


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_digits(n):
    return [int(x) for x in str(n)]


def to_number(digits):
    print (digits)
    n = 0
    for i in digits:
        dc = count_digits(i)
        n = n*(10**dc) + i
    return n

if __name__ == '__main__':
    digits = [int(x) for x in sys.argv[1:]]
    print(to_number(digits))
