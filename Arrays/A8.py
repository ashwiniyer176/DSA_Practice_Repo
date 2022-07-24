# Largest contiguous subarray
n = int(input("Enter number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter {i+1} ele:")))
# Kadane's Algorithm
max_so_far = float("-inf")
max_ending_here = 0
for i in arr:
    max_ending_here += i
    if max_so_far < max_ending_here:
        max_so_far = max_ending_here
    if max_ending_here < 0:
        max_ending_here = 0
print(max_so_far)
