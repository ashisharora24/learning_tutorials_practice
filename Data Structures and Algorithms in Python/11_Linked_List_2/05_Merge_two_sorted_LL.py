class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(head1,head2):
    startholder = None
    currholder = None

    while head1 and head2:
        print("----------------------")
        print("head2.data : ", head2.data)
        print("head1.data : ", head1.data)
        if head1.data < head2.data:
            if startholder is None:
                print("T1")
                currholder = head1
                startholder = currholder
            else:
                print("F1")
                currholder.next = head1
                currholder = currholder.next
            head1 = head1.next
        else:
            if startholder is None:
                print("T2")
                currholder = head2
                startholder = currholder
            else:
                print("F2")
                currholder.next = head2
                currholder = currholder.next
            head2 = head2.next
        print("currholder.data : ", currholder.data)
        print("startholder.data : ", startholder.data)

    if head1:
        print("T3")
        currholder.next = head1
    if head2:
        print("F3")
        currholder.next = head2
    return startholder

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
# Read the link list elements including -1
arr1 = list(int(i) for i in input().strip().split(' '))
arr2 = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)
