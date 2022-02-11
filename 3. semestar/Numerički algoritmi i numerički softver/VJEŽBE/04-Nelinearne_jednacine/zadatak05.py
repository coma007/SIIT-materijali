import numpy as np
import matplotlib.pyplot as plt
import zero_false_position

if __name__ == '__main__':

    a = -2
    b = 2

    f = lambda x: x**2 - 2
    g = lambda x: - x**2 + 2

    x = np.linspace(a, b, 100)
    fX = f(x)
    gX = g(x)

    plt.plot(x, fX, 'blue', x, gX, 'red')

    f_diff = lambda x: f(x) - g(x)

    intersection1, it1 = zero_false_position.zero_false_position(f_diff, a, 0, 10e-5, 100, 0)
    intersection2, it2 = zero_false_position.zero_false_position(f_diff, 0, b, 10e-5, 100, 0)
    print("x1 = ", intersection1)
    print("x2 = ", intersection2)
    f_intersection1 = f(intersection1)
    f_intersection2 = f(intersection2)

    plt.scatter(intersection1, f_intersection1, color='green')
    plt.scatter(intersection2, f_intersection2, color='green')
    plt.show()
