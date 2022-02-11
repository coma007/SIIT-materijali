import numpy as np


def sort_by_first_column(A):
    rows, cols = A.shape
    for i in range(rows-1):
        for j in range(i + 1, rows):
            if A[j][0] > A[i][0]:
                tmp = A[i, :].copy()
                A[i, :] = A[j, :]
                A[j, :] = tmp
    return A


if __name__ == '__main__':

    A = np.array([[66, 1],
                  [100, 2],
                  [133, 3],
                  [200, 4],
                  [33, 5],
                  [66, 6],
                  [133, 7],
                  [266, 8]])

    A = sort_by_first_column(A)
    print(A)
