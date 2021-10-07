"""
Modul sadrži implementaciju min heapa
"""
from pqueue import PQItem, PQError

class MinHeap(object):

    def __init__(self):
        self._data = []
        self._heap_size = 0

    def _left(self, index):
        """
        Metoda izračunava indeks levog potomka čvora.

        Argument:
        - `i`: indeks čvora čiji se potomak računa
        """
        return index*2+1

    def _right(self, index):
        """
        Metoda izračunava indeks desnog potomka čvora.

        Argument:
        - `i`: indeks čvora čiji se potomak računa
        """
        return index*2+2

    def _parent(self, index):
        """
        Metoda izračunava indeks roditelja čvora.

        Argument:
        - `i`: indeks čvora čiji se roditelj računa
        """
        return (index-1)//2

    def _swap(self, a, b):
        """
        Metoda menja vrednosti čvorova sa zadatim indeksima.

        Argument:
        - `a`: indeks prvog čvora
        - `b`: indeks drugog čvora
        """
        self._data[a], self._data[b] = self._data[b], self._data[a]

    def add(self, key, value=None):
        """
        Metoda dodaje novi element u heap
        :param key: prioritet novog čvora
        :param value: vrednost novog čvora
        """
        new_item = PQItem(key, value)
        self._data.append(new_item)
        self._heap_size += 1
        self._upheap(len(self._data)-1)

    def _upheap(self, index):
        """
        Metoda postavlja čvor na ispravnu poziciju poređenjem sa roditeljem
        :param index: pozicija čvora
        """
        parent_index = self._parent(index)
        if parent_index < 0 or self._data[index] > self._data[parent_index]:
            return
        self._swap(index, parent_index)
        self._upheap(parent_index)

    def min(self):
        """
        Pronalazi i vraća najmanji element heap-a
        :return: uređeni par (prioritet, vrednost) za minimalni element
        """
        if self.is_empty():
            raise PQError("Heap je prazan")
        return (self._data[0].key, self._data[0].value)

    def remove_min(self):
        """
        Uklanaj i vraća najmanji element heap-a
        :return: uređeni par (prioritet, vrednost) za minimalni element
        """
        if self.is_empty():
            raise PQError("Heap je prazan")

        self._swap(0, self._heap_size-1)
        ret_node = self._data.pop(self._heap_size-1)
        self._heap_size -= 1

        self._downheap(0)
        return (ret_node.key, ret_node.value)

    def _downheap(self, index):
        """
        Metoda (ponovo) uspostavlja ispravan redosled elemenata heap-a. Od tri čvora (roditelj, levo i desno dete),
        pronalazi se najmanji i on se postavlja na poziciju roditelja. Postupak se ponavlja dok svi elementi heap-a
        ne dođu u ispravan poredak.
        :param index: pozicija za koju se utvrđuje element
        """
        left_child = self._left(index)
        right_child = self._right(index)

        min_index = index

        if left_child < self._heap_size and self._data[left_child] < self._data[index]:
            min_index = left_child

        if right_child < self._heap_size and self._data[right_child] < self._data[min_index]:
            min_index = right_child

        if min_index != index:
            self._swap(min_index, index)
            self._downheap(min_index)

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)


if __name__ == '__main__':
    heap = MinHeap()
    heap.add(5)
    heap.add(10)
    heap.add(7)
    heap.add(4)
    heap.add(6)

    print(heap.remove_min())
    heap.add(17)
    heap.add(1)
    heap.add(3)
    print(heap.min())
    print(heap.remove_min())
    print(heap.remove_min())





