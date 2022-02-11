import numpy as np
import matplotlib.pyplot as plt

def rk4(a, b, h, fX0, dfX, plot_speed):
    if plot_speed <= 0:
        return rk4WithoutPlot(a, b, h, fX0, dfX)
    return rk4WithPlot(a, b, h, fX0, dfX, plot_speed)


def rk4WithoutPlot(a, b, h, fX0, dfX):
    x = np.arange(a, b, h)
    n = len(x)
    fX = np.zeros(n)
    fX[0] = fX0

    for it in range(1,n):
        k1 = dfX(x[it - 1], fX[it -1])
        k2 = dfX(x[it - 1] + h/2, fX[it -1] + k1*h/2)
        k3 = dfX(x[it - 1] + h/2,  fX[it -1] + k2*h/2)
        k4 = dfX(x[it - 1] + h,  fX[it -1] + k3*h)

        fX[it] = fX[it - 1] + h/6*(k1 + 2*k2 + 2*k3 + k4)
    return fX

def rk4WithPlot(a, b, h, fX0, dfX, plotSpeed):
    x = np.arange(a, b, h)
    n = len(x)
    fX = np.zeros(n)
    fX[0] = fX0

    plt.plot([a, b], [0 ,0], 'black')
    for it in range(1,n):
        k1 = dfX(x[it - 1], fX[it -1])
        k2 = dfX(x[it - 1] + h/2, fX[it -1] + k1*h/2)
        k3 = dfX(x[it - 1] + h/2,  fX[it -1] + k2*h/2)
        k4 = dfX(x[it - 1] + h,  fX[it -1] + k3*h)

        fX[it] = fX[it - 1] + h/6*(k1 + 2*k2 + 2*k3 + k4)

        plt.plot([x[it-1], x[it]], [fX[it-1], fX[it]], 'blue')
        plt.pause(1/plotSpeed)
    
    plt.show()

    return fX
