# v01z02
# Naći najveći palindrom nastao kao proizvod dva trocifrena broja.

from time import time


def is_palindrome(number):

    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


# iterate from the biggest to the smallest number,
# if a palindrome found, it must be the largest for the first (bigger) factor,
# therefore, set the result to that palindrome and break,
# also break when the product becomes smaller than the result if palindrome not found
def iterate_for_palindrome():

    result = num1 = num2 = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if is_palindrome(i*j):
                if i*j > result:
                    result = i*j
                    num1 = i
                    num2 = j
                    break
            elif result > i*j:
                break

    return result, num1, num2


if __name__ == '__main__':

    print("------The biggest palindrome------")

    start = time()
    palindrome, number1, number2 = iterate_for_palindrome()
    print(f"\nThe biggest palindrome made of 3-digit numbers is: {palindrome} \nNumbers: {number1} and {number2}")
    print("Elapsed time: ", time()-start)
