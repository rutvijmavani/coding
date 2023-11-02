def JtoI(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()

        corrected_data = data.replace("J", "I")

        print(corrected_data)
    
    except FileNotFoundError:
        print("File '{filename}' not found.")

JtoI("words.txt")
