"""
Write a program to count a frequency of each charactor in string
string = "automation"
o/p = {a:2, u:1, t=2, o:2, m:1, i:1, n:1}
"""
string = "automation"
# string=input("Enter the string\n")
char_count = {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
