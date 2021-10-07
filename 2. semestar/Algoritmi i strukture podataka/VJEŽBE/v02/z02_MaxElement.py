# v02z02
# Naći maksimalni element niza rekurzivnim putem.


def max_recursion_linear(array):

    if len(array) == 1:
        return array[0]
    elif array[0] > max_recursion_linear(array[1:]):
        return array[0]
    else:
        return max_recursion_linear(array[1:])


def max_recursion_binary(array):

    if len(array) == 1:
        return array[0]
    middle = len(array) // 2
    if max_recursion_binary(array[:middle]) > max_recursion_binary(array[middle:]):
        return max_recursion_binary(array[:middle])
    else:
        return max_recursion_binary(array[middle:])


if __name__ == '__main__':

    print("------Max element of the Array - recursion------")
    n = [1, 2, 3, 2, 20, 4, 5, 6, 7, 2]
    print(f"\nLinear - The max element of {n} is: {max_recursion_linear(n)}")
    print(f"Binary - The max element of {n} is: {max_recursion_binary(n)}")
