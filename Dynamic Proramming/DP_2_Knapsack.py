knapsack_wt = 10
num_of_items = 4

values = [10, 40, 30, 50]
weights = [5, 4, 6, 3]

mat = [[0 for i in range(knapsack_wt+1)] for j in range(num_of_items+1)]

for i in range(1, num_of_items+1):
    for j in range(1, knapsack_wt+1):
        maxValueWithoutCurrent = mat[i-1][j]
        maxValueWithCurrent = 0
        if weights[i-1] <= j:
            maxValueWithCurrent = values[i-1]
            remainingCapacity = j-weights[i-1]
            maxValueWithCurrent += mat[i-1][remainingCapacity]
        mat[i][j] = max(maxValueWithCurrent, maxValueWithoutCurrent)
print(f"Max possible values are:{mat[num_of_items][knapsack_wt]}")
