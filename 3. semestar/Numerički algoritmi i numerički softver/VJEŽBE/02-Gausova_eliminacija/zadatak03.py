from gauss import gauss_vect
import numpy as np


if __name__ == '__main__':

    A = np.array([[1., 0.1, 0.1**2, 0.1**3],
                  [1., 0.3, 0.3**2, 0.3**3],
                  [1., 0.6, 0.6**2, 0.6**3],
                  [1., 1.2, 1.2**2, 1.2**3]])

    b = np.array([1.023, 1.261, 2.368, 9.064])

    print("Rješenje: ", gauss_vect(A, b))
