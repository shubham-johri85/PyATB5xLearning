"""
Dictionary using two lists ---> for this we use zip method
"""

keys = ["name", "role", "exp"]
values = ["Ram", "SDET", 15]

my_dict = dict(zip(keys, values))
print(my_dict)

keys2 = ["name", "role", "exp"]
values2 = ["Ram", "SDET"]

my_dict2 = dict(zip(keys2, values2))
print(my_dict2)

# Merge two dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = dict1 | dict2
print(merged_dict)
print(merged_dict.get("c")) # print value of an element using get()
