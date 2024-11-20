"""
Create a program for sum of three numbers.
if user does not enter anything then use default as 100, 200 and 300
"""

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
num3 = int(input("Enter third number\n"))


def sum(num1=100, num2=200, num3=300):
    return num1 + num2 + num3


result = sum(num1, num2, num3)
print(result)

result2= sum()
print(result2)

result3= sum(2,3)
print(result3)

