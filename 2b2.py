def count_digits_and_letters(input_string):
    digits = 0
    letters = 0
    
    
    for char in input_string:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    
    return digits, letters


input_string = input("Enter a string: ")


digits, letters = count_digits_and_letters(input_string)


print(f"Number of digits: {digits}")
print(f"Number of letters: {letters}")
