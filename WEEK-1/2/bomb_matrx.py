#!/usr/bin/python3
from sum_matrix import sum_matrix
from find_neighbours import find_neighbors
import copy


def reduce_neigbours(matrix, neighbours, bomb_charge):
    matrix_bomb = copy.deepcopy(matrix)
    for n in neighbours:
        if matrix_bomb[n[0]][n[1]] - bomb_charge < 0:
            matrix_bomb[n[0]][n[1]] = 0
        else:
            matrix_bomb[n[0]][n[1]] = matrix_bomb[n[0]][n[1]] - bomb_charge
    return matrix_bomb


def matrix_bombing_plan(matrix):
    matrix_bombed = []
    matrix_boom_dmg = {}
    print ("Original Matrix and Sum = %d" % sum_matrix(m))
    for row in matrix:
        print (row)
    print ("----------------")

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            xy = (row, col)
            print ("Bomba X-Y", xy)
            bomb_charge = matrix[row][col]
            print ("BombCHarge %d" % bomb_charge)
            # Find the bomb's neighbours:
            neighbours = (find_neighbors(row, col, len(matrix) - 1, len(matrix[0]) - 1))
            # Create New Matrix After DA BOOM:
            matrix_bombed = reduce_neigbours(matrix, neighbours, bomb_charge)
            print ("Sum of matrix after bombing = %d" % sum_matrix(matrix_bombed))
            for row1 in matrix_bombed:
                print (row1)
            print ("----------------")
            matrix_boom_dmg[xy] = sum_matrix(matrix_bombed)  # Sumata na matricata + X-Y na bombata

    for k in matrix_boom_dmg:
        print (k, matrix_boom_dmg[k])


if __name__ == '__main__':
    m = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]]
    matrix_bombing_plan(m)
