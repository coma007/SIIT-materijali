import numpy as np


def gauss(A, b):
    (n, m) = A.shape
    for k in range(n-1):
        for i in range(k+1, n):
            p = -A[i, k]/A[k, k]
            for j in range(n):
                A[i, j] = A[i, j] + A[k, j]*p
            b[i] = b[i] + b[k]*p
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = 0.
        for j in range(i+1, n):
            s = s + A[i, j]*x[j]
        x[i] = (b[i]-s)/A[i, i]
    return x


def gauss_with_pivoting(A, b):
    (n, m) = A.shape

    for k in range(n-1):
        loc = np.argmax(np.abs(A[k:n, k]))
        loc = k+loc
        A[k, :], A[loc, :] = A[loc, :].copy(), A[k, :].copy()

        b[k], b[loc] = b[loc].copy(), b[k].copy()
        
        for i in range(k+1, n):
            p = -A[i, k]/A[k, k]
            for j in range(n):
                A[i, j] = A[i, j] + A[k, j]*p
            b[i] = b[i] + b[k]*p

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = 0.
        for j in range(i+1, n):
            s = s + A[i, j]*x[j]
        x[i] = (b[i]-s)/A[i, i]
    return x


def gauss_vect(A, b):
    (n, m) = A.shape
    Aaug = np.zeros((n, n+1))
    Aaug[0:n, 0:n] = A
    Aaug[:, n] = b

    for k in range(n-1):
        for i in range(k+1, n):
            m = -Aaug[i, k]/Aaug[k, k]
            Aaug[i, :] = Aaug[i, :]+m*Aaug[k, :]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Aaug[i, n]-np.dot(Aaug[i, 0:n], x))/Aaug[i, i]
    return x
