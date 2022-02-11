
import numpy as np
def ddf(h):
    arr = np.array([1, -2, 1])
    fX = arr/(h**2)
    return fX