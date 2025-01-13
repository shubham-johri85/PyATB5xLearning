class car:
    def __init__(self, o_name, o_make, o_model):
        self.o_name = o_name
        self.o_make = o_make
        self.o_model = o_model

    def start_engine(self):
        print("Starting the car with-->", self.o_name)
        print("Starting the car with-->", self.o_make)
        print("Starting the car with-->", self.o_model)
        return "lets go!!!"


Object_ref1 = car("Merc", "TCT", "2024")
a = Object_ref1.start_engine()
print(a)

Object_ref2 = car("Audi", "Q3", "2019")
a = Object_ref2.start_engine()
print(a)
