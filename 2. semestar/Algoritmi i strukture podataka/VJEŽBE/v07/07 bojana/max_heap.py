"""
Modul sadrži implementaciju heapa (sa akcentom na heap sort)
"""


class MaxHeap(object):
    """
    Klasa modeluje max heap.
    """
    def __init__(self, data):
        """
        Konstruktor.

        Konstruktor vrši inicijalizaciju liste podataka i njenu reorganizaciju
        u max heap.
        """
        # lista podataka
        self._data = data

        # broj elemenata na heapu (<= len(self._data))
        self._heap_size = len(self._data)
        
        # formiranje max heapa 
        self._build_max_heap()

    def _left(self, i):
        """
        Metoda izračunava indeks levog potomka čvora.

        Argument:
        - `i`: indeks čvora čiji se potomak računa
        """
        return 2*i + 1

    def _right(self, i):
        """
        Metoda izračunava indeks desnog potomka čvora.

        Argument:
        - `i`: indeks čvora čiji se potomak računa
        """
        return 2*i + 2

    def _swap(self, a, b):
        """
        Metoda menja vrednosti čvorova sa zadatim indeksima.

        Argument:
        - `a`: indeks prvog čvora
        - `b`: indeks drugog čvora
        """
        self._data[a], self._data[b] = self._data[b], self._data[a]

    def _max_heapify(self, i):
        """
        Metoda formira max-heap od podstabla sa korenom u čvoru i.

        Argument:
        - `i`: indeks korena podstabla
        """

        # određivanje levog i desnog potomka čvora
        left = self._left(i)
        right = self._right(i)

        # provera levog potomka
        #   - da li je još na heapu
        #   - da li je podatak levog veći od podatka korena
        if left < self._heap_size and self._data[left] > self._data[i]:
            largest = left
        else:
            largest = i

        # provera desnog potomka
        if right < self._heap_size and self._data[right] > self._data[largest]:
            largest = right

        # zameni vrednosti ako nisu u max-heap redosledu
        if largest != i:
            self._swap(i, largest)
            self._max_heapify(largest)

    def _build_max_heap(self):
        """
        Metoda vrši formiranje max heapa.
        """
        self._size = len(self._data)
        
        # svi elementi sa indeksom većim od n/2 biće listovi stabla 
        start = (self._size-1) // 2
        for i in range(start, -1, -1):
            self._max_heapify(i)

    def sort(self):
        """
        Heap sort algoritam
        """
        for i in range(self._size-1, 0, -1):
            # zameni prvi i poslednji 
            self._swap(0, i)

            # izbaci poslednji sa heapa
            self._heap_size -= 1

            # preostale elemente transformiši u max-heap
            self._max_heapify(0)

    def get_items(self):
        return self._data


if __name__ == '__main__':
    a = []
    for i in range(10):
        if i % 2 == 0:
            a.append(i)
        else:
            a.append(i**2)

    heap = MaxHeap(a)
    heap.sort()

    print(heap.get_items())
