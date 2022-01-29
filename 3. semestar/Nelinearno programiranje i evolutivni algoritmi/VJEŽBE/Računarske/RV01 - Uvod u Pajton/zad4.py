import matplotlib.pyplot as plt
import numpy as np
import math


def ackley(x):

    sum1 = 0
    sum2 = 0
    for k in range(len(x)):
        sum1 += x[k]**2.0
        sum2 += math.cos(2.0*math.pi*x[k])
    total = -20.0*math.exp(-0.2*math.sqrt(sum1/len(x)))-math.exp(sum2/len(x))+20.0+math.e
    return total


if __name__ == '__main__':

    x1vect = np.arange(-6, 6, 0.01)
    x2vect = np.arange(-6, 6, 0.01)
    # meshgrid - kombinacije svih vrijednosti - bez ovoga bi se dobio samo obod
    x1, x2 = np.meshgrid(x1vect, x2vect)

    # instaciranje funkcije 2d matricom 0
    f = np.zeros((len(x1), len(x2)))

    # racunanje funkcije
    for i in range(0, len(x1)):
        for j in range(0, len(x1)):
            # funkciji se prosljedjuje jedna vrijednost
            # iz matrice x1 i jedna vrijednost iz matrice x2
            # kao jedan parametar x
            f[i, j] = ackley((x1[i, j], x2[i, j]))

    # istanciranje figure (3d)
    fig = plt.figure()
    # govorimo da cemo koristiti 3d projekciju, ovo mora jer se plot_surface prosljedjuje matrica !
    ax = fig.add_subplot(projection='3d')
    p1 = ax.plot_surface(x1, x2, f)
    plt.show()
