class person:
    id = None
    name = None
    age = None
    email = None

    def talk(self):  # No arg no return type
        print("I can Talk")

    def sleep(self, name):  # Arg with no return type
        print("I am a method")
        print("sleep", name)

    def sleep2(slef, name):  # Arg with return type
        print("I am a method")
        return None

    def walk(self):  # No arg with return type
        return "I am walking"


Shubham = person()
Shubham.id = 64682
Shubham.name = "Shubham Johri"
Shubham.age = 40
Shubham.email = "Shubham@test.com"

print(Shubham.talk())
print(Shubham.sleep("Ram"))
print(Shubham.sleep2("Shyam"))
print(Shubham.walk())
print(Shubham.name)
