class bank:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private
        self.balance = balance  # public

    def check_balance(self):
        print(self.balance)

    def deposit_amount(self, amount):
        self.balance = self.balance + amount

    def show_account(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not allowed")


icici = bank(12345, 500)
icici.deposit_amount(200)
icici.check_balance()
print(icici.balance)
# print(icici.__account_number)# 'bank' object has no attribute '__account_number'
icici.show_account(True)
