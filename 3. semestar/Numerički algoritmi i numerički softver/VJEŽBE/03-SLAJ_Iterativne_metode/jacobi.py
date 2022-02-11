import numpy as np


def jacobi(A, b, x0, errMax=0.0001, itMax=100):
    n, _ = A.shape
    x1 = np.zeros(n)
    for _ in range(itMax):
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s = s + A[i, j] * x0[j]
                x1[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(x0 - x1, np.Inf) < errMax:
            break
        x0 = x1.copy()
    return x1


def jacobi_vect(A, b, x0, err_max=0.001, it_max=100):
    D = np.diag(A)
    R = A - np.diagflat(D)
    for i in range(it_max):
        x = (b - np.dot(R, x0)) / D
        if np.linalg.norm(x0 - x, np.Inf) < err_max:
            break
        x0 = x.copy()
    return x, i


# def jacobi(A, b, x0, err_max=0.001, it_max=100):
#     x = x0.copy()
#     rows = A.shape[0]
#     for i in range(it_max):
#         for r in range(rows):
#             x[r] = 1 / A[r, r] * (b[r] - np.dot(A[r, :r], x0[:r]) - np.dot(A[r, r + 1:], x0[r + 1:]))
#         if np.linalg.norm(x0 - x, np.Inf) < err_max:
#             break
#         x0 = x.copy()
#     return x, i
