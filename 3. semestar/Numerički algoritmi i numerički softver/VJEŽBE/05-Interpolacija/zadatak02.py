import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation as li


if __name__ == '__main__':

    x = np.array([1, 2, 4])
    fx = np.array([4, 5, 4])

    p = li.lagrange_interpolation(x, fx)
    plt.scatter(x, fx, c="b")
    x = np.linspace(np.min(x), np.max(x), 100)
    px = np.polyval(p, x)
    px = plt.plot(x, px, 'red')

    print('f(3) = ', np.polyval(p, 3))
    plt.scatter(3, np.polyval(p, 3), c='g')

    plt.show()
