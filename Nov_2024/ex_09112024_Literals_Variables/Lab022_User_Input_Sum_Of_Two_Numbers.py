# Write a program to take 2 user input
# Then Sum of these --> +
# Then Sub--> -, Mul--> *, DIv--> /
from ast import Param

# Logic Building
# step 1 --> Figuring Out I/O
# I/P --> num1, num2 --> int
# O/P --> sum--> int, sub--> int, div-->float

num1 = input("Enter the number 1") # here we can use num1=int(input("Enter the number 1")) instead of
                                   # declaring data type in row 14 and 15
num2 = input("Enter the number 2")

num1=int(num1) # Input() function always return string data type so we need to change the data type
num2=int(num2)

Sum = num1 + num2
Sub = num1 - num2
Mul = num1 * num2
Div = num1 / num2

print("Sum is", num1 + num2)
print("Sub is", num1 - num2)
print("Multiplication is", num1 * num2)
print("Division is", num1 / num2)

# print("Sum is", num1 + num2) ---> Can be write as this also with storing value in variable
# print("Sub is", num1 - num2)
# print("Multiplication is", num1 * num2)
# print("Division is", num1 / num2)

# step 2




# step 3
