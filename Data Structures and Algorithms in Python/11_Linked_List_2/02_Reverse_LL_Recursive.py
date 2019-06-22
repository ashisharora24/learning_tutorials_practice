from sys import setrecursionlimit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class NodePair:
    def __init__(self, start, tail):
        self.start = start
        self.tail = tail


def reverseRecursive(head):
    currNode = head
    if head.next is None:
        ans = NodePair(head, head)
        return ans
    recurObj = reverseRecursive(head.next)
    currNode.next = None
    start = recurObj.start
    tails = recurObj.tail
    start.next = currNode
    ans = NodePair(currNode, tails)
    return ans


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

arr = ll(arr[:-1])
arr = reverseRecursive(arr)
printll(arr.tail)
