def decorator1(func):
    def wrapper():
        print("decorator 1")
        func()
    return wrapper # here no () is required in case of multiple decorator


def decorator2(func):
    def wrapper():
        print("decorator 2")
        func()
    return wrapper # here no () is required in case of multiple decorator

@decorator1
@decorator2
def say_hello():
    print("Hello")

say_hello() # In case of multiple decorators, we have to call the program function()
