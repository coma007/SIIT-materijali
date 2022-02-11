import numpy as np
import matplotlib.pyplot as plt

def least_squares_regression(x, fX, order):

    n = x.size
    m = min(order + 1, n)
    x = x.T
    fX = fX.T

    A = np.zeros((n, m))
    for it in range(m):
        A[:, it] = x ** it
    a = np.linalg.solve(np.matmul(A.T, A), np.matmul(A.T, fX))
    p = a[::-1]

    return p


if __name__ == '__main__':

    x = np.array([0.0000, 1.2500, 2.5000, 3.7500, 5.0000])
    fX = np.array([1.7499, 0.9830, 1.2554, 3.0802, 2.3664])
    plt.scatter(x, fX, c='black')

    p = least_squares_regression(x, fX, 4)

    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, 'red')
    print("p = ", p)

    plt.show()
