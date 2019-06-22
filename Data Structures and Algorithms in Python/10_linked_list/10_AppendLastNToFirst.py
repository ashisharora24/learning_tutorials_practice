class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append_LinkedList(head,n):

    count = 0
    header = head
    while head is not None:
        count += 1
        head = head.next
    start_LL_length = count - n
    # print("start_LL_length : ", start_LL_length)
    # print("count : ", count)
    if start_LL_length == count or start_LL_length<=0:
        return head
    start_LL_starter =  None
    start_LL_ender = None
    new_header = None
    # print("start_LL_length : ", start_LL_length)

    count = 0
    while header:
        # print("**********************************")
        # print("header.data : ", header.data)
        # print("count : ", count)
        # print("----------------------")
        if count < start_LL_length:
            if start_LL_starter is None:
                start_LL_starter = header
            start_LL_ender =  header
        else:
            if new_header is None:
                new_header = header
            if header.next is None:
                header.next = start_LL_starter
                start_LL_ender.next = None
                break
        count += 1
        header = header.next
    return new_header

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = append_LinkedList(l, i)
printll(l)
