from abc import ABC, abstractmethod

class PC(ABC):
    def __init__(self):
        print("PC Initiated")

class MotherBoard(PC):
    @abstractmethod
    def start(self):
        pass

class RAM(MotherBoard):
    @abstractmethod
    def read(self):
        pass

class Processor(RAM):
    @abstractmethod
    def run(self):
        pass

class Storage(Processor):
    @abstractmethod
    def store(self):
        pass


class MyComputer(Storage):

    def start(self):
        print("starting MotherBoard")

    def read(self):
        print("Read RAM")

    def run(self):
        print("Run Processor")

    def store(self):
        print("1TB storage")

    @staticmethod
    def LoadOs():
        return "Operating system loaded"

    def StartMouse(self):
        print("Mouse Connected")

    def UseHeadPhone(self):
        print("headphones connected")


    def Boot(self):
        self.start()
        self.read()
        self.run()
        self.store()
        print(MyComputer.LoadOs())
        self.StartMouse()
        self.UseHeadPhone()

test = MyComputer()
result = test.Boot()
print(result)
