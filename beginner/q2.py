input_string = input("Enter a string: ")

no_letter = 0
no_digit = 0


for char in input_string:
    if char.isalpha():
        no_letter =no_letter+ 1
    elif char.isdigit():
        no_digit =no_digit+ 1


print("Number of Alphabets: {no_letter} &Number of  digits: {no_digit}")
