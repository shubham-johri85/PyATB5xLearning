global_v = 12


def my_function():
    local_v = 22  # local variable within function and cannot be used outside it
    print(local_v)
    print(global_v)


my_function()

print(global_v)  # global variable outside function and can be used outside it
