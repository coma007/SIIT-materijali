import numpy as np


def reverse_even_cols(matrix):

    rows, cols = np.shape(matrix)

    for col in range(0, cols, 2):
        matrix[:, col] = np.flip(matrix[:, col])

    return matrix


if __name__ == '__main__':

    A = np.array([[-0.5, 10, 2],
                  [-1, 1, 0],
                  [1, -6, -3]])

    print("A = ", A)
    print("Matrica sa obrnutim kolonama: ", reverse_even_cols(A))



