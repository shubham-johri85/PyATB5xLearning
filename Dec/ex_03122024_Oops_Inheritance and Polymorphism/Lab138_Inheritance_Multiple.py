class father():

    def father_prop(self):
        return 1000

    def home(self):
        return "From Father"


class mother():

    def mother_prop(self):
        return 5000

    def home(self):
        return "From Mother"


class son(mother, father):  # --> Multiple Inheritance
    def print_info(self):
        print("Received with thanks")


SJ = son()
SJ.print_info()
print(SJ.home())
"""
Here if we have same attributes,like home here, in parent classes then it will print attribute 
from the first class called in child class (Firstclass, secondclass)
"""
print(SJ.father_prop() + SJ.mother_prop())
