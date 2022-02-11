import numpy as np
from gs import gauss_seidel_vect


if __name__ == '__main__':

    A = np.array([[4, 2],
                  [1, 2]])
    b = np.array([1, -1])
    x_0 = np.zeros(b.shape[0])

    print("A =\n", A)
    print("b = ", b)
    print("x_0 = ", x_0)

    xt = np.linalg.solve(A, b)
    [xt, yt] = xt
    zt = -4 / (2*xt + yt)
    print("Rješenje [x, y, z]: [", np.round(xt, 2), ", ", np.round(yt, 2), ", ", np.round(zt, 2), "]")

    [x, y], it = gauss_seidel_vect(A, b, x_0, 1e-05, 100)
    z = -4 / (2*x + y)
    print("\n=== Gauss-Seidel ===")
    print("Rješenje:\nx = ", np.round(x, 2), "\ny = ", np.round(y, 2), "\nz = ", np.round(z, 2))
    print("Broj iteracija: ", it)
    print("Apsolutna greška: ", abs(np.array([xt, yt, zt]) - np.array([x, y, z])))
