from priprema02 import gauss_seidel
import numpy as np

if __name__ == '__main__':

    A = np.array([[2, 5, 6],
                 [5, 4, 9],
                 [6, 2, 3]])
    b = np.array([69, 100, 67])
    x_0 = np.array([0, 0, 0], "d")

    print("A =\n", A)
    print("b = ", b)
    print("x_0 = ", x_0)

    xt = np.linalg.solve(A, b)
    print("Rješenje: ", np.round(xt, 2))

    x, it = gauss_seidel(A, b, x_0, 10e-05, 100)
    print("\n=== Gauss-Seidel ===")
    print("Rješenje: ", np.round(x, 2))
    print("Broj iteracija: ", it)
    print("Apsolutna greška: ", abs(xt - x))
