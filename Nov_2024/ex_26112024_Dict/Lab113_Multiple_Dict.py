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

student_list=[student_info1,student_info2]
print(student_list)
print(student_list[0])
print(student_list[1])
print(student_list[0]["name"])
print(student_list[0]["address"])
print(student_list[0]["address"]["home_address"])
print(student_list[1]["age"])
