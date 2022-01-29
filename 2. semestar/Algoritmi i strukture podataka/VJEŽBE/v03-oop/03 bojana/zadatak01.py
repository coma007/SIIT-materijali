
class Rectangle(object):

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def set_a(self, a):
        self._a = a

    def set_b(self, b):
        self._b = b

    def obim(self):
        return 2*(self._a+self._b)

    def povrsina(self):
        return self._a*self._b

    def __str__(self):
        return "Rectangle(a=%f, b=%f)" % (self._a, self._b)

class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return "Square(a=%f)" % self._a

if __name__ == '__main__':

    rectangle = Rectangle(3, 4)
    print(rectangle, ": ")
    print("\tPovršina =", rectangle.povrsina())
    print("\tObim =", rectangle.obim())

    square = Square(5)
    print("\n", square, ": ")
    print("\tPovršina =", square.povrsina())
    print("\tObim =", square.obim())

    print("\nDužina stranice a kvadrata iznosi ", square.get_a())

    square.set_a(12)
    print("\n", square, ": ")
    print("\tPovršina =", square.povrsina())
    print("\tObim =", square.obim())
