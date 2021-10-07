"""
Program izračunava sumu liste rekurzivnim putem.
"""


def recursive_sum_linear(seq, n):
    """
    Funkcija izračunava sumu liste od n elemenata upotrebom linearne rekurzije.

    Argumenti:
    - `seq`: lista čija suma se izračunava
    - `n`: broj preostalih elemenata za sumiranje
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

    Argumenti:
    - `seq`: lista čija suma se izračunava
    """

    # bazni slučaj
    if len(seq) == 1:
        return seq[0]
    else:
        # izračunava se zbir poslednjeg i svih ostalih elemenata
        return recursive_sum_binary(seq[:len(seq)//2]) + recursive_sum_binary(seq[len(seq)//2:])

def iterative_sum(seq, n):
    sum = 0
    for element in seq:
        sum += element

    return sum


if __name__ == '__main__':
    a = [x for x in range(1, 998)]

    print("------Linearna rekurzija------")
    print("Rezultat: %d" % recursive_sum_linear(a, len(a)))

    print("------Binarna rekurzija------")
    print("Rezultat: %d" % recursive_sum_binary(a))


