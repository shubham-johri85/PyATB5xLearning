my_list=[1,5,3,8,2,8,9,6]
print(my_list)

my_list.sort()

print(my_list)

"""
Sorting will be done only on same data type.
"""

my_list2=[1,5,3,"two"] # not supported between instances of 'str' and 'int'.
my_list2.sort()
print(my_list2)