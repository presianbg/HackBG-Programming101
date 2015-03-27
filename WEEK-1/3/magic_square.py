#!/usr/bin/python3


def diag2(matrix):
    dl = 0
    dimention = len(matrix)
    for index in range(dimention):
        dl += matrix[index][dimention - (index + 1)]
    return dl


def diag1(matrix):
    dl = 0
    dimention = len(matrix)
    for index in range(dimention):
        dl += matrix[index][index]
    return dl


def row_sum(matrix):
    sumrow = 0
    for row in matrix:
        sumrow += sum(row)
    return sumrow // len(matrix)


def col_sum(matrix):
    sumcol = 0
    dimention = len(matrix)
    for row_index in range(dimention):
        for col_index in range(dimention):
            sumcol += matrix[col_index][row_index]
    return sumcol // dimention


def magic_square(matrix):
    if row_sum(matrix) == col_sum(matrix) == diag1(matrix) == diag2(matrix):
        return True
    else:
        return False


if __name__ == '__main__':
    matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
    print((magic_square(matrix)))
