class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def stockSpan(price,n):
    head = None
    span = []
    for i in range(len(price)):
        currValue = price[i]
        s = Node(currValue)
        if head is None:
            head = s
        else:
            temp = head
            head = s
            head.next = temp
    while head:
        print("----------------")
        currData = head.data
        print("currData : ", currData)
        h = head
        count = 1
        while h.next:
            if h.next.data < currData:
                count += 1
            else:
                break
            h = h.next
        span.append(count)
        head = head.next
    #print(span)
    return span[::-1]

n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')
