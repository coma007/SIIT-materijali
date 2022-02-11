import numpy as np

def lSquares(x, fX, order):

    n = x.size
    m = min(order+1, n)
    A = np.zeros((n, m))

    for it in range(m):
        A[:, it] = x**(it)

    a = np.linalg.solve(np.matmul(A.T, A), np.matmul(A.T, fX))

    p = a[::-1]
    return p