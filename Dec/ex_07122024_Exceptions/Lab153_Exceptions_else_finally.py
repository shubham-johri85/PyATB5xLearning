try:
    a = int(input("Enter first Number\n"))
    b = int(input("Enter first Number\n"))
    c = a / b
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Result is-->", c)
finally:
    print("finally Code will always execute")
