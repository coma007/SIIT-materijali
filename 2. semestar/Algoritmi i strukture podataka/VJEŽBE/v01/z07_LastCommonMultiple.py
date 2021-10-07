# v01z07
# Naći najmanji broj koji je deljiv svim brojevima od 1 do 20.

from time import time


# Euclid algorithm
def greatest_common_divisor(num1, num2):

    gcd = 0
    while num2 != 0:
        gcd = num2
        num2 = num1 % num2
        num1 = gcd
    return gcd


def last_common_multiple(num1, num2):

    return num1 * num2 // greatest_common_divisor(num1, num2)


def interval_lcm(border):

    n = 1
    for i in range(n, border+1):
        n = last_common_multiple(n, i)
    return n


if __name__ == '__main__':

    print("------Last Common Multiple of First 20 Numbers------")

    start = time()
    print("\nLCM = ", interval_lcm(20))
    print("Elapsed time: ", time()-start)
