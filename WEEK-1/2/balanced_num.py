#!/usr/bin/python3
import sys


def is_number_balanced(n):
    numbs = [int(x) for x in str(n)]
    hnum = len(numbs)//2
    if len(numbs) % 2 == 0:
        return sum(numbs[:hnum]) == sum(numbs[hnum:])
    else:
        return sum(numbs[:hnum]) == sum(numbs[hnum+1:])

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(is_number_balanced(n))
