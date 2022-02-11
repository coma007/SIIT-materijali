import numpy as np


def reverse_diagonals(matrix):

    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Matrica nije kvadratna!")

    for row in range(rows):
        matrix[row][row], matrix[row][rows - row - 1] = matrix[row][rows - row - 1],  matrix[row][row]

    return matrix


if __name__ == '__main__':

    A = np.array([[-0.5, 10, 2],
                  [-1, 1, 0],
                  [1, -6, -3]])

    print("A = ", A)
    print("Matrica sa zamijenjenim dijagonalama: ", reverse_diagonals(A))

