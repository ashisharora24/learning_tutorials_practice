# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    currEven = None
    startEven = None
    currOdd = None
    startOdd = None

    while head:
        if head.data%2 == 0:
            if startEven is None:
                currEven = head
                startEven = currEven
            else:
                currEven.next = head
                currEven = currEven.next
        else:
            if startOdd is None:
                currOdd = head
                startOdd = currOdd
            else:
                currOdd.next = head
                currOdd = currOdd.next
        head = head.next
    currEven.next = None
    currOdd.next = None
    if startEven is None:
        return startOdd
    if startOdd is None:
        return startEven
    currOdd.next = startEven
    return startOdd
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
l = arrange_LinkedList(l)
printll(l)
