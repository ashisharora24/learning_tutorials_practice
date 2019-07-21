# Next larger
# Send Feedback
# Given a generic tree and an integer n. Find and return the node with next larger element in the Tree i.e.
# find a node with value just greater than n.
# Return NULL if no node is present with the value greater than n.
# Input Format :
# Line 1 : Integer n
# Line 2 : Elements in level order form separated by space (as per done in class). Order is -
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element
# Output Format :
# Node with value just greater than n.
# Sample Input 1 :
# 18
# 10 3 20 30 40 2 40 50 0 0 0 0
# Sample Output 1 :
# 20
# Sample Input 2 :
# 21
# 10 3 20 30 40 2 40 50 0 0 0 0
# Sample Output 2:
# 30
# Download Test Cases
import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def nextLargest(tree, n):
    q = queue.Queue()
    q.put(tree)
    maxN = None
    max = 0
    if tree.data > n:
        maxN = tree
        max = tree.data
    ans = 0
    ansN = None
    while not(q.empty()):
        cNode = q.get()
        if cNode.data < max:
            ans = cNode.data
            ansN = cNode
        else:
            max = cNode.data
            maxN = cNode

        for child in tree.children:
            q.put(child)
    return ansN

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(nextLargest(tree, n).data)
