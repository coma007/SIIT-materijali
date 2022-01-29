import numpy as np
import matplotlib.pyplot as plt


def secant(x01, x02, f, df, tol):
    x3 = x02
    x2 = x01
    x1 = np.inf
    it = 0

    while abs(x3 - x2) > tol:
        it += 1
        x1 = x2
        x2 = x3
        x3 = x2 - df(x2)/(df(x2) - df(x1)) * (x2-x1)
    x_opt = x2
    f_opt = f(x_opt)

    return x_opt, f_opt, it


if __name__ == '__main__':

    f = lambda x: -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    df = lambda x: -(4*x**3 - 15*x**2 - 4*x + 24)

    init_guess1 = 0
    init_guess2 = 3
    optimum, f_optimum, iterations = secant(init_guess1, init_guess2, f, df, 0.0001)
    print(f"x_opt = {optimum}\tf(x_opt) = {f_optimum}\tit = {iterations}")

    x = np.linspace(0, 4, 100)
    f = f(x)
    plt.plot(x, f, color="b")
    plt.scatter(optimum, f_optimum, color="red")
    plt.show()
