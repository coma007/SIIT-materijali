import numpy as np


def gauss_seidel(A, b, x0, errMax=0.0001, itMax=100):
    n, _ = A.shape
    x1 = np.zeros(n)
    for _ in range(itMax):
        for i in range(n):
            s = 0
            for j in range(i):
                s = s + A[i, j] * x1[j]
            for j in range(i + 1,n):
                s = s + A[i, j] * x0[j]
            x1[i] = (b[i] - s)/A[i, i]
        if np.linalg.norm(x0 - x1, np.Inf) < errMax:
            break
        x0 = x1.copy()
    return x1


def gauss_seidel_vect(A, b, x0, err_max=0.0001, it_max=100):
    x = x0.copy()
    rows = A.shape[0]
    for i in range(it_max):
        for r in range(rows):
            x[r] = 1 / A[r, r] * (b[r] - np.dot(A[r, :r], x[:r]) - np.dot(A[r, r + 1:], x[r + 1:]))
        if np.linalg.norm(x0 - x, np.Inf) < err_max:
            break
        x0 = x.copy()
    return x, i+1
