import numpy as np
import matplotlib.pyplot as plt


def integrate_trapezoid(f, a, b, intervals, plotSpeed):
    if plotSpeed <= 0:
        return integrate_trapezoid_no_plot(f, a, b, intervals)

    return integrate_trapezoid_plot(f, a, b, intervals, plotSpeed)


def integrate_trapezoid_no_plot(f, a, b, intervals):
    x = np.linspace(a, b, intervals + 1)
    fX = f(x)
    width = (b-a)/intervals

    I = 0
    for it in range(intervals):
        x1 = x[it]
        x2 = x[it + 1]
        fX1 = fX[it]
        fX2 = fX[it + 1]
        plt.stackplot([x1, x2],  [fX1, fX2], colors=['b'])

        I = I + (fX1 + fX2) * width/2
    return I


def integrate_trapezoid_plot(f, a, b, intervals, plotSpeed):
    x = np.linspace(a, b, intervals + 1)
    fX = f(x)
    width = (b-a)/intervals

    I = 0
    for it in range(intervals):
        x1 = x[it]
        x2 = x[it + 1]
        fX1 = fX[it]
        fX2 = fX[it + 1]
        plt.stackplot([x1, x2],  [fX1, fX2], colors=['b'])

        I = I + (fX1 + fX2) * width/2
        plt.pause(1/plotSpeed)
    plt.show()
    return I
