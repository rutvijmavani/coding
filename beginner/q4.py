start = int(input("Enter value of start: "))
stop = int(input("Enter value of stop: "))

sum = 0

for i in range(start, stop + 1):    
    if i % 2 != 0:
        sum =sum+i

print("Sum of odd numbers between start and stop: {sum}")
