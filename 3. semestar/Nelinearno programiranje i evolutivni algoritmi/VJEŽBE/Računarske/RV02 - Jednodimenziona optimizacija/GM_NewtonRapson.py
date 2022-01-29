import numpy as np
import matplotlib.pyplot as plt


def newton_rapson(x0, f, df, ddf, tol):
    x2 = x0
    x1 = np.inf
    it = 0

    while abs(x2 - x1) > tol:
        it += 1
        x1 = x2
        x2 = x1 - df(x1)/ddf(x1)
    x_opt = x2
    f_opt = f(x_opt)

    return x_opt, f_opt, it


if __name__ == '__main__':

    f = lambda x: -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    df = lambda x: -(4*x**3 - 15*x**2 - 4*x + 24)
    ddf = lambda x: -(12*x**2 - 30*x - 4)

    init_guess = 1
    optimum, f_optimum, iterations = newton_rapson(init_guess, f, df, ddf, 0.00001)
    print(f"x_opt = {optimum}\tf(x_opt) = {f_optimum}\tit = {iterations}")

    x = np.linspace(0, 4, 100)
    f = f(x)
    plt.plot(x, f, color="b")
    plt.scatter(optimum, f_optimum, color="red")
    plt.show()


