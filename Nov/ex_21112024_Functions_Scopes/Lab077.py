public_toilet = "pb"


def home():
    private_toilet = "pt"
    print(public_toilet)
    print(private_toilet)


def stranger():
    print(public_toilet)
    # print(private_toilet) - NameError: name 'private_toilet' is not defined


stranger()
home()

print(public_toilet)
# print(private_toilet) - Not allowed outside the function
