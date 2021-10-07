# v01z05
# Izračunati zbir prostih brojeva manjih od	2*10**6

from time import time


# Sieve Of Eratosthenes
def find_primes(border):

    numbers = [True] * border
    numbers[0] = numbers[1] = False
    prime = 2
    while prime * prime <= border:
        if numbers[prime]:
            for i in range(prime ** 2, border, prime):
                numbers[i] = False
        prime += 1

    for i in range(len(numbers)):
        if numbers[i]:
            yield i


def sum_primes(border):

    return sum(find_primes(border))


if __name__ == '__main__':

    print("------Sum of all prime numbers less than 2*10**6------")

    start = time()
    print("\nSum of primes: ", sum_primes(2*10**6))
    print("Elapsed time: ", time()-start)
