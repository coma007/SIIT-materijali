import numpy as np


def jacobi(A, b, x_0, err_max=0.01, iter_max=200):

    x = x_0.copy()
    rows, cols = A.shape

    for i in range(iter_max):
        for r in range(rows):
            x[r] = 1/A[r, r]*(b[r]-np.dot(A[r, :r], x_0[:r])-np.dot(A[r, r+1:], x_0[r+1:]))
        if np.linalg.norm(x_0 - x, np.inf) < err_max:
            return x, i+1
        x_0 = x.copy()

    return x_0, iter_max


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

    x, it = jacobi(A, b, x_0, 1e-05, 100)
    print("Rješenje (Jacobi metoda): ", np.round(x, 2))
    print("Broj iteracija: ", it)
    print("Apsolutna greška: ", abs(xt - x))
