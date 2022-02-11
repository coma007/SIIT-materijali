import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import zero_false_position

if __name__ == '__main__':

    a = 0
    b = 2 * np.pi

    f = lambda x: np.sin(2*x) - x

    x = np.linspace(a, b, 100)
    fX = f(x)
    plt.plot(x, fX, 'blue')

    x_sym = sym.Symbol('x')
    df_sym = sym.diff(sym.sin(2 * x_sym) - x_sym)
    df = sym.lambdify(x_sym, df_sym, 'numpy')

    maxi, it1 = zero_false_position.zero_false_position(df, a, np.pi/2)
    mini, it2 = zero_false_position.zero_false_position(df, np.pi*3/2, b)
    print("max = ", maxi)
    print("min = ", mini)
    f_max = f(maxi)
    f_min = f(mini)

    plt.scatter(maxi, f_max, color='green')
    plt.scatter(mini, f_min, color='green')

    plt.show()
