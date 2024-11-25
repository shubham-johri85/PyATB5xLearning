cities = ("Goa", "Patna", "Pune", "Etah")
print("Pune" in cities)
print("Agra" in cities)

t = (12, 23, 34, 67)
# t.append(78) - AttributeError: 'tuple' object has no attribute 'append'

my_list = list(t)
my_list.append(78)
t = tuple(my_list)
print(t)
