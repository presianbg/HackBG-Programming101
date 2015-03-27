#!/usr/bin/python3
from random import randint
import sys
import os.path


def generate_numbers(f_name, n):
    with open(f_name, "w") as f:
        for i in range(n):
            f.write('%s ' % randint(1, 10))


if __name__ == '__main__':
    f_name = os.path.normpath(sys.argv[1])
    n = int(sys.argv[2])
    generate_numbers(f_name, n)
