import os

try:
    path = os.getcwd()
    print(path)
    path_file = path + "/example.txt"
    print(path_file)
    file = open(path_file)
except Exception as fnfe:
    print("File not found, fix the path or create one")
finally:
    print("This code will be executed anyhow")
