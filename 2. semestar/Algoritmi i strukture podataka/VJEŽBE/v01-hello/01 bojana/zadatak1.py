"""
Program vrši obrtanje redosleda cifara u zadatom broju.
"""

RADIX = 10


def str_rev(n):
    """
    Obrtanje redosleda cifara upotrebom stringova.

    Argument:
    - `n`: zadati broj
    """
    return int(str(n)[::-1])


def math_rev(n):
    """
    Obrtanje redosleda cifara upotrebom matematičkih operatora.

    Arguments:
    - `n`: zadati broj
    """
    r = 0
    while n > 0:
        r = RADIX*r + n % RADIX
        n //= RADIX

    return r

if __name__ == '__main__':
    num = input('Unesi broj: ')
    print('str_rev = %d' % str_rev(num))
    print('math_rev = %d' % math_rev(int(num)))