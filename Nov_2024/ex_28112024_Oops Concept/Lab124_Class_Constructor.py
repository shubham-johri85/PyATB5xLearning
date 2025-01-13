class Dog:
    name = None
    breed = None
    height = None
    weight = None

    def __init__(self):  # ----->  Constructor (it is default constructor as it has no parameters or arguments)
        print("I will be called")

    def bark(self):
        print("barking")

    def sleep(self):
        print("sleeping")

    def talk(self):
        pass


chow_ref = Dog()
Mow_ref = Dog()

print(chow_ref.name)
