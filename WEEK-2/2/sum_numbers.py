#!/usr/bin/python3
import sys
import os.path


def sum_numbers(f_name):
    result = 0
    with open(f_name, "r") as f:
        data = f.read()
        for num in range(len(data.split(' '))-1):
            result += int(data.split(' ')[num])
    return result


if __name__ == '__main__':
    f_name = os.path.normpath(sys.argv[1])
    print(sum_numbers(f_name))
