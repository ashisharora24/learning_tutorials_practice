from Node import Node


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def takeInput():
    inputList = input("Enter the List with spaces in between : ").split()
    head = None
    tail = None
    for currInput in inputList:
        currData = int(currInput)

        if currData == -1:
            break

        currNode = Node(currData)
        if head is None:
            head = currNode
        else:
            tail.next = currNode
        tail = currNode
    return head


head = takeInput()
printLL(head)
