import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Root_To_Node_Path_In_Binary_Tree(root, searchElement):
    if root is None:
        return None
    if root.data == searchElement:
        return [root.data]
    listLeft = Root_To_Node_Path_In_Binary_Tree(root.left, searchElement)
    if listLeft is not None:
        return listLeft.extend([root.data])
    listRight = Root_To_Node_Path_In_Binary_Tree(root.right, searchElement)
    if listRight is not None:
        return listRight.extend([root.data])
    return None


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root


def printLevelWise(root):
    if root is None:
        return None
    q = queue.Queue()
    q.put(root)
    while not(q.empty()):
        currentNode = q.get()
        print(currentNode.data,":",sep="",end="")
        if currentNode.left is not None:
            q.put(currentNode.left)
            print("L:", currentNode.left.data, ",", sep="", end="")
        else:
            print("L:-1,", sep="", end="")
        if currentNode.right is not None:
            q.put(currentNode.right)
            print("R:", currentNode.right.data, sep="")
        else:
            print("R:-1", sep="")


levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
#printLevelWise(root)
print(Root_To_Node_Path_In_Binary_Tree(root, 7))
