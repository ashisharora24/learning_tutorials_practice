class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTreeHelper(self, root):
        if root is None:
            return
        print(root.data, end=":")
        if root.left is not None:
            print("L:", end='')
            print(root.left.data, end=',')
        if root.right is not None:
            print("R:", end='')
            print(root.right.data, end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        #print("1111")
        #print(self.root.data)
        self.printTreeHelper(self.root)

    def searchHelper(self, root, data):
        #print("data : ", data)
        if root is None:
            return False
        #rint("root.data : ", root.data)
        if root.data == data:
            return True
        if root.data > data:
            return self.searchHelper(root.left, data)
        else:
            return self.searchHelper(root.right, data)

    def search(self, data):
        return self.searchHelper(self.root, data)

    def insertHelper(self, root, data):
        # print("data : ", data)
        if root is None:
            # print("root None")
            node = BinaryTreeNode(data)
            self.root = node
            return node
        # print("root.data : ", root.data)
        if root.data > data:
            # print("root low")
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            # print("root high")
            root.right = self.insertHelper(root.right, data)
            return root

    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)

    def min(self,root):
        if root is None:
            return 10000

        if root.left is None:
            return root.data

        return self.min(root.left)

    def deleteHelper(self, root, data):
        #print("data : ",  data)
        if root is None:
            #print("root is none")
            return False, None
        #print("root.data : ", root.data)
        if root.data < data:
            #print("root is greater")
            deleted, newRightNode = self.deleteHelper(root.right,data)
            root.right = newRightNode
            return deleted, root

        if root.data > data:
            #print("root is smaller")
            deleted, newLeftChild = self.deleteHelper(root.left, data)
            root.left = newLeftChild
            return deleted, root
        #print("DATA AND ROOTDATA ARE SAME")
        if root.left is None and root.right is None:
            #print("leaf")
            return True, None

        if root.left is None:
            #print("no left child")
            return True, root.right

        if root.right is None:
            #print("no right child")
            return True, root.left

        #print("BOTH EXIST")

        replacement = self.min(root.right)
        #print("MIN cleared")
        #print("replacement : ", replacement)

        root.data = replacement
        #print("replacement done")
        deleted, newRightNode = self.deleteHelper(root.right, replacement)

        root.right = newRightNode
        return True, root

    def delete(self, data):
        deleted, new_root = self.deleteHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = new_root
        return deleted

    def count(self):
        return self.numNodes

b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while(i < (len(li) )):
    choice = li[i]
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1

    
