class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def eliminate_duplicate(head):
    base_value = None
    starter = None
    while head:
        if base_value is None:
            base_value = head
        if starter is None:
            starter = head
        else:
            currNode = head
            if currNode.data == base_value.data:
                if currNode is None:
                    base_value.next = None
                else:
                    base_value.next = currNode.next
            else:
                base_value = currNode
        head = head.next

    return starter

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
l = eliminate_duplicate(l)
printll(l)
