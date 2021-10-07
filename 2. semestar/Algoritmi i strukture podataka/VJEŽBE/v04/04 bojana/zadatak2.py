"""
Program vrši konverziju broja iz dekadnog brojnog sistema u zadatu brojnu osnovu
na intervalu [2, 16].
"""
from stack import Stack

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
    stack = Stack()

    while num > 0:
        rem = num % radix
        stack.push(rem)
        num = num//radix

    result = ""
    while not stack.is_empty():
        result += DIGITS[stack.pop()]

    return result


if __name__ == '__main__':
    num = int(input('Unesi broj: '))
    radix = int(input('Unesi osnovu: '))

    print(convert(num, radix))
