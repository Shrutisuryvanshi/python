def multiply_list(sample_list):
    result = 1
    for num in sample_list:
        result *= num
    return result


sample_list = [8, 2, 3, -1, 7]
print(multiply_list(sample_list))  
