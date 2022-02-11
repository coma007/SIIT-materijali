import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation as li

if __name__ == '__main__':

    A = np.array([[0.7854, 0.7071], [1.9635, 0.9239], [3.1416, 0], [4.3197, -0.9239], [5.4978, -0.7071]])

    plt.scatter(A[:, 0], A[:, 1], c='black')
    p = li.lagrange_interpolation(A[:, 0], A[:, 1])

    x = np.linspace(np.min(A[:, 0]), np.max(A[:, 0]), 100)
    px = np.polyval(p, x)

    plt.plot(x, px, 'r')

    plt.show()
