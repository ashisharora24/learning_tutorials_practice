import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST2(root):
    if root is None:
        return 100000, -100000, True

    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isRightBST = isBST2(root.right)

    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)

    isBST = True

    if root.data <= leftMax or root.data > rightMin:
        isBST = False
    if not(isLeftBST) or not(isRightBST):
        isTreeBST = False

    return minimum, maximum, isTreeBST



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
print(isBST(root))
