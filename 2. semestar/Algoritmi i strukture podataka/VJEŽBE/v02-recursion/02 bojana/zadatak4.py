"""
Program za replikaciju.
"""

import time


def replicate(number, times):
    """
    Funkcija umnožava zadati element zadati broj puta.

    Argumenti:
    - `number`: element koji se umnožava
    - `times`: broj umnožavanja
    """

    # bazni slučaj
    if times == 0:
        return []
    elif times == 1:
        return [number]
    else:
        return [number] + replicate(number, times-1)


if __name__ == '__main__':
    start_time = time.time()
    result = replicate(5,6)
    end_time = time.time()

    passed = end_time-start_time
    print('Elapsed time: %fs' % passed)
    print('Solution:' + str(result))


