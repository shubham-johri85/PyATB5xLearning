# Write a program to calculate evn and odd numbers.

num = int(input("enter number\n"))
result_even_odd = lambda num: "Even" if num % 2 == 0 else "odd"
print(result_even_odd(num))
