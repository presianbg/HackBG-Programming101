#!/usr/bin/python3


def nan_expand(times):
    nan_str = ""
    if times == 0:
        return nan_str
    nan_str = "Not a " * times + "NaN"
    return nan_str

if __name__ == '__main__':
    times = 9
    print(nan_expand(times))
