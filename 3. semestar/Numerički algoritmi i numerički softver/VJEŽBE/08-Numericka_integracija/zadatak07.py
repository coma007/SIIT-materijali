import numpy as np
from integrate_simpson import integrate_simpson

if __name__ == '__main__':

    f = lambda x: x**2 + 2
    f_1 = lambda y: np.sqrt(y - 2)

    a = 0
    b = 4
    y1 = f(a)
    y2 = f(b)

    f_sqr = lambda x: f_1(x) ** 2
    V1 = np.pi * integrate_simpson(f_sqr, y1, y2, 100, 0)
    V2 = (b - a) ** 2 * np.pi * (y2 - 0)
    V = V2 - V1

    print("V = ", np.round(V, 4))
