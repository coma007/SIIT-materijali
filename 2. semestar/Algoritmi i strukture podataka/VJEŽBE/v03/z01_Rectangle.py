# v03z01
# Napisati klasu Rectangle koja reprezentuje pravougaonik.
# Klasa sadrži metode za izračunavanje obima i površine pravougaonika.
# Na osnovu napisane klase izvesti klasu Square.


class Rectangle(object):

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    def area(self):
        return self._a * self._b

    def perimeter(self):
        return 2 * (self._a + self._b)


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)


if __name__ == '__main__':

    pravougaonik = Rectangle(1, 2)
    kvadrat = Square(5)

    print(f"Rectangle a = {pravougaonik.a} b = {pravougaonik.b}\nArea: {pravougaonik.area()}\nPerimeter: {pravougaonik.perimeter()}")
    print(f"\nSquare a = {kvadrat.a}\nArea: {kvadrat.area()}\nPerimeter: {kvadrat.perimeter()}")
