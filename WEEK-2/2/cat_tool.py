#!/usr/bin/python3
import sys
import os.path


def cat(f_name):
    with open(f_name, "r") as f:
        data = f.read()
        return data


if __name__ == '__main__':
    f_name = os.path.normpath(sys.argv[1])
    print (cat(f_name))
