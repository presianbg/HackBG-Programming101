#!/usr/bin/python3
import sys
from contains_digit import contains_digit


def contains_digits(number, digits):
    for d in digits:
        if not contains_digit(number, d):
            return False
    return True


if __name__ == '__main__':
    number = int(sys.argv[1])
    digits = list(sys.argv[2:])
    print(contains_digits(number, digits))
