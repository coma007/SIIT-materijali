"""
Modul sadrži različite implementacije reda sa prioritetom.
"""


class PQError(Exception):
    """
    Klasa modeluje izuzetke vezane za prioritetni red.
    """
    pass


class PQItem(object):
    """
    Klasa modeluje element prioritetnog reda.
    """
    __slots__ = '_key', '_value'

    def __init__(self, key, value):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    def __lt__(self, x):
        return self._key < x._key

    def __str__(self):
        return "(" + str(self._key) + ")"


class PriorityQueueBase(object):
    """
    Baza prioritetnog reda

    Klasa sadrži operacije nezavisne od organizacije strukture podataka
    koja se koristi za smeštanje elemenata prioritetnog reda.
    """
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return ', '.join('(%s, %s)' % (e.key, e.value) for e in self._data)

    def is_empty(self):
        """
        Metoda proverava da li je red prazan.
        """
        return len(self) == 0


class SortedPriorityQueue(PriorityQueueBase):
    """
    Klasa modeluje prioritetni red korišćenjem sortirane liste.
    """
    def __init__(self):
        super().__init__()
        #super(SortedPriorityQueue, self).__init__()


    def min(self):
        """
        Metoda omogućava pristup elementu sa najmanjim ključem.
        """
        if self.is_empty():
            raise PQError('Red je prazan.')

        min_item = self._data[0]
        return (min_item.key, min_item.value)

    def remove_min(self):
        """
        Metoda uklanja element sa najmanjim ključem.
        """
        if self.is_empty():
            raise PQError('Red je prazan.')

        removed = self._data.pop(0)
        return (removed.key, removed.value)

    def add(self, key, value):
        """
        Metoda dodaje novi element u red.
        """
        new_item = PQItem(key, value)

        last = len(self)-1
        position = 0

        # pronalaženje pozicije za dodavanje elementa
        for i in range(last, -1, -1):
            current_item = self._data[i]
            if not new_item < current_item:
                position = i+1
                break

        self._data.insert(position, new_item)


class UnsortedPriorityQueue(PriorityQueueBase):
    """
    Klasa modeluje prioritetni red korišćenjem nesortirane liste.
    """
    def __init__(self):
        super(UnsortedPriorityQueue, self).__init__()

    def _find_min(self):
        """
        Metoda pronalazi element sa najmanjim ključem.
        """
        if self.is_empty():
            raise PQError('Red je prazan.')

        min_item = self._data[0]
        size = len(self)
        for i in range(1, size):
            current_item = self._data[i]
            if current_item < min_item:
                min_item = current_item

        return min_item

    def min(self):
        """
        Metoda omogućava pristup elementu sa najmanjim ključem.
        """
        min_item = self._find_min()
        return (min_item.key, min_item.value)

    def remove_min(self):
        """
        Metoda uklanja element sa najmanjim ključem.
        """
        min_item = self._find_min()
        index = self._data.index(min_item)
        removed = self._data.pop(index)
        return (removed.key, removed.value)

    def add(self, key, value):
        """
        Metoda dodaje novi element u red.
        """
        new_item = PQItem(key, value)
        self._data.append(new_item)


if __name__ == '__main__':
    upq = UnsortedPriorityQueue()
    upq.add(3, 'abc')
    upq.add(2, 'ab')
    upq.add(1, 'a')
    upq.add(11, 'abcdefghijk')

    print('------------------------------')
    print('UNSORTED PRIORITY QUEUE')
    print('------------------------------')
    print('Content: %s' % upq)
    print('Minimum: (%s, %s)' % upq.min())
    print('------------------------------')
    print('Removed (%s, %s)' % upq.remove_min())
    print('------------------------------')
    print('Content: %s' % upq)
    print('Minimum: (%s, %s)' % upq.min())
    print('------------------------------')
    spq = SortedPriorityQueue()
    spq.add(3, 'abc')
    spq.add(2, 'ab')
    spq.add(1, 'a')
    spq.add(11, 'abcdefghijk')

    print('\n------------------------------')
    print('SORTED PRIORITY QUEUE')
    print('------------------------------')
    print('Content: %s' % spq)
    print('Minimum: (%s, %s)' % spq.min())
    print('------------------------------')
    print('Removed (%s, %s)' % spq.remove_min())
    print('------------------------------')
    print('Content: %s' % spq)
    print('Minimum: (%s, %s)' % spq.min())
