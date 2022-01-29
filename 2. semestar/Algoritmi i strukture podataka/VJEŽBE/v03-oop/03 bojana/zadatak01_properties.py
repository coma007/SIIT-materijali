
class Rectangle(object):

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return

    @b.setter
    def b(self, b):
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

    # Ako implementiramo property, umesto get_a koristimo istu sintaksu kao kod direktnog pristupa ali se poziva metoda
    # sa nazivom a označena sa @property
    print("\nDužina stranice a kvadrata iznosi ", square.a)

    # Ako implementiramo property, umesto metode set_a koristimo istu sintaksu kao kod direktne dodele vrednosti
    # atributu a (poziva se metoda označena sa a.property)
    square.a = 12
    print("\n", square, ": ")
    print("\tPovršina =", square.povrsina())
    print("\tObim =", square.obim())

