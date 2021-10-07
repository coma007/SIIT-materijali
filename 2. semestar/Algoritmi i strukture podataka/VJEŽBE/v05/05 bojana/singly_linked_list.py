class EmptyListException(Exception):
    pass

class SinglyLinkedListNode(object):
    """
        Klasa modeluje čvor - element jednostruke spregnute liste.
        Sastoji se od vrednosti i reference na sledeći element
    """
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @value.setter
    def value(self, value):
        self._value = value

    @next.setter
    def next(self, node):
        self._next = node

    def __str__(self):
        return str(self._value)


class SinglyLinkedList(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    '''
    Osnovne operacije liste
    '''
    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node
            current_node = current_node.next

    def get_first(self):
        if self.is_empty():
            raise EmptyListException("List is empty.")

        return self._head

    def get_last(self):
        if self.is_empty():
            raise EmptyListException("List is empty.")

        return self._tail

    def add_first(self, value):
        new_node = SinglyLinkedListNode(value)

        if self.is_empty():
            self._tail = new_node

        else:
            new_node.next = self._head.next

        self._head = new_node
        self._size += 1

    def add_last(self, value):
        new_node = SinglyLinkedListNode(value)

        if self.is_empty():
            # Inserted value creates first list node
            self._head = new_node
        else:
            # New node is inserted after the last existing one
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise EmptyListException("List is empty.")

        if self._size == 1:
            self._tail = None

        self._head = self._head.next
        self._size -= 1

    def remove_last(self):
        if self.is_empty():
            raise EmptyListException("List is empty.")

        if self._size == 1:
            self._head = None

        for node in self:
            if node.next == self._tail:
                node.next = None
                self._tail = node

                break

        self._size -= 1

    '''
    Dodatne operacije liste da bi se iskoristila sintaksa ugrađene liste
    '''
    def append(self, value):
        self.add_last(value)

    def extend(self, other_list):
        """
        Extends list with other_list elements.
        """
        for item in other_list:
            self.append(item)

    def insert(self, index, value):
        """
        Inserts value on given index. If index is out of range, element is inserted as last.
        :param index: number, position of new element
        :param value: new node value
        :return:
        """
        new_node = SinglyLinkedListNode(value)
        if self.is_empty():
            self._head = new_node
            return

        index = self._fix_index(index)

        if index == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            previous_node = self._get_node_by_index(index-1)
            new_node.next = previous_node.next
            previous_node.next = new_node

        self._size += 1

    def remove(self, value):
        previous_node = None
        current_node = self._head

        while current_node:
            if value == current_node.value:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self._head = current_node.next
                self._size -= 1
                return
            previous_node = current_node
            current_node = current_node.next

        raise ValueError("Value " + str(value) + " is not in list.")

    def pop(self, index = -1):
        if index < 0:
            index = len(self)+index

        del self[index]
        self._size -= 1

    def _fix_index(self, index, more_than_len_allowed=False):

        if not more_than_len_allowed and (-self._size>index or index>self._size):
            raise IndexError("list index out of range")

        if index < -self._size:
            return 0

        elif index < 0:
            return self._size + index + 1

        if index >= self._size:
            return self._size
        return index

    def _get_node_by_index(self, index):
        counter = 0
        current_node = self._head
        index = self._fix_index(index)

        while current_node and counter <= index:
            if counter == index:
                return current_node

            current_node = current_node.next
            counter += 1
        raise IndexError("List assignment index out of range")

    def __getitem__(self, index):
        return self._get_node_by_index(index).value

    def __setitem__(self, index, value):
        self._get_node_by_index(index).value = value

    def __delitem__(self, index):
        counter = 0
        previous_node = None
        current_node = self._head

        while current_node and counter <= index:
            if counter == index:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self._head = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next
            counter += 1
        raise IndexError("list assignment index out of range")

    def __add__(self, other):
        new_list = SinglyLinkedList()
        new_list.extend(self)
        new_list.extend(other)
        return new_list

    def __str__(self):
        ret = "["
        ret += ", ".join([str(item) for item in self])
        ret += "]"
        return ret


if __name__ == '__main__':

    L1 = SinglyLinkedList()
    L1.append(3)
    L1.append(7)
    for el in L1:
        print(el)
    L1[1] = 9
    print(L1[1])
    print(L1)
    print(len(L1))
    L2 = SinglyLinkedList()
    L2.append(99)
    L2.append(100)

    L1 += L2
    print(L1)

    L1.insert(2, "A")
    print(L1)


