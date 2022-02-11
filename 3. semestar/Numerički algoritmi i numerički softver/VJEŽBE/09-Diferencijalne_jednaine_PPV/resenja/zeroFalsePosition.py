import numpy as np
from matplotlib import pyplot as plt


def zeroFalsePosition(f, a, b, errMax=0.0001, itMax=100, plotSpeed=-1):
    if f(a)*f(b) > 0:
        raise Exception('Invalid input: f(a)*f(b) > 0!')

    if plotSpeed <= 0:
        return zeroFalsePositionNoPlot(f, a, b, errMax, itMax)
    
    return zeroFalsePositionPlot(f, a, b, errMax, itMax, plotSpeed)


def zeroFalsePositionNoPlot(f, a, b, errMax, itMax):
    for it in range(itMax):
        fA = f(a)
        fB = f(b)
        zero = b - fB*(b - a)/(fB - fA)

        fZero = f(zero)

        if abs(fZero) < errMax or abs(b - a) < errMax:
            return zero, it

        if fA*fZero < 0:
            b = zero
        else:
            a = zero

    return zero, it

def zeroFalsePositionPlot(f, a, b, errMax, itMax, plotSpeed):

    x = np.linspace(a, b, 100)
    fX = f(x)
    fMin = min(fX)
    fMax = max(fX)
    plt.plot(x, fX, 'b', [a, b], [0, 0], 'k')

    for it in range(itMax):
        fA = f(a)
        fB = f(b)
        zero = b - fB*(b - a)/(fB - fA)
        plt.plot([a, b], [fA, fB], 'r', zero, 0, 'rx')

        fZero = f(zero)
        
        plt.plot([zero, zero], [fMin, fMax], 'g', zero, fZero, 'og')

        if abs(fZero) < errMax or abs(b - a) < errMax:
            break

        plt.pause(1/plotSpeed)

        if fA*fZero < 0:
            b = zero
        else:
            a = zero
            
        plt.plot([zero, zero], [fMin, fMax], 'r', zero, fZero, 'og')

    plt.show()
    return zero, it + 1
