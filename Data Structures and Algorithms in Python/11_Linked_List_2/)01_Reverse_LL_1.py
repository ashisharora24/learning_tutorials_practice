from sys import setrecursionlimit
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseRecursive(head):
    if head.next is None or head is None:
        return head
    currNode = Node(head.data)
    currNode.next = None
    child = reverseRecursive(head.next)
    child.next = currNode
    return currNode

def ll(arr):
    if len(arr) == 0:
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

setrecursionlimit(11000)
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = reverseRecursive(l)
printll(l)
