class Car:
    def __init__(self, mark, model, year, speed=0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speedup(self):
        return self.__speed + 5

    def speeddown(self):
        return self.__speed - 5

    def stop(self):
        return self.__speed - self.__speed

    def speedview(self):
        return self.__speed

    def backspeed(self):
            return self.__speed - self.__speed * 2


c = Car('BMW', 'X5', 2013, 15)
print(c.speedview())
print(c.speedup())
print(c.speeddown())
print(c.backspeed())
print(c.stop())