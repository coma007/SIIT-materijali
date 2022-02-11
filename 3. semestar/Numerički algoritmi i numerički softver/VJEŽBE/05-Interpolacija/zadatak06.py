import numpy as np
import lagrangeInterpolation as li


if __name__ == '__main__':

    x = np.array([0.1, 0.3, 0.6, 1.2])
    y = np.array([1.023, 1.261, 2.368, 9.064])

    p = li.lagrange_interpolation(x, y)
    print(p[::-1])
