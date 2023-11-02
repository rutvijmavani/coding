def count_vowels(string):
    string = string.lower()
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
    
    return count

string = "Hello, World!"

ans = count_vowels(string)

print("Number of vowels: {ans}")
