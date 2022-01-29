"""
Program vrši konverziju broja iz dekadnog brojnog sistema u zadatu brojnu osnovu
na intervalu [2, 16].
"""

# moguće cifre na zadatom intervalu
DIGITS = "0123456789ABCDEF"


def convert(num, radix):
    """
    Funkcija vrši konverziju broja zadatog u dekadnom sistemu u string predstavu
    u zadatoj brojnoj osnovi.

    Argumenti:
    - `num`: zadati broj
    - `radix`: zadata brojna osnova
    """

    # bazni slučaj (cifra manja od brojne osnove)
    if num < radix:
        return DIGITS[num]
    else:
        return convert(num//radix, radix) + DIGITS[num % radix]


if __name__ == '__main__':
    num = int(input('Unesi broj: '))
    radix = int(input('Unesi osnovu: '))

    print(convert(num, radix))
