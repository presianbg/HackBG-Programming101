#!/usr/bin/python3.4
import sys
import math

n=int(sys.argv[1])
def to_digits(n):
    ln = [int(i) for i in str(n)]
    print (ln)
    return ln


if __name__ == '__main__':
    to_digits(n)


