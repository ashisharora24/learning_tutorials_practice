
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isbalanacedTree(root):
    if root is None:
        return None
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False
    isLeftBalanced = isbalanacedTree(root.left)
    isRightBalanced = isbalanacedTree(root.right)

    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False

def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left), height(root.right))

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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(isbalanacedTree(root))
