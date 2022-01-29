# v04z03
# Implementirati klasu	Queue.
# U prvoj implementaciji, dozvolite neograničen broj elemenata
# Prepraviti prvu implementaciju tako da broj elemenata bude ograničen na N.
# U	cilju efikasnijeg upravljanja memorijskim prostorom, implementirati cirkularno smeštanje elemenata.


class EmptyQueueException(Exception):
    pass


class FullQueueException(Exception):
    pass


class LimitedQueue(object):

    def __init__(self, default_capacity):
        self._front = 0
        self._rear = 0
        self._size = 0
        self._capacity = default_capacity
        self._queue = [None] * default_capacity

    def __len__(self):
        return self._size

    def __str__(self):
        string = ''
        if self._rear > self._front:
            for index in range(self._front, self._rear):
                string += str(self._queue[index]) + ' '
            return string
        elif self._rear <= self._front:
            for index in range(self._front, self._capacity):
                string += str(self._queue[index]) + ' '
            for index in range(self._rear):
                string += str(self._queue[index]) + ' '
            return string
        if self._size == 0:
            raise EmptyQueueException("Empty queue.")

    def show_queue(self):
        for i in range(self._capacity):
            print((i-self._front) % self._capacity, ".", self._queue[i], end="\t")

    def is_empty(self):
        return self._size == 0

    def get_frist(self):
        if self.is_empty():
            raise EmptyQueueException("Empty queue !")
        return self._queue[self._front]

    def enqueue(self, elem):
        if self._rear == self._capacity:
            for index in range(self._front):
                if self._queue[index] is None:
                    self._rear = index + 1
                    self._queue[index] = elem
                    self._size += 1
        elif (self._rear != self._front and self._rear < self._capacity) or self.is_empty():
            self._queue[self._rear] = elem
            self._rear += 1
            self._size += 1
        elif self._front == self._rear and self._size != 0:
            raise FullQueueException("Full queue !")

    def dequeue(self):
        tmp = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return tmp


if __name__ == '__main__':

    queue = LimitedQueue(5)
    queue.enqueue("Mika") # 0
    queue.enqueue("Zika") # 1
    queue.enqueue("Tika") # 2
    queue.enqueue("Ika")  # 3
    print("Queue: ", queue)
    queue.dequeue() # Zika 0 Tika 1 Ika 2
    print("Queue after first dequeue: ", queue)
    queue.enqueue("Kika") # 3
    queue.enqueue("Vika") # 4
    print("Queue after two enqueues: ", queue)
    print("Real configuration of queue: ", end=" ")
    queue.show_queue()
    # queue.enqueue("Fika") -> baca exception



