arr = []
n = int(input("Enter number of terms in array:"))
for i in range(1, n + 1):
    x = int(input("Enter element"))
    if i < n:
        arr.append(x)
    elif i == n:
        arr.insert(0, x)
print(arr)
