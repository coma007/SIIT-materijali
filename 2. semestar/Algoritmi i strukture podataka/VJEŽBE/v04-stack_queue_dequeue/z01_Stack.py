# v04z01
# Implementirati klasu Stack.
# U prvoj implementaciji dozvoliti neograničen broj elemenata
# Kreirati klasu LimitedStack čiji je broj elemenata ograničen (ograničenje se zadaje prilikom kreiranja).
# U	slučaju da se pokuša dodavanje elementa u pun stek baca se FullStackException


class Stack(object):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        strng = ''
        for index in range(len(self._data)-1, -1, -1):
            strng += str(self._data[index]) + '\n'
        return strng

    def is_empty(self):
        return len(self._data) == 0

    def push(self, elem):
        self._data.append(elem)

    def pop(self):
        if self.is_empty():
            raise EmptyStackException("Stack is empty")
        return self._data.pop()

    def top(self):
        if len(self._data) == 0:
            raise EmptyStackException("Stack is empty")
        return self._data[-1]


class LimitedStack(Stack):

    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity

    def push(self, elem):
        if len(self._data) < self._capacity:
            super().push(elem)
        else:
            raise FullStackException("Stack is full !")


class FullStackException(Exception):
    pass


class EmptyStackException(Exception):
    pass


if __name__ == '__main__':

    string = "Milica"

    stack = Stack()
    for character in string:
        stack.push(character)
    print(stack)

    lim_stack = LimitedStack(5)
    for character in string:
        lim_stack.push(character)
        print(lim_stack)
