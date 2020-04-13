import random


def not_in_row(matrix, row, col):
    count = 0
    for x in matrix[row]:
        if matrix[row][col] == x:
            count = count + 1
    return count


def not_in_column(matrix, row, col):
    count = 0
    for x in range(3):
        if matrix[x][col] == matrix[row][col]:
            count = count + 1
    return count


def not_in_matrix(matrix, row, col):
    count = 0
    for x in range(3):
        for y in matrix[x]:
            if y == matrix[row][col]:
                count = count + 1
    return count


# assign the matrix
def assign_matrix(arr_tb):
    for a_i in range(3):
        arr_row = []
        for a_j in range(3):
            arr_row.append(random.randint(1, 9))
        arr_tb[a_i - 1] = arr_row
    return arr_tb


# validate matrix positions
def validate_matrix(arr_tb, i, j, depth):
    depth = depth + 1
    if depth > 3:
        return arr_tb
    print("Depth = "+str(depth))
    if (i + j) == 0:
        arr_tb = assign_matrix(arr_tb)
        print(arr_tb)
    if (i + j) > 0:
        arr_tb[i][j] = random.randint(1, 9)
    for i in range(3):
        for j in range(3):
            print(str(arr_tb[i][j]) + " : " + str(
                not_in_row(arr_tb, i, j) + not_in_column(arr_tb, i, j) + not_in_matrix(arr_tb, i, j)) + str(" i : ") + str(i) + str(" j : ") + str(j))
            if (not_in_row(arr_tb, i, j) + not_in_column(arr_tb, i, j) + not_in_matrix(arr_tb, i, j)) > 3:
                arr_tb = validate_matrix(arr_tb, i, j, depth)
    return arr_tb


# create matrix
rows, cols = (3, 3)
arr = [[0] * cols] * rows
print(arr)

arr = validate_matrix(arr, 0, 0, 0)
print(arr)
