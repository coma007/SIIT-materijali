"""
Program izračunava sumu prostih brojeva manjih od 2 000 000.
"""
import time

MAX_VALUE = 2000000


def is_prime(n):
    """
    Funkcija proverava da li je zadati broj prost pomoću probnih deljenja.

    Argument:
    - `n`: broj koji se proverava
    """
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    root = int(n**0.5) + 1
    for i in range(3, root, 2):
        if n % i == 0:
            return False

    return True


def es_simple(n):
    """
    Funkcija pronalazi proste brojeve manje od n pomoću Eratostenovog sita.

    Argument:
    - `n`: gornja granica
    """
    if n < 2:
        return []

    limit = int(n**0.5) + 1
    sieve = [True] * (n+1)

    # 0 i 1 nisu prosti brojevi
    sieve[0] = sieve[1] = False

    # parni brojevi nisu prosti
    for i in range(4, n+1, 2):
        sieve[i] = False

    # izbaci sve umnoške prostih brojeva
    for i in range(3, limit, 2):
        if sieve[i]:
            for j in range(i*i, n, 2*i):
                sieve[j] = False

    return [index for index, value in enumerate(sieve) if value]


def es_optimized(n):
    """
    Funkcija pronalazi proste brojeve manje od n pomoću optimizovanog
    Eratostenovog sita.

    Argument:
    - `n`: gornja granica
    """
    if n < 2:
        return []

    length = (n-1) // 2
    upper_bound = int(n**0.5) // 2

    sieve = [True] * (length+1)

    for num in range(upper_bound):
        if sieve[num]:
            step = num*2 + 3
            sieve[num+step:length:step] = [False] * (
                (length-num-step-1)//step + 1)

    return [2] + [i*2 + 3 for i in range(length) if sieve[i]]


if __name__ == '__main__':

    start_time = time.time()
    prime_sum = 0
    for i in range(2, MAX_VALUE):
        if is_prime(i):
            prime_sum += i
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Division by primes: %d' % prime_sum)
    print('Elapsed time: %fs' % elapsed_time)

    start_time = time.time()
    primes = es_simple(MAX_VALUE)
    result = sum(primes)
    end_time = time.time()
    print('Sieve of Eratosthenes (basic): %d' % result)
    elapsed_time = end_time - start_time
    print('Elapsed time: %fs' % elapsed_time)

    start_time = time.time()
    primes = es_optimized(MAX_VALUE)
    result = sum(primes)
    end_time = time.time()
    print('Sieve of Eratosthenes (optimized): %d' % result)
    elapsed_time = end_time - start_time
    print('Elapsed time: %fs' % elapsed_time)
