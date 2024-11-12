"""
Take three input from user and perform
Sum
Sub
Mul
Div
"""

fvalue = float(input("Enter 1st value"))
svalue = float(input("Enter 2st value"))
tvalue = float(input("Enter 3st value"))

sum = fvalue + svalue + tvalue
sub = fvalue - svalue - tvalue
mul = fvalue * svalue * tvalue
div = fvalue / svalue / tvalue

print("The sum is",sum)
print("The sub is",sub)
print("The mul is",mul)
print("The div is",div)
