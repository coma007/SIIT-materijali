"""
Modul sadrži implementaciju deka na osnovu liste.
"""


class DequeError(Exception):
    """
    Klasa modeluje izuzetke vezane za klasu Deque.
    """
    pass


class Deque(object):
    """
    Implementacija deka na osnovu liste.
    """

    def __init__(self, capacity=10):
        """
        Konstruktor.

        Argument:
        - `capacity`: inicijalni broj raspoloživih mesta
        """
        # broj elemenata u deku
        self._size = 0

        # indeks prvog elementa deka
        self._first = 0

        # broj mesta u deku
        self._capacity = capacity
        self._data = [None]*self._capacity

    def __len__(self):
        return self._size

    def is_empty(self):
        """
        Metoda proverava da li je dek prazan.
        """
        return self._size == 0

    def first(self):
        """
        Metoda omogućava pristup prvom elementu deka.
        """
        if self.is_empty():
            raise DequeError('Dek je prazan.')
        return self._data[self._first]

    def last(self):
        """
        Metoda omogućava pristup poslednjem elementu deka.
        """
        if self.is_empty():
            raise DequeError('Dek je prazan.')

        # indeks poslednjeg elementa
        last = (self._first+self._size-1) % self._capacity
        return self._data[last]

    def add_first(self, e):
        """
        Metoda dodaje element na početak deka.

        Argument:
        - `e`: novi element
        """
        # dupliranje kapaciteta ukoliko je dek popunjen
        if self._size == self._capacity:
            self._resize(2*self._capacity)

        # indeks novog elementa (prvi pre trenutno prvog)
        self._first = (self._first-1) % self._capacity
        self._data[self._first] = e
        self._size += 1

    def add_last(self, e):
        """
        Metoda dodaje element na kraj deka.

        Argument:
        - `e`: novi element
        """
        # dupliranje kapaciteta ukoliko je dek popunjen
        if self._size == self._capacity:
            self._resize(2*self._capacity)

        # indeks novog elementa (prvi iza trenutno poslednjeg)
        index = (self._first+self._size) % self._capacity
        self._data[index] = e
        self._size += 1

    def delete_first(self):
        """
        Metoda izbacuje prvi element iz deka.
        """
        if self.is_empty():
            raise DequeError('Dek je prazan.')

        element = self._data[self._first]

        # brisanje se vrši postavljanjem sadržaja na vrednost None
        self._data[self._first] = None

        # pomeranje indeksa prvog elementa
        self._first = (self._first+1) % self._capacity
        self._size -= 1

        # kapacitet se polovi kada je popunjeno manje od 1/4 kapaciteta
        if 0 < self._size < self._capacity//4:
            self._resize(self._capacity//2)

        return element

    def delete_last(self):
        """
        Metoda izbacuje poslednji element iz deka.
        """
        if self.is_empty():
            raise DequeError('Dek je prazan.')

        # indeks poslednjeg elementa
        last = (self._first+self._size-1) % self._capacity
        element = self._data[last]

        # brisanje se vrši postavljanjem sadržaja na vrednost None
        self._data[last] = None
        self._size -= 1

        # kapacitet se polovi kada je popunjeno manje od 1/4 kapaciteta
        if 0 < self._size < self._capacity//4:
            self._resize(self._capacity//2)

        return element

    def _resize(self, capacity):
        """
        Metoda vrši skaliranje kapaciteta deka.

        Argument:
        - `capacity`: novi kapacitet
        """
        current_data = self._data
        current_first = self._first

        # kreira se "prazna" lista sa zadatim brojem mesta
        self._data = [None]*capacity

        # prepisivanje trenutnog sadržaja u novu listu
        for k in range(self._size):
            self._data[k] = current_data[current_first]
            current_first = (current_first+1) % self._capacity

        self._first = 0
        self._capacity = capacity


if __name__ == '__main__':
    d = Deque()
    d.add_last(5)
    d.add_first(7)
    d.add_first(3)
    print(d.first())

    d.delete_last()
    print(len(d))

    d.delete_last()
    d.delete_last()
    d.add_first(6)
    print(d.last())

    d.add_first(8)
    print(d.is_empty())
    print(d.last())
