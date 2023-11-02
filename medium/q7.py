
def find_median(list1):
    list1.sort()
    
    n = len(list1)
    
    if n == 0:
        return None
    
    if n % 2 == 1:
        median = list1[n // 2]
    else:
        middle1 = list1[n // 2 - 1]
        middle2 = list1[n // 2]
        ans = (middle1 + middle2) / 2.0
    
    return ans

list1 = [7, 2, 5, 1, 9, 3]

median = find_median(list1)

if ans is not None:
    print("Median: {ans}")
else:
    print("The list is empty.")
