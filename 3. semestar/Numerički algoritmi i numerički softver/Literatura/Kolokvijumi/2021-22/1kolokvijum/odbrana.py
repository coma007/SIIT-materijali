import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from NANS_lib import *

if __name__ == '__main__':

    x = np.array([1., 3., 4., 5., 6., 7., 8.])
    fX = np.array([2., 5., 1., -1.5, -3., -0.4, 0.7])

    plt.scatter(x, fX, color="blue")

    p = least_squares_regression(x, fX, 4)
    print(np.round(p, 2))
    x = np.linspace(1, 8, 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, color="red")

    x_sym = sym.Symbol("x")
    f_diff = sym.diff(-0.07 * x_sym**4 + 1.55 * x_sym**3 - 10.98 * x_sym**2 + 28.19 * x_sym**1 - 16.7, x_sym)
    f_diff = sym.lambdify(x_sym, f_diff, 'numpy')
    x_min, _ = zeroFalsePosition(f_diff, 5.3, 5.8)
    x_max, _ = zeroFalsePosition(f_diff, 1, 3)
    plt.scatter(x_min, np.polyval(p, x_min), color="Red")
    plt.scatter(x_max, np.polyval(p, x_max))
    print(x_min)
    print(x_max)

    plt.show()
