"""
Exceptions are handled using try and except block.
try:
    # Try this code,if error
except:
    # Execute me if try has some errors
"""

print("---Start of Program---")
try:
    a = int(input("Enter a first number\n"))  # -->Can get ValueError if enter string
    b = int(input("Enter a second number\n"))  # -->Can get ValueError if enter string
    c = a / b  # --> Can get ZeroDivisionError if enter b=0
    print("Result is-->", c)
except Exception as e:
    print(e)
    print("---End of Program---")
