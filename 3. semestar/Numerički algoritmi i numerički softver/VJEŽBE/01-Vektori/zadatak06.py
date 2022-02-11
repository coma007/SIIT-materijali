import numpy as np


def reverse_odd(matrix):

    rows, cols = matrix.shape

    for row in range(0, rows, 2):
        matrix[row, :] = np.flip(matrix[row, :])

    return matrix


if __name__ == '__main__':

    A = np.array([[0.3, 1, -5],
                  [-1, 4, 0],
                  [1, 5, 2]])

    print("A = ", A)
    print("Matrica nakon obrtanja: ", reverse_odd(A))

