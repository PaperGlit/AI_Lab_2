def array_to_file(array, filename):
    with open(filename+ ".txt", "w") as f:
        for i in array:
            f.write(str(i) + " ")