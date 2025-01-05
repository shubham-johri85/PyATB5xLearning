class home:
    def __init__(self):
        self.public_var = "father"
        self.__private_var = "son"

    def mom(self):
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("Private Property")


C167 = home()
print(C167.public_var)
# print(C167.__private_var) --> can't be accessed directly
# C167.__wife()
C167.mom()
