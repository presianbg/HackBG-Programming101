#!/usr/bin/python3
import sys

def is_hack_number(n):
    bn = bin(n)[2:]
    if bn == bn[::-1] and bn.count('1') % 2 != 0:
        return True

    return False

def next_hack(n):
    if is_hack_number(n):
        return n

    while not is_hack_number(n):
        n += 1

    return n 




if __name__ == '__main__':
    n = int(sys.argv[1])
    print(next_hack(n))