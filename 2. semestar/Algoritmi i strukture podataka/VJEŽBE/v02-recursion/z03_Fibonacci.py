# v02z03
# Izračunati n-ti Fibonačijev broj pomoću:
# 1. Linearne
# 2. Binarne rekurzije.
# Uporedite vreme izvršavanja za obe implementacije.

from time import time


# binary
def fib_binary(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib_binary(n-1) + fib_binary(n-2)


# linear
def fib_linear(n):

    if n == 1:
        return 1, 0

    (fib_n_minus_1, fib_n_minus_2) = fib_linear(n-1)

    return fib_n_minus_1 + fib_n_minus_2, fib_n_minus_1


def unpack_fib(n):

    return fib_linear(n)[0]


if __name__ == '__main__':

    print("------n-th Fibonacci number------")
    start = time()
    print("\nBinary result: ", fib_binary(40))
    print("Elapsed time: ", time() - start)
    start = time()
    print("\nLinear result: ", unpack_fib(40))
    print("Elapsed time: ", time() - start)
