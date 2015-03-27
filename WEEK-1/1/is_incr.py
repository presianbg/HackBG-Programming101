#!/usr/bin/python3
import sys

def is_increasing(seq):
    for index in range(0, len(seq) - 1):
        if int(seq[index]) > int(seq[index+1]):
            return False
    return True





if __name__ == '__main__':
    seq = list(sys.argv[1:])
    print (is_increasing(seq))