"""
Program izračunava sumu liste rekurzivnim putem.
"""

import time,sys

def recursive_sum_linear(seq, n):
    """
    Funkcija izračunava sumu liste od n elemenata upotrebom linearne rekurzije.

    :param seq: lista čija suma se izračunava
    :param n: broj preostalih elemenata za sumiranje
    :return: suma elemenata
    """

    # bazni slučaj
    if n == 0:
        return 0
    else:
        # izračunava se zbir poslednjeg i svih ostalih elemenata
        return seq[n-1] + recursive_sum_linear(seq, n-1)


def recursive_sum_binary(seq):
    """
    Funkcija izračunava sumu liste od n elemenata upotrebom binarne rekurzije.

    :param seq: lista čija suma se izračunava
    :return: suma elemenata
    """

    # bazni slučaj
    if len(seq) == 1:
        return seq[0]
    else:
        # izračunava se zbir poslednjeg i svih ostalih elemenata
        return recursive_sum_binary(seq[:len(seq)//2]) + recursive_sum_binary(seq[len(seq)//2:])

def iterative_sum(seq):
    """
    Funkcija izračunava sumu elemenata liste seq iterativnim postupkom.

    :param seq: lista čija suma se izračunava
    :return: suma elemenata
    """
    sum = 0
    for element in seq:
        sum += element

    return sum

if __name__ == '__main__':
    a = [x for x in range(1, 1998)]
    # Dobavlja se podatak o maksimalnoj dubini rekurzije
    print("Maksimalna dubina rekurzije: %d" % sys.getrecursionlimit())

    # Postavljanje maksimalne dubine rekurzije na 2000
    #sys.setrecursionlimit(2000)
    # Izvršavanje linearne rekurzije
    start_time = time.time()
    rezultat = recursive_sum_linear(a, len(a))
    vreme = time.time() - start_time
    print("------Linearna rekurzija------")
    print("Rezultat: %d" % rezultat)
    print("Vreme izvršavanja: %f" % vreme)

    start_time = time.time()
    rezultat = iterative_sum(a)
    vreme = time.time() - start_time
    print("------Iterativni  postupak------")
    print("Rezultat: %d" % rezultat)
    print("Vreme izvršavanja: %f" % vreme)

    # Izvršavanje binarne rekurzije
    start_time = time.time()
    rezultat = recursive_sum_binary(a)
    vreme = time.time() - start_time
    print("------Binarna rekurzija------")
    print("Rezultat: %d" % rezultat)
    print("Vreme izvršavanja: %f " % vreme)

