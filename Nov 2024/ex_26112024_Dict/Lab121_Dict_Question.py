"""
Remove the duplicates from below list
my_list=[1,2,2,3,4,4,5]

"""

my_list = [1, 2, 2, 3, 4, 4, 5]
set_my_list = set(my_list)
new_list = list(set_my_list)
print(new_list)
