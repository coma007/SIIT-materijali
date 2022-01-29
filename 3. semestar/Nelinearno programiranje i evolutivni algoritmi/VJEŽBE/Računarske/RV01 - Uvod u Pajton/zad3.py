import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    x = np.arange(-10, 10, 0.01)
    y = np.sin(x) + 1/25*x**2

    p1 = plt.plot(x, y)
    plt.show()
