import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    if len(lst) == 0:
        return None
    print("----------------------------")
    print("lst : ", lst)
    if len(lst) == 1:
        return BinaryTreeNode(lst[0])
    mid = len(lst)//2
    if len(lst)%2 == 1:
        mid += 1
    #mid -= 1
    print("mid : ", mid)
    root = BinaryTreeNode(lst[mid-1])
    root.left = constructBST(lst[:mid-1])
    root.right = constructBST(lst[mid:])
    return root
def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)
