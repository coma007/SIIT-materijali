import numpy as np
def normalize(in_vector):
    magnitude = np.norm(in_vector)
    if magnitude == np.Infinity or magnitude <= 0:
        out = [1, 0]
    else:
        out = in_vector/magnitude
    return out

