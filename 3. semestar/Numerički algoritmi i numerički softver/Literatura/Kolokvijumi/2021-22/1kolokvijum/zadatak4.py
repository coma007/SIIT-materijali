import numpy as np


def fz4a(A, B):
    """
    Funkcija pravi matricu sa sumama elemenata odgovarajuce podmatrice matrice A
    sa odgovarajucim elementom matrice B.

    :param A: Matrica A, dimenzija mxn.
    :type A: numpy.array
    :param B: Matrica B, dimenzija kxk.
    :type B: numpy.array

    :return: Matrica sa zbirovima, dimenzija (m-(k-1))x(n-(k-1))
    :rtype: numpy.array
    """

    m, n = A.shape
    k, j = B.shape
    if k != j:
        raise Exception("B mora biti kvadratna matrica !!")
    if k >= m or k >= n:
        raise Exception("k mora biti manje od m i n !!")

    # shape i matrica koja seta po velikoj matrici A
    new_m, new_n = m - (k - 1), n - (k - 1)
    sum_matrix = np.zeros((new_m, new_n))

    for i in range(new_m):
        for j in range(new_n):
            sample_matrix = A[i:i + k, j:j + k]
            sum = np.sum(sample_matrix * B)
            sum_matrix[i][j] = sum

    return sum_matrix


def fz4b(A, equal_elems_num):
    """
    Funkcija trazi uzastopna ponavljanja istog elementa unutar matrice zadan broj puta.

    :param A: Matrica A, dimenzija mxn.
    :type A: numpy.array
    :param equal_elems_num: Broj ponavljanja elementa.
    :type equal_elems_num: int

    :return: True ukoliko se neki element matrice A uzastopno ponavlja zadan broj puta.
    :rtype: bool
    """
    m, n = A.shape
    if n <= equal_elems_num - 1 or m <= equal_elems_num - 1:
        raise Exception(f"n i m moraju biti veci od {equal_elems_num - 1} !!")
    new_m, new_n = m - (equal_elems_num - 1), n - (equal_elems_num - 1)

    for i in range(new_m):
        for j in range(new_n):
            sample_matrix = A[i:i + 3, j:j + 3]
            if np.all(sample_matrix.diagonal() == sample_matrix[0, 0]):
                return True
            if np.all(np.fliplr(sample_matrix).diagonal() == np.fliplr(sample_matrix)[0, 0]):
                return True
            for k in range(equal_elems_num):
                if np.all(sample_matrix[:, k] == sample_matrix[0, k]):
                    return True
                if np.all(sample_matrix[k, :] == sample_matrix[k, 0]):
                    return True

    return False


if __name__ == '__main__':

    print("Zadatak 4:\n")
    print("4. a")
    A = np.array([[1, 2, 3],
                  [0, 3, 7],
                  [4, 1, 2]])
    B = np.array([[4, 3],
                  [2, 1]])

    sum1 = fz4a(A, B)
    print(f"\nPrimjer 1:\nA = \n{A}\nB = \n{B}\nRezultat: \n{sum1}")

    A = np.array([[1, 2, 3, 1, 1],
                  [0, 3, 0, 1, 3],
                  [0, 3, 0, 1, 4],
                  [0, 3, 2, 1, 2],
                  [4, 1, 2, 1, 4]])
    B = np.array([[0, 3, 1],
                  [0, 2, 2],
                  [2, 1, 1]])

    sum2 = fz4a(A, B)
    print(f"\nPrimjer 2:\nA = \n{A}\nB = \n{B}\nRezultat: \n{sum2}")

    A = np.array([[1, 2, 3, 1],
                  [5, 75, 0, 1],
                  [12, 3, 18, 1],
                  [21, 16, 25, 1],
                  [8, 1, 2, 1]])
    B = np.array([[19, 3, 14],
                  [17, 18, 2],
                  [2, 1, 12]])

    sum3 = fz4a(A, B)
    print(f"\nPrimjer 3:\nA = \n{A}\nB = \n{B}\nRezultat: \n{sum3}")

    print("\n4. b")

    A = np.array([[1, 2, 1, 1],
                  [1, 4, 1, 4],
                  [0, 0, 5, 3],
                  [0, 0, 7, 1]])
    assert fz4b(A, 3) is False
    A = np.array([[1, 2, 1, 4],
                  [0, 0, 5, 3],
                  [1, 4, 1, 4],
                  [0, 0, 0, 1]])
    assert fz4b(A, 3)
    A = np.array([[1, 2, 1, 4],
                  [0, 0, 1, 3],
                  [1, 4, 1, 4],
                  [0, 0, 7, 1]])
    assert fz4b(A, 3)
    A = np.array([[1, 2, 1, 4],
                  [0, 0, 4, 3],
                  [1, 4, 1, 4],
                  [0, 0, 7, 1]])
    assert fz4b(A, 3)
    A = np.array([[1, 2, 1, 2, 5],
                  [2, 2, 2, 2, 5],
                  [1, 2, 1, 0, 1],
                  [0, 0, 2, 1, 2]])
    assert fz4b(A, 4)  # trebalo bi da radi i sa 4 ponavljanja
    A = np.array([[1, 2, 1],
                  [7, 4, 8],
                  [1, 6, 5],
                  [0, 9, 3]])
    assert fz4b(A, 2) is False
    print("Testovi prosli !")
