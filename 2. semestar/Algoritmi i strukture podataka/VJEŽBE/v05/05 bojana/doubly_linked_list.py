class EmptyListException(Exception):
    pass

class DoublyLinkedListNode(object):
    """
        Klasa modeluje čvor - element dvostruko spregnute liste.
        Sastoji se od vrednosti i reference na dva elementa - prethodni i sledeći
    """
    def __init__(self, value, previous_node=None, next_node=None):
        self._value = value
        self._next = next_node
        self._previous = previous_node

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @value.setter
    def value(self, value):
        self._value = value

    @next.setter
    def next(self, node):
        self._next = node

    @previous.setter
    def previous(self, node):
        self._previous = node

    def __str__(self):
        return str(self._value)

class DoublyLinkedList(object):

    def __init__(self):
        self._head = DoublyLinkedListNode(None)
        self._tail = DoublyLinkedListNode(None, None, self._head)
        self._head.next = self._tail
        self._size = 0

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def __iter__(self):
        current_node = self._head.next
        while current_node != self._tail:
            yield current_node
            current_node = current_node.next

    def get_first(self):
        if self.is_empty():
            raise EmptyListException("List is empty.")

        return self._head.next

    def get_last(self):
        if self.is_empty():
            raise EmptyListException("List is empty.")

        return self._tail.previous

    def add_first(self, value):
        new_node = DoublyLinkedListNode(value)

        if self.is_empty():
            self._tail.previous = new_node

        else:
            new_node.next = self._head.next
            self._head.next.previous = new_node
            new_node.previous = self._head

        self._head.next = new_node
        self._size += 1

        return new_node

    def add_last(self, value):
        new_node = DoublyLinkedListNode(value)

        if self.is_empty():
            # Inserted value creates first list node
            self._head.next = new_node
        else:
            # New node is inserted after the last existing one
            new_node.next = self._tail
            self._tail.previous.next = new_node
            new_node.previous = self._tail.previous

        self._tail.previous = new_node
        self._size += 1

        return new_node

    def remove_first(self):
        if self.is_empty():
            raise EmptyListException("List is empty.")

        if self._size == 1:
            to_remove = self._head.next
            self._tail.previous = self._head
            self._head.next = self._tail

        else:
            to_remove = self._head.next
            new_first = self._head.next.next
            new_first.previous = self._head
            self._head.next = new_first

        self._size -= 1
        return to_remove

    def remove_last(self):
        if self.is_empty():
            raise EmptyListException("List is empty.")

        if self._size == 1:
            to_remove = self._tail.previous
            self._head.next = self._tail
            self._tail.previous = self._head

        else:
            to_remove = self._tail.previous
            new_last = self._tail.previous.previous
            new_last.next = self._tail
            self._tail.previous = new_last

        self._size -= 1
        return to_remove

    def insert_after(self, node1, new_value):

        new_node = DoublyLinkedListNode(new_value)
        node1.next.previous = new_node
        new_node.next = node1.next
        node1.next = new_node
        new_node.previous = node1

        self._size += 1

        return new_node

    def insert_before(self, node1, new_value):

        new_node = DoublyLinkedListNode(new_value)
        node1.previous.next = new_node
        new_node.previous = node1.previous
        node1.previous = new_node
        new_node.next = node1

        self._size += 1

        return new_node

if __name__ == '__main__':

    L1 = DoublyLinkedList()
    n1 = L1.add_last(3)
    n2 = L1.add_last(7)
    n3 = L1.add_first(1)
    for el in L1:
        print(el)

    print(len(L1))

    L1.insert_before(n3, 99)

    for el in L1:
        print(el)





