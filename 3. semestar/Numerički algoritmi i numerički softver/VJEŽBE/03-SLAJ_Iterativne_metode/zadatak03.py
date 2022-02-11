import numpy as np
from gs import gauss_seidel_vect


if __name__ == '__main__':

    A = np.array([[0, 1, 2],
                  [1, 2, 0],
                  [-1, -1, 0]])
    A[0][0] = 22
    A[2][2] = 22
    b = np.array([1, 2, 3])
    x_0 = np.array([0, 0, 0], "d")
    # DIJAGONALNO DOMINANTNA MATRICA - elementi na glavnoj dijagonali su veci od
    # zbira ostalih apsolutne vrijednosti u istom redu i to je uslov konvergentnosti

    print("A =\n", A)
    print("b = ", b)
    print("x_0 = ", x_0)

    xt = np.linalg.solve(A, b)
    print("Rješenje: ", np.round(xt, 2))

    x, it = gauss_seidel_vect(A, b, x_0, 1e-05, 100)
    print("\n=== Gauss-Seidel ===")
    print("Rješenje: ", np.round(x, 2))
    print("Broj iteracija: ", it)
    print("Apsolutna greška: ", abs(xt - x))
