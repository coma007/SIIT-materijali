# v05z02
# Implementirati klasu LinkedList

from z01_Node import Node


class EmptyListException(Exception):
    pass


class SinglyLinkedList(object):

    def __init__(self, head=None):
        self._head = head
        self._tail = head

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current
            current = current.get_next()

    def __len__(self):
        length = 0
        for node in self:
            length += 1
        return length

    def __getitem__(self, my_index):
        index = 0
        if my_index < 0:
            my_index += len(self)
        for node in self:
            if index == my_index:
                return node
            index += 1
            if index >= len(self):
                raise IndexError("Index out of range !")

    def __delitem__(self, index):
        if index < 0:
            index = len(self) + index
        node = self[index]
        if node == self._head:
            self._head = node.get_next()
        elif node == self._tail:
            self[index-1].set_next(None)
            self._tail = self[index-1]
        else:
            previous = self[index - 1]
            previous.set_next(node.get_next())

    def __setitem__(self, index, value):
        self[index].set_data(value)

    def add_first(self, data):
        node = Node(data, self._head)
        self._head = node
        if self._tail is None:
            self._tail = self._head

    def append(self, data):  # add_last
        node = Node(data)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.set_next(node)
            self._tail = node

    def remove(self, element):
        for i in range(0, len(self)):
            if self[i].get_data() == element:
                del self[i]
                break

    def insert(self, index, element):
        self.append(None)
        if index < 0:
            index += len(self)
        for i in range(len(self)-1, index, -1):
            self[i] = self[i-1].get_data()
        self[index] = element
        if self[index] != self._tail:
            self[index].set_next(self[index+1])

    def extend(self, another_list):
        self._tail.set_next(another_list.get_first())
        self._tail = another_list.get_last()

    def remove_first(self):
        # if self._head is None:
        #     raise EmptyListException("List is empty !")
        # self._head = self._head.get_next()
        # # TODO update tail
        del self[0]

    def remove_last(self):
        # if self._head is None:
        #     raise EmptyListException("List is empty !")
        # current = self._head
        # while current.get_next() is not self._tail:
        #     current = current.get_next()
        # self._tail = current
        # self._tail.set_next(None)
        del self[-1]

    def is_empty(self):
        return self._head == self._tail

    def get_first(self):
        return self._head

    def get_last(self):
        return self._tail

    def __str__(self):
        string = "["
        string += ", ".join([str(item) for item in self])
        string += "]"
        return string


if __name__ == '__main__':

    lista = SinglyLinkedList()

    print("Is the list empty: ", lista.is_empty(), " ", lista)
    lista.add_first('D')
    print("Added first element ! ", lista)
    lista.add_first('C')
    print("Added first element ! ", lista)
    lista.add_first('B')
    print("Added first element ! ", lista)
    lista.add_first('A')
    print("Added first element ! ", lista)
    lista.remove_last()
    print("Removed last element ! ", lista)
    lista.append('E')
    print("Added last element ! ", lista)
    lista.append('F')
    print("Added last element ! ", lista)
    lista.append('G')
    print("Added last element ! ", lista)
    lista.append('H')
    print("Added last element ! ", lista)
    lista.append('I')
    print("Added last element ! ", lista)
    print("Is list empty ?", lista.is_empty())
    lista.remove('G')
    print("Element G removed ! ", lista)
    lista.remove_first()
    print("First element removed ! ", lista)
    print("List[-2]: ", lista[-2])
    del lista[-2]
    print("Deleted List[-2] ! ", lista)
    lista[2] = 'Mica'
    print("Added Mica to List[2] ", lista)
    lista[3] = 'Boki'
    print("Added Boki to List[3] ", lista)
    lista[4] = 'Mico'
    print("Added Mico to List[4] ", lista)
    print("First element of the list: ", lista.get_first().get_data())
    print("Last element of the list: ", lista.get_last().get_data())
    lista.insert(1, "FTN")
    print("FTN inserted at List[1] ", lista)
    lista.insert(-1, "NS")
    print("NS inserted at List[-1] ", lista)

    print("\nLIST: ", lista)

    list2 = SinglyLinkedList()
    list2.append(1)
    list2.append(2)
    list2.append(3)

    lista.extend(list2)
    print("\nList has been extended by ", list2, " !")
    print("LIST NOW:", lista)

