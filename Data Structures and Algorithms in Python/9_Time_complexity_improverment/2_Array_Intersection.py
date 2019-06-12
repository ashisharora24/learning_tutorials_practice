def intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    if len(arr2) < len(arr1):
        arr1, arr2 = arr2, arr1
    temp_start = 0
    for i in range(len(arr1)):
        for j in range(temp_start, len(arr2)):
            if arr1[i] == arr2[j]:
                temp_start = j+1
                print(arr1[i])
                break


# Main
# n1 = int(input())
# arr1 = list(int(i) for i in input().strip().split(' '))
# n2 = int(input())
# arr2 = list(int(i) for i in input().strip().split(' '))
arr1 = [10, 2, 9, 2, 1, 7, 6, 5]
arr2 = [9, 1, 5, 6, 3, 5, 2, 1]
intersection(arr1, arr2)
