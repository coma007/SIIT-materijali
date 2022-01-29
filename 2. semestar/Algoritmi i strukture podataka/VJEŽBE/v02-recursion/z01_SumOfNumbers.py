# v02z01
# Naći sumu prvih n	prirodnih brojeva rekurzivnim putem.


def sum_recursion(n):

    if n == 1:
        return 1
    return n + sum_recursion(n-1)


if __name__ == '__main__':

    print("------Sum of n numbers - recursion------")
    number = 500
    print(f"\nSum of first {number} numbers: {sum_recursion(number)}")
