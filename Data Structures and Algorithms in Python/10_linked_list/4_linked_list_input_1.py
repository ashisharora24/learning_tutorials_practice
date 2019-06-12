from Node import Node


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def takeInput():

    inputList = input().split()
    head = None
    for currInput in inputList:
        currData = int(currInput)

        if currData == -1:
            break

        currNode = Node(currData)
        if head is None:
            head = currNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = currNode
    return head


head = takeInput()
printLL(head)
