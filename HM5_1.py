from abc import ABC, abstractmethod


class Animal(ABC):
    name: str

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def says(self):
        return self


class Dog(Animal):
    def says(self):
        return f'{self.name} - собака. Говорит ГАВ!'


class Cat(Animal):
    def says(self):
        return f'{self.name} - кот. Говорит МЯУ!!'


class Cow(Animal):
    def says(self):
        return f'{self.name} - корова. Говорит МУУ!'


i = Dog('Бобик')
o = Cat('Барсик')
p = Cow('Буренка')
print(i.says())
print(o.says())
print(p.says())