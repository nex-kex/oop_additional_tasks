"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.subtract(<значение>)` вычитает указанное число из value
"""

class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, addition):
        self.value += addition
        return self.value

    def subtract(self, subtraction):
        self.value -= subtraction
        return self.value


# код для проверки 
n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.subtract(5)
print(n.get())  # 5
