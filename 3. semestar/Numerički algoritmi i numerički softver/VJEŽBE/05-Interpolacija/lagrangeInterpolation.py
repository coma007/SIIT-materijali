import numpy as np

def lagrange_interpolation(x, fX):
    order = x.size

    p = 0

    for itFX in range(order):
        lNumer = 1
        lDenom = 1

        for itX in range(itFX):
            lNumer = np.convolve(lNumer, np.array([1, -x[itX]]))
            lDenom = lDenom * (x[itFX] - x[itX])
        
        for itX in range(itFX+1, order):
            lNumer = np.convolve(lNumer, np.array([1, -x[itX]]))
            lDenom = lDenom*(x[itFX] - x[itX])

        p = p + lNumer/lDenom*fX[itFX]

    return p