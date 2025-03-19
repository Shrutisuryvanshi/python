def reverse_string(s):
    for char in reversed(s):
        yield char


input_string = "hello"
reversed_str = ''.join(reverse_string(input_string))
print(reversed_str)  
