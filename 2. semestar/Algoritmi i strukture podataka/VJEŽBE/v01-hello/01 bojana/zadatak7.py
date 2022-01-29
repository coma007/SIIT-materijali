"""
Program izračunava najmanji broj deljiv svim brojevima od 1 do 20.
"""


def gcd(x, y):
    """
    Funkcija izračunava NZD dva broja.

    Argumenti:
    - `x`: prvi broj
    - `y`: drugi broj
    """
    while y != 0:
        x, y = y, x % y

    return x


def lcm(x, y):
    """
    Funkcija izračunava NZS dva broja.

    Argumenti:
    - `x`: prvi broj
    - `y`: drugi broj
    """
    return (x*y)/gcd(x, y)

if __name__ == '__main__':
    n = 1
    for i in range(1, 21):
        n = lcm(n, i)

    print('NZS [1,20] = %d' % n)
