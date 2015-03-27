#!/usr/bin/python3.4
import sys
import math


def to_number(digits):
    print (digits)
    n = 0
    for i in digits:
        l = int(i)
        n = n*(10**(int(math.log10(l))+1)) + l
    return n

if __name__ == '__main__':
    digits = list(sys.argv[1:])
    print(to_number(digits))
