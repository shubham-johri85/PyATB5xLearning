# Find the first non-repeating character in string using sets.

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1: #  return number of occurrences of value'
            return char

    return None

print(first_non_repeating("swiss"))
print(first_non_repeating("papa"))
print(first_non_repeating("pepper"))
