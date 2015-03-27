#!/usr/bin/python3


def iterations_of_nan_expand(expanded):

    if expanded.count('Not a') == 0 and expanded != '':
        return False
    return expanded.count('Not a')


if __name__ == '__main__':
    expanded = ''
    print(iterations_of_nan_expand(expanded))
