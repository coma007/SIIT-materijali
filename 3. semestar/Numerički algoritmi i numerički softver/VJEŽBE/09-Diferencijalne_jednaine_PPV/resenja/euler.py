import numpy as np
import matplotlib.pyplot as plt

def euler(a, b, h, fX0, dfX, plot_speed):
    if plot_speed <= 0:
        return eulerWithoutPlot(a, b, h, fX0, dfX)
    return eulerWithPlot(a, b, h, fX0, dfX, plot_speed)

def eulerWithoutPlot(a, b, h, fX0, dfX):
    x = np.arange(a, b, h)
    n = len(x)
    fX = np.zeros(n)
    fX[0] = fX0

    for it in range(1, n):
        fX[it] = fX[it -1] + h* dfX(x[it - 1], fX[it - 1])

    return fX

def eulerWithPlot(a, b, h, fX0, dfX, plot_speed):
    x = np.arange(a, b, h)
    n = len(x)
    fX = np.zeros(n)
    fX[0] = fX0

    plt.plot([a, b], [0 ,0], 'black')
    for it in range(1, n):
        fX[it] = fX[it -1] + h* dfX(x[it - 1], fX[it - 1])

        plt.plot([x[it-1], x[it]], [fX[it-1], fX[it]], 'blue')
        plt.pause(1/plot_speed)

    plt.show()

    return fX
