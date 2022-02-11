from gauss import gauss_vect
import numpy as np


if __name__ == '__main__':

    A = np.array([[3., 4., 1.],
                  [1., 0, 1.],
                  [2., 3., 2.]])

    b = np.array([3, 3, 1.5])

    print("Rješenje: ", np.round(gauss_vect(A, b), decimals=2))
