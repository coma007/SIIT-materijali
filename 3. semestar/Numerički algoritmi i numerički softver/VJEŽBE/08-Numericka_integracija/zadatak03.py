import numpy as np
from integrate_simpson import integrate_simpson
import matplotlib.pyplot as plt

if __name__ == '__main__':

    f = lambda x: x**2
    g = lambda x: np.sqrt(x)

    a = 0
    b = 2

    fg = lambda x: np.abs(f(x) - g(x))

    P = integrate_simpson(fg, a, b, 100, 0)
    print("P = ", np.round(P, 4))
