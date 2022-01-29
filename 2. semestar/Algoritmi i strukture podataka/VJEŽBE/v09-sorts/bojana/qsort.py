"""
Modul sadrži implementaciju quick sort algoritma
"""
import random


def partition(A, left, right):
    """
    Funkcija vrši particionisanje niza nad zadatim intervalom

    Particionisanje niza vrši se dovođenjem elemenata u takav
    redosled da su svi elementi manji ili jednaki pivotu levo
    od njega, dok se elementi veći od pivota dovode na pozicije
    desno od njega.

    Argumenti:
    - `A`: niz koji se particioniše
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    # poslednji element postaje pivot
    pivot = A[right]

    # varijabla čuva indeks krajnjeg levog elementa (pod)sekvence
    i = left-1

    for j in range(left, right):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    i = i+1
    A[i], A[right] = A[right], A[i]
    return i


def sort(A, left, right):
    """
    Quick sort algoritam

    Argumenti:
    - `A`: niz koji se sortira
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    if left < right:
        pivot = partition(A, left, right)
        sort(A, left, pivot-1)
        sort(A, pivot+1, right)


def rpartition(A, left, right):
    """
    Funkcija vrši particionisanje niza nad zadatim intervalom

    Pre samog particionisanja niza, unosi se `šum` zamenom poslednjeg
    elementa niza (pivota) i nasumično odabranog elementa u nizu.

    Argumenti:
    - `A`: niz koji se particioniše
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    i = random.randrange(left, right)
    A[right], A[i] = A[i], A[right]
    return partition(A, left, right)


def rsort(A, left, right):
    """
    Quick sort uz randomized particionisanje

    Argumenti:
    - `A`: niz koji se sortira
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    if left < right:
        pivot = rpartition(A, left, right)
        rsort(A, left, pivot-1)
        rsort(A, pivot+1, right)


def tail_sort(A, left, right):
    """
    Quick sort, jedan rekurzivni poziv manje

    Argumenti:
    - `A`: niz koji se sortira
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    while left < right:
        pivot = rpartition(A, left, right)
        tail_sort(A, left, pivot-1)
        left = pivot + 1


if __name__ == '__main__':
    a = []
    for i in range(200):
        if i % 2 == 0:
            a.append(i)
        else:
            a.append(i**2)

    print(a)
    rsort(a, 0, len(a)-1)
    print(a)
