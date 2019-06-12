arr = [1, 2, 5, 4, 6, 8, 9, 2, 1, 4, 5, 8, 9, 8]
v = 0
for i in range(len(arr)):
    print(v)
    v = v ^ arr[i]
print("final V : ", v)
