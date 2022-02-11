import numpy as np
import matplotlib.pyplot as plt
from leastsquares import least_squares_regression
from zero_false_position import zero_false_position

if __name__ == '__main__':

    x = np.array([0, 1, 2, 3, 4, 5])
    fX = np.array([5, 3, 5, 1, 3, 5])

    plt.scatter(x, fX, c="y")

    p = least_squares_regression(x, fX, 5)
    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)

    plt.plot(x, pX, c="g")

    p_diff = np.polyder(p) # vraca izvod
    h = lambda x: np.polyval(p_diff, x)

    x_min, _ = zero_false_position(h, 3, 4)
    x_max, _ = zero_false_position(h, 4, 5)

    print("x_min = ", np.round(x_min, 4))
    print("x_max = ", np.round(x_max, 4))

    plt.scatter(x_min, np.polyval(p, x_min), c="b")
    plt.scatter(x_max, np.polyval(p, x_max), c="b")

    plt.show()
