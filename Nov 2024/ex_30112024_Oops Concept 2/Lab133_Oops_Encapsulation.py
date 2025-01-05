class car:
    def __init__(self):
        print("DC")
        self.password = "Shubham"  # --> Public instance variable
        self.__password_secure = "Shubham"  # --> Private instance variable

    def change_password(self):
        print(self.password)
        return "public"


my_car = car()
print(my_car.password)
my_car.change_password()
my_car.password = "Johri"
print(my_car.password)
my_car.change_password()

print(my_car.__password_secure)  # ---> 'car' object has no attribute '__password_secure'.
