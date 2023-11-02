def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

num = int(input("Enter a number: "))

sum_digits = num
while sum_digits > 9:
    sum_digits = sum_of_digits(sum_digits)

print(f"Sum of digits = {sum_digits}")
