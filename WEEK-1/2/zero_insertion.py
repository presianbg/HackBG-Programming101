#!/usr/bin/python3
import sys
from digit_to_numb import to_number


def zero_insert(n):
    numbs = [int(x) for x in str(n)]
    digitn = []
    index = 0
    for index in range(0, len(numbs) - 1):
        is_equal_neightbours = numbs[index] == numbs[index+1]
        is_equal_to_ten = (numbs[index] + numbs[index+1]) % 10 == 0
        if is_equal_neightbours or is_equal_to_ten:
            digitn.append(numbs[index])
            digitn.append(0)
        else:
            digitn.append(numbs[index])
    digitn.append(numbs[index+1])
    return (to_number(digitn))

if __name__ == '__main__':
    n = int(sys.argv[1])
    print (zero_insert(n))
