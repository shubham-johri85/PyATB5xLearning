"""
Write a Python program to calculate the area of a circle. Take pi=3.14

"""
radius_circle = float(input("Enter the radius of a circle: "))
# print(radius_circle)
# pi = 3.14
# area_circle = pi * (radius_circle ** 2)
#
# print(f"The area of a circle is {area_circle}")


# Second way of doing this
import math
print(math.pi)
print(math.pow(radius_circle, 2))
area = math.pi * math.pow(radius_circle, 2)
print("area of a circle: ", area)

