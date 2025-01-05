"""
User defined functions
1. They can't return -- non return
2. They can return something
3. They have parameters/arguments
4. They don't have parameters/arguments
"""


# 1. They can't return -- non return
# No return type and no parameters/arguments - NRNP

def nrnp():
    print("NRNP")


nrnp()


# 2. They can't return -- non return and with parameters/arguments
# No return type and have parameters/arguments - NRWP

def nrwp(name):
    print("hello", name)


nrwp("shubham")
nrwp("NRWP")


# 3. No return type and with default parameters/arguments or positional parameters/arguments - NRDP

def nrdp(name="shubham"):
    print("hello", name.upper())


nrdp()
nrdp("NRDP")


def multi_args(name1="A", name2="B"):
    print("Multiple--> ", name1, name2)


multi_args()
multi_args("shubham")
multi_args("shubham", "Johri")


# multi_args("shubham", "Johri", "Not allowed") --->TypeError: multi_args() takes from 0 to 2 positional arguments but 3 were given


# 4. Arguments + Return Type

def sum_of_two(a, b):
    return a + b


result = sum_of_two(4, 6)
print(result)


def sum_of_two_with_default(a=100, b=200):
    print("I will sum of two numbers")
    return a + b


result = sum_of_two_with_default(a=16, b=60)
result1 = sum_of_two_with_default()
print(result)
print(result1)


