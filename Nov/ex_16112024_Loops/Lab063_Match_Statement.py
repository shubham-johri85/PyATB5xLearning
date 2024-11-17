"""
match statement is similar to switch in java
match the op and execute
python>3.10

match variable:
  case pattern 1:
    #code block
  case pattern 2:
    #code block
"""

# Write a program to ask a user on which browser he wants to run the automation

browser_name = input("Enter browser name\n")
match browser_name:
    case "chrome":
        print("Executing the code in chrome")
    case "edge":
        print("Executing the code in Edge")
    case "safari":
        print("Executing the code in Safari")
    case "firefox":
        print("Executing the code in firefox")
    case _:
        print("Browser not found!!!")