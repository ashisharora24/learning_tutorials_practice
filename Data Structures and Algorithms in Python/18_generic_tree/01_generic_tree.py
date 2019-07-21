import queue

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = list()

def printTree(root):
    if root is None:
        return

    print(root.data)

    for child in root.children:
        printTree(child)

def printTreeStructure(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while q.empty() is False:
        currentNode = q.get()
        print(currentNode.data, ":", sep="", end="")
        for child in currentNode.children:
            q.put(child)
            print(child.data, ",", sep="", end="")
        print()

# ---------------------------------------------
def printTreeDetailed(root):
    if root is None:
        return

    print(root.data, " :", sep="", end="")
    for child in root.children:
        print(child.data, ",", sep="", end="")

    print()

    for child in root.children:
        printTreeDetailed(child)
# -----------------------------------------------
def inputForTree(root):
    string = "how many elements does " + str(root.data) + " have : "
    count = int(input(string))
    if count == 0:
        return
    for n in range(count):
        element = int(input("Enter child value : "))
        elementNode = TreeNode(element)
        root.children.append(elementNode)

    for child in root.children:
        inputForTree(child)

def numNodes(root):
    count = 1
    for child in root.children:
        count += numNodes(child)
    return count

n5 = TreeNode(5)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n6 = TreeNode(6)
n7 = TreeNode(7)

n5.children.append(n1)
n5.children.append(n2)
n5.children.append(n3)
n5.children.append(n4)
n3.children.append(n6)
n3.children.append(n7)

printTree(n5)
printTreeStructure(n5)
print("----------------------")
printTreeDetailed(n5)

# ---------------------------------------
element = int(input("Enter the first element : "))
elementNode = TreeNode(element)
inputForTree(elementNode)
printTreeDetailed(elementNode)
print(numNodes(elementNode))
