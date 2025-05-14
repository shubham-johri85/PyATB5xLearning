class Dog:
    name = None
    breed = None
    height = None
    weight = None

    def __init__(self, name, breed):  # --->  Constructor (it is parameterized constructor as it has parameters or arguments)
        print("parameterized constructor ")
        self.name = name
        self.breed = breed

    def bark(self):
        print("barking")

    def sleep(self):
        print("who is sleeping-->" + self.name)

    def talk(self):
        pass


chow_ref = Dog("chow", "pug")
print(chow_ref.name, "-->", chow_ref.breed)
chow_ref.sleep()
print(
    id(chow_ref))  # id - Return the identity of an object.This is guaranteed to be unique among simultaneously existing objects.
# (Python uses the object's memory address.)

print("-------------------------------------------")
Mow_ref = Dog("Mow", "German Shephard")
print(Mow_ref.name, "-->", Mow_ref.breed)
Mow_ref.sleep()
print(id(Mow_ref))
