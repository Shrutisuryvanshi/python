def is_palindrome(input_string):
    cleaned_string =input_string.replace(" ", " ").lower()
    if cleaned_string == cleaned_string[::-1]:
        return true
    else:
        return false

input_string = input("enter a string:")
if is_palindrome(input_string):
    print("the string is a palindrome.")
else:
        print("the string is not palindrome.")
    
