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
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)

    def isPresentHelper(self,root,data):
        if root==None:
            return False
        if root.data==data:
            return True
        if root.data>data:
            return self.isPresentHelper(root.left,data)
        else:
            return self.isPresentHelper(root.right,data)


    def search(self, data):
    #Implement this function here
        return self.isPresentHelper(self.root,data)
    def insertHelper(self,root,data):
        if root==None:
            node=BinaryTreeNode(data)
            return node
        if root.data>data:
            root.left=self.insertHelper(root.left,data)
            return root
        else:
            root.right=self.insertHelper(root.right,data)
            return root






    def insert(self, data):
    #Implement this function here
        self.numNodes += 1
        self.root=self.insertHelper(self.root,data)
    def min(self,root):
        if root==None:
            return 10000
        if root.left==None:
            return root.data
        return self.min(root.left)

    def deleteDataHelper(self,root,data):
        if root==None:
            return False,None
        if root.data<data:
            deleted,newRightNode=self.deleteDataHelper(root.right,data)
            root.right=newRightNode
            return deleted,root
        if root.data>data:
            deleted,newLeftNode=self.deleteDataHelper(root.left,data)
            root.left=newLeftNode
            return deleted,root
        if root.left==None and root.right==None:
            return True,None
        if root.left==None:
            return True,root.right
        if root.right==None:
            return True,root.left
        replacement=self.min(root.right)
        root.data=replacement
        deleted,newRightNode=self.deleteDataHelper(root.right,replacement)
        root.right=newRightNode
        return True,root


    def delete(self, data):
    #Implement this function here
        deleted,newRoot=self.deleteDataHelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root=newRoot
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
