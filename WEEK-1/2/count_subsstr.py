#!/usr/bin/python3
import sys


def count_substrings(haystack, needle):
    nstack = ""
    cs = 0
    for ch in haystack:
        nstack += ch
        if needle in nstack:
            cs += 1
            nstack = ""
    return cs

if __name__ == '__main__':
    haystack = str(sys.argv[1])
    needle = str(sys.argv[2])
    print(count_substrings(haystack, needle))
