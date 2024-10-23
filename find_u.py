def find_u(letter, array):
    s = 0
    for i in range(len(array)):
        s += letter[i] * array[i]
    return round(s, 1)