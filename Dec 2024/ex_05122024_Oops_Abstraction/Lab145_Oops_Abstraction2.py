from abc import ABC, abstractmethod


class father(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class son(father):

    def loan(self):
        print("Loan paid by")
        print(self.name)

Shubham=son("Ram")
Shubham.loan()