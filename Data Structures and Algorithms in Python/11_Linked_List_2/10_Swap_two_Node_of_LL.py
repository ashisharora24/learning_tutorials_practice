class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    C1, C2 = 0

    if i == j:
        return None
    if i < 0 or j < 0:
        return None
    if i < j:
        C1,C2 = i,j
    else:
        C1,C2 = j,i


    previousNode1 = None
    currNode1,nextNode1,previousNode2,currNode2,nextNode2,previous = None
    #nextNode1 = None
    #previousNode2 = None
    #currNode2 = None
    #nextNode2 = None
    #previous = None
    starthead = head
    counter = 0

    while head:
        # print("----------------------")
        # print("head.data = : ",head.data)
        # print("counter : ", counter)
        if counter == C1:
            # print("Found i")
            previousNode1 = previous
            currNode1 = head
            nextNode1 = head.next
        if counter == C2:
            # print("FOUND j")
            previousNode2 = previous
            currNode2 = head
            nextNode2 = head.next
        previous = head
        print
        counter += 1
        head = head.next
    # print("starthead.data : ", starthead.data)
    # print("previousNode1.data : ", previousNode1.data)
    # print("previousNode1.next.data : ", previousNode1.next.data)

    if previousNode1 is None:
        #previousNode1.next = None
        starthead = currNode2
    currNode1.next = None
    previousNode2.next = None
    currNode2.next = None

    # print("starthead.data : ", starthead.data)

    if previousNode1 is not None:
        previousNode1.next = currNode2
    if previousNode2 != currNode1:
        previousNode2.next = currNode1

    if currNode2 == nextNode1:
        print(currNode2.data)
        currNode2.next = currNode1
    else:
        currNode2.next = nextNode1

    if nextNode2 is not None:
        currNode1.next = nextNode2
    return starthead



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
i, j=list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)
