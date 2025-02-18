def remove_odd_index_characters(input_string):
    
    result = "".join(input_string[i] for i in range(len(input_string))if i % 2 ==0)
    return result


input_string = input("enter a string:")


result = remove_odd_index_charecters(input_string)


print(f"string after removing cha racter with odd index values: {result}")
