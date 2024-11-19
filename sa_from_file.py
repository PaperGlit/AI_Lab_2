import numpy as np

def sa_from_file():
    # Load the array from file
    loaded_array = np.loadtxt("sa.csv", delimiter=",", dtype=float)
    return loaded_array
