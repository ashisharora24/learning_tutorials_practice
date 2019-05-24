# Print output as specified in the question.
# def intersection(list1,list2):
#     li=[]
#     for i in range(len(list1)):
#          for j in range(len(list2)):
#             if list1[i] == list2[j] :
#                 li.append(list1[i])
#                 break
#     m=len(li)
#     for i in range(len(li)):
#         print(li[i])
def intersection(m_array,n_array):
    for i in m_array:
        for j in range(len(n_array)):
            if i==n_array[j]:
                print(i)
                n_array.pop(j)
                break



n=int(input())
list1=[int(x) for x in input().split()]
print ("list1 : ",list1)
b=int(input())
list2=[int(x) for x in input().split()]
print ("list2 : ",list2 )
intersection(list1,list2)
