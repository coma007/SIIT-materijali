import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation as li

if __name__ == '__main__':

    a = -np.pi
    b = np.pi
    f = lambda x: x**2 * np.sin(x)

    x = np.linspace(a, b, 100)
    fx = f(x)
    plt.plot(x, fx, color="blue")

    points = np.array([a, -3, -2, 2, 3, b])
    f_points = f(points)
    plt.scatter(points, f_points, c="g")

    p = li.lagrange_interpolation(points, f_points)
    print(np.round(p, 4))

    pX = np.polyval(p, x)
    plt.plot(x, pX, c="r")

    plt.show()
