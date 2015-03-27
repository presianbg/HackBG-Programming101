#!/usr/bin/python3
import os.path


def reduce_file_path(path):
    return os.path.normpath(path)


if __name__ == '__main__':
    path = '/etc//wtf/../'
    print (reduce_file_path(path))
