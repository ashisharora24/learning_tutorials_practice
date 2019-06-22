class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubbleSortLL(head) :
    length = 0
    headStart = head
    headpointer = head
    previousNode = None
    last = None
    start = None
    middle = None
    end = None
    # print("-----------------------------------------------")
    while head:
        length += 1
        head = head.next
    length_record = length
    # print("Length is input linked lisit is : ", length)
    # print("-----------------------------------------------")
    # print(" while look start")
    while length > 1:
#        print("------------")

        head = headpointer
        previousNode = None
        for i in range(length-1):
#            print(i," - ",head.data)
            if i == 0:
                last = None
            else:
                last = previousNode
            start = head
            middle = head.next
            if i == length_record - 2:
                end = None
            else:
                end = head.next.next

            if start.data > middle.data:
                if i == 0:
                    headpointer = middle
                else:
                    previousNode.next = middle
                middle.next = start
                if i == length_record - 2:
                    start.next = None
                else:
                    start.next = end
                head = middle
            previousNode = head
            head = head.next
#            printll(headpointer)
        length -= 1
    return headpointer


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
l = bubbleSortLL(l)
printll(l)
