import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST2(root, lowLimit, highLimit):
    if root is None:
        return True
    isLeftBST = isBST2(root.left, lowLimit, root.data)
    isRightBST = isBST2(root.right, root.data, highLimit)

    isBST = True

    if root.data < lowLimit or root.data >= highLimit:
        isBST = False

    if not(isLeftBST) or not(isRightBST):
        isBST = False

    return isBST





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
printLevelWise(root)
print(isBST2(root, -100000, 100000))
