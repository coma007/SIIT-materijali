import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':

    f = lambda x: np.sin(x)
    x = np.linspace(np.pi/3, 4*np.pi/3, 100)
    fX = f(x)
    plt.plot(x, fX, 'b')  # grafik
    plt.plot([np.pi/3, 4*np.pi/3], [0, 0], 'k')  # x osa

    zero = np.pi
    fZero = f(zero)
    plt.plot(zero, fZero, 'go')  # nule

    plt.show()
