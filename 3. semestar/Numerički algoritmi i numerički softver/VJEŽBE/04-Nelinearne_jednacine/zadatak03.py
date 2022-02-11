import numpy as np
import matplotlib.pyplot as plt
import zero_false_position

if __name__ == '__main__':

    a = np.pi / 4
    b = np.pi * 7 / 4

    f = lambda x: np.sin(2*x)

    x = np.linspace(a, b, 100)
    fX = f(x)

    plt.plot(x, fX, 'blue')
    plt.plot([a, b], [0, 0], 'black')

    zero1, it1 = zero_false_position.zero_false_position(f, np.pi/4, np.pi*3/4, 10e-5, 100, 0)
    print("x1 = ", zero1)
    zero2, it2 = zero_false_position.zero_false_position(f, np.pi*3/4, np.pi*5/4, 10e-5, 100, 0)
    print("x2 = ", zero2)
    zero3, it3 = zero_false_position.zero_false_position(f, np.pi*5/4, np.pi*7/4, 10e-5, 100, 0)
    print("x3 = ", zero3)
    f_zero1 = f(zero1)
    f_zero2 = f(zero2)
    f_zero3 = f(zero3)

    plt.scatter(zero1, f_zero1, color='red')
    plt.scatter(zero2, f_zero2, color='red')
    plt.scatter(zero3, f_zero3, color='red')
    plt.show()
