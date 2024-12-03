class login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirmation(self):
        if (self.email == "shubham@test.com") and (self.password == "test123"):
            print("successfully logged in")
        else:
            print("Wrong Credentials")
        return "Thanks!!!!"


email = input("Enter the email\n")
password = input("Enter the password\n")

Shubham = login(email, password)
a = Shubham.login_confirmation()
print(a)
