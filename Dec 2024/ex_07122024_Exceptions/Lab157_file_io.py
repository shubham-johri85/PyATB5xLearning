# file_name = "shubham.txt"
# content = "Created first file...Python"
#
# with open(file_name, "w") as file:
#     file.write(content)
#
# with open(file_name, "r") as file:
#     rf = file.read()
#     print(rf)
#
# with open(file_name, "a") as file:
#      file.write(". I also append the file")
#
# with open(file_name, "r") as file:
#     rf = file.read()
#     print(rf)
with open("sdet.txt", "x") as file:
     file.write("Hey! created new one also!!!")

with open("sdet.txt", "r") as file:
    rf = file.read()
    print(rf)