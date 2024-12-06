class father():

    def house(self):
        print("villa")


class shubham(father):

    def car(self):
        print("Santro")


class ram(father):

    def gold(self):
        print("1 kg of gold")


class tom(father):

    def land(self):
        print("2000sqft")


son1 = shubham()
son1.house()
son1.car()

son2 = ram()
son2.house()
son2.gold()

son3 = tom()
son3.house()
son3.land()

fat = father()
fat.house()
