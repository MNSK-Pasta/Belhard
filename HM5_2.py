from abc import ABC, abstractmethod

pi = 3.14


class Shape(ABC):
    @abstractmethod
    def get_perimeter(self):
        return self

    @abstractmethod
    def get_square(self):
        return self


class Circle(Shape):
    r: float

    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        self.r = 2 * pi * self.r
        return self.r

    def get_square(self):
        self.r = pi * self.r ** 2
        return self.r


class Rectangle(Shape):
    a: float
    b: float

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        self.a = 2 * (self.a + self.b)
        return self.a

    def get_square(self):
        self.a = self.a * self.b
        return self.a


class Square(Rectangle):
    def __init__(self, a, b=None):
        super(Square, self).__init__(a, b)
        self.b = self.a


c = Circle(10)
r = Rectangle(5, 4)
s = Square(2)
print(s.get_perimeter())
print(r.get_square())
print(c.get_square())
