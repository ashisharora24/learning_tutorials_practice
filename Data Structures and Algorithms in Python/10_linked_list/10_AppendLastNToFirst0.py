class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append_LinkedList(head,n):
    l = 0
    header = head
    while head is not None:
        l += 1
        head = head.next
    curr = header
    i = 0
    previousNode = None
    while i < l - n:
        previousNode = curr
        curr = curr.next
        i += 1
    previousNode.next = None
    previousNode2 = Node
    startHeader = curr
    while curr:
        previousNode2 = curr
        curr = curr.next
    previousNode2.next = header
    return startHeader

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
