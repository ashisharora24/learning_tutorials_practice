# Nodes without sibling
# Send Feedback
# Given a binary tree, print all nodes that don’t have a sibling.
# Edit : Print the elements in different lines. And order of elements doesn't matter.
# Input format :
# Elements in level order form (separated by space). If any node does not have left or right child, take -1 in its place.
# Output format :
# Print nodes separated by new line.
# Sample Input :
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# Sample Output :
# 9

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesWithoutSibling(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    left_side = nodesWithoutSibling(root.left)
    right_side = nodesWithoutSibling(root.right)
    if root.left is not None and root.right is None:
        print(root.data)
    if root.right is not None and root.left is None:
        print(root.data)


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
printTree(root)
nodesWithoutSibling(root)
