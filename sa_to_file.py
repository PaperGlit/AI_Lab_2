import numpy as np

def sa_to_file(sa):
    np.savetxt("sa.csv", sa, delimiter=",", fmt="%.2f")
