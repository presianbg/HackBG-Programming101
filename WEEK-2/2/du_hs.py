#!/usr/bin/python3
import sys
import os
import humanfriendly


def du_hs(dir_name):
    dsize = 0
    for root, dirs, files in os.walk(dir_name):
        for fn in files:
            try:
                path = os.path.join(root, fn)
                dsize += os.path.getsize(path)
            except FileNotFoundError as error:
                print(error)
    return humanfriendly.format_size(dsize)


if __name__ == '__main__':
    dir_name = os.path.normpath(sys.argv[1])
    print("%s size is %s" % (dir_name, du_hs(dir_name)))
