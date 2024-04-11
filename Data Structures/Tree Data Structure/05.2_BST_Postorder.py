# Post order traversal algorithm : lchild -> rchild -> key 

class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key == None:
            self.key = data
            return
        
        if self.key == data:
            return
        
        if data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
        else:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)


    def search(self, data):
        if self.key == data:
            print("Node is found!")
            return
        
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree!")

    
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild is not None:
            self.lchild.preorder()
        if self.rchild is not None:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild is not None:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild is not None:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild is not None:
            self.lchild.postorder()
        if self.rchild is not None:
            self.rchild.postorder()
        print(self.key,end=" ")


root = BST(10)
list1 = [6,3,1,6,98,3,7]
# list1 = [6,3,1,25,30,62]
for i in list1:
    root.insert(i)


print("Preorder")
root.preorder()
print()
print("Inorder")
root.inorder()
print()
print("Postorder")
root.postorder()