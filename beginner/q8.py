num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // find_gcd(a, b)


ans = lcm(num1, num2)
print("LCM of number1 and number2 is: {ans}")
