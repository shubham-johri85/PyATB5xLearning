import os

print(os.getcwd())  # Returns current working directory

files = os.listdir(".")  # Returns list of files in current directory
print(files)

files2 = os.listdir("/Users/HP/PycharmProjects/PyATB5xLearning")  # Returns list of files in current path
print("files in current directory-->", files2)

# os.mkdir('New Directory') # --> Creates new directory under current working directory/folder

file_exists = os.path.exists("TestData.txt")
print(file_exists)
