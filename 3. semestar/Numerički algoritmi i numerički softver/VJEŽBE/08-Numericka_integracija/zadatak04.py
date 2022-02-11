import numpy as np
from integrate_simpson import integrate_simpson

if __name__ == '__main__':

    f = lambda x: np.exp(2**x) / x
    a = 1
    b = 2

    f_sqr = lambda x: f(x) ** 2

    V = np.pi * integrate_simpson(f_sqr, a, b, 100, 0)
    print("V = ", np.round(V, 4))
