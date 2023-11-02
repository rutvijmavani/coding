def find_stone_piles(n):
    if n % 2 == 0:
        return [2] * (n // 2)
    else:
        return [2] * (n // 2) + [1]

n = int(input("Enter the number of stone piles (n): "))

stone_piles = find_stone_piles(n)

print("Number of stones in each pile:", stone_piles)
