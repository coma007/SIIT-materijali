from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_value):
        self._x = new_value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_value):
        self._y = new_value

    def __str__(self):
        return "Point(x=" + str(self._x) + \
               ", y=" + str(self._y) + ")"

    def distance(self, other_point):
        x2 = other_point.x
        y2 = other_point.y
        x1 = self._x
        y1 = self._y

        return sqrt((x1-x2)**2+(y1-y2)**2)


if __name__ == '__main__':
    p1 = Point(4, 5)

    print(p1.x)
    p1.x = 5

    print(p1)

    p2 = Point()
    p2.x = 1
    p2.y = 4

    print(p1.distance(p2))
