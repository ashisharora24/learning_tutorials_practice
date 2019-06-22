class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def check_palindrome(head) :
    temp = []
    while head:
        temp.append(str(head.data))
        if head.next is None:
            break
        head = head.next
    # a = " ".join(temp)
    # b = " ".join(temp[-1::-1])
    if " ".join(temp) == " ".join(temp[-1::-1]):
        return True
    else:
        return False

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")
