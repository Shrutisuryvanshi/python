# Sample dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Removing a key (e.g., 'a')
key_to_remove = 'a'
if key_to_remove in d:
    del d[key_to_remove]

# Printing the updated dictionary
print("Dictionary after removal:", d)
