# Ternary Operator ---- True if condition else False
# Program --> if age>= 18 you are allowed to vote else you are not allowed

age = int(input("Enter your age in years\n"))

# print("You are allowed to vote" if age>=18 else "You are not allowed") # --> using Ternary Operator

if age >= 18:
    print("You are allowed to vote")
else:
    print("you are not allowed")

