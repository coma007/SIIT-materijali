# v01z01
# Obrnuti redosled cifara broja n.

from time import time


def reverse_strign(number):

    number_string = str(number)
    return number_string[::-1]


def reverse_arithmetic(number):

    new_number = 0
    while number != 0:
        new_number *= 10
        new_number += number % 10
        number = number // 10
    return new_number


if __name__ == '__main__':

    print("------Number reverse------")

    start = time()
    print("\nString method: ", reverse_strign(12345))
    print("Elapsed time: ", time()-start)
    start = time()
    print("\nArithmetic method: ", reverse_strign(12345))
    print("Elapsed time: ", time()-start)

    # almost equal time even with really big numbers
