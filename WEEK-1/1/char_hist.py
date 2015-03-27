#!/usr/bin/python3.4
import sys


def char_histogram(sttt):
    print (sttt)
    d = {}
    for i in sttt:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print (d)
    return d




if __name__ == '__main__':
    sttt = str(sys.argv[1])
    char_histogram(sttt)