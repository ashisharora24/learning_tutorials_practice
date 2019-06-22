class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    startPointer = head
    previousNode = None
    # currentNode = None
    nextNode = None

    while head:
        # currentNode = head
        nextNode = head.next
        head.next = previousNode
        previousNode = head
        head = nextNode
    return previousNode, startPointer

def kReverse(head, n):
    if n < 2:
        return head
    header_clone = head
    startPointer = None
    startHeader = None
    nextHolder = None
    newStart = None
    newEnd = None
    counter = 1
    previousNode = None

    while head:
        # print("---------------")
        # print("head.data",head.data)
        if counter == 1:
            startPointer = head
        if counter == n:
            nextHolder = head.next
            head.next = None
            if previousNode is not None:
                previousNode.next = None
            newStart, newEnd = reverse(startPointer)
            if previousNode is not None:
                previousNode.next = newStart
            # printll(newStart)
            if startHeader is None:
                startHeader = newStart
            newEnd.next = nextHolder
            head = newEnd
            previousNode = head
            counter = 0
        counter += 1
        head = head.next

    if startHeader is None:
        newStart1, newEnd1 = reverse(header_clone)
        return newStart1
    if startPointer.next is not None:
        if previousNode is not None:
            previousNode.next = None
        newStart1, newEnd1 = reverse(startPointer)
        if previousNode is not None:
            previousNode.next = newStart
        newEnd.next = newStart1
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
l = kReverse(l, i)
printll(l)
