#!/usr/bin/python3


def max_consecutive(items):
    c = 1
    mc = 0
    for index in range(len(items) - 1):
        if items[index] == items[index+1]:
            c += 1
        elif c > mc:
            mc = c
            c = 1
    return mc


if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]
    print(max_consecutive(items))
