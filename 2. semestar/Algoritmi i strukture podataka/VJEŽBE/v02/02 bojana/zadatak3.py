"""
Program izračunava n-ti Fibonačijev broj rekurzivnim putem.
"""

import time


def linear_fib(n):
    """
    Funkcija izračunava n-ti Fibonačijev broj pomoću linearne rekurzije.

    Argument:
    - `n`: pozicija u Fibonačijevom nizu
    """

    # bazni slučaj
    if n <= 1:
        return (n, 0)
    else:
        # uvek se izračunavaju poslednja dva broja u nizu
        (a, b) = linear_fib(n-1)
        return (a+b, a)


def binary_fib(n):
    """
    Funkcija izračunava n-ti Fibonačijev broj pomoću binarne rekurzije.

    Argument:
    - `n`: pozicija u Fibonačijevom nizu
    """

    # bazni slučaj
    if n <= 1:
        return n
    else:
        return binary_fib(n-1) + binary_fib(n-2)


if __name__ == '__main__':
    n = eval(input('Unesi broj n: '))
    # Izvršavanje linearne rekurzije
    start_time = time.time()
    rezultat = linear_fib(n)[0]
    vreme = time.time() - start_time
    print("------Linearna rekurzija------")
    print("Rezultat: %d" % rezultat)
    print("Vreme izvršavanja: %f" % vreme)

    # Izvršavanje binarne rekurzije
    start_time = time.time()
    rezultat = binary_fib(n)
    vreme = time.time() - start_time
    print("------Binarna rekurzija------")
    print("Rezultat: %d" % rezultat)
    print("Vreme izvršavanja: %f " % vreme)
