class TV:

    def __init__(self, display, diag, resolution):
        self.__display = display
        self.__diag = diag
        self.__resolution = resolution

    def charect(self):
        return f'Характеристики ТВ: {self.__display, self.__diag, self.__resolution}'

    @property
    def diag(self):
        return self.__diag

    @diag.setter
    def diag(self, diag):
        self.diag = diag

    @property
    def resolution(self):
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution):
        self.__resolution = resolution

    @property
    def display(self):
        return self.display

    @display.setter
    def display(self, display):
        self.__display = display

    def resol(self):
        if self.__resolution == '4K':
            return 'ТВ с высоким разрешением'
        else:
            return 'Обычный ТВ'


t = TV('OLED', 55, '4K')
t.display = 'QLED'
print(t.charect())


class Mobile:

    def __init__(self, model, RAM, proc):
        self.__RAM = RAM
        self.__proc = proc
        self.__model = model

    @property
    def RAM(self):
        return self.__RAM

    @RAM.setter
    def RAM(self, RAM):
        self.__RAM = RAM

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def proces(self):
        return self.__proc

    @proces.setter
    def proces(self, proc):
        self.__proc = proc

    def charect(self):
        return f'Характеристики:{self.__model, self.__proc, self.__RAM}'

    def cong(self):
        if self.__model == 'Apple':
            return f'Поздравляем у вас {self.__model}'
        elif self.__model == 'Samsung':
            return f'Поздравляем у вас {self.__model}'
        else:
            return 'Обычное ведро'


m = Mobile('Samsung', 8, 'Exynos2200')
m.model = 'Xiaomi'
print(m.cong())


class Watch:
    def __init__(self, batary, size, color):
        self.__batary = batary
        self.__size = size
        self.__color = color

    @property
    def batary(self):
        return self.__batary

    @batary.setter
    def batary(self, batary):
        self.__batary = batary

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def charct(self):
        if self.__size > 47 or self.__color == 'Pink':
            return f'Характристики женских часов: {self.__batary}, {self.__color}, {self.__size}'
        else:
            return f'Характристики мужских часов: {self.__batary}, {self.__color}, {self.__size}'

    def batarylow(self):
        return f'Заряд батареи равен {self.__batary - self.__batary + 5}%, зарядите аккумулятор'


w = Watch(100, 46, 'Black')
print(w.batarylow())