def parse_string(string):
    parts = [part for part in string.split('000') if part]

    if len(parts) == 3:
        result = {
            "first_name": parts[0],
            "last_name": parts[1],
            "id": parts[2]
        }
        return result
    else:
        return None  

string = "Robert000Smith000123"
result = parse_string(string)

if result:
    print(result)
else:
    print("Invalid input format.")
