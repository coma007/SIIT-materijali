import matplotlib.pyplot as plt
import numpy as np
import math


def griewank(x):

    sum = 0
    pr = 1

    for i in range(len(x)):
        sum += (x[i]**2)/4000
        pr *= math.cos(x[i]/math.sqrt(i+1))
    total = sum - pr + 1
    return total


if __name__ == '__main__':

    x1v = np.arange(-6, 6, 0.01)
    x2v = np.arange(-6, 6, 0.01)
    x1, x2 = np.meshgrid(x1v, x2v)

    f = np.zeros((len(x1), len(x2)))

    for i in range(len(x1)):
        for j in range(len(x1)):
            f[i, j] = griewank((x1[i, j], x2[i, j]))

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    p1 = ax.plot_surface(x1, x2, f)
    plt.show()
