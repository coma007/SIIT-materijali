import numpy as np
from matplotlib import pyplot as plt


def zeroBisectionPlot(f, a, b, errMax=0.0001, itMax = 100, plotSpeed=-1):

    it = 0   # iteracije i novi presjeci
    zero = 0
    while it < itMax:
        zero = (a + b)/2
        fZero = f(zero)
        plt.plot([zero, zero], [fMin, fMax], 'g', zero, fZero, 'go')
        if np.abs(fZero) < errMax or np.abs(b - a) < errMax:
            break
        plt.pause(1/plotSpeed)

        if f(a)*fZero < 0:
            b = zero
        else:
            a = zero
            it += 1
            plt.plot([zero, zero], [fMin, fMax], 'r', zero, fZero, 'ro')

    plt.show()
    return zero,


def zeroBisectionNoPlot(f, a, b, errMax=0.0001, itMax = 100):

    it = 0   # iteracije i novi presjeci
    zero = 0
    while it < itMax:
        zero = (a + b)/2
        fZero = f(zero)
        plt.plot([zero, zero], [fMin, fMax], 'g', zero, fZero, 'go')
        if np.abs(fZero) < errMax or np.abs(b - a) < errMax:
            break

        if f(a)*fZero < 0:
            b = zero
        else:
            a = zero
            it += 1
            plt.plot([zero, zero], [fMin, fMax], 'r', zero, fZero, 'ro')

    plt.show()
    return zero, it


def zeroBisection(f, a, b, errMax=0.001, itMax=100, plotSpeed=-1):
    if f(a)*f(b) > 0:
        raise Exception('Invalid parameters: f(a)*f(b) > 0!')
    if plotSpeed <= 0:
        return zeroBisectionNoPlot(f, a, b, errMax, itMax)
    return zeroBisectionPlot(f, a, b, errMax, itMax, plotSpeed)


if __name__ == '__main__':

    f = lambda x: np.sin(x)
    a = np.pi/3
    b = 4*np.pi/3

    x = np.linspace(np.pi/3, 4*np.pi/3, 100)
    fX = f(x)
    fMin = np.min(fX)
    fMax = np.max(fX)
    plt.plot(x, fX, 'b', [a, b], [0, 0], 'k')  # plot funkcija
    plt.plot([a, a], [fMin, fMax], 'r', [b, b], [fMin, fMax], 'r')  # ogranicavanje intervala

    zero, it = zeroBisection(f, a, b,  0.0001, 100, -1)
    fZero = f(zero)
    print("zero = ", zero, "\nit = ", it, "\nf(zero) = ", fZero)
