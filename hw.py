def longest_ones(n):
    count = 0
    while n > 0:
        n = n & (n << 1)
        count  += 1
    return count
num = int(input("Enter a number: "))
print(f"Longest consecutive 1s: {longest_ones(num)}")