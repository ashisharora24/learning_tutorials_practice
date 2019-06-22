class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def merge(head1,head2):
    startholder = None
    currholder = None

    while head1 and head2:
        if head1.data < head2.data:
            if startholder is None:
                currholder = head1
                startholder = currholder
            else:
                currholder.next = head1
                currholder = currholder.next
            head1 = head1.next
        else:
            if startholder is None:
                currholder = head2
                startholder = currholder
            else:
                currholder.next = head2
                currholder = currholder.next
            head2 = head2.next
    if head1:
        currholder.next = head1
    if head2:
        currholder.next = head2
    return startholder

def midpoint_linkedlist(head):
    slowNode = head
    fastNode = head
    if head is not None:
        while fastNode.next is not None and fastNode.next.next is not None:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        return slowNode
    else:
        return None

def mergeSort(head):
    if head.next is None or head is None:
        return head
    midpoint = midpoint_linkedlist(head)

    head1 = head
    head2 = midpoint.next
    midpoint.next = None

    headleft = mergeSort(head1)
    headright = mergeSort(head2)

    return merge(headleft,headright)
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
l = mergeSort(l)
printll(l)
