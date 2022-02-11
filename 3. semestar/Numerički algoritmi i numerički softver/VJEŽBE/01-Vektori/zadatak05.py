import numpy as np


def min_indices_diagonal(matrix):

    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Matrica nije kvadratna !")

    min_value = np.inf
    indices = (0, 0)

    # Iterativni pristup
    for row in range(rows):
        for col in range(cols):
            if row == col:
                if matrix[row][col] < min_value:
                    min_value = matrix[row][col]
                    indices = row, col
            elif col == rows - row - 1:
                if matrix[row][col] < min_value:
                    min_value = matrix[row][col]
                    indices = row, col

    # Vektorski pristup
    mask = np.maximum(np.eye(rows), np.fliplr(np.eye(rows)))
    new_matrix = mask * matrix
    bool_mask = new_matrix == np.min(new_matrix)
    indices = np.nonzero(bool_mask)[0][0], np.nonzero(bool_mask)[1][0]

    return indices


if __name__ == '__main__':

    A = np.array([[-2, 5, -7],
                  [-1, -1, -8],
                  [-3, -5, 1]])

    print("A = ", A)
    print("Indeksi min elementa: ", min_indices_diagonal(A))
