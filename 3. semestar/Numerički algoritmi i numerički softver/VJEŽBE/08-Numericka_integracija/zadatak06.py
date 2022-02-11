import numpy as np
from integrate_simpson import integrate_simpson

if __name__ == '__main__':

    f = lambda x: x**2 + 2
    f_1 = lambda y: np.sqrt(y-2)

    y1 = 2
    y2 = 4

    P = integrate_simpson(f_1, y1, y2, 100, 0)
    print("P = ", np.round(P, 4))

