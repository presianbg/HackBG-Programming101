#!/usr/bin/python3
import sys
import os.path
from cat_tool import cat


def cat_multiple(f_name):
    for f in f_name:
        print (cat(os.path.normpath(f)))


if __name__ == '__main__':
    f_name = sys.argv[1:]
    cat_multiple(f_name)
