import numpy as np


def find_max_indices(matrix):

    rows, cols = np.shape(matrix)
    b = np.zeros(rows)

    for col in range(cols):
        maximum = -np.inf
        for row in range(rows):
            if matrix[col][row] > maximum:
                maximum = matrix[col][row]
                b[col] = row

    return b


if __name__ == '__main__':

    A = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-1, -5, -3]])

    print("A = ", A)
    print("Vektor b: ", find_max_indices(A))
