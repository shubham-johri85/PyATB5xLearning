from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class dog(Animal):
    def make_sound(self):
        print("Bhaw Bark")
        print(self.name)


Shera = dog("shera")
Shera.make_sound()
