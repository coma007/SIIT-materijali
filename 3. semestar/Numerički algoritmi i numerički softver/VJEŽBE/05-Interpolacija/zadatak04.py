import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation as li
import zero_false_position as zfp

if __name__ == '__main__':

    x = np.array([1, 3, 5])
    y = np.array([0, 3, 0])

    plt.scatter(x, y, color="black")

    p = li.lagrange_interpolation(x, y)
    x = np.linspace(np.min(x), np.max(x), 100)
    px = np.polyval(p, x)
    plt.plot(x, px, color="red")

    f = lambda x: 1
    fx = f(x)
    plt.plot([np.min(x), np.max(x)], [f(np.min(x)), f(np.max(x))])

    h_inter = lambda x: np.polyval(p, x) - f(x)
    inter1, it1 = zfp.zero_false_position(h_inter, 1, 2)
    print('x1 = ', inter1)
    f_inter1 = f(inter1)
    plt.scatter(inter1, f_inter1, color="green")
    inter2, it2 = zfp.zero_false_position(h_inter, 4, 5)
    print('x2 = ', inter2)
    f_inter2 = f(inter2)
    plt.scatter(inter2, f_inter2, color="green")


    plt.show()
