"""
✅ Leap Year Checker:
Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.

"""

y = int(input("Enter the year\n"))

if y%4==0 or y%400==0 and y%100!=0:
    print("It is a leap year")
else:
    print("It is not a leap year")
