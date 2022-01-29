"""
Modul sadrži algoritme sortiranja bazirane na prioritetnom redu
"""
from pqueue import UnsortedPriorityQueue


def pq_sort(A):
    """
    Funkcija sortira listu koristeći dodatni prioritetni red

    Argument:
    - `A`: lista koja se sortira
    """
    size = len(A)
    pq = UnsortedPriorityQueue()

    # svi elementi liste prebacuju se u prioritetni red
    for i in range(size):
        element = A.pop()
        pq.add(element, element)

    # vraćanje elementa iz prioritetnog reda u listu
    for i in range(size):
        (k,v) = pq.remove_min()
        A.append(v)


def selection_sort(A):
    """
    Sortiranje selekcijom

    Argument:
    - `A`: lista koja se sortira
    """
    size = len(A)
    for i in range(size-1):
        # nalaženje najmanjeg elementa u nesortiranom delu liste 
        t_min = i
        for j in range(i+1, size):
            if A[j] < A[t_min]:
                t_min = j

        # najmanji element postavlja se na početak nesortiranog dela 
        if t_min != i:
            A[t_min], A[i] = A[i], A[t_min]


def insertion_sort(A):
    """
    Sortiranje umetanjem

    Argument:
    - `A`: lista koja se sortira
    """
    size = len(A)
    for i in range(1, size):
        # element koji se ubacuje u sortirani deo
        current = A[i]
        j = i-1

        # poredi trenutni sa elementima u sortiranom delu (levo od njega)
        while j > -1 and A[j] > current:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = current


def generator(n):
    """
    Generator test skupa

    Argument:
    - `n`: broj elemenata u skupu
    """
    for i in range(n):
        if i % 2 == 0:
            yield i
        else:
            yield i**2

if __name__ == '__main__':
    print('--------')
    print('PQ BASED')
    print('--------')
    aa = [n for n in generator(15)]
    print(aa)
    pq_sort(aa)
    print(aa)

    print('\n--------------')
    print('INSERTION SORT')
    print('--------------')
    bb = [n for n in generator(15)]
    print(bb)
    insertion_sort(bb)
    print(bb)

    print('\n--------------')
    print('SELECTION SORT')
    print('--------------')
    cc = [n for n in generator(15)]
    print(cc)
    selection_sort(cc)
    print(cc)
