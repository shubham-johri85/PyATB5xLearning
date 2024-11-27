student_info = {
    "Name": "Amit",
    # "age": 65,
    "age": 67,
    "add": "KA"
}
print(student_info["Name"])
print(student_info["age"])
print(student_info["add"])
student_info["age"] = 100
print(student_info)

student_info2=dict(name="Shubham",age=39, role="SDET")
print(student_info2)

print("-----------------------------------")

# Dictionay within dictionary : -

emp_info= {
    "name": "Ram",
    "age": 37,
    "address": {
        "h.add": "GC",
        "o.add": "ND"
        }
}
print(emp_info)

