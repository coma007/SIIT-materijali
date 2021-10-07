"""
Program demonstira jedan postupak rešavanja problema Hanojskih kula.
"""


def move(n, pole_a, pole_b, pole_c):
    """
    Funkcija rešava problem Hanojskih kula.

    Argumenti:
    - `n`: broj diskova
    - `pole_a`: ime polaznog stuba
    - `pole_b`: ime odredišnog stuba
    - `pole_c`: ime pomoćnog stuba
    """
    if n >= 1:
        # n-1 disk prebacuje se na pomoćni stub
        move(n-1, pole_a, pole_c, pole_b)

        # poslednji disk prebacuje se na odredišni stub
        print('Pomeram disk sa stuba %s na stub %s' % (pole_a, pole_b))

        # n-1 disk prebacuje se sa pomoćnog na odredišni stub
        move(n-1, pole_c, pole_b, pole_a)


if __name__ == '__main__':
    move(3, 'A', 'C', 'B')
