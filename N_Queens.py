import random
import numpy as np


def not_in_row(matrix, row):
    count = 0
    for x in matrix[row]:
        if x == 1:
            count = count + 1
    return count


def not_in_column(matrix, col):
    count = 0
    for x in range(8):
        if matrix[x][col] == 1:
            count = count + 1
    return count


def not_in_diagonal(matrix, row, col):
    return np.sum(arr.diagonal(col - row)) + np.sum(np.fliplr(arr).diagonal(abs((col - 7)) - row))


def sum_matrix(matrix):
    sm = 0
    for i in range(8):
        for j in range(8):
            sm = sm + matrix[i][j]
    return sm


def generate_matrix(arr_tb, depth):
    print("Depth : " + str(depth))

    print(arr_tb)
    if sum_matrix(arr_tb) == 8:
        return arr_tb

    i = random.randint(0, 7)
    j = random.randint(0, 7)
    if (not_in_row(arr_tb, i) + not_in_column(arr_tb, j) + not_in_diagonal(arr_tb, i, j)) == 0:
        arr[i][j] = 1
        generate_matrix(arr_tb, depth + 1)
    else:
        generate_matrix(arr_tb, depth + 1)
    return arr_tb


arr = np.zeros((8, 8))
arr = generate_matrix(arr, 0)
