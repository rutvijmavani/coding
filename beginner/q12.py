num = int(input("Enter a number: "))

ans = 0

while num > 0:
    last_digit = num % 10
    ans = ans * 10 + last_digit
    num = num // 10

print("Reversed number: {ans}")
