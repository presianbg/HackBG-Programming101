#!/usr/bin/python3


def groupby(func, seq):
    d = {}
    for i in seq:
        if func(i) in d:
            d[func(i)].append(i)
        else:
            d[func(i)] = []
    print (d)

if __name__ == '__main__':
    func = lambda x: x % 2
    seq = [1, 2, 3, 5, 8, 9, 10, 12]
    groupby(func, seq)
