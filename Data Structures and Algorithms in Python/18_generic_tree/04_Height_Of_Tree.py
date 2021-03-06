# Height Of Tree
# Send Feedback
# Given a generic tree, find and return the height of given tree.
# Input format :
# Elements in level order form separated by space (as per done in class). Order is -
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element
# Output Format :
# Height
# Sample Input :
# 10 3 20 30 40 2 40 50 0 0 0 0
# Sample Output :
# 3

## Read input as specified in the question.
## Print output as specified in the question.
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def height_of_tree(tree,currentHeight = 0, max_height = 0):
    currentHeight += 1
    max_height = max(max_height, currentHeight)

    for child in tree.children:
        max_height = max(height_of_tree(child, currentHeight, max_height), currentHeight)

    currentHeight -= 1
    return max_height



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
print(height_of_tree(tree))
