class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
    print()


# myCheck = None
def treeInput(root="main", side="root"):
    if root == "main":
        string1 = 'Enter data for ' + str(root) + ' : '
    else:
        string1 = 'Enter data for ' + side + 'child of ' + str(root) + ' : '
    rootData = int(input(string1))
    if rootData == -1:
        return None
    else:
        rootNode = BinaryTreeNode(rootData)
        # if root == "main":
        #     myCheck = rootNode
        rootNode.left = treeInput(root=rootData, side="left")
        rootNode.right = treeInput(root=rootData, side="right")
        return rootNode

def numNodes(root):
    if root is None:
        return 0
    return 1 + numNodes(root.left) + numNodes(root.right)

#printTree(treeInput())
print(numNodes(treeInput()))
# btn1 = BinaryTreeNode(1)
# btn2 = BinaryTreeNode(4)
# btn3 = BinaryTreeNode(5)
#
# btn1.left = btn2
# btn1.right = btn3
#
# printTree(btn1)
