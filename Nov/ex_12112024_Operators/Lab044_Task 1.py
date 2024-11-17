# Write a program to take user age and let him know if he can go to club. Age = 21

user_age = int(input("Enter your age in years\n"))

# print("You can go to club" if user_age>=21 else "You are not allowed") # --> using Ternary Operator

if user_age >= 21:
    print("You can go to club")
else:
    print("you are not allowed")
