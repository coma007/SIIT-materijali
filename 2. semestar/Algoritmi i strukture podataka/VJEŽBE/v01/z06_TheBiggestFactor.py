# v01z06
# Naći najveći prost delitelj zadatog broja n

from time import time


def factorize(number):

    if number == 1:
        return number
    factor = 2
    while number > 1:
        if number % factor == 0:
            number //= factor
        else:
            factor += 1
    return factor


if __name__ == '__main__':

    print("------The Biggest Prime Factor of the Number n------")

    start = time()
    n = 1929837192847
    print(f"\nThe biggest factor of {n} is {factorize(n)}")
    print("Elapsed time: ", time()-start)
