my_list = [1, 2.9, "Three", True]
print(my_list)

my_list.remove("Three")
print(my_list)

my_list[2] = 3  # Replacing the value at index 2
my_list[1] = 2
my_list.append(4)
print(my_list)

my_list.remove(1)
print(my_list)

"""
We can also copy the list
"""

new_copy_list = my_list.copy()
print(new_copy_list)
