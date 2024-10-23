import random


def create_array(col):
    array = []
    values = [round(0.1 * i, 1) for i in range(1, 10)]
    for i in range(col):
        array.append(random.choice(values))
    return array