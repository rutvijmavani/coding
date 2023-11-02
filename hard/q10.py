def run_length_encode(string):
    if not string:
        return ""

    encoded_string = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            encoded_string += string[i - 1] + str(count)
            count = 1

    encoded_string += string[-1] + str(count)

    return encoded_string

string = "wwwwaaadebbbbbw"
result = run_length_encode(string)
print(result)
