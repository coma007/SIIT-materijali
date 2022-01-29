# v01z03
# Izračunati sumu svih	parnih elemenata (elemenata koji su parni brojevi) Fibonačijevog niza manjih od	4*10^6.

from time import time


def fibonacci_basic(number):

    if number == 0:
        return 1
    if number == 1:
        return 1
    else:
        return fibonacci_basic(number-1) + fibonacci_basic(number-2)


tmp = {}


def fibonacci_optimised(number):

    if number == 0:
        tmp[0] = 1
        return 1
    if number == 1:
        tmp[1] = 1
        return 1

    if number in tmp.keys():
        return tmp[number]
    else:
        tmp[number] = fibonacci_optimised(number-1) + fibonacci_optimised(number-2)
        return tmp[number]


def sum_fibonacci(border, func):

    sumy = 0
    number = 0
    index = 0
    while number < border:
        number = func(index)
        if number % 2 == 0:
            sumy += number
        index += 1
    return sumy


if __name__ == '__main__':

    print("------Sum of Fibonacci numbers------")

    start = time()
    print("\nSum (basic fibonacci): ", sum_fibonacci(4*10**6, fibonacci_basic))
    print("Elapsed time: ", time()-start)
    start = time()
    print("\nSum (optimised fibonacci): ", sum_fibonacci(4*10**6, fibonacci_optimised))
    print("Elapsed time: ", time()-start)
