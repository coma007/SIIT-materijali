def find_sum_iter(n):
    """
    Funkcija izračunava sumu prvih n prirodnih brojeva iterativnim postupkom.

    Argumenti:
    - `n`: broj prirodnih brojeva koji se sabiranju
    """
    sum = 0
    for number in range(1, n+1):
        sum += number
    return sum

def find_sum_recursive(n):
    """
    Funkcija izračunava sumu prvih n prirodnih brojeva rekurzivnim postupkom.

    Argumenti:
    - `n`: broj prirodnih brojeva koji se sabiranju
    """

    # bazni slučaj
    if n == 1:
        print("sum(1) = 1")
        return 1
    else:
        sum_remaining = find_sum_recursive(n-1)
        return sum_remaining+n

if __name__ == '__main__':
    n = int(input("Unesite n: "))
    print("Ukupna suma: " + str(find_sum_recursive(n)))