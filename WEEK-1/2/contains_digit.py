#!/usr/bin/python3
import sys


def contains_digit(number, digit):
    return str(digit) in str(number)


if __name__ == '__main__':
    number = int(sys.argv[1])
    digit = int(sys.argv[2])
    print(contains_digit(number, digit))
