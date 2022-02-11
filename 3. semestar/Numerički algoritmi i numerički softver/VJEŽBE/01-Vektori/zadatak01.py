import numpy as np


def sum_d(matrix):

    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Matrica nije kvadratna!")
    total_sum = 0

    # Iterativni pristup
    for row in range(rows):
        total_sum += matrix[row][row]

    # Vektorski pristup 1 - vektor elemenata sa dijagoanle
    diag_elems = np.diagonal(matrix)
    total_sum = np.sum(diag_elems)

    # Vektorski pristup 2 - množenje jediničnom matricom
    I = np.eye(rows)
    matrix_sum = I * matrix
    total_sum = np.sum(matrix_sum)

    # Vektorski pristup 3 - jedinična matrica sa boolean vrijednostima
    mask = np.eye(rows).astype(bool)
    masked_matrix = matrix[mask]
    total_sum = np.sum(masked_matrix)

    return total_sum


if __name__ == '__main__':

    A = np.array([[2, 1, 6, 1],
                  [1, 3, 8, 2],
                  [5, 9, 4, 3],
                  [1, 1, 8, 5]])

    print("A = ", A)
    print("Suma elemenata na dijagonali: ", sum_d(A))
