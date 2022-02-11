import numpy as np
from nans_lib_1 import *
import matplotlib.pyplot as plt
import sympy as sym

if __name__ == '__main__':
    # a
    f = lambda x: x * np.cos(2 * x) - 2
    a = -5 * np.pi / 3
    b = 3 * np.pi / 4

    x = np.linspace(a, b, 100)
    fX = f(x)
    plt.plot(x, fX, 'blue')
    plt.plot([a, b], [0, 0], 'black')

    # b
    zero, it = zeroSecant(f, -4.5, -3.5)
    print("x = ", zero)
    f_zero = f(zero)
    plt.scatter(zero, f(zero), c='r')

    # c
    x_sym = sym.Symbol('x')
    df_sym = sym.diff(x_sym * sym.cos(2 * x_sym) - 2)
    df = sym.lambdify(x_sym, df_sym, 'numpy')

    min, it = zeroSecant(df, -4, -3)
    print('x_min = ', min)
    f_min = f(min)
    plt.scatter(min, f_min, c='orange')

    max, it = zeroSecant(df, -5, -4.5)
    print('x_max = ', max)
    f_max = f(max)
    plt.scatter(max, f_max, c='black')

    # d
    g = lambda x: -np.sin(x) * np.exp(x) - 2
    gX = g(x)
    plt.plot(x, gX, 'green')

    h = lambda x: f(x) - g(x)
    p1, _ = zeroFalsePosition(h, -4.5, -3.5)
    print('p1 = ', p1)
    plt.scatter(p1, f(p1), c='grey')
    p2, _ = zeroFalsePosition(h, -1.5, -0.5)
    print('p2 = ', p1)
    plt.scatter(p2, f(p2), c='grey')
    p3, _ = zeroFalsePosition(h, -0.5, 0.5)
    print('p3 = ', p3)
    plt.scatter(p3, f(p3), c='grey')

    plt.show()
