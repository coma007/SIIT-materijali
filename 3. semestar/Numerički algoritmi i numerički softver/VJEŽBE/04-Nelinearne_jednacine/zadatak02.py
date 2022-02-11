import numpy as np
import matplotlib.pyplot as plt
import zero_secant

if __name__ == '__main__':

    a = np.pi / 3
    b = np.pi * 4 / 3

    f = lambda x: np.cos(x)

    x = np.linspace(a, b, 100)
    fX = f(x)

    plt.plot(x, fX, 'blue')
    plt.plot([a, b], [0, 0], 'black')

    zero, it = zero_secant.zero_secant(f, 1, 2, 10e-5, 100, 0)
    print("x = ", zero)
    f_zero = f(zero)

    plt.scatter(zero, f_zero, color='red')
    plt.show()
