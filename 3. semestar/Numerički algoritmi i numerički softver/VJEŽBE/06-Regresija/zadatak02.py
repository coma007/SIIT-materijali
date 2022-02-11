import numpy as np
import matplotlib.pyplot as plt
from leastsquares import least_squares_regression

if __name__ == '__main__':

    x = np.array([1, 2, 3, 5, 6])
    y = np.array([2, 4, 4, 1, 3])
    plt.scatter(x, y, c="b")

    p = least_squares_regression(x, y, 3)
    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)

    print("p = ", np.round(p, 4))
    plt.plot(x, pX)

    x_new = 4
    y_new = np.polyval(p, x_new)
    print("x = ", x_new, "y = ", np.round(y_new, 4))

    plt.show()
