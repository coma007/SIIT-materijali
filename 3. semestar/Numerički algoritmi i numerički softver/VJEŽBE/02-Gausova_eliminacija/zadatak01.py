from gauss import gauss_vect
import numpy as np


if __name__ == '__main__':

    A = np.array([[5., 8., 5.],
                  [4., 2., 7.],
                  [8., 5., 8.]])

    b = np.array([48, 43, 69])

    print("Rješenje: ", gauss_vect(A, b))
