class Phone:
    def __init__(self, name, brand, model, year):
        self.name = name
        self.brand = brand
        self.model = model
        self.year = year
    def receive_call(self):
        return f'Звонит {self.name}'
    def get_info (self):
        return self.brand, self.model, self.year
    def __str__(self):
        return f'Бренд {self.brand}, Модель {self.model}, Год {self.year}'
i = Phone('Виктор', 'Apple', '12 pro', 2021)
print(i)
print(i.receive_call())
