# Can create empty tuple
t = tuple()
print(t)

# convert a list to tuple
my_list=[1,2,3,45,7]
t = tuple(my_list)
print(t)

hero1=("Bratman", "BruceLee")
hero2=("supman", "spidman", "hman", "shakman")
new_tuple=(hero1, hero2)
print(new_tuple)
#   Out put will be tuple within tuple - (('Bratman', 'BruceLee'), ('supman', 'spidman', 'hman', 'shakman'))

print(new_tuple[0])
print(new_tuple[0][0])
print(new_tuple[1][1])