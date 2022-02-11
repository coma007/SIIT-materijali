import numpy as np
import matplotlib.pyplot as plt
from leastsquares import least_squares_regression
from zero_false_position import zero_false_position

if __name__ == '__main__':

    f = lambda x: x**2 * np.sin(x)
    a = - np.pi
    b = + np.pi

    x = np.linspace(a, b, 100)
    fX = f(x)
    plt.plot(x, fX)

    p = least_squares_regression(x, fX, 3)
    print("p = ", p)
    pX = np.polyval(p, x)
    plt.plot(x, pX, c="r")

    h = lambda x: f(x) - np.polyval(p, x)
    c = -1/2
    d = +1/2
    intersection, _ = zero_false_position(h, c, d)
    print("x1 = ", np.round(intersection, 4))
    plt.scatter(intersection, f(intersection), c="g")

    plt.show()
