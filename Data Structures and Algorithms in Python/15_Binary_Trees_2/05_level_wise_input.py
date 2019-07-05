import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def takeLevelWiseTreeInput():
    q = queue.Queue()
    rootData = int(input("Enter the Main root Data : "))
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while not(q.empty()):
        currentNode = q.get()
        statement = "Enter Left child data " + str(currentNode.data) + " :: "
        leftData = int(input(statement))
        if leftData != -1:
            currentNode_left = BinaryTreeNode(leftData)
            q.put(currentNode_left)
        statement = "Enter right child data" + str(currentNode.data) + " :: "
        rightData = int(input(statement))
        if rightData != -1:
            currentNode_right = BinaryTreeNode(rightData)
            q.put(currentNode_right)

    return root

def printTree(root):
    if root is None:
        return
    print(root.data,end= ':')
    if root.left is not None:
        print("L ", root.left.data, end=',')
    if root.right is not None:
        print("R ", root.right.data)
    printTree(root.left)
    printTree(root.right)

root = takeLevelWiseTreeInput()
printTree(root)
