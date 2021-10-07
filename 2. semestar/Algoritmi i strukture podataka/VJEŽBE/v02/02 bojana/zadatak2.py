"""
Program izračunava maksimalni element liste rekurzivnim putem.
"""

def find_max_with_len(seq, n):
    """
    Funkcija izračunava maksimalni element liste rekurzivnim putem.

    Argumenti:
    - `seq`: lista čiji maksimum se traži
    - `n`: broj preostalih elemenata za poređenje
    """

    # bazni slučaj
    if n == 1:
        return seq[0]
    else:
        max_remaining_el = find_max_with_len(seq, n-1)
        if max_remaining_el > seq[n-1]:
            return max_remaining_el
        else:
            return seq[n-1]


def find_max(seq):
    """
    Funkcija izračunava maksimalni element liste rekurzivnim putem.

    Argumenti:
    - `seq`: lista čiji maksimum se traži
    - `n`: broj preostalih elemenata za poređenje
    """

    # bazni slučaj
    if len(seq) == 1:
        return seq[0]
    else:
        max_remaining_el = find_max(seq[1:])
        if max_remaining_el > seq[0]:
            return max_remaining_el
        else:
            return seq[0]

def find_max_binary(seq):
    n = len(seq)
    if n == 1:
        return seq[0]
    else:
        middle = n//2
        first = find_max_binary(seq[:middle])
        second = find_max_binary(seq[middle:])
        if first > second:
            return first
        else:
            return second

def find_max_binary_limits(seq, begin, end):
    if begin >= end:
        return seq[begin]

    else:
        middle = (end + begin)//2
        first = find_max_binary_limits(seq, begin, middle)
        second = find_max_binary_limits(seq, middle+1, end)
        if first > second:
            return first
        else:
            return second

if __name__ == '__main__':
    seq = [88, 2, 123, 4, 11, 10, 19]
    length = str(len(seq))
    print("Solution with 2 params: max(" + length + ") = " + str(find_max_with_len(seq, len(seq))))
    print("Solution with 1 param: max(" + length + ") = " + str(find_max(seq)))
    print("Binary solution with 1 param: max(" + length + ") = " + str(find_max_binary(seq)))
    print("Binary solution with limits: max(" + length + ") = " + str(find_max_binary_limits(seq, 0, len(seq)-1)))

