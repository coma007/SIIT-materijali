import numpy as np
import matplotlib.pyplot as plt


def integrate_simpson(f, a, b, intervals, plotSpeed):
    if plotSpeed <= 0:
        return integrate_simpson_no_plot(f, a, b, intervals)

    return integrate_simpson_plot(f, a, b, intervals, plotSpeed)


def integrate_simpson_no_plot(f, a, b, intervals):
    x = np.linspace(a, b, intervals + 1)
    fX = f(x)
    width = (b-a)/intervals

    I = 0
    for it in range(0, intervals, 2):
        x1 = x[it]
        x2 = x[it + 1]
        x3 = x[it + 2]
        fX1 = fX[it]
        fX2 = fX[it + 1]
        fX3 = fX[it + 2]
        p = np.polyfit([x1, x2, x3], [fX1, fX2, fX3], 2)
        xP = np.linspace(x1, x3, 100)
        fXP = np.polyval(p, xP)
        plt.stackplot(xP, fXP, colors=['b'])

        I = I + (fX1 + 4*fX2 + fX3) * width/3
    return I


def integrate_simpson_plot(f, a, b, intervals, plotSpeed):
    x = np.linspace(a, b, intervals + 1)
    fX = f(x)
    width = (b-a)/intervals

    I = 0
    for it in range(0, intervals, 2):
        x1 = x[it]
        x2 = x[it + 1]
        x3 = x[it + 2]
        fX1 = fX[it]
        fX2 = fX[it + 1]
        fX3 = fX[it + 2]
        p = np.polyfit([x1, x2, x3], [fX1, fX2, fX3], 2)
        xP = np.linspace(x1, x3, 100)
        fXP = np.polyval(p, xP)
        plt.stackplot(xP, fXP, colors=['b'])

        I = I + (fX1 + 4*fX2 + fX3) * width/3

        plt.pause(1/plotSpeed)
    plt.show()
    return I
