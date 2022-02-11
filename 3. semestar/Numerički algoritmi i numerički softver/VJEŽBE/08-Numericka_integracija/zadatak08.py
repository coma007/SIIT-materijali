import numpy as np
from integrate_simpson import integrate_simpson

if __name__ == '__main__':

    v = lambda t: t**2 - 2*t + 3
    t0 = 0
    t1 = 5

    s = integrate_simpson(v, t0, t1, 100, 0)
    print("s = ", np.round(s, 4))
