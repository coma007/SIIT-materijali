import numpy as np
from nans_lib_1 import gauss


def row(x, y):
    return np.array([x, -x * y, x ** 3, -4 * y])


if __name__ == '__main__':
    A = np.array([row(1, 2), row(3, 3), row(4, 3), row(2, 1)])
    b = np.array([11.5, 7.8, 9.9, 5])

    print(np.round(gauss(A, b), 3))
