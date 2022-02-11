import numpy as np


def sum_greater(matrix):

    rows, cols = matrix.shape
    elems_sum, greater_elems_sum = 0, 0
    elems_number = rows*cols

    # Iterativni pristup
    for row in range(rows):
        for col in range(cols):
            elems_sum += matrix[row][col]
    avg = elems_sum / elems_number

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] > avg:
                greater_elems_sum += matrix[row][col]

    # Vektorski pristup
    avg = np.average(matrix)
    mask = matrix > avg

    greater_elems_matrix = matrix[mask]
    greater_elems_sum = np.sum(greater_elems_matrix)

    return greater_elems_sum


if __name__ == '__main__':

    A = np.array([[2, 1, 2, 6, 8, 1, -2],
                  [15, 4, 7, 18, 4, 0, 12],
                  [11, 6, 9, -1, 4, 8, 0],
                  [2, 8, 6, 8, 1, 8, 7]])

    print("A = ", A)
    print("Suma elemenata većih od srednje vrijednosti: ", sum_greater(A))
