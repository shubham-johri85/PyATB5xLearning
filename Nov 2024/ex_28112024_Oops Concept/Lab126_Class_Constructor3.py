class Person:
    name = None
    age = None
    mobile = None
    occupation = None

    def __init__(self):
        print("parameterized constructor ")
        self.name = input("Enter your name\n")
        self.age = int(input("Enter your age\n"))
        self.mobile = int(input("Enter your mobile\n"))
        self.occupation = input("Enter your occupation\n")

    def function_display(self):
        print("Name is", self.name)
        print("Age is", self.age)
        print("Mobile is", self.mobile)
        print("Occupation is", self.occupation)


new_person = Person()
new_person.function_display()
