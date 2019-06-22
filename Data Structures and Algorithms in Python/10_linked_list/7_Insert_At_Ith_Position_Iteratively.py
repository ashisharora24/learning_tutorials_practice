from Node import Node


def deleteRec(head, i):
    if i < 0:
        return head
    if i == 0:
        return head.next
    if i == 1:
        head.next = head.next.next
        return head
    if head.next is None:
        return head
    head.next == deleteRec(head.next, i-1)
    return head


def lengthRecursive(head):
    if head is None:
        return 0
    return 1+lengthRecursive(head.next)


def delete_node(head, i):
    previous = None
    start_header = head
    count = 0
    while head is not None:
        currNode = head
        if count == i:
            if previous is None:
                start_header = currNode.next
            else:
                previous.next = currNode.next
        head = head.next
        previous = currNode
        count += 1
    return start_header


def insert_item_to_linked_list(head, i, val):
    orginial_head = head
    newNode = Node(val)
    previous = None
    count = 0
    while head is not None:
        currNode = head
        if count == i:
            if previous is None:
                print("true")
                orginial_head = newNode
                newNode.next = currNode
            else:
                previous.next = newNode
                newNode.next = currNode
        previous = currNode
        count += 1
        head = head.next
    return orginial_head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


def takeInput():
    inputList = input("Enter the List : ").split()
    head = None
    tail = None
    for currData in inputList:
        # print("currData", currData)
        currData = int(currData)

        if currData == -1:
            break

        currNode = Node(currData)
        if head is None:
            head = currNode
        else:
            tail.next = currNode
        tail = currNode
    return head


print("1")
head = takeInput()
print("2")
printLL(head)
print("3")
i = int(input("Enter the position number : "))
val = int(input("Enter the number to be added: "))
head = insert_item_to_linked_list(head, i, val)
printLL(head)
i = int(input("position to be deleted : "))
head = delete_node(head, i)
printLL(head)
print("-------------------")
print(lengthRecursive(head))
