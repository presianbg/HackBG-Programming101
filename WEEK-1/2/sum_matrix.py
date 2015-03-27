#!/usr/bin/python3


def sum_matrix(matrix):
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)
    return total_sum


if __name__ == '__main__':
    m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print(sum_matrix(m))
