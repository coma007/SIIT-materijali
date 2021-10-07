# v05z01
# Implementirati klasu Node	koja odgovara jednom elementu liste.

class Node(object):

    def __init__(self, data, next=None, prev=None):
        self._data = data
        self._next = next
        self._prev = prev

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next

    def get_prev(self):
        return self._prev

    def set_prev(self, new_prev):
        self._prev = new_prev

    def __eq__(self, other):
        return self._data == other.get_data()

    def __str__(self):
        return str(self._data)
