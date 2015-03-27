#!/usr/bin/python3.4
import sys


def p_score(n):
    s = 0
    c = 0
    l = str(n)
    if l == l[::-1]:
        return 1
    s = n + int(l[::-1])
    l = ( 1 + p_score(s))
    return l





if __name__ == '__main__':
    n=int(sys.argv[1])
    x = 0
    print(p_score(n))
