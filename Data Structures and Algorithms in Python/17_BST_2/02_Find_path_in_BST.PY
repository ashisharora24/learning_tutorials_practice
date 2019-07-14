

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findPathBST(root,data):
    print("---------------------------")
    if root is None:
        return None
    print("root.data : ", root.data)
    print("data : ", data)
    if root.data == data:
        return [root.data]
    listLeft = findPathBST(root.left, data)
    print("listLeft : ", listLeft)
    if listLeft is not None:
        listLeft.extend([root.data])
        print("listLeft : ", listLeft)
        return listLeft
    listRight = findPathBST(root.right, data)
    print("listRight : ", listRight)
    if listRight is not None:
        print("True")
        listRight.extend([root.data])
        print("listRight : ", listRight)
        return listRight
    else:
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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
data = int(input())
path = findPathBST(root,data)
print(path)
if path is not None:
    for ele in path:
        print(ele)
