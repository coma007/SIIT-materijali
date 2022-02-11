import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation as li
import zero_false_position as zfp


if __name__ == '__main__':

    x = np.array([1, 4, 5])
    y = np.array([1, 3, 3])

    plt.scatter(x, y, color="black")
    p = li.lagrange_interpolation(x, y)
    x = np.linspace(np.min(x), np.max(x))
    px = np.polyval(p, x)
    plt.plot(x, px, "red")

    fX_new = 2
    h = lambda x: np.polyval(p, x) - fX_new

    x_new, it = zfp.zero_false_position(h, np.min(x), np.max(x))
    print("x1 = ", x_new)
    plt.scatter(x_new, fX_new, c="g")

    plt.show()
