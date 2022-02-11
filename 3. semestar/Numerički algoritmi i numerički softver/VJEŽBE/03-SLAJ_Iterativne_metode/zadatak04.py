import numpy as np
from gs import gauss_seidel_vect
from jacobi import jacobi_vect


if __name__ == '__main__':

    A = np.array([[2, 1],
                  [1, 2]])
    b = np.array([1, -2])
    x_0 = np.zeros(b.shape)

    print("A =\n", A)
    print("b = ", b)
    print("x_0 = ", x_0)

    xt = np.linalg.solve(A, b)
    print("Rješenje: ", np.round(xt, 2))

    x, it = jacobi_vect(A, b, x_0, 1e-05, 100)
    print("\n=== Jacobi ===")
    print("Rješenje:\nx = ", np.round(x[0], 2), "\ny = ", np.round(1/x[1], 2))
    print("Broj iteracija: ", it)
    print("Apsolutna greška: ", abs(xt - x))

    x, it = gauss_seidel_vect(A, b, x_0, 1e-05, 100)
    print("\n=== Gauss-Seidel ===")
    print("Rješenje:\nx = ", np.round(x[0], 2), "\ny = ", np.round(1/x[1], 2))
    print("Broj iteracija: ", it)
    print("Apsolutna greška: ", abs(xt - x))
