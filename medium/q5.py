def analyze_temp(temp_read):
    if not temp_read:
        return None  

    avg_temp = sum(temp_read) / len(temp_read)

    high_temp = max(temp_read)

    low_temp = min(temp_read)

    return {
        "Average Temperature": avg_temp,
        "Highest Temperature": high_temp,
        "Lowest Temperature": low_temp
    }


list1 = [25, 28, 21, 24, 27]

result = analyze_temperature(list1)

if result:
    for key, value in result.items():
        print("{key}: {value}")
else:
    print("No temperature readings provided.")
