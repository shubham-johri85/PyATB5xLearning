set1 = {"tta.com", "sdet.live", "tta.com."}
print(set1)
print(len(set1))

for i in set1:
    print(i)
set1.add("Shubham")
set1.add("Shubham")
print(set1)  # It will just add only one time as duplicates are not allowed.

