import numpy as np


def sum_non_diagonal(matrix):

    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Matrica nije kvadratna !")
    b = np.zeros(rows)

    # Iterativni pristup
    for i in range(rows):
        row_sum = 0
        for j in range(cols):
            if i == rows - j - 1:
                continue
            row_sum += matrix[i][j]
        b[i] = row_sum

    # Vektorski pristup
    flipped_matrix = np.fliplr(matrix)
    np.fill_diagonal(flipped_matrix, 0)
    b = np.sum(flipped_matrix, axis=1)  # Sad se nije moralo flipovati, ali ne zaboraviti to u opštem slučaju !
    
    return b


if __name__ == '__main__':

    A = np.array([[-0.5, 10, 2],
                  [-1, 1, 0],
                  [1, -6, -3]])

    print("A = ", A)
    print("Vektor b: ", sum_non_diagonal(A))
