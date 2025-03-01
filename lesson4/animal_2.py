"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print("I am walking")


class Dog(Animal):

    def speak(self):
        print('Bark!')


class Cat(Animal):

    def speak(self):
        print('Meow!')



animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:
    animal.speak()
