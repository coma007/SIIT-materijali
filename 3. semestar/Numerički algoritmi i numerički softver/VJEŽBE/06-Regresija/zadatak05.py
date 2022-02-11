import numpy as np
import matplotlib.pyplot as plt
from leastsquares import least_squares_regression
from zero_false_position import zero_false_position

if __name__ == '__main__':

    f = lambda x: x**3 * np.cos(x)

    a = - np.pi / 2
    b = 5 * np.pi / 9

    x = np.linspace(a, b, 100)
    fX = f(x)
    plt.plot(x, fX, c="r")

    p = least_squares_regression(x, fX, 5)
    pX = np.polyval(p, x)
    plt.plot(x, pX, c="b")

    val = - 0.5
    h = lambda x: np.polyval(p, x) - val
    x1, _ = zero_false_position(h, -1.5, -1)
    x2, _ = zero_false_position(h, -1, -0.5)
    x3, _ = zero_false_position(h, 1.5, 2)
    plt.scatter(x1, np.polyval(p, x1), c="brown")
    plt.scatter(x2, np.polyval(p, x2), c="brown")
    plt.scatter(x3, np.polyval(p, x3), c="brown")
    print("x1 = ", x1)
    print("x2 = ", x2)
    print("x3 = ", x3)

    plt.show()
