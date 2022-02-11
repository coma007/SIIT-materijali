import numpy as np


def upper_triangular3(matrix):

    # Rješenje za striktno 3x3 matrice
    print(matrix)

    matrix[1, :] = matrix[1, :] - matrix[0, :] * matrix[1, 0] / matrix[0, 0]
    print(matrix)

    matrix[2, :] = matrix[2, :] - matrix[0, :] * matrix[2, 0] / matrix[0, 0]
    print(matrix)

    matrix[2, :] = matrix[2, :] - matrix[1, :] * matrix[2, 1] / matrix[1, 1]
    print(matrix)


def upper_triangular(matrix, radicals):

    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Matrica nije kvadratna")

    for it1 in range(0, rows-1):
        for it2 in range(it1 + 1, rows):
            coef = matrix[it2, it1] / matrix[it1, it1]
            matrix[it2, :] = matrix[it2, :] - matrix[it1, :] * coef
            radicals[it2] = radicals[it2] - radicals[it1] * coef

    return matrix, b


def solve_upper_triangular(matrix, radicals):

    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Matrica nije kvadratna")
    x = np.zeros(rows)

    for it in range(rows-1, -1, -1):
        x[it] = (radicals[it] - np.matmul(matrix[it, (it + 1):], x[(it + 1):])) / matrix[it, it]

    return x


def gauss(matrix, radicals):

    A, b = upper_triangular(matrix, radicals)
    x = solve_upper_triangular(A, b)
    return x


if __name__ == '__main__':

    A = np.array([[5., 8., 5.],
         [4., 2., 7.],
         [8., 5., 8.]])

    b = np.array([48., 43., 69.])

    # upper_triangular3(A)

    x = gauss(A, b)
    print("Matrica: ", A, "\nSlobodni članovi: ", b, "\nRJEŠENJE: ", x)

