import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    # Given Postorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 8 Nodes with following input:
    # postOrder: 8 4 5 2 6 7 3 1
    # inOrder: 4 8 2 5 1 6 3 7
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if len(postorder) == 0:
        return None
    rootData = postorder[-1]
    rootIndexInInorder = inorder.index(rootData)
    inorderLeft, inorderRight = inorder[:rootIndexInInorder], inorder[rootIndexInInorder+1:]
    postorderLeft, postorderRight = postorder[0:len(inorderLeft)], postorder[len(inorderLeft):-1]

    print("inorderLeft : ", inorderLeft)
    print("inorderRight : ", inorderRight)
    print("postorderLeft : ", postorderLeft)
    print("postorderRight : ", postorderRight)


    # root = BinaryTreeNode(rootData)
    #
    # root.left = buildTreePostOrder(postorderLeft, inorderLeft)
    # root.right = buildTreePostOrder(postorderRight, inorderRight)
    # return root



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
n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)
