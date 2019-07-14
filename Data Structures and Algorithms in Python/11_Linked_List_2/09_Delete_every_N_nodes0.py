class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skipMdeleteN(head, M, N):
    if N == 0 or head is None:
        return head
    if M == 0:
        return None

    startClone = head
    startNode = None
    holderNode = None
    counter = 1

    while head is not None:
        if counter == 1:
            if startNode is None:
                startNode = head
            else:
                holderNode.next = head
        if counter == M:
            holderNode = head
        if counter == M+N:
            counter = 0
        counter += 1
        head = head.next
    if holderNode.next is not None:
        holderNode.next = None
    return startClone


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
m=int(input())
n=int(input())
l = skipMdeleteN(l, m, n)
printll(l)
