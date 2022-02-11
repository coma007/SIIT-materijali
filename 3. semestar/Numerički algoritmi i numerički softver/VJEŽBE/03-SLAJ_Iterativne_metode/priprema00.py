import numpy as np

if __name__ == '__main__':

    A = np.array([[9, 3, 1],
                  [7, 8, 9],
                  [4, 1, 9]])
    b = np.array([33, 54, 13])

    x = np.linalg.solve(A, b)
    print(np.round(x, 2))
    print(b == np.dot(A, x))
