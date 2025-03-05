set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. Union (elements that are in set1 or set2 or both)
u= set1.union(set2)
print("Union", u)

# 2. Intersection (elements that are in both set1 and set2)
i = set1.intersection(set2)
print("I", i)

# 3. Difference (elements that are in set1 but not in set2)
d = set1.difference(set2)
print("Difference", d)

# 4. Symmetric Difference (elements that are in either set1 or set2, but not both)
s = set1.symmetric_difference(set2)
print("Symmetric Difference", s)

# 5. Subset (check if set1 is a subset of set2)
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

# 6. Superset (check if set1 is a superset of set2)
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)

# 7. Disjoint (check if set1 and set2 have no elements in common)
disjoint = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?", disjoint)

# 8. Adding an element to a set
set1.add(9)
print("Set1 after adding 9:", set1)

# 9. Removing an element from a set (using discard to avoid error if element is not found)
set1.discard(1)
print("Set1 after discarding 1:", set1)

# 10. Clearing all elements from a set
set1.clear()
print("Set1 after clearing all elements:", set1)
