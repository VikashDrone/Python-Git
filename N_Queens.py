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
    for x in range(16):
        if matrix[x][col] == 1:
            count = count + 1
    return count


def not_in_diagonal(matrix, row, col):
    return np.sum(arr.diagonal(col - row)) + np.sum(np.fliplr(arr).diagonal(abs((col - 15)) - row))


def sum_matrix(matrix):
    sm = 0
    for i in range(16):
        for j in range(16):
            sm = sm + matrix[i][j]
    return sm


def generate_matrix(arr_tb, i, j, l_i, l_j, depth):
    print("Depth : "+str(depth))
    print(arr_tb)
    print("-----------------")
    if sum_matrix(arr_tb) == 16:
        return arr_tb

    for i in range(16):
        for j in range(16):
            if (not_in_row(arr_tb, i) + not_in_column(arr_tb, j) + not_in_diagonal(arr_tb, i, j)) == 0:
                arr[i][j] = 1
                arr_tb = generate_matrix(arr_tb, i + 1, 0, i, j, depth + 1)
        if arr_tb[i].sum() == 0:
            arr_tb[l_i, l_j] = 0
            return arr_tb
    return arr_tb


arr = np.zeros((16, 16))
init_j = random.randint(0, 15)
arr[0][init_j] = 1
arr = generate_matrix(arr, 1, 0, 0, init_j, 0)
print(arr)
