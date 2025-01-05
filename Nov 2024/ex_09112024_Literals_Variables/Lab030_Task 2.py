"""
Take two inputs from user
print quotient and reminder

"""

num1 = input("Enter the dividend: ")
num2 = input("Enter the divisor: ")

num1 = int(num1)
num2 = int(num2)

q = num1 // num2
r = num1 % num2

# print("The quotient is", q)
# print("The reminder is", r)

print(f"The quotient is {q}")
print(f"The reminder is {r}")
