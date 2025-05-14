
list_of_unique_items= {2,4,3,7,8,2,5,7,4,1,8}
print(list_of_unique_items)

my_list = [1,3,1,4,3,5,2]
my_set = set(my_list)
print(my_set)

t=("Test", "For", "Test")
print(t)
print(set(t))


my_set = {1, 2, 3}  # create a set with elements 1, 2, and 3
my_set.add(4)  # add the element 4 to the set
print(my_set)  # prints {1, 2, 3, 4}
my_set.remove(1)
print(my_set)
my_set.discard(3)
print(my_set)

def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the map object to a list to see the results
squared_numbers = list(squared_numbers)
print(squared_numbers)


