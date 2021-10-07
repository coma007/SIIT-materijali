"""
Program izračunava sumu parnih Fibonačijevih brojeva manjih od 4 000 000.
"""
import time

MAX_VALUE = 4000000


def fibonacci():

    previous, current, fib_sum = 0, 1, 0

    while current <= MAX_VALUE:
        if current % 2 == 0:
            fib_sum += current

        previous, current = current, previous+current

    return fib_sum


def fibonacci_steps():
    '''
    Ovo rešenje se bazira na na pretpostavci da je svaki treći element Fibonačijevog niza paran broj
    na osnovu čega se izdvaja formula za njegovo izračunavanje.
    '''
    previous, current, fib_sum = 2, 3, 0

    while previous <= MAX_VALUE:

        fib_sum += previous

        new_previous = previous + 2 * current
        new_current = 2 * previous + 3 * current

        previous, current = new_previous, new_current

    return fib_sum


if __name__ == '__main__':

    start_time = time.time()
    fib_sum = fibonacci()
    end_time = time.time()

    passed = end_time-start_time
    print('Elapsed time: %fs' % passed)
    print('Solution: %d' % fib_sum)

    start_time = time.time()
    fib_sum = fibonacci_steps()
    end_time = time.time()

    passed = end_time-start_time
    print('Elapsed time %fs' % passed)
    print('Solution: %d' % fib_sum)


