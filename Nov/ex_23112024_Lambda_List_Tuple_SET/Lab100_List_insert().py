my_list = [1, 2.9, "Three", True]
print(my_list)

print("Item at index 2-->", my_list[2])


print("----------------")

my_list.insert(2, 5)
print(my_list)
print("Item at index 2-->", my_list[2])


print("----------------")

my_list.insert(5, "New")
print(my_list)
print(len(my_list))

print("----------------")

my_list.insert(0, 0)
print(my_list)
print(len(my_list))