"""
✅ Triangle Classifier:

Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.

"""

side1 = float(input("Enter the length of side1--> "))
side2 = float(input("Enter the length of side2--> "))
side3 = float(input("Enter the length of side3--> "))

if side1 > 0 and side2 > 0 and side3 > 0:
    if (side1 + side2 > side3) or (side1 + side3 > side2) or (side3 + side2 > side1):
        if side1 == side2 == side3:
            print("The triangle is equilateral")
        elif side1 == side2 or side2 == side3 or side3 == side1:
            print("The triangle is isosceles")
        else:
            print("The triangle is scalene")
    else:
        print("Not a triangle")
else:
    print("Not a valid length")
