class grandfather:
    key = "2bhk"
    shares = "$1000"

    def grandfather_prop(self):
        print("A car --> Honda City")
        print(self.key)
        print(self.shares)


class father(grandfather):  # ---> Single Inheritance
    key2 = "Villa"

    def father_prop(self):
        print("Royal Enfield")
        print(self.key2)


class son(father):  # ---> Multilevel Inheritance
    key3 = "R15"

    def son_prop(self):
        print("A new Bike")
        print(self.key3)


SJ = son()
print(SJ.shares)
print(SJ.key2)
SJ.son_prop()
