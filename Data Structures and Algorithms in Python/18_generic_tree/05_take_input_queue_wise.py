# Height Of Tree
# Send Feedback
# Given a generic tree, find and return the height of given tree.
# Input format :
# Elements in level order form separated by space (as per done in class). Order is -
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element
# Output Format :
# Height
# Sample Input :
# 10 3 20 30 40 2 40 50 0 0 0 0
# Sample Output :
# 3

## Read input as specified in the question.
## Print output as specified in the question.
import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def takeInputQueueWise():

    q = queue.Queue()

    element = int(input("Enter Root Data : "))

    root = treeNode(element)
    q.put(root)

    while q.empty() is False:
        node = q.get()
        #str = "how many child for ", node.data, " exist : "
        print("how many child for ", node.data, " exist : ")
        count = int(input())
        for i in range(count):
            element = int(input("enter element : "))
            elementNode = treeNode(element)
            root.children.append(elementNode)
            q.put(elementNode)

    return root

root = takeInputQueueWise()
