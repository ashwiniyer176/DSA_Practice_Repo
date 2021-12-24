# Largest contiguous subarray
n = int(input("Enter number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter {i+1} ele:")))

sum = [0 for i in range(n)]
big = 0
for i in range(n):
    for j in range(i + 1):
        sum[i] += arr[j]
    if sum[i] > big:
        big = sum[i]
print(big)
