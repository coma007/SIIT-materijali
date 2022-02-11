import numpy as np
import matplotlib.pyplot as plt
from leastsquares import least_squares_regression

if __name__ == '__main__':

    x = np.array([0.0, 1.23, 2.5, 3.75, 5.0])
    fX = np.array([1.7499, 0.9830, 1.2554, 3.0802, 2.3664])

    plt.scatter(x, fX, color="blue")
    p = least_squares_regression(x, fX, 3)
    print("p = ", np.round(p, 4))

    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX)

    plt.show()
