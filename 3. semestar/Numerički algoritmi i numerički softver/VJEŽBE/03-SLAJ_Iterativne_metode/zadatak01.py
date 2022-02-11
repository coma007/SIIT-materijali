import numpy as np
from gs import gauss_seidel_vect
from jacobi import jacobi_vect


if __name__ == '__main__':

    A = np.array([[9, 3, 1],
                  [7, 8, 9],
                  [4, 1, 9]])
    b = np.array([33, 54, 13])
    x_0 = np.array([0, 0, 0], "d")

    print("A =\n", A)
    print("b = ", b)
    print("x_0 = ", x_0)

    xt = np.linalg.solve(A, b)
    print("Rješenje: ", np.round(xt, 2))

    x, it = jacobi_vect(A, b, x_0, 1e-05, 100)
    print("\n=== Jacobi ===")
    print("Rješenje: ", np.round(x, 2))
    print("Broj iteracija: ", it)
    print("Apsolutna greška: ", abs(xt - x))

    x, it = gauss_seidel_vect(A, b, x_0, 1e-05, 100)
    print("\n=== Gauss-Seidel ===")
    print("Rješenje: ", np.round(x, 2))
    print("Broj iteracija: ", it)
    print("Apsolutna greška: ", abs(xt - x))
