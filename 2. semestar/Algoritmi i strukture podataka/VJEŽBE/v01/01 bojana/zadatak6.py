"""
Program izračunava najveći prost delitelj zadatog broja.
"""


def factorize(n):
    """
    Funkcija vrši faktorizaciju zadatog broja.

    Argument:
    - `n`: broj koji se faktoriše
    """
    if n == 1:
        return n

    f = 2
    while n > 1:
        if n % f == 0:
            n //= f
        else:
            f += 1

    return f


if __name__ == '__main__':
    num = int(input('Number: '))
    print('Result: %d' % factorize(num))
