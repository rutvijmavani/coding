def power_of_two(number):
    if number == 1:
        return True
    elif number % 2 != 0 or number == 0:
        return False
    else:
        return power_of_two(number // 2)

number = int(input("Enter a number: "))

ans = power_of_two(number)

if ans:
    print("number is a power of two.")
else:
    print("number is not a power of two.")
