def outer_function():
    var = 12

    def inner_function1():
        print(var) # inner function can use the variables defined in parent(outer) function

    def inner_function2():
        print(var) # inner function can use the variables defined in parent(outer) function

    inner_function1()
    inner_function2()


outer_function()
