class father:
    key = "2bhk"
    shares = "$1000"

    def father_prop(self):
        print("A car --> Honda City")
        print(self.key)
        print(self.shares)


class son(father):  # ---> Single Inheritance
    key2 = "Villa"

    def son_prop(self):
        print("Royal Enfield")
        print(self.key2)


# DK=father()
# DK.father_prop()
SK = son()
print(SK.shares)
SK.son_prop()
SK.father_prop()
