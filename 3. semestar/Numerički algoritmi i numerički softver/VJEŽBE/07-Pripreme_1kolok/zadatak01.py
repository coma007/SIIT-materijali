import numpy as np


def fz1a(A, n):

    sum = 0
    unique, counts = np.unique(A, return_counts=True)
    for i in range(len(unique)):
        if counts[i] >= n:
            sum += unique[i]

    return sum


def fz2A(A):

    rows, cols = A.shape

    # central = np.array(A[:, (cols-1)//2])
    # A = np.fliplr(A)
    # A[:, (cols-1)//2] = np.diagonal(A)
    # np.fill_diagonal(A, central)
    # A = np.fliplr(A)

    center_index = (cols - 1) // 2
    for i in range(rows):
        temp = A[i, center_index]
        A[i, center_index] = A[i, rows - i - 1]
        A[i, rows - i - 1] = temp

    return A


if __name__ == '__main__':

    A = np.array([[6, 2, 3, 5], [5, 3, 9, 7], [2, 7, 9, 2], [2, 7, 5, 9]])
    print(fz1a(A, 3))

    B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(fz2A(B))
    print(fz2A(A))
