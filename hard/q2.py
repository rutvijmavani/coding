with open("demo.txt", "r") as file:
    lines = file.readlines()

count = len(lines)

print("Number of lines in 'demo.txt': {count}")
