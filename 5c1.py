from collections import defaultdict


keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]


result = defaultdict(list)


for i in range(len(keys)):
    result[keys[i]].append(values[i])


print(result)
