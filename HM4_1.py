class Counter:
    def __init__(self, value=0):
        self.num = value
    def __iter__(self):
        return self
    def __next__(self):
        num = self.num
        self.num +=1
        return num
    def increase(self):
        num = self.num
        self.num += 1
        return num
    def decrease(self):
        num = self.num
        self.num -= 1
        return num
i = Counter()
print(i.increase())
print(i.increase())
print(i.increase())
print(i.decrease())
print(i.decrease())
print(i.decrease())
print(i.decrease())
