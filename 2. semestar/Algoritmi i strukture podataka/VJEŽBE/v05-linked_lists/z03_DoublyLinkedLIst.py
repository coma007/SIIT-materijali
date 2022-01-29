# v05z03
# Implementirati klasu DoublyLinkedList

from z01_Node import Node


class EmptyListException(Exception):
    pass


class DoublyLinkedList(object):

    def __init__(self):
        self._head = Node(None)
        self._tail = Node(None)
        self._head.set_next(self._tail)
        self._tail.set_prev(self._head)

    def __iter__(self):
        current = self._head.get_next()
        while current is not self._tail:
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
        if node.get_prev() is self._head:
            self._head.set_next(node.get_next())
            node.get_next().set_prev(self._head)
        elif node.get_next() is self._tail:
            node.get_prev().set_next(self._tail)
            self._tail.set_prev(node.get_prev())
        else:
            next = node.get_next()
            previous = node.get_prev()
            previous.set_next(next)
            next.set_prev(previous)

    def __setitem__(self, index, value):
        self[index].set_data(value)

    def add_first(self, data):
        old_first = self._head.get_next()
        node = Node(data, old_first, self._head)
        old_first.set_prev(node)
        self._head.set_next(node)

    def append(self, data):
        node = Node(data)
        if self._head.get_next() == self._tail:
            self._head.set_next(node)
            node.set_prev(self._head)
            node.set_next(self._tail)
            self._tail.set_prev(node)
        else:
            self._tail.get_prev().set_next(node)
            node.set_prev(self._tail.get_prev())
            node.set_next(self._tail)
            self._tail.set_prev(node)

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
            self[i] = self[i].get_prev().get_data()
        self[index] = element
        if self[index].get_next() is not self._tail:
            self[index].set_next(self[index+1])
        if self[index].get_prev() is not self._head:
            self[index].set_prev(self[index-1])

    def extend(self, another_list):
        old_last = self._tail.get_prev()
        old_last.set_next(another_list.get_first().get_next())
        another_list.get_first().get_next().set_prev(old_last)
        self._tail = another_list.get_last()

    def remove_first(self):
        # if self._head.get_next == self._tail:
        #     raise EmptyListException("List is empty !")
        # self._head.set_next(self._head.get_next().get_next())
        # self._head.get_next().set_prev(self._head)
        del self[0]

    def remove_last(self):
        # # TODO
        # if self._head is None:
        #     raise EmptyListException("List is empty !")
        # current = self._head
        # while current.get_next() is not self._tail:
        #     current = current.get_next()
        # self._tail = current
        # self._tail.set_next(None)
        del self[-1]

    def is_empty(self):
        return self._head.get_next() == self._tail

    def get_first(self):
        return self._head

    def get_last(self):
        return self._tail

    def __str__(self):
        string = "["
        string += ", ".join([str(item) for item in self])
        string += "]"
        return string

    def insert_after(self, existing, new):
        new_node = Node(new)
        for node in self:
            if node.get_data() == existing:
                next = node.get_next()
                node.set_next(new_node)
                new_node.set_prev(node)
                next.set_prev(new_node)
                new_node.set_next(next)
                break

    def insert_before(self, existing, new):
        new_node = Node(new)
        for node in self:
            if node.get_data() == existing:
                prev = node.get_prev()
                node.set_prev(new_node)
                new_node.set_next(node)
                prev.set_next(new_node)
                new_node.set_prev(prev)
                break


if __name__ == '__main__':

    lista = DoublyLinkedList()

    print("Is the list empty: ", lista.is_empty(), " ", lista)
    lista.add_first('D')
    print("Added first element ! ", lista)
    lista.add_first('C')
    print("Added first element ! ", lista)
    lista.add_first('B')
    print("Added first element ! ", lista)
    lista.add_first('A')
    print("Added first element ! ", lista)
    print("Length of list: ", len(lista), " list: ", lista)
    lista.remove_first()
    print("Removed first element ! ", lista)
    lista.append("A")
    print("Added last element ! ", lista)
    print("List[-1]: ", lista[-1])
    lista.remove_last()
    print("Removed last element ! ", lista)
    lista.remove_first()
    print("Removed first element !", lista)
    lista.insert(0, "Mica")
    print("Inserted Mica at List[0] !", lista)
    print("Is the list empty: ", lista.is_empty(), " ", lista)
    lista[1] = "Boki"
    lista[-1] = "Mico"
    print("Changed List[1] to Boki and List[-1] to Mico", lista)

    print("\nLIST: ", lista)

    list2 = DoublyLinkedList()
    list2.append(1)
    list2.append(2)
    list2.append(3)

    lista.extend(list2)
    print("\nList has been extended by ", list2, " !")
    print("LIST NOW:", lista)

    lista.remove(2)
    print("\nRemoved 2 from list ! ", lista)

    lista.insert_after(1, "FTN")
    print("After 1 inserted FTN ! ", lista)
    lista.insert_before("Mica", "NS")
    print("Before Mica inserted NS ! ", lista)
