import numpy as np
from gauss import gauss_vect


def create_matrix(*args):

    c = len(args) - 1
    A = np.zeros(c, c)
    b = np.zeros(c)

    for i in range(c):
        for j in range(c):
           A[i][j] = 2 * (args[j+1][j+1] - args[i][0])


if __name__ == '__main__':


    coef = 1
    prag = 0.01
    s1 = (2088.202, -11757.191, 25391.472)
    s2 = (11092.568, -14198.201, 21471.166)
    s3 = (s2[0]*coef + prag, s2[1]*coef + prag, s2[2]*coef + prag)
    s4 = (3966.929, 7362.852, 26388.447)

    r = (23204.699, 21585.835, 31364.260, 24966.799)
