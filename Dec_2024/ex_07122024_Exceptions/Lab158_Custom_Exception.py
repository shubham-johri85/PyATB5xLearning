class LowBalanceCustomException(Exception):
    def __init__(self, message):
        self.message=message
        super().__init__(message)
balance=100
withdraw=int(input("Enter the amaount--> "))
if withdraw>balance:
    raise LowBalanceCustomException("Balance is low")
else:
    print("Remaining balance", (balance-withdraw))