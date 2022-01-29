# v04z04
# Implementirati klasu Deque

class FullDequeException(Exception):
    pass


class EmptyDequeException(Exception):
    pass


class Deque(object):

    def __init__(self, default_capacity=5):
        self._front = 0
        self._rear = 0
        self._size = 0
        self._capacity = default_capacity
        self._deque = [None] * default_capacity

    def __len__(self):
        return self._size

    def __str__(self):
        string = ''
        if self._rear > self._front:
            for index in range(self._front, self._rear):
                string += str(self._deque[index]) + ' '
            return string
        elif self._rear <= self._front:
            for index in range(self._front, self._capacity):
                string += str(self._deque[index]) + ' '
            for index in range(self._rear):
                string += str(self._deque[index]) + ' '
            return string
        if self._size == 0:
            raise EmptyDequeException("Empty deque.")

    def show_dequeue(self):
        for i in range(self._capacity):
            print((i-self._front) % self._capacity, ".", self._deque[i], end="\t")

    def is_empty(self):
        return self._size == 0

    def add_first(self, elem):
        if self._rear == self._front and self._size != 0:
            raise FullDequeException("Full deque !")
        if self._front != 0:
            self._front -= 1
        elif self._front == 0:
            self._front = self._capacity - 1
        self._deque[self._front] = elem
        self._size += 1

    def add_last(self, elem):
        if self._rear == self._capacity:
            for index in range(self._front):
                if self._deque[index] is None:
                    self._rear = index + 1
                    self._deque[index] = elem
                    self._size += 1
        elif (self._rear != self._front and self._rear < self._capacity) or self.is_empty():
            self._deque[self._rear] = elem
            self._rear += 1
            self._size += 1
        elif self._front == self._rear and self._size != 0:
            raise FullDequeException("Full deque !")

    def get_frist(self):
        if self.is_empty():
            raise EmptyDequeException("Empty deque !")
        return self._deque[self._front]

    def get_last(self):
        if self.is_empty():
            raise EmptyDequeException("Empty deque !")
        if self._rear == 0:
            return self._deque[self._capacity-1]
        else:
            return self._deque[self._rear-1]

    def remove_first(self):
        if self.is_empty():
            raise EmptyDequeException("Empty deque !")
        self._deque[self._front] = None
        self._size -= 1
        if self._front != self._capacity - 1:
            self._front += 1
        elif self._front == self._capacity - 1:
            self._front = 0

    def remove_last(self):
        if self.is_empty():
            raise EmptyDequeException("Empty deque !")
        self._deque[self._rear-1] = None
        self._size -= 1
        if self._rear == 0:
            self._rear = self._capacity - 1
        elif self._rear != 0:
            self._rear -= 1


if __name__ == '__main__':

    dek = Deque()
    dek.add_first("Mika") # 2
    dek.add_first("Zika") # 1
    dek.add_last("Tika") # 3
    dek.add_first("Ika")  # 0
    print("Deque: ", dek)
    dek.remove_first() # Zika Mika Tika
    print("Deque after removing first: ", dek)
    dek.add_first("Kika") # Kika Zika Mika Tika
    dek.remove_last() # Kika Zika Mika
    dek.add_last("Vika") # Kika Zika Mika Vika
    print("Queue after adding first and removing last: ", dek)
    print("Real configuration of queue: ", end=" ")
    dek.show_dequeue()
