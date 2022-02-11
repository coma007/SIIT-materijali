from priprema01_04 import solve_upper_triangular
import numpy as np


def upper_triangular_pp(matrix, radicals):
    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Matrica nije kvadratna !")

    for it1 in range(0, rows - 1):
        mi = np.argmax(np.abs(matrix[it1:, it1]))
        mi = mi + it1
        matrix[[it1, mi], :] = matrix[[mi, it1], :]
        radicals[[it1, mi]] = radicals[[mi, it1]]
        for it2 in range(it1 + 1, rows):
            coef = matrix[it2, it1] / matrix[it1, it1]
            matrix[it2, :] = matrix[it2, :] - matrix[it1, :] * coef
            radicals[it2] = radicals[it2] - radicals[it1] * coef

    return matrix, radicals


def gauss_pp(matrix, radicals):
    A, b = upper_triangular_pp(matrix, radicals)
    x = solve_upper_triangular(A, b)
    return x


if __name__ == '__main__':
    A = np.array([[5., 8., 5.],
                  [4., 2., 7.],
                  [8., 5., 8.]])

    b = np.array([48., 43., 69.])

    x = gauss_pp(A, b)
    xt = np.linalg.solve(A, b)
    diff = np.abs(x - xt)
    print("Matrica: ", A, "\nSlobodni članovi: ", b, "\nRJEŠENJE: ", x)
    print("Apsolutna greška: ", diff)
