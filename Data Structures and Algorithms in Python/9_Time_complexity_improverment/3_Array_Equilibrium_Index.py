def equilibriumIndex(arr):
    right_sum = 0
    for i in range(1, len(arr)):
        right_sum = right_sum + arr[i]
    left_sum = 0
    for i in range(1, len(arr)-1):
        left_sum = left_sum + arr[i-1]
        right_sum = right_sum - arr[i]
        if left_sum == right_sum:
            return i
    return -1

# Main
# n = int(input())
# arr = [int(i) for i in input().strip().split()]
n = 7
arr = [-7, 1, 5, 2, -4, 3, 0]
print(equilibriumIndex(arr))
