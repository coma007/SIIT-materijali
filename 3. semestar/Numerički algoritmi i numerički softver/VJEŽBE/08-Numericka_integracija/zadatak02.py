import numpy as np
from integrate_simpson import integrate_simpson

if __name__ == '__main__':

    f = lambda x: np.exp(-(x**2)/2)
    a = 0
    b = 0.2

    I = 2/np.sqrt(2*np.pi) * integrate_simpson(f, a, b, 10, 0)
    print("I = ", np.round(I, 4))
