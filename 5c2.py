
d = {
    'x': list(range(11, 20)),  # List from 11 to 19
    'y': list(range(21, 30)),  # List from 21 to 29
    'z': list(range(31, 40))   # List from 31 to 39
}


fifth_values = {key: value[4] for key, value in d.items()}


print(d)
print(fifth_values)
