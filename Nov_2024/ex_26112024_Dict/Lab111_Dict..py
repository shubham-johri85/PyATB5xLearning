my_dict = {
    "Name": "Aman",
    "Age": 34,
    "Role": "SDET",
    "Exp": 3
}

print(my_dict["Role"])

my_dict["Name"] = "Shubham"
my_dict["Exp"] = 15
my_dict["Place"] = "Noida"

print(my_dict)

del my_dict["Age"]

print(my_dict)

print("Place" in my_dict)
print("Age" in my_dict)

for key,value in my_dict.items():
    print(key,"--->",value)
