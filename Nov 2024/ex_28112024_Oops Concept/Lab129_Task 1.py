"""
Create a Class PyATB , 5 Attributes, 3 Functions/Methods
Use PC - to set the value of the attributes
create a Print student information method/function
3 students objects
PyATB().print_student_infomation()
"""

class PyATB:
    s_name= None
    s_email= None
    s_mobile= None
    s_exp= None
    s_age= None

    def __init__(self, s_name, s_email, s_mobile, s_exp, s_age):
        print("PC called")
        self.s_name = s_name
        self.s_email = s_email
        self.s_mobile = s_mobile
        self.s_exp = s_exp
        self.s_age = s_age

    def student_profession(self):
        return "Thanks!!!"

    def print_student_Information(self):
        print("Name is", self.s_name)
        print("Email is", self.s_email)
        print("Mobile is", self.s_mobile)
        print("Exp is", self.s_exp)
        print("Age is", self.s_age)
        return "Thats it !!!"

student1=PyATB("Ram", "abc@test.com", 11111, 15, 40)
print(student1.print_student_Information())
print(student1.student_profession())

student2=PyATB("Shyam", "def@test.com", 22222, 6, 32)
print(student2.print_student_Information())
print(student2.student_profession())


student3=PyATB("Mohan", "ghi@test.com", 33333, 9, 29)
print(student3.print_student_Information())
print(student3.student_profession())






