#############################
## id 112
## Puzzle Elo 1353
## Correctly solved 41 %
#############################


def matrix_find(matrix, value):
    if not matrix or not matrix[0]:
        return False

    j = len(matrix) - 1
    for row in matrix:
        while row[j] > value:
            j = j - 1
            if j == -1:
                return False
        if row[j] == value:
            return True
    return False

matrix = [[3, 4, 4, 6],
          [6, 8, 11, 12],
          [6, 8, 11, 15],
          [9, 11, 12, 17]]
print(matrix_find(matrix=matrix, value=11))
