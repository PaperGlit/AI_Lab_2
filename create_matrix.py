from create_array import create_array


def create_matrix(row, col):
    matrix = []
    for i in range(row):
        matrix.append(create_array(col))
    return matrix