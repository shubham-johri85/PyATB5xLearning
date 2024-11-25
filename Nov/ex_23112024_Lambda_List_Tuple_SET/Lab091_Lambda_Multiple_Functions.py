# Write a program to calculate evn and odd numbers.

# def find_even_odd(num):
#     if num % 2 == 0:
#         print("number is even")
#     else:
#         print("number is odd")
#
# find_even_odd(8)

result_even_odd = lambda num: "Even" if num % 2 == 0 else "odd"
print(result_even_odd(9))
print(result_even_odd(916))
print(result_even_odd(1))
print(result_even_odd(88888888))

