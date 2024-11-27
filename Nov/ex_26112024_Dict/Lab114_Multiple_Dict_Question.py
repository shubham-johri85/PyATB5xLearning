# Print office address of Manu.

student_info1={
    "name":"Ram",
    "age":39,
    "address":{
        "home_address":"C-167",
        "office_address":"ABC"
    }
}

student_info2={
    "name":"shyam",
    "age":40,
    "address":{
        "home_address":"C-22",
        "office_address":"ABC"
    }
}

student_info3={
    "name":"Manu",
    "age":67,
    "address":{
        "home_address":"20150",
        "office_address":"BSL"
    }
}
student_list=[student_info1,student_info2,student_info3]
print(student_list[2]["address"]["office_address"])

"""
Alternate way - 
print(student_info3["address"]["office_address"])
"""
