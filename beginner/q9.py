input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

ans = {}

for i in input_list:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1

print("Frequency count: {ans}")
