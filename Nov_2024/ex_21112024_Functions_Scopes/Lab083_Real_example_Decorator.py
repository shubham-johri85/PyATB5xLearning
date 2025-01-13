import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print("end_time")
        print("Total time taken by Function is--> ", end_time - start_time)
    return wrapper

def print_logs(func):
    def wrapper():
        print("logs generated for function")
        func()
        print("logs available")
    return wrapper


@time_decorator
@print_logs
def test_ui1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)  # This means it will wait for 2 seconds
test_ui1()

@time_decorator
@print_logs
def test_ui2():
    print("Add a function, time taken by this function 2")
#     time.sleep(4)  # This means it will wait for 4 seconds
test_ui2()