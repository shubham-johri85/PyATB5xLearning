"""✅ Grade Calculator:
Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F)
based on the following grading scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
"""
score = int(input("Enter your score\n"))

if score >= 90 and score <= 100:
    print("your grade is A")
elif score >= 80 and score <= 89:
    print("your grade is B")
elif score >= 70 and score <= 79:
    print("your grade is C")
elif score >= 60 and score <= 69:
    print("your grade is D")
elif score >= 0 and score <= 59:
    print("your grade is F")
else:
    print("As per grading system your score is not valid")
