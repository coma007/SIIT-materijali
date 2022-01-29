import numpy as np


def f(x):
    return -(x**4 - 5*x**3 - 2*x**2 + 24*x)


def golden_ratio(a, b, tol):

    c = (3 - np.sqrt(5)) / 2
    x1 = a + c * (b-a)
    x2 = a + b - x1
    it = 1

    while (b-a) > tol:
        it += 1
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + b - x2
        else:
            a = x1
            x1 = x2
            x2 = a + b - x1

    if f(x1) < f(x2):
        return x1, f(x1), it
    else:
        return x2, f(x2), it


if __name__ == '__main__':

    optimum, f_optimum, iterations = golden_ratio(0, 3, 0.0001)
    print(f"x_opt = {optimum}\tf(x_opt) = {f_optimum}\tit = {iterations}")
