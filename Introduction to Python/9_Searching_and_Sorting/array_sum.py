m = int(input())
arr1 = [int (x) for x in input().split()[:m]]
n = int(input())
arr2 = [int (x) for x in input().split()[:n]]
arr3 = []
len1 = len(arr1)
len2 = len(arr2)

if len1 > len2:
  while len(arr1) > len(arr2):
    arr2.insert(0,0)
else:
  while len(arr1) < len(arr2):
    arr1.insert(0,0)

#print(arr1)
#print(arr2)
for i in range(0, len(arr1)):
  arr3.insert(0,0)

#print(arr3)
carry = 0
for i in range(len(arr1) - 1, -1, -1):
  sum = arr1[i] + arr2[i]
  #print(sum)
  if sum > 9 and i == 0:
    carry = 1
    arr1[i-1] = arr1[i-1] + 1
    arr3[i] =  sum % 10
  elif sum > 9:
    arr1[i-1] = arr1[i-1] + 1
    arr3[i] =  sum % 10
  else:
    arr3[i] =  sum

if carry:
  print(carry, end = ' ')
  for ele in arr3:
    print(ele, end = ' ')
else:
  print(0, end = ' ')
  for ele in arr3:
    print(ele, end = ' ')
