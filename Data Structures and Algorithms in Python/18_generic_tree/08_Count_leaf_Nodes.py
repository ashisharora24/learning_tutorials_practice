# Count leaf Nodes
# Send Feedback
# Given a generic tree, count and return the number of leaf nodes present in the given tree.
# Input format :
# Elements in level order form separated by space (as per done in class). Order is -
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element
# Output Format :
# Count of leaf nodes
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0
# Sample Output 1 :
# 4
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def leafNodeCount(tree):
    if tree is None:
        return 0
    count = 0
    if not(tree.children):
        return 1
    for child in tree.children:
        count = count + leafNodeCount(child)
    return count

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(leafNodeCount(tree))
