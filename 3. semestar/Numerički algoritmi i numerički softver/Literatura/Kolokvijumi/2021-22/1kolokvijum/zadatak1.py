import numpy as np
from NANS_lib import *

if __name__ == '__main__':

    print("Zadatak 1:\n")
    x2 = 1.7
    x1 = x2 - 1.2

    A = np.array([[1, x1, x1**2, x1**3],
                  [1, (4*x1-2*x2), (4*x1-2*x2)**2, (4*x1-2*x2)**3],
                  [1, 2*x1, (2*x1)**2, (2*x1)**3],
                  [1, x2, x2**2, x2**3]])
    b = np.array([5.625, -0.512, x2 + 14.3, 44.469])

    a = gauss(A, b)
    print("[a0, a1, a2, a3] = ", a)

    [a0, a1, a2, a3] = a
    assert np.round(np.sqrt(a0) - 2/5*a1 - a2 + a3**2, 0) == 1.0, "Problem, jednakost ne vazi !!"
    # morala sam primjeniti np.round jer je bilo suvisnih decimala na 10+ poziciji koje su kvarile jednakost
