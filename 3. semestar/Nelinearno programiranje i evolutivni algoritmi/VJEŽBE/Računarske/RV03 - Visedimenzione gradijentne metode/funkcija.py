import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


def f(x):
    return 0.01*((x[0]-1)**2 + 2*(x[1]-1)**2)*((x[0]+1)**2 + 2*(x[1]+1)**2+0.5)*((x[0]+2)**2 + 2*(x[1]-2)**2 + 0.7)


def df(x_vect):
    x = sym.Symbol('x')
    y = sym.Symbol('y')
    f = 0.01*((x-1)**2 + 2*(y-1)**2)*((x+1)**2 + 2*(y+1)**2+0.5)*((x+2)**2 + 2*(y-2)**2 + 0.7)
    f_dx = sym.diff(f, x)
    f_dy = sym.diff(f, y)
    f_diff_x = sym.lambdify((x, y), f_dx, "numpy")
    f_diff_y = sym.lambdify((x, y), f_dy, "numpy")
    return np.array((f_diff_x(x_vect[0], x_vect[1]), f_diff_y(x_vect[0], x_vect[1]))).reshape(len(x_vect), 1)


if __name__ == '__main__':

    x1v = np.arange(-6, 6, 0.01)
    x2v = np.arange(-6, 6, 0.01)
    x1, x2 = np.meshgrid(x1v, x2v)
    z = np.zeros((len(x1), len(x2)))
    for i in range(len(x1)):
        for j in range(len(x2)):
            z[i, j] = f((x1[i, j], x2[i, j]))
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    p = ax.plot_surface(x1, x2, z)
    plt.show()
