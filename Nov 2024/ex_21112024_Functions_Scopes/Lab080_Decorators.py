def decorator(func):
    def wrapper():
        print("Before driving take your car papers and driving licence")
        func()  # This is taking function as drive_car()
        print("Nice!! put your documents back")

    return wrapper()


@decorator
def drive_car():
    print("i am driving")

@decorator
def drive_friend_car():
    print("This is amazing")

# We can use single decorator to multiple functions.