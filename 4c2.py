original_set = {10, 20, 30, 40}


shallow_copy_set = original_set.copy()


shallow_copy_set.add(50)
shallow_copy_set.remove(20)


print("Original set:", original_set)
print("Shallow copy set:", shallow_copy_set)
