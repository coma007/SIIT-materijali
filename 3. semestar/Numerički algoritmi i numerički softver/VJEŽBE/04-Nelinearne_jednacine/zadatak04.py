import numpy as np
import matplotlib.pyplot as plt
import zero_false_position

if __name__ == '__main__':

    a = 0
    b = 2

    f = lambda x: x**2 - x + 3
    g = lambda x: np.exp(x)

    x = np.linspace(a, b, 100)
    fX = f(x)
    gX = g(x)

    plt.plot(x, fX, 'blue', x, gX, 'red')

    f_diff = lambda x: f(x) - g(x)

    intersection, it = zero_false_position.zero_false_position(f_diff, a, b, 10e-5, 100, 0)
    print("x = ", intersection)
    f_intersection = f(intersection)

    plt.scatter(intersection, f_intersection, color='green')
    plt.show()
