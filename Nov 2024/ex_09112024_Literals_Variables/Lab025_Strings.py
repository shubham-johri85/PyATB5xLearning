name = "This is a line"
# name= name+1 -----> TypeError: can only concatenate str (not "int") to str
name = name + str(1)
print(name)
firstname = "Shubham"
lastname = "Johri"
fullname = firstname + " " + lastname
print(fullname)
