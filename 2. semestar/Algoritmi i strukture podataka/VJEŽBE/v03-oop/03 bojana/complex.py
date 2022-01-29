class ComplexNumber(object):

    def __init__(self, real=0, imaginary=0):
        self._real = real
        self._imaginary = imaginary

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, new_value):
        self._real = new_value

    @property
    def imaginary(self):
        return self._imaginary

    @imaginary.setter
    def imaginary(self, new_value):
        self._imaginary = new_value

    def __str__(self):
        return str(self._real) + " + " + str(self._imaginary) + "i"

    def __add__(self, other_number):
        r2 = other_number.real
        i2 = other_number.imaginary
        r1 = self._real
        i1 = self._imaginary

        return ComplexNumber(r1+r2, i1+i2)

    def __sub__(self, other_number):
        r2 = other_number.real
        i2 = other_number.imaginary
        r1 = self._real
        i1 = self._imaginary

        return ComplexNumber(r1-r2, i1-i2)

if __name__ == '__main__':
    n1 = ComplexNumber(4, 5)

    print(n1.real)
    n1.real = 5

    n2 = ComplexNumber()
    n2.real = 1
    n2.imaginary = 4

    print(n1 - n2)
