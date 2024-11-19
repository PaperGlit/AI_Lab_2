import os

def array_from_file(filename):
    if not os.path.exists(filename + ".txt"):
        print("Error: no values have been saved yet!")
        return []
    with open(filename + ".txt", "r") as f:
        array = f.readline().split()

    for i in range(len(array)):
        array[i] = float(array[i])
        array[i] = round(array[i], 1)
    return array