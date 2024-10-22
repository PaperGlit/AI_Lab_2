from find_u import find_u


def create_array_u(letter, matrix):
    array = []
    for i in range(len(matrix)):
        array.append(find_u(letter, matrix[i]))
    return array