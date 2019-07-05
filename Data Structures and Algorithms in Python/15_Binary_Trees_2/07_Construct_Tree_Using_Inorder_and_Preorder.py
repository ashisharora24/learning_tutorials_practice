# Construct Tree Using Inorder and Preorder
# Send Feedback
# Given Preorder and Inorder traversal of a binary tree, create the binary tree associated with the traversals.You just need to construct the tree and return the root.
# Note: Assume binary tree contains only unique elements.
# Input format :
#
# Line 1 : n (Total number of nodes in binary tree)
#
# Line 2 : Pre order traversal
#
# Line 3 : Inorder Traversal
#
# Output Format :
#
# Elements are printed level wise, each level in new line (separated by space).
#
# Sample Input :
# 12
# 1 2 3 4 15 5 6 7 8 10 9 12
# 4 15 3 2 5 1 6 10 8 7 9 12
# Sample Output :
# 1
# 2 6
# 3 5 7
# 4 8 9
# 15 10 12

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePreOrder(preorder, inorder):
    # Given Preorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 12 Nodes with following input:
    # preOrder: 1 2 3 4 15 5 6 7 8 10 9 12
    # inOrder: 4 15 3 2 5 1 6 10 8 7 9 12
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if len(preorder) == 0:
        return None
    rootData = preorder[0]
    root_index = inorder.index(rootData)
    inorderLeft, inorderRight = inorder[:root_index], inorder[root_index+1:]
    preorderLeft, preorderRight = preorder[1:len(inorderLeft)+1], preorder[len(inorderLeft)+1:]

    root = BinaryTreeNode(rootData)

    root.left = buildTreePreOrder(preorderLeft, inorderLeft)
    root.right = buildTreePreOrder(preorderRight, inorderRight)
    return root

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
#n=int(input())
#preorder = [int(i) for i in input().strip().split()]
#inorder = [int(i) for i in input().strip().split()]
inorder = [4,2,5,1,6,3,7]
preorder = [1,2,4,5,3,6,7]
# inorder = [4, 2, 5, 1, 3]
# preorder = [1, 2, 4, 5, 3]

print("inorder : ", inorder)
print("preorder : ", preorder)
root = buildTreePreOrder(preorder, inorder)
printLevelATNewLine(root)
