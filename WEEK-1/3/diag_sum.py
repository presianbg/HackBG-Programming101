#!/usr/bin/python3


def diag1(matrix):
    dl = 0
    dimention = len(matrix)
    for index in range(dimention):
        dl += matrix[index][dimention - (index + 1)]
    return dl

if __name__ == '__main__':
    matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
    print(diag1(matrix))
