def count_pairs(arr, K):
    element_count = {}

    pair_count = 0

    for num in arr:
        diff = K - num

        if diff in element_count:
            pair_count += element_count[diff]

        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    return pair_count

arr = [1, 2, 3, 4, 5]
k = 6

ans = count_pairs(arr, k)

print("Pair count: {ans}")
