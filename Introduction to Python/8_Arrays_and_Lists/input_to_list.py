# # n = int(input("Enter number of elements : "))
# #
# # li=[]
# # for i in range(n):
# #     c=int(input("Enter "+str(i)+" element :" ))
# #     li.append(c)
# #
# # print(li)
#
#
# li1=[int(input("Enter "+str(i)+" element :" )) for i in range(int(input("Enter number of elements : ")))]
# print(li1)
#
#
# # li=[]
# # str = input("enter the string : ")
# # str_list = str.split()
# # for element in str_list:
# #     c=int(element)
# #     li.append(c)
# # print(li)
#
# li2=[int(element) for element in input("enter the string : ").split()]
# print(li2)

# def loop(a_f):
#     print("a_f : ",a_f)
#     print("a_f id: ",id(a_f))
#     for i in range(1,3):
#         print("loop : ",i)
#         a_f=a_f+1
#         print("a_f : ",a_f)
#         print("a_f id: ",id(a_f))
#
#
#
# a_main=2
# print("a_main : ",a_main)
# print("a_main id: ",id(a_main))
# loop(a_main)

def loop(a_l):
    print("a_l : ",a_l)
    print("a_l id: ",id(a_l))
    for i in range(0,4):
        print("loop : ",i)
        a_l[i]=a_l[i]+1
    print("a_l : ",a_l)
    print("a_l id: ",id(a_l))



a_list=[1,2,3,4]
print("a_list : ",a_list)
print("a_list id: ",id(a_list))
loop(a_list)
print("a_list : ",a_list)
print("a_list id: ",id(a_list))
