import numpy as np


def min_indices_of_rows(matrix):

    rows, cols = matrix.shape
    b = np.zeros(cols)

    for col in range(cols):
        min_el = np.inf
        for row in range(rows):
            if matrix[row][col] <= min_el:
                min_el = matrix[row][col]
                b[col] = row

    return b


if __name__ == '__main__':

    A = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-3, -5, 1]])

    print("A = ", A)
    print("Vektor b: ", min_indices_of_rows(A))
