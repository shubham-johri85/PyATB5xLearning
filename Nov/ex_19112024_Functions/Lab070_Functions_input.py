"""
Write a program to take user input and say hello to him.
"""

user_name = input("Enter your name\n")

def say_hello(name):
     print("hello", name)

say_hello(user_name) # No need to pass variable in parameters while defining function
