import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    x = np.array([0.0000, 1.2500, 2.5000, 3.7500, 5.0000])
    fX = np.array([1.7499, 0.9830, 1.2554, 3.0802, 2.3664])

    plt.scatter(x, fX, c='black')
    p = np.polyfit(x, fX, 3)
    print("p = ", p)

    pX = np.polyval(p, x)
    dif = fX - pX
    sumSquaredErr = np.sum(dif ** 2)
    print("sumSquaredErr = ", sumSquaredErr)

    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, 'red')

