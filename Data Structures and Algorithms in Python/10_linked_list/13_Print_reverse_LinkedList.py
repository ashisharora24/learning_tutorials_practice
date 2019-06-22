class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linkedlist_spl(head):
    if head.next is None:
        return str(head.data)
    return str(print_linkedlist_spl(head.next))+" "+str(head.data)

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
from sys import setrecursionlimit
setrecursionlimit(10000)
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
print(print_linkedlist_spl(l))
