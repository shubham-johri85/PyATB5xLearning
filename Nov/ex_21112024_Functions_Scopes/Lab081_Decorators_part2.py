def add_before_after_test(func):
    def wrapper():
        print("Before running UI TC")
        print("Open browser")
        func()
        print("Ending UI TC")
        print("quit browser")
    return wrapper()



@add_before_after_test
def test_ui():
    print("I will test UI")
